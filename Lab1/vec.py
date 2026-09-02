import sys
import math
import random
from typing import Self


"""
A custom vector class implementation for educational purposes.
"""

class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = []
        else:
            elements = list(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        return Vec([round(x + y, 5) for x, y in zip(self.elements, t.elements)])


    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        #
        return Vec([round(x * scalar, 5) for x in self.elements])

    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        for i, val in enumerate(self.elements):
            self.elements[i] = round(val * scalar, 5)
        #
        return self

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")

        if len(self) != len(t):
            raise TypeError("Type error - vectors must be of same dimensions")

        result = []
        for i in range(len(self.elements)):
            result.append(round(self.elements[i] - t.elements[i], 5))

        return Vec(result)

    def __neg__(self) -> Self:
        result = []

        for value in self.elements:
            result.append(-value)

        return Vec(result)

    def __radd__(self, other):
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")

        return other + self

    def __iadd__(self, other):
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")

        if len(self.elements) != len(other.elements):
            raise TypeError("Type error - vectors must be of same dimensions")

        for i in range(len(self.elements)):
            self.elements[i] = round(
                self.elements[i] + other.elements[i], 5
            )

        return self

    # return a vector of @n zeroes. precondition: @n > 0
    @staticmethod
    def zeros(n: int) -> Self:
        if n <= 0:
            raise ValueError("Vector dimension must be greater than zero")

        return Vec([0 for _ in range(n)])

    # return a vector of @n. precondition: @n > 0
    @staticmethod
    def ones(n: int) -> Self:
        if n <= 0:
            raise ValueError("Vector dimension must be greater than zero")

        return Vec([1 for _ in range(n)])

    # return a vector of @n uniformly distributed numbers in [0, 1]. precondition: @n > 0
    @staticmethod
    def uniform(n: int) -> Self:
        if n <= 0:
            raise ValueError("Vector dimension must be greater than zero")

        values = []
        for _ in range(n):
            values.append(random.random())

        return Vec(values)

    # Calculates the Euclidean norm (L2 norm) of the vector.
    # sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)
    def norm(self) -> float:
        total = 0

        for value in self.elements:
            total += value * value

        return math.sqrt(total)


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
    v1 = Vec([0, 1, 1.03])
    print("Original vector:", v1)

    v2 = 2.2 * v1
    print("After scalar multiplication:", v2)

    v2 *= 5
    print("After multiplying again:", v2)

    result = v1 + v2
    print("Addition result:", result)

    zero_vec = Vec.zeros(7)
    print("Zero vector:", zero_vec)

    one_vec = Vec.ones(4)
    print("One vector:", one_vec)

    difference = v1 - v2
    print("Subtraction result:", difference)

    negative = -v1
    print("Negative of v1:", negative)

    v3 = Vec([2, 4, 6])
    v4 = Vec([1, 2, 3])

    print("v3:", v3)
    print("v4:", v4)
    print("v3 + v4:", v3 + v4)

    v3 += v4
    print("v3 after addition:", v3)

    random_vec = Vec.uniform(5)
    print("Random vector:", random_vec)

    print("Norm of v1:", v1.norm())