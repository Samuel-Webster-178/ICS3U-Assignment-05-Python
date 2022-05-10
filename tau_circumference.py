#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


def CalculateFactors(number):
    # I calculate circumference
    i = 1
    factors = []

    # process
    while i <= number:
        is_int = number % i
        if is_int == 0:
            factors.append(i)
        i += 1

    # output
    return factors


def main():
    # I calculate circumference
    factors = []

    # input & output
    print("This program calculates the factors of an integer.")
    str_number = input("Your number is: ")
    try:
        int_number = int(str_number)
        factors = CalculateFactors(int_number)
        print("\nFactors: ", end="")
        for i in range(len(factors)):
            if i == len(factors) - 1:
                print(factors[i])
            else:
                print(factors[i], end=", ")
    except Exception:
        print("\nInvalid Input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
