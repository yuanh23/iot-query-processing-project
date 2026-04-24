def build_latest_cache(data):
    latest_cache = {}

    for reading in data:
        sensor_id = reading["sensor_id"]

        if (
            sensor_id not in latest_cache
            or reading["timestamp"] > latest_cache[sensor_id]["timestamp"]
        ):
            latest_cache[sensor_id] = reading

    return latest_cache


def latest_reading_optimized(sensor_id, latest_cache):
    return latest_cache.get(sensor_id)