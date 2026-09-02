from vec import Vec

zero_vector = Vec.zeros(5)
assert zero_vector.elements == [0, 0, 0, 0, 0]
print("zeros test successful")

v1 = Vec([1, 3, 5])
v2 = Vec([2, 4, 4])

addition = v1 + v2
assert addition.elements == [3, 7, 9]
print("addition test successful")

subtraction = v1 - v2
assert subtraction.elements == [-1, -1, 1]
print("subtraction test successful")

v3 = Vec([1, 2, 3])

multiplication = 2 * v3
assert multiplication.elements == [2, 4, 6]
print("scalar multiplication test successful")

v4 = Vec([1, 2, 3])
v4 *= 3

assert v4.elements == [3, 6, 9]
print("in-place multiplication test successful")

v5 = Vec([1, 2, 3])

negative = -v5
assert negative.elements == [-1, -2, -3]
print("negation test successful")

v6 = Vec([1, 2, 3])
v7 = Vec([4, 5, 6])

v6 += v7

assert v6.elements == [5, 7, 9]
print("in-place addition test successful")

one_vector = Vec.ones(4)
assert one_vector.elements == [1, 1, 1, 1]
print("ones test successful")

v8 = Vec([10, 20, 30, 40])
assert len(v8) == 4
print("length test successful")

v9 = Vec([3, 4])
assert v9.norm() == 5
print("norm test successful")

try:
    Vec([1, 3, "Hellohiiiiholaaaa"])
    assert False
except TypeError:
    print("invalid element test successful")

try:
    Vec([1, 2]) + Vec([1, 2, 3])
    assert False
except TypeError:
    print("dimension mismatch test successful")