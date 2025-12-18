import os
from dotenv import load_dotenv

load_dotenv()

OUTPUT_TOPIC = os.getenv("OUTPUT_TOPIC")
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS")
SASL_USERNAME = os.getenv("SASL_USERNAME")
SASL_PASSWORD = os.getenv("SASL_PASSWORD")
SECURITY_PROTOCOL = os.getenv("SECURITY_PROTOCOL")
SASL_MECHANISM = os.getenv("SASL_MECHANISM")
INTERVAL_MS = int(os.getenv("INTERVAL_MS"))