#!/usr/bin/python

# Jack Cacela and Spencer Marks
# This Python program accepts a yes or no value, as well as a birth month and a day of the month from the command line and displays the corresponding constellation and related information.

# You need the CPHelper.py file in the same folder so it can be referenced from this file.
# Run this file like this in the command prompt: Python Celestial_Guide.py <yes> <february> <14>

import sys
import CPHelper


def CelestialGuide():
    print()
    print("Welcome to the Celestial Guide program.")
    print()
    print("This version is for those born in the Northern Hemisphere...")
    print()
    print("It is now time for you to discover what your birth constellation is.")
    print()
    print(
        "Once you discover and identify your constellation in the Northern Hemisphere night sky, this constellation will resonate with you and it will be available as a guide for you as you walk through life."
    )
    print()
    print()

    print("Are you ready to become awakened? ")

    print()
    print()

    answer = input("Enter yes or no: ")

    if answer != "yes":
        print("Please type 'yes' to proceed. ")

    else:
        birthday = input("Please enter your birth month in all lowercase. ")

        if birthday not in [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        ]:
            print("Please type a month such as 'february' to proceed. ")

        elif birthday == "january":
            janreply = input("Which day in January were you born? Enter a number such as 5 or 24: ")
            if janreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
                "31",
            ]:
                CPHelper.january()  # Corrected function call
            else:
                print("The number you entered is not within the month of January.")

        elif birthday == "february":
            febreply = input("Which day in february were you born? Enter a number such as 5 or 24: ")
            if febreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
            ]:
                CPHelper.february()  # Corrected function call
            else:
                print("The number you entered is not within the month of February.")

        elif birthday == "march":
            marchreply = input("Which day in March were you born? Enter a number such as 5 or 24: ")
            if marchreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
		"31",
            ]:
                CPHelper.march()  # Corrected function call
            else:
                print("The number you entered is not within the month of March.")


        elif birthday == "april":
            aprilreply = input("Which day in April were you born? Enter a number such as 5 or 24: ")
            if aprilreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
            ]:
                CPHelper.april()  # Corrected function call
            else:
                print("The number you entered is not within the month of April.")


        elif birthday == "may":
            mayreply = input("Which day in May were you born? Enter a number such as 5 or 24: ")
            if mayreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
		"31",
            ]:
                CPHelper.may()  # Corrected function call
            else:
                print("The number you entered is not within the month of May.")


        elif birthday == "june":
            junereply = input("Which day in June were you born? Enter a number such as 5 or 24: ")
            if junereply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
            ]:
                CPHelper.june()  # Corrected function call
            else:
                print("The number you entered is not within the month of June.")


        elif birthday == "july":
            julyreply = input("Which day in July were you born? Enter a number such as 5 or 24: ")
            if julyreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
		"31",
            ]:
                CPHelper.july()  # Corrected function call
            else:
                print("The number you entered is not within the month of July.")


        elif birthday == "august":
            augreply = input("Which day in August were you born? Enter a number such as 5 or 24: ")
            if augreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
		"31",
            ]:
                CPHelper.august()  # Corrected function call
            else:
                print("The number you entered is not within the month of August.")

        elif birthday == "september":
            sepreply = input("Which day in September were you born? Enter a number such as 5 or 24: ")
            if sepreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
            ]:
                CPHelper.september()  # Corrected function call
            else:
                print("The number you entered is not within the month of September.")

        elif birthday == "october":
            octreply = input("Which day in October were you born? Enter a number such as 5 or 24: ")
            if octreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
		"31",
            ]:
                CPHelper.october()  # Corrected function call
            else:
                print("The number you entered is not within the month of Cctober.")


        elif birthday == "november":
            novreply = input("Which day in November were you born? Enter a number such as 5 or 24: ")
            if novreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
            ]:
                CPHelper.november()  # Corrected function call
            else:
                print("The number you entered is not within the month of November.")


        elif birthday == "december":
            decreply = input("Which day in December were you born? Enter a number such as 5 or 24: ")
            if decreply in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
		"30",
		"31",
            ]:
                CPHelper.december()  # Corrected function call
            else:
                print("The number you entered is not within the month of December.")

CelestialGuide()


	
	

