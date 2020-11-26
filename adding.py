#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Program adds 2 numbers


def main():
    # This function calculates the cost of a pizza

    # Input
    first_number = int(input("Please enter the first number: "))
    second_number = int(input("Please enter the second number: "))
    print("This program adds 2 numbers together!")
    
    # Process
    sum = first_number + second_number

    # Output
    print("{0}+{1}={2}".format(first_number, second_number, sum))

if __name__ == "__main__":
    main()
