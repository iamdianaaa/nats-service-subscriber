import asyncio
from nats.aio.client import Client as NATS
from api.subscriber import NatsSubscriber
from data.repository import message_repository

NATS_URL = "nats://localhost:4222"
NATS_SUBJECT = "messages"


async def test_publish_message():
    nc = NATS()
    await nc.connect(NATS_URL)
    print("Connected to NATS")

    subject = NATS_SUBJECT
    test_message = "Test message content"
    await nc.publish(subject, test_message.encode())
    print(f"Published message to subject: {subject}")

    subscriber = NatsSubscriber()

    await subscriber.connect()
    await subscriber.subscribe()

    await asyncio.sleep(2)

    await subscriber.close()

    repository = message_repository()
    messages = repository.get_messages()

    assert messages[0].content == test_message
    assert len(messages) > 0

    print("Test passed successfully")

    await nc.close()

if __name__ == "__main__":
    asyncio.run(test_publish_message())
