"""
name: Warehouse Management System
author: Gary N
functionality:
    1 - Register products
"""

# I M P O R T S
import sys
from os import system
import time
from datetime import datetime
from menu import *
from product import Product


# G L O B A L   V A R S
all_products = []


# C R E A T E   P R O D U C T
def create_product():
    clear_screen()
    print_header("Register a new product:")

    try:
        prod_name = input("Enter product name: ")
        prod_cat = input("Enter product category: ")
        prod_stock = int(input("Enter total stock: #"))
        prod_price = float(input("Enter product price: $"))

        # validate

        new_product = Product(1, prod_name, prod_cat, prod_stock, prod_price)
        all_products.append(new_product)

        print("adding product...")
        print(new_product.name)
        time.sleep(0.5)

        print("\n")
        print("Product added.")

    except ValueError:
        print("*** Error: Invalid number ***")
        again = input("Try again? (y / n): ")
        if (again == "y"):
            create_product()
        elif (again == "n"):
            init()
        else:
            init()

    except:
        print("*** Error: Invalid input ***")

    input("Press any key to continue...")


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
        system('clear')
        break

    elif (option == "1"):
        create_product()

    elif (option == "2"):
        display_products()
