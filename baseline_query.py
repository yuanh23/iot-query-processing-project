def latest_reading_baseline(sensor_id, data):
    latest = None

    for reading in data:
        if reading["sensor_id"] == sensor_id:
            if latest is None or reading["timestamp"] > latest["timestamp"]:
                latest = reading

    return latest