import asyncio
import sys
from nats.aio.client import Client as NATSClient

NATS_URL = "nats://localhost:4222"
NATS_SUBJECT = "messages"
NUM_MESSAGES = 5
DELAY_BETWEEN = 1


async def publish_test_messages():
    print(f"Connecting to NATS server at {NATS_URL}")

    try:
        nc = NATSClient()
        await nc.connect(NATS_URL)
        print("Connected to NATS server")

        for i in range(NUM_MESSAGES):
            message = f"Test message #{i}"
            payload = message.encode()

            await nc.publish(NATS_SUBJECT, payload)

            print(f"Published message #{i}: {message}")

            await asyncio.sleep(DELAY_BETWEEN)

        await asyncio.sleep(1)

        await nc.close()
        print(f"Successfully published {NUM_MESSAGES} messages")

    except Exception as e:
        print(f"Error: {str(e)}")
        return False

    return True


if __name__ == "__main__":

    success = asyncio.run(publish_test_messages())

    if success:
        print("Test completed successfully")
    else:
        print("Test failed")
        sys.exit(1)