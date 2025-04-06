from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from .models.message import Base, Message
import config


class MessageRepository:

    def __init__(self):
        self.engine = create_engine(config.DATABASE_URL)
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = scoped_session(self.session_maker)

    def initialize_db(self):
        Base.metadata.create_all(self.engine)

    def create_message(self, subject, content):
        try:
            message = Message(subject=subject, content=content)
            self.session.add(message)
            self.session.commit()
            return message
        except Exception as e:
            self.session.rollback()
            raise e

    def get_messages(self):
        messages = self.session.query(Message).order_by(Message.id.desc()).all()
        return messages


def message_repository():
    return MessageRepository()
