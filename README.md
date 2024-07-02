# Realtime Data Streaming | End-to-End Data Engineering Project

## Table of Contents
- Introduction
- System Architecture
- What I Learned
- Technologies
- Reference

## Introduction
This project provides a comprehensive guide to building an end-to-end data engineering pipeline, covering stages from data ingestion to processing and storage. It utilizes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, Cassandra, and Docker.

![System Architecture](https://github.com/darshan601/Real-Time-Data-Processing-and-Analytics-Pipeline/blob/main/Screenshot%202024-04-10%20at%207.07.06%E2%80%AFPM.png)

## System Architecture
- **Data Source:** Generates random user data from randomuser.me API.
- **Apache Airflow:** Orchestrates the pipeline and stores fetched data in PostgreSQL.
- **Apache Kafka and Zookeeper:** Streams data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry:** Monitors and manages Kafka streams.
- **Apache Spark:** Processes data with its master and worker nodes.
- **Cassandra:** Stores the processed data.

## What I Learned
- Setting up a data pipeline with Apache Airflow
- Real-time data streaming with Apache Kafka
- Distributed synchronization with Apache Zookeeper
- Data processing techniques with Apache Spark
- Data storage with Cassandra and PostgreSQL
- Containerizing the setup with Docker

## Technologies
- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker

##Reference 
YouTube Video Tutorial.(https://www.youtube.com/watch?v=GqAcTrqKcrY)
