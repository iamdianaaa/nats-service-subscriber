# NATS Service Subscriber with PostgreSQL Persistence

This application follows a 3-layered architecture to subscribe to a NATS service (NATS), process messages, and store them in a PostgreSQL database.

## Architecture

The application is structured into three layers:

1. **API Layer**
    - Responsible for subscribing to the Nuts service. 
    - Receives messages and passes them to the Service layer.

2. **Service (Business) Layer**
   - Contains the business logic
   - Validates and processes messages
   - Passes validated data to the Data layer

3. **Data Layer**
   - Communicates with PostgreSQL
   - Handles saving messages to the database. 

## Prerequisites

- Python 3.9+
- [Docker and Docker Compose](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [NATS Server](https://nats.io/)


# Application setup

The project is hosted in GitHub, so firstly it needs to be cloned.

```bash
# Clone the repository
git clone https://github.com/iamdianaaa/nats-service-subscriber
```

## Installing requirements locally

It is suggested to create a virtual environment firstly:

```bash
python -m venv venv
.\venv\Scripts\activate # on Windows
source venv/bin/activate # on Ubuntu
```
Then install the requirements specified in requirements.txt file:

```bash
pip install -r requirements.txt
```

Everything related to starting is also in Dockerfile in the root folder.

docker-compose is used to run the services:

```bash
# Start all services
docker-compose up -d
```
You can also run specific service by mentioning it at the end of the command.


# Run the application

```bash
python main.py
```

You can set environmental variables if needed, otherwise default ones will be used

## Testing


There ara tests in the tests folder (in the root folder):
- test_app.py - this will test the functionality of the application and publish messages
- test_publish.py - this is simply for checking the NATS publishing, and the connection to NATS

To run them:
```bash
python tests/test_app.py
```
```bash
python tests/test_publish.py
```


After publishing, check that the message was received and stored in the database:

```bash
# Connect to PostgreSQL
psql -U someone -h localhost -d messages_db

# Query the messages table
SELECT * FROM messages;
```
