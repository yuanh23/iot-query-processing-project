import time

from baseline_query import latest_reading_baseline, range_query_baseline
from optimized_query import latest_reading_optimized, range_query_optimized


def compare_latest_query_times(sensor_id, data, latest_cache):
    start = time.perf_counter()
    baseline_result = latest_reading_baseline(sensor_id, data)
    baseline_time = time.perf_counter() - start

    start = time.perf_counter()
    optimized_result = latest_reading_optimized(sensor_id, latest_cache)
    optimized_time = time.perf_counter() - start

    return {
        "baseline_result": baseline_result,
        "baseline_time": baseline_time,
        "optimized_result": optimized_result,
        "optimized_time": optimized_time,
    }


def compare_range_query_times(sensor_id, start_time, end_time, data, data_by_sensor):
    start = time.perf_counter()
    baseline_result = range_query_baseline(sensor_id, start_time, end_time, data)
    baseline_time = time.perf_counter() - start

    start = time.perf_counter()
    optimized_result = range_query_optimized(sensor_id, start_time, end_time, data_by_sensor)
    optimized_time = time.perf_counter() - start

    return {
        "baseline_result_count": len(baseline_result),
        "baseline_time": baseline_time,
        "optimized_result_count": len(optimized_result),
        "optimized_time": optimized_time,
    }