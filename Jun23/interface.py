# There is a simple trick to forse a child to implement
# some methods without using abc


class Super:
    def method(self):
        raise NotImplementedError("Method should be implemented.")


class Child(Super):
    def another_method(self):
        print('Another')


if __name__ == '__main__':
    c = Child()
    # Will print 'Another'
    c.another_method()
    # And crash with
    # NotImplementedError: Method should be implemented.
    c.method()
