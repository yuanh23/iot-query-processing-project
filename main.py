from sensor_simulator import simulate_data
from optimized_query import build_latest_cache
from experiment import compare_query_times


def main():
    sensor_ids = [f"S{i}" for i in range(1, 11)]

    print("Generating sensor data...")
    data = simulate_data(sensor_ids, readings_per_sensor=1000)

    print(f"Total readings generated: {len(data)}")

    latest_cache = build_latest_cache(data)

    target_sensor = "S1"
    result = compare_query_times(target_sensor, data, latest_cache)

    print("\nBaseline result:")
    print(result["baseline_result"])
    print(f"Baseline time: {result['baseline_time']:.10f} seconds")

    print("\nOptimized result:")
    print(result["optimized_result"])
    print(f"Optimized time: {result['optimized_time']:.10f} seconds")


if __name__ == "__main__":
    main()