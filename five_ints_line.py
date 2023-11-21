#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 20th, 2023
# This program displays all the integers between 1000 and 2000,
# 5 integers per line


def main():
    for counter in range(1000, 2001):
        if counter == 1000:
            print(counter, " ", end="")
        elif counter % 5 == 0:
            print("{} \n".format(counter))
        else:
            print(counter, " ", end="")


if __name__ == "__main__":
    main()
