from sympy import pi, isprime


def first_10prime_in_pi() -> int:
    digits = "3" + str(pi.evalf())[2:]
    M = len(digits)
    for i in range(1, M - 9):
        n = int(digits[i:i + 10])
        if isprime(n):
            return n
    return 0


if __name__ == '__main__':
    print(first_10prime_in_pi())
