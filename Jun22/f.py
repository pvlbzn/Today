from functools import reduce

n = [1, 2, 3, 4, 5]


def t1_iter():
    q = []
    for x in n:
        q.append(x**2)
    return q


def t1_map():
    def sqr(x):
        return x**2

    return list(map(sqr, n))


def t1_map_lambda():
    return list(map((lambda x: x**2), n))


print(t1_iter())
print(t1_map())
print(t1_map_lambda())

# [1, 4, 9, 16, 25]
# [1, 4, 9, 16, 25]
# [1, 4, 9, 16, 25]


def sq(x):
    return x**2


def cb(x):
    return x**3


f = [sq, cb]

for r in range(3):
    val = list(map(lambda x: x(r), f))
    print(val)

# [0, 0]
# [1, 1]
# [4, 8]

#
# Filter
#

res = list(filter(lambda x: x < 0, range(-5, 5)))
print(res)
# [-5, -4, -3, -2, -1]

#
# Reduce
#

red = reduce(lambda x, y: x / y, [1, 2, 3, 4])
print(red)
# 0.041666666666666664