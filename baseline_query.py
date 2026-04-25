def latest_reading_baseline(sensor_id, data):
    latest = None

    for reading in data:
        if reading["sensor_id"] == sensor_id:
            if latest is None or reading["timestamp"] > latest["timestamp"]:
                latest = reading

    return latest


def range_query_baseline(sensor_id, start_time, end_time, data):
    results = []

    for reading in data:
        if (
            reading["sensor_id"] == sensor_id
            and start_time <= reading["timestamp"] <= end_time
        ):
            results.append(reading)

    return results