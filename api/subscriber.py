from logging import getLogger
from nats.aio.client import Client as NATS
import config
from business.message_processor import MessageProcessor

logger = getLogger(__name__)

class NatsSubscriber:
    def __init__(self):
        self.processor = MessageProcessor()
        self.nc = None
        self.subscription = None

    async def connect(self):
        try:
            logger.info(f"Connecting to NATS at {config.NATS_URL}")
            self.nc = NATS()
            await self.nc.connect(
                config.NATS_URL,
                connect_timeout=5,
                max_reconnect_attempts=3
            )
            logger.info("Successfully connected to NATS")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to NATS: {str(e)}")
            return False

    async def subscribe(self):
        if not self.nc or not self.nc.is_connected:
            success = await self.connect()
            if not success:
                return False

        try:
            logger.info(f"Subscribing to subject: {config.NATS_SUBJECT}")
            self.subscription = await self.nc.subscribe(
                config.NATS_SUBJECT,
                cb=self._process_message
            )
            logger.info(f"Successfully subscribed to {config.NATS_SUBJECT}")
            return True
        except Exception as e:
            logger.error(f"Subscription error: {str(e)}")
            return False

    async def _process_message(self, msg):
        try:
            self.processor.process_message(msg)
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")

    async def close(self):
        if self.subscription:
            await self.subscription.unsubscribe()
        if self.nc:
            await self.nc.close()