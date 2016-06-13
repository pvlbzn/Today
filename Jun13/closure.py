def close_over(n):
    def func(j):
        return n + j

    return func


if __name__ == '__main__':
    c = close_over(5)
    print(c(15))
