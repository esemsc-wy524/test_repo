import argparse

def find_prime(n):
    primes = []
    i = 2
    while True:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1
        if len(primes) >= n:
            break
    return primes


# The function find_prime(n) returns a list of prime numbers less than n.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Perform arithmetic operations'
    )
    parser.add_argument('-n', "--num", type=int)
    args = parser.parse_args()
    print(find_prime(args.num))