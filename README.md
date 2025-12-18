# vitals-producer-anomaly-v8

A Kafka producer that generates random vitals data and pushes it to a Kafka topic. It also injects anomalies into heart rate and breaths per minute.

## Usage

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/vitals-producer-anomaly-v8.git
    cd vitals-producer-anomaly-v8
    ```

2.  Create a `.env` file with the following contents:

    ```
    OUTPUT_TOPIC=vitals_topic
    BOOTSTRAP_SERVERS=localhost:9092
    SASL_USERNAME=your_sasl_username
    SASL_PASSWORD=your_sasl_password
    SECURITY_PROTOCOL=SASL_SSL
    SASL_MECHANISM=PLAIN
    INTERVAL_MS=1000
    ```

    Replace `your_sasl_username` and `your_sasl_password` with your actual SASL credentials.

3.  Run with Docker:

    ```bash
    docker build -t vitals-producer .
    docker run vitals-producer
    ```