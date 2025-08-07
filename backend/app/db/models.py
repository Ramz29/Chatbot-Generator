#SQLAlchemy ORM models
from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="user")  # 'admin' or 'user'

    bots = relationship("Chatbot", back_populates="owner")
    documents = relationship("Document", back_populates="uploader")

class Chatbot(Base):
    __tablename__ = "chatbots"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    tone = Column(String)
    color = Column(String)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    owner = relationship("User", back_populates="bots")
    documents = relationship("Document", back_populates="chatbot")

class Document(Base):
    __tablename__ = "documents"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String)
    filepath = Column(String)
    uploader_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    chatbot_id = Column(UUID(as_uuid=True), ForeignKey("chatbots.id"))

    uploader = relationship("User", back_populates="documents")
    chatbot = relationship("Chatbot", back_populates="documents")

class ChatHistory(Base):
    __tablename__ = "chat_history"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    chatbot_id = Column(UUID(as_uuid=True), ForeignKey("chatbots.id"))
    question = Column(String)
    answer = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
