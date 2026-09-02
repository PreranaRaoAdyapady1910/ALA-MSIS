from vec import Vec
import numpy as np
import timeit

sizes = [2000, 4000, 8000, 16000, 32000, 64000]


def average_time(operation, runs=10):
    elapsed = timeit.timeit(operation, number=runs)
    return elapsed / runs


for size in sizes:

    vec_a = Vec.uniform(size)
    vec_b = Vec.uniform(size)

    np_a = np.random.random(size)
    np_b = np.random.random(size)

    results = {}

    results["Addition"] = (
        average_time(lambda: vec_a + vec_b),
        average_time(lambda: np_a + np_b)
    )

    results["Subtraction"] = (
        average_time(lambda: vec_a - vec_b),
        average_time(lambda: np_a - np_b)
    )

    results["Multiplication"] = (
        average_time(lambda: 2 * vec_a),
        average_time(lambda: 2 * np_a)
    )

    results["Negation"] = (
        average_time(lambda: -vec_a),
        average_time(lambda: -np_a)
    )

    results["Norm"] = (
        average_time(lambda: vec_a.norm()),
        average_time(lambda: np.linalg.norm(np_a))
    )

    print("\n" + "=" * 60)
    print(f"Vector size: {size}")
    print("=" * 60)

    print(f"{'Operation':<18}{'Vec (sec)':<18}{'NumPy (sec)':<18}")

    for operation, times in results.items():
        vec_time, numpy_time = times
        print(f"{operation:<18}{vec_time:<18.8f}{numpy_time:<18.8f}")