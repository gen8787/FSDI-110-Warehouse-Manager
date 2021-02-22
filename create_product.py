# I M P O R T S
import time

from menu import init, clear_screen, print_header
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

        if (prod_stock < 0):
            print("*** Error: Stock cannot be less than 0 ***")

        new_product = Product(1, prod_name, prod_cat, prod_stock, prod_price)
        all_products.append(new_product)

        print("adding product...")
        print(new_product.name)
        time.sleep(0.5)

        print("\n")
        print("Product added.")

        another = input("Add another product? (y / n)")
        if (another == "y"):
            create_product()
        elif (another == "n"):
            init()
        else:
            init()

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
