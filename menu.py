# I M P O R T S
import os


# I N I T
def init():
    clear_screen()
    print("\n")
    print("*" * 30)
    print("Warehouse Management System")
    print("*" * 30)
    print("\n")

    print("Main Menu:")
    print("\n")
    print(" [1] Register Product")
    print(" [2] Print Catalog")
    print(" [3] Report: Out of Stock")
    print(" [4] Report: Stock Value")
    print(" [5] Report: Cheapest Product")
    print(" [q] Quit")
    print("\n")


# C L E A R   S C R E E N
def clear_screen():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")


# P R I N T   H E A D E R
def print_header(header_txt):
    print("\n")
    print("-" * 30)
    print(header_txt)
    print("-" * 30)
    print("\n")
