import argparse

def mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calculate the mean of a list of numbers'
    )
    parser.add_argument('-n', "--num", type=float, nargs='+')
    args = parser.parse_args()
    print(mean(args.num))