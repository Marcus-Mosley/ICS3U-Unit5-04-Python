#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on November 2020
# This program calculates the volume of a cylinder

import math


def cylinder_volume(radius_int, height_int):
    # This functions calculates the volume of a cylinder

    # Process
    volume = math.pi * radius_int**2 * height_int

    return volume


def main():
    # This function gets radius and height

    # Input
    while True:
        radius_str = input("Enter the radius of the cylinder (cm): ")

        try:
            radius_int = int(radius_str)
        except Exception:
            print("That is not an integer, please input a number!")
            print("")
        else:
            if radius_int <= 0:
                print("You have not a valid radius, please input a"
                      " positive number!")
                print("")
            else:
                break
    while True:
        height_str = input("Enter the height of the cylinder (cm): ")

        try:
            height_int = int(height_str)
        except Exception:
            print("That is not an integer, please input a number!")
            print("")
        else:
            if height_int <= 0:
                print("You have not a valid height, please input a"
                      " positive number!")
                print("")
            else:
                break
    print("")

    # Call Functions
    volume = cylinder_volume(radius_int, height_int)

    print("The volume of the cylinder is {0:.2f}cm^3!".format(volume))


if __name__ == "__main__":
    main()
