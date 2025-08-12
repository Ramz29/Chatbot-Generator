import importlib
import pkgutil
from fastapi import FastAPI
from backend.app.db.database import engine
from backend.app.db import models
import backend.app.routes as routes_pkg

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Chatbot Generator API",
    description="Backend API for the Chatbot Generator project",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Chatbot backend is running!"}

# Dynamically load all routers from app/routes
for _, module_name, _ in pkgutil.iter_modules(routes_pkg.__path__):
    module = importlib.import_module(f"{routes_pkg.__name__}.{module_name}")
    if hasattr(module, "router"):
        app.include_router(module.router)
