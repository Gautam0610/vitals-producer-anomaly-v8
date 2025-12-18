import time
import random
import json
from kafka import KafkaProducer
from config import config

def get_producer():
    producer = KafkaProducer(
        bootstrap_servers=config.BOOTSTRAP_SERVERS,
        security_protocol=config.SECURITY_PROTOCOL,
        sasl_mechanism=config.SASL_MECHANISM,
        sasl_plain_username=config.SASL_USERNAME,
        sasl_plain_password=config.SASL_PASSWORD,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer

def generate_vitals():
    body_temp = round(random.uniform(36.5, 37.5), 1)
    heart_rate = random.randint(60, 100)
    systolic_pressure = random.randint(110, 130)
    diastolic_pressure = random.randint(70, 90)
    breaths_per_minute = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 100)
    blood_glucose = random.randint(70, 140)

    return {
        "body_temp": body_temp,
        "heart_rate": heart_rate,
        "systolic_pressure": systolic_pressure,
        "diastolic_pressure": diastolic_pressure,
        "breaths_per_minute": breaths_per_minute,
        "oxygen_saturation": oxygen_saturation,
        "blood_glucose": blood_glucose
    }

def generate_anomalous_vitals():
    body_temp = round(random.uniform(36.5, 37.5), 1)
    heart_rate = random.randint(150, 220)  #Unrealistically high
    systolic_pressure = random.randint(110, 130)
    diastolic_pressure = random.randint(70, 90)
    breaths_per_minute = random.randint(30, 50) #Unrealistically high
    oxygen_saturation = random.randint(95, 100)
    blood_glucose = random.randint(70, 140)

    return {
        "body_temp": body_temp,
        "heart_rate": heart_rate,
        "systolic_pressure": systolic_pressure,
        "diastolic_pressure": diastolic_pressure,
        "breaths_per_minute": breaths_per_minute,
        "oxygen_saturation": oxygen_saturation,
        "blood_glucose": blood_glucose
    }


def run_producer():
    producer = get_producer()
    anomaly_chance = 0.1  # 10% chance of anomaly

    while True:
        if random.random() < anomaly_chance:
            vitals = generate_anomalous_vitals()
            print("Sending anomalous vitals")
        else:
            vitals = generate_vitals()
        producer.send(config.OUTPUT_TOPIC, vitals)
        producer.flush()
        print(f"Sent vitals: {vitals}")
        time.sleep(config.INTERVAL_MS / 1000)

if __name__ == "__main__":
    run_producer()