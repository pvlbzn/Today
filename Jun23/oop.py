class Human(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Greet you. My name is: " + self.name)


class Engineer(Human):
    def __init__(self, name):
        Human.__init__(self, name)

    def prof(self):
        print("My profession is an engineer.")


if __name__ == '__main__':
    eng = Engineer("Jack")
    eng.greet()
    eng.prof()