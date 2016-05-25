import argparse


def multiply(arr):
    a = 0
    if len(arr) > 0 and arr[0] > 0:
        a = 1
    for n in arr:
        a *= n
    return a


parser = argparse.ArgumentParser(description='Another try to make it.')
parser.add_argument('--verbose',
                    '-v',
                    action='store_true',
                    help='verbose flag')
parser.add_argument('nums', nargs='+', type=int)

argv = parser.parse_args()

if argv.verbose:
    print(argv.nums)
    print(multiply(argv.nums))
else:
    print(multiply(argv.nums))
