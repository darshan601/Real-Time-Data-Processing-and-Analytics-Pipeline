Introduction
This project provides a comprehensive guide to building an end-to-end data engineering pipeline, covering stages from data ingestion to processing and storage. It utilizes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, Cassandra, and Docker.



System Architecture:
Data Source: Generates random user data from randomuser.me API.
Apache Airflow: Orchestrates the pipeline and stores fetched data in PostgreSQL.
Apache Kafka and Zookeeper: Streams data from PostgreSQL to the processing engine.
Control Center and Schema Registry: Monitors and manages Kafka streams.
Apache Spark: Processes data with its master and worker nodes.
Cassandra: Stores the processed data.

What I Learned
Setting up a data pipeline with Apache Airflow
Real-time data streaming with Apache Kafka
Distributed synchronization with Apache Zookeeper
Data processing techniques with Apache Spark
Data storage with Cassandra and PostgreSQL
Containerizing the setup with Docker

Technologies:
Apache Airflow
Python
Apache Kafka
Apache Zookeeper
Apache Spark
Cassandra
PostgreSQL
Docker

Getting Started:

Clone the repository:

git clone https://github.com/airscholar/e2e-data-engineering.git

Navigate to the project directory:

cd e2e-data-engineering

Run Docker Compose to spin up the services:

docker-compose up

reference: YouTube Video Tutorial.(https://www.youtube.com/watch?v=GqAcTrqKcrY)
