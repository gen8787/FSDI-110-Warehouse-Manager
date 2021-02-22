"""
name: Warehouse Management System
author: Gary N
functionality:
    1 - Register products
"""

# I M P O R T S
import os
import time

from datetime import datetime
from menu import init, clear_screen, print_header
from product import Product
from create_product import *


# G L O B A L   V A R S


# D I S P L A Y   A L L   P R O D U C T S
def display_products():
    clear_screen()
    print_header("All Products:")

    for prod in all_products:
        prod.print()

    print("\n")
    input("Press any key to continue...")


# I N S T R U C T I O N S
while (True):
    init()
    option = input("Select an option: ")

    if (option == "q"):
        print("Closing...")
        time.sleep(0.5)
        os.system('clear')
        break

    elif (option == "1"):
        create_product()

    elif (option == "2"):
        display_products()
