from enum import Enum


class Animal(Enum):
    cat = 1
    dog = 2
    goat = 3
    whale = 4
    alpaca = 5


Animals2 = Enum(value='Animals', names=('cat dog goat whale alpaca'))

if __name__ == '__main__':
    print(Animal.goat)  # Animal.goat
    print(Animal.goat.name)  # goat
    print(Animal.goat.value)  # 3

    # Iteration

    for item in Animal:
        print(item.name, item.value)

    for member in Animals2:
        print(member)
