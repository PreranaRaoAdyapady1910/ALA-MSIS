
import sys
import random
import math
from typing import Self


"""
A custom vector class implementation for educational purposes.
"""

class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = ()
        else:
            elements = tuple(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        return Vec(tuple(
            round(x + y, 5)
            for x, y in zip(self.elements, t.elements)
        ))


    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        return Vec(tuple(
            round(x * scalar, 5)
            for x in self.elements
        ))

    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        self.elements = tuple(
            round(x * scalar, 5)
            for x in self.elements
        )
        return self

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        return Vec(tuple(
            round(x - y, 5)
            for x, y in zip(self.elements, t.elements)
        ))

    def __neg__(self) -> Self:
        return Vec(tuple(-x for x in self.elements))

    def __radd__(self, other: Self) -> Self:
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")

        return other + self

    def __iadd__(self, other: Self) -> Self:
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")

        if len(self.elements) != len(other):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        self.elements = tuple(
            round(x + y, 5)
            for x, y in zip(self.elements, other.elements)
        )
        return self

    # return a vector of @n zeroes. precondition: @n > 0
    @staticmethod
    def zeros(n: int) -> Self:
        if n <= 0:
            raise ValueError("The dimension must be greater than 0")

        return Vec((0,) * n)

    # return a vector of @n. precondition: @n > 0
    @staticmethod
    def ones(n: int) -> Self:
        if n <= 0:
            raise ValueError("The dimension must be greater than 0")

        return Vec((1,) * n)

    # return a vector of @n uniformly distributed numbers in [0, 1]. precondition: @n > 0
    @staticmethod
    def uniform(n: int) -> Self:
        if n <= 0:
            raise ValueError("The dimension must be greater than 0")

        return Vec(tuple(
            round(random.uniform(0, 1), 5)
            for _ in range(n)
        ))

    # Calculates the Euclidean norm (L2 norm) of the vector.
    # sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)
    def norm(self) -> float:
        return math.sqrt(
            sum(x * x for x in self.elements)
        )


"""
(1) Understand the basic design of the vector abstraction. Review the implementation.
(2) Document each function.
(3) Implement all unimplemented methods.
(4) Create appropriate tests for this implementation, increasing the confidence about its correctness.
(5) Test this implementation by importing the class in a sepatate python script.

(6) Measure the performance of each of these functions on vectors of varying lengths.
    Try 2k to 64k dimension vectors and time the results.
    How would you do the measurements?
(7) Measure the performance on your machine. Check it on colab.

(8) use numpy and compare the performance.
"""


if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":
    v1 = Vec([1, 2, 3])
    v2 = Vec([3, 5, 6])

    print("v1 =", v1)
    print("v2 =", v2)

    v3 = -v1
    print("Negative v1 =", v3)

    print("Type of v1 =", type(v1))
    print("Type of elements =", type(v2.elements))

    v4 = v1 + v2
    print("v1 + v2 =", v4)

    v5 = v1 - v2
    print("v1 - v2 =", v5)

    v6 = 5 * v5
    print("5 * v5 =", v6)

    v6 *= 67
    print("v6 after *= 67 =", v6)

    v7 = v1 + v2
    print("v7 =", v7)

    v7 += v1
    print("v7 after += v1 =", v7)

    print("Zeros =", Vec.zeros(6))
    print("Ones =", Vec.ones(7))
    print("Uniform =", Vec.uniform(3))

    v8 = Vec([-3, 2, -1, 1, -1])
    print("v8 =", v8)
    print("Norm of v8 =", v8.norm())