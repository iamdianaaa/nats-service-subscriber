from data.repository import message_repository
from logging import getLogger

logger = getLogger(__name__)

class MessageProcessor:
    def __init__(self):
        self.repository = message_repository()

    def process_message(self, message):
        try:
            subject = message.subject
            content = message.data.decode()

            logger.info(f"Processing message for subject {subject}", extra={'message_content': content})
            self.repository.create_message(subject, content)
            return True
        except Exception as e:
            logger.error(f"Error occurred while processing the message", extra={'error': str(e)})
            return False
