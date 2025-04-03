#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: Feb 27, 2025
# This program tell the user if they are tall enough to go on the rollercoaster


def main():

    try:

        # Get user_height
        user_height = int(input("Enter you height in cm:"))

        # Check if they are eligible to ride the rollercoaster

        if user_height < 0:
            print("Enter a valid height")
        elif user_height >= 155:
            print("You can get on the ride")
        else:
            print("You are too short to get on the ride")

    except ValueError:
        print("This is not a valid number")

    finally:
        print("Thanks for playing")


if __name__ == "__main__":

    main()
