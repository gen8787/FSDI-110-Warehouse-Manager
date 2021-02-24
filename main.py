"""
name: Warehouse Management System
author: Gary N
functionality:
    1 - Register products
"""

# I M P O R T S
import os
import time
import pickle

from datetime import datetime
from menu import init, clear_screen, print_header
from product import Product
from create_product import *


# G L O B A L   V A R S
data_file = "warehouse.data"


# D I S P L A Y   A L L   P R O D U C T S
def display_products():
    clear_screen()
    print_header("All Products:")

    # print("ID".ljust(3)("Product Name").ljust(20)(
    #     "Category").ljust(10)("Stock").ljust(3)("Price"))
    for prod in all_products:
        prod.print()

    print("\n")
    input("Press any key to continue...")


# O U T   O F   S T O C K
def out_of_stock():
    clear_screen()
    print_header("Report: Out of Stock Products:")

    for prod in all_products:
        if prod.stock == 0:
            prod.print()

    print("\n")
    input("Press any key to continue...")


# S T O C K   V A L U E
def stock_value():
    clear_screen()
    print_header("Report: Total Stock Value:")

    stock_value = 0.00

    for prod in all_products:
        stock_value += (prod.stock * prod.price)

    print(f"Total Stock Value: ${'{:,.2f}'.format(stock_value)}")
    print("\n")
    input("Press any key to continue...")


# C H E A P E S T   P R O D U C T
def cheapest_prod():
    clear_screen()
    print_header("Report: Cheapest Product:")

    cheapest_prod_name = ""
    cheapest_prod_price = all_products[0]

    for prod in all_products:
        if (prod.price < cheapest_prod_price):
            cheapest_prod_name = prod.name
            cheapest_prod_price = prod.price

    print(
        f"Cheapest Product: {cheapest_prod_name} ${'{:,.2f}'.format(cheapest_prod_price)}")
    print("\n")
    input("Press any key to continue...")


# S A V E   D A T A
def save_data(file_name):
    try:
        writer = open(file_name, 'wb')
        pickle.dump(all_products, writer)
        writer.close()
        print("*** Data Serialized ***")

    except:
        print("*** Error: Data not saved ***")


# L O A D   D A T A
def load_data(file_name):
    try:
        reader = open(file_name, 'rb')
        temp_list = pickle.load(reader)

        for prod in temp_list:
            all_products.append(prod)

        reader.close()

        # num_prod = len(all_products)
        print(f"*** {len(all_products)} products loaded ***")

    except:
        print("*** Error: Data not loaded ***")


# I N S T R U C T I O N S
load_data(data_file)
input("Press any key to continue...")

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
        save_data(data_file)

    elif (option == "2"):
        display_products()

    elif (option == "3"):
        out_of_stock()

    elif (option == "4"):
        stock_value()

    elif (option == "5"):
        cheapest_prod()
