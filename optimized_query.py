from bisect import bisect_left, bisect_right


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


def build_partitioned_index(data):
    data_by_sensor = {}

    for reading in data:
        sensor_id = reading["sensor_id"]

        if sensor_id not in data_by_sensor:
            data_by_sensor[sensor_id] = []

        data_by_sensor[sensor_id].append(reading)

    for sensor_id in data_by_sensor:
        data_by_sensor[sensor_id].sort(key=lambda reading: reading["timestamp"])

    return data_by_sensor


def range_query_optimized(sensor_id, start_time, end_time, data_by_sensor):
    readings = data_by_sensor.get(sensor_id, [])

    timestamps = [reading["timestamp"] for reading in readings]

    left_index = bisect_left(timestamps, start_time)
    right_index = bisect_right(timestamps, end_time)

    return readings[left_index:right_index]