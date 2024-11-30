import argparse


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Perform arithmetic operations'
    )
    parser.add_argument('-o',
                        "--operation",
                        choices=['add', 'subtract', 'multiply', 'divide']
                        )
    parser.add_argument('-n1', "--x", type=float)
    parser.add_argument('-n2', "--y", type=float)
    args = parser.parse_args()
    if args.operation == 'add':
        print(add(args.x, args.y))
    elif args.operation == 'subtract':
        print(subtract(args.x, args.y))
    elif args.operation == 'multiply':
        print(multiply(args.x, args.y))
    elif args.operation == 'divide':
        print(divide(args.x, args.y))
    else:
        print('Invalid operation')
