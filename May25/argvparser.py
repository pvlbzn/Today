import argparse


def parse_args(p):
    args = p.parse_args()

    print(args.square)

    if args.version:
        print("argvparser 0.01")
        return 0

    if args.num and args.num != "0":
        print(args.num)


def set_args():
    p = argparse.ArgumentParser(
        description="Dummy programm to understand how to parse "
        "arguments in more robustly, conviniently. ")
    p.add_argument("-v",
                   "--version",
                   action="store_true",
                   help="show version number")
    p.add_argument("num", nargs="?", default="0")
    return p


if __name__ == '__main__':
    p = set_args()
    parse_args(p)