import time
import random


def generate_sensor_reading(sensor_id, zone="A", sensor_type="temperature"):
    return {
        "sensor_id": sensor_id,
        "timestamp": time.time(),
        "zone": zone,
        "type": sensor_type,
        "value": round(random.uniform(20.0, 35.0), 2)
    }


def simulate_data(sensor_ids, readings_per_sensor=1000):
    data = []

    for _ in range(readings_per_sensor):
        for sensor_id in sensor_ids:
            data.append(generate_sensor_reading(sensor_id))

    return data