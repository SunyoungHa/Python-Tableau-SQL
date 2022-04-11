# importing  all from simpleInterest
from simpleInterest import *
from mortgage import *
from name import *

name()

def printMenu():
    print("____________________________")
    print("1 . Calculate Interest Rate")
    print("2 . Calculate Mortagae Payment")
    print("99 Quit the program")
    print("____________________________")


def main():
    printMenu()
    selection = input("Select one of the command number above: ")

    while selection != "99" :
        if selection == "1":
            print(interest())
        elif selection == "2":
            print(mortgage())
        else:
            print("Error: ", selection, "command not recongized")
        printMenu()
        selection = input("Select one of the command number above: ")

    print("Have a nice day..")


main()
