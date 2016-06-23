def mut1(arr):
    # .append called against arr object. arr obj
    # will be mutated.
    arr.append(15)


def mut2(arr):
    # arr variable is rebinded to a new reference
    # which points to another array. Original arr
    # has nothing in common with it.
    arr = [29]


j = []
mut1(j)
print(j)

mut2(j)
print(j)