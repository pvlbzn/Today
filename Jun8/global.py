'''
Execution of this script will output following:
> 5
> 5
> There is no n
> 10
> There is n: 105
'''

# Global variable
x = 5


def glob():
    # Mutate global variable
    global x
    x = 10
    # Declare new global variable
    global n
    n = 105


def loc():
    # Declare and intialize local variable
    # They wont be visible in the global scope
    x = 25
    n = 50


def check_n():
    try:
        if n:
            print("There is n:", n)
    except NameError:
        print("There is no n")


if __name__ == '__main__':
    # Print initial state
    print(x)
    # Mutate localy
    loc()
    print(x)
    # Check
    check_n()
    # Mutate and print new state
    glob()
    print(x)
    # Check
    check_n()