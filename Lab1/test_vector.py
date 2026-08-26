from vec import Vec

v = Vec.zeros(5)
assert v.elements == (0, 0, 0, 0, 0)

v1 = Vec([1, 3, 5])
v2 = Vec([2, 4, 4])

addition = v1 + v2
assert addition.elements == (3, 7, 9)

subtraction = v1 - v2
assert subtraction.elements == (-1, -1, 1)

v3 = Vec([1, 2, 3])
multiplication = 2 * v3
assert multiplication.elements == (2, 4, 6)

v4 = Vec([1, 2, 3])
v4 *= 3
assert v4.elements == (3, 6, 9)

v5 = Vec([1, 2, 3])
negative = -v5
assert negative.elements == (-1, -2, -3)

v6 = Vec([1, 2, 3])
v7 = Vec([4, 5, 6])
v6 += v7
assert v6.elements == (5, 7, 9)

v8 = Vec.ones(4)
assert v8.elements == (1, 1, 1, 1)

v9 = Vec([10, 20, 30, 40])
assert len(v9) == 4

v10 = Vec([3, 4])
assert v10.norm() == 5

try:
    Vec([1, 3, "Hellohiiiiholaaaa"])
    assert False
except TypeError:
    pass

try:
    Vec([1, 2]) + Vec([1, 2, 3])
    assert False
except TypeError:
    pass