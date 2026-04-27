from sensor_simulator import simulate_data
from optimized_query import build_latest_cache, build_partitioned_index
from experiment import compare_latest_query_times, compare_range_query_times


def run_experiment(readings_per_sensor):
    sensor_ids = [f"S{i}" for i in range(1, 11)]

    print(f"\nGenerating data with {readings_per_sensor} readings per sensor...")
    data = simulate_data(sensor_ids, readings_per_sensor=readings_per_sensor)

    total_readings = len(data)
    print(f"Total readings generated: {total_readings}")

    latest_cache = build_latest_cache(data)
    data_by_sensor = build_partitioned_index(data)

    target_sensor = "S1"

    # Latest-reading query
    latest_result = compare_latest_query_times(
        target_sensor,
        data,
        latest_cache
    )

    # Time-range query
    sensor_readings = data_by_sensor[target_sensor]

    start_index = int(len(sensor_readings) * 0.2)
    end_index = int(len(sensor_readings) * 0.8)

    start_time = sensor_readings[start_index]["timestamp"]
    end_time = sensor_readings[end_index]["timestamp"]

    range_result = compare_range_query_times(
        target_sensor,
        start_time,
        end_time,
        data,
        data_by_sensor
    )

    print("\n--- Latest Reading Query ---")
    print(f"Baseline time: {latest_result['baseline_time']:.10f} seconds")
    print(f"Optimized time: {latest_result['optimized_time']:.10f} seconds")

    print("\n--- Time-Range Query ---")
    print(f"Baseline results found: {range_result['baseline_result_count']}")
    print(f"Optimized results found: {range_result['optimized_result_count']}")
    print(f"Baseline time: {range_result['baseline_time']:.10f} seconds")
    print(f"Optimized time: {range_result['optimized_time']:.10f} seconds")

    return {
        "total_readings": total_readings,
        "latest_baseline_time": latest_result["baseline_time"],
        "latest_optimized_time": latest_result["optimized_time"],
        "range_baseline_time": range_result["baseline_time"],
        "range_optimized_time": range_result["optimized_time"],
        "range_baseline_count": range_result["baseline_result_count"],
        "range_optimized_count": range_result["optimized_result_count"],
    }


def main():
    experiment_sizes = [1000, 5000, 10000]

    results = []

    for size in experiment_sizes:
        result = run_experiment(size)
        results.append(result)

    print("\n==============================")
    print("Summary Results")
    print("==============================")

    print(
        "Total Readings | Latest Baseline | Latest Optimized | "
        "Range Baseline | Range Optimized"
    )

    for result in results:
        print(
            f"{result['total_readings']} | "
            f"{result['latest_baseline_time']:.10f} | "
            f"{result['latest_optimized_time']:.10f} | "
            f"{result['range_baseline_time']:.10f} | "
            f"{result['range_optimized_time']:.10f}"
        )


if __name__ == "__main__":
    main()