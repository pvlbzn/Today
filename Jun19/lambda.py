# Python also has an anonymous functions, but a bit differently.
# General syntax is `lambda arg1, ...argN : expression using args`
l = lambda x, y: x * y
print(l(4, 4))

# Or, alternatively
print((lambda x, y: x * y)(4, 4))

# More useful. Title arg will be passed as default.
def writer():
    title = 'Mr.'
    name = (lambda x: title + ' ' + x)
    return name

who = writer()
print(who('James Johnes'))
