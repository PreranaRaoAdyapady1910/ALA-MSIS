from vec import Vec
import timeit
import platform

sizes = [2000, 4000, 8000, 16000, 32000, 64000]


def get_time(operation):
    runs = 10
    result = timeit.timeit(operation, number=runs)
    return result / runs


def test_inplace_multiply(vector):
    copy = Vec(vector.elements)
    copy *= 2


def test_inplace_add(vector1, vector2):
    copy = Vec(vector1.elements)
    copy += vector2


for size in sizes:
    vector1 = Vec.uniform(size)
    vector2 = Vec.uniform(size)

    timings = {
        "Addition": get_time(lambda: vector1 + vector2),
        "Subtraction": get_time(lambda: vector1 - vector2),
        "Multiplication": get_time(lambda: 2 * vector1),
        "In-place multiplication": get_time(
            lambda: test_inplace_multiply(vector1)
        ),
        "In-place addition": get_time(
            lambda: test_inplace_add(vector1, vector2)
        ),
        "Negation": get_time(lambda: -vector1),
        "Norm": get_time(lambda: vector1.norm())
    }

    print("\n" + "-" * 50)
    print(f"Vector dimension: {size}")
    print("-" * 50)

    for operation, elapsed in timings.items():
        print(f"{operation:<25} {elapsed:.8f} seconds")


print("\nMachine Information")
print("-" * 50)
print("Python version :", platform.python_version())
print("System         :", platform.system())
print("Machine        :", platform.machine())
print("Processor      :", platform.processor())