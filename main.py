from sensor_simulator import simulate_data
from optimized_query import build_latest_cache, build_partitioned_index
from experiment import compare_latest_query_times, compare_range_query_times


def main():
    sensor_ids = [f"S{i}" for i in range(1, 11)]

    print("Generating sensor data...")
    data = simulate_data(sensor_ids, readings_per_sensor=1000)

    print(f"Total readings generated: {len(data)}")

    latest_cache = build_latest_cache(data)
    data_by_sensor = build_partitioned_index(data)

    target_sensor = "S1"

    print("\n--- Latest Reading Query ---")
    latest_result = compare_latest_query_times(target_sensor, data, latest_cache)

    print(f"Baseline time: {latest_result['baseline_time']:.10f} seconds")
    print(f"Optimized time: {latest_result['optimized_time']:.10f} seconds")

    sensor_readings = data_by_sensor[target_sensor]
    start_time = sensor_readings[200]["timestamp"]
    end_time = sensor_readings[800]["timestamp"]

    print("\n--- Time-Range Query ---")
    range_result = compare_range_query_times(
        target_sensor,
        start_time,
        end_time,
        data,
        data_by_sensor
    )

    print(f"Baseline results found: {range_result['baseline_result_count']}")
    print(f"Optimized results found: {range_result['optimized_result_count']}")
    print(f"Baseline time: {range_result['baseline_time']:.10f} seconds")
    print(f"Optimized time: {range_result['optimized_time']:.10f} seconds")


if __name__ == "__main__":
    main()