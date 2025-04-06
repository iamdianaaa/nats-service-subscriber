from api.subscriber import NatsSubscriber
from data import message_repository
import asyncio
import signal
from logging import getLogger

logger = getLogger(__name__)


async def main():
    repo = message_repository()
    repo.initialize_db()


    subscriber = NatsSubscriber()
    await subscriber.connect()

    connected = await subscriber.connect()
    if connected:
        subscribed = await subscriber.subscribe()
        if subscribed:
            logger.info("Successfully connected and subscribed!")
        else:
            logger.error("Failed to subscribe!")
    else:
        logger.error("Failed to connect!")

    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass
    finally:
        await subscriber.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    def handle_signal(sig, frame):
        logger.info(f"Received signal {sig}, shutting down...")
        loop.stop()

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        logger.error("Execution interrupted.")
    finally:
        loop.close()