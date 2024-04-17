from datetime import datetime
import logging
from airflow import DAG
from airflow.operators.python import PythonOperator
import json
import requests
from kafka import KafkaProducer
import time


default_args = {
    "owner": "Darshan",
    "start_date": datetime(2024, 4, 10, 8, 00),
}


def get_data():

    res = requests.get("https://randomuser.me/api/?nat=us,gb,ca,ie,nz,in")
    res = res.json()
    res = res["results"][0]
    return res


def format_data(res):

    data = {}
    data["first_name"] = res["name"]["first"]
    data["last_name"] = res["name"]["last"]
    data["gender"] = res["gender"]
    location = res["location"]
    data["address"] = (
        f"{str(location['street']['number'])}, {location['street']['name']}"
        f"{location['city']}, {location['state']}, {location['country']}"
    )

    data["postcode"] = location["postcode"]
    data["email"] = res["email"]
    data["username"] = res["login"]["username"]
    data["dob"] = res["dob"]["date"]
    data["registered_date"] = res["registered"]["date"]
    data["phone"] = res["phone"]
    data["picture"] = res["picture"]["medium"]

    # print('Formatted Data: {}'.format(json.dumps(data)))
    return data


def stream_data():

    
    # print(json.dumps(res, indent=3))

    producer = KafkaProducer(
        # security_protocol="PLAINTEXT",
        # bootstrap_servers=['localhost:9092'],
        bootstrap_servers=['broker:29092'],
        max_block_ms=5000,
        # api_version=("7.4.0"),
    )

    curr_time=time.time()

    while True:
        if time.time()> curr_time+60:   # every minute
            break

        try:
            res = get_data()
            res = format_data(res)

            producer.send('users_created', json.dumps(res).encode("utf-8"))

        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

        
# task_id
with DAG(
    'user_automation',
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    # Tasks
    streaming_task = PythonOperator(
        task_id='stream_data_from_api', python_callable=stream_data
    )

