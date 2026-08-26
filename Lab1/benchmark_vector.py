from vec import Vec
import timeit

dimensions = [2000, 4000, 8000, 16000, 32000, 64000]

REPEAT_COUNT = 10


def average_time(function, repetitions=REPEAT_COUNT):
    elapsed = timeit.timeit(function, number=repetitions)
    return elapsed / repetitions


for dimension in dimensions:

    first = Vec.uniform(dimension)
    second = Vec.uniform(dimension)

    add_time = average_time(lambda: first + second)
    sub_time = average_time(lambda: first - second)
    mul_time = average_time(lambda: 2 * first)
    neg_time = average_time(lambda: -first)
    norm_time = average_time(lambda: first.norm())

    inplace_mul_time = average_time(
        lambda: Vec(first.elements).__imul__(2)
    )

    inplace_add_time = average_time(
        lambda: Vec(first.elements).__iadd__(second)
    )

    print("\n" + "=" * 15 + f" Vector size: {dimension} " + "=" * 15)

    print(f"Addition                  : {add_time:.8f} seconds")
    print(f"Subtraction               : {sub_time:.8f} seconds")
    print(f"Scalar multiplication     : {mul_time:.8f} seconds")
    print(f"In-place multiplication   : {inplace_mul_time:.8f} seconds")
    print(f"In-place addition         : {inplace_add_time:.8f} seconds")
    print(f"Negation                  : {neg_time:.8f} seconds")
    print(f"Norm                      : {norm_time:.8f} seconds")