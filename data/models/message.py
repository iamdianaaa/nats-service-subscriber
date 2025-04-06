from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, DateTime, String
from datetime import datetime, timezone

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Message(id={self.id}, subject={self.subject}, content={self.content}, timestamp={self.timestamp})>"
