# I M P O R T S
import os
import time
import pickle

from datetime import datetime
from menu import init, clear_screen, print_header, print_table_header
from product import Product
from create_product import *


# G L O B A L   V A R S
data_file = "warehouse.data"


# D I S P L A Y   A L L   P R O D U C T S
def display_products(header_txt=" All Products:"):
    clear_screen()
    print_header(header_txt)

    print_table_header()

    for prod in all_products:
        prod.print()

    print("\n")


# O U T   O F   S T O C K
def out_of_stock():
    clear_screen()
    print_header(" Report: Out of Stock Products:")

    print_table_header()

    for prod in all_products:
        if prod.stock == 0:
            prod.print()

    print("\n")


# S T O C K   V A L U E
def stock_value():
    clear_screen()
    print_header(" Report: Total Stock Value:")

    stock_value = 0.00

    for prod in all_products:
        stock_value += (prod.stock * prod.price)

    print(f"Total Stock Value: ${'{:,.2f}'.format(stock_value)}")
    print("\n")


# C H E A P E S T   P R O D U C T
def cheapest_prod():
    clear_screen()
    print_header(" Report: Cheapest Product:")

    cheapest_prod_name = ""
    cheapest_prod_price = all_products[0].price

    for prod in all_products:
        if (prod.price < cheapest_prod_price):
            cheapest_prod_name = prod.name
            cheapest_prod_price = prod.price

    print(
        f"Cheapest Product: {cheapest_prod_name} ${'{:,.2f}'.format(cheapest_prod_price)}")
    print("\n")


# D E L E T E   P R O D U C T
def delete_product():
    display_products(" Delete Product:")

    try:
        prod_to_delete = int(input("Enter Id to delete: "))

        found = False
        for prod in all_products:
            if (prod.id == prod_to_delete):
                found = True
                all_products.remove(prod)
                print(f"{prod.name} deleted")

        if (not found):
            print("*** Error: Id not found ***")

    except:
        print("*** Error: Invalid number ***")

    print("\n")


# U P D A T E   P R O D U C T
def update_product():
    display_products(" Update Product:")

    try:
        prod_to_update = int(input("Enter Id to update: "))

        found = False
        for prod in all_products:
            if (prod.id == prod_to_update):
                found = True
                prod_stock = int(input("Enter total stock: #"))
                prod_price = float(input("Enter product price: $"))
                prod.stock = prod_stock
                prod.price = prod_price
                print(f"{prod.name} updated")

        if (not found):
            print("*** Error: Id not found ***")

    except:
        print("*** Error: Invalid number ***")

    print("\n")


# P R O D U C T   C A T E G O R I E S
def prod_categories():
    clear_screen()
    print_header(" Report: Product Categories:")

    cats_list = []

    for prod in all_products:
        cats_list.append(prod.cat)
        # cats_set.add(prod.cat)

    cats_set = set(cats_list)

    for cat in cats_set:
        print(f" {cat}")

    print("\n")


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

        print(f"*** {len(all_products)} products loaded ***")

    except:
        print("*** Error: Data not loaded ***")


# I N S T R U C T I O N S
load_data(data_file)
input("Press enter to continue...")

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

    elif (option == "6"):
        delete_product()
        save_data(data_file)

    elif (option == "7"):
        update_product()
        save_data(data_file)

    elif (option == "8"):
        prod_categories()

    input("Press enter to continue...")
