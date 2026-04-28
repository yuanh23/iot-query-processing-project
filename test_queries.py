from sensor_simulator import simulate_data
from baseline_query import latest_reading_baseline, range_query_baseline
from optimized_query import (
    build_latest_cache,
    build_partitioned_index,
    latest_reading_optimized,
    range_query_optimized,
)


def test_latest_query_correctness():
    sensor_ids = [f"S{i}" for i in range(1, 11)]
    data = simulate_data(sensor_ids, readings_per_sensor=1000)

    latest_cache = build_latest_cache(data)
    target_sensor = "S1"

    baseline_result = latest_reading_baseline(target_sensor, data)
    optimized_result = latest_reading_optimized(target_sensor, latest_cache)

    assert baseline_result == optimized_result


def test_range_query_correctness():
    sensor_ids = [f"S{i}" for i in range(1, 11)]
    data = simulate_data(sensor_ids, readings_per_sensor=1000)

    data_by_sensor = build_partitioned_index(data)
    target_sensor = "S1"
    sensor_readings = data_by_sensor[target_sensor]

    start_time = sensor_readings[200]["timestamp"]
    end_time = sensor_readings[800]["timestamp"]

    baseline_result = range_query_baseline(target_sensor, start_time, end_time, data)
    optimized_result = range_query_optimized(
        target_sensor,
        start_time,
        end_time,
        data_by_sensor
    )

    assert len(baseline_result) == len(optimized_result)