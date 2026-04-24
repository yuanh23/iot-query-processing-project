import time
from baseline_query import latest_reading_baseline
from optimized_query import latest_reading_optimized


def compare_query_times(sensor_id, data, latest_cache):
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