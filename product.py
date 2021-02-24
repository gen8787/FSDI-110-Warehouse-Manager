class Product:
    id = 0
    name = ""
    cat = ""
    stock = 0
    price = 0.00

    def __init__(self, id, name, cat, stock, price):
        self.id = id
        self.name = name
        self.cat = cat
        self.stock = stock
        self.price = price

    def __str__(self):
        return self.name

    def print(self):
        print(f"ID: {str(self.id).rjust(3)} | {self.name.ljust(20)} | Category: {self.cat.ljust(10)} | Stock: {str(self.stock).ljust(3)} | Price: ${'{:,.2f}'.format(self.price)}")

# var.ljust(30)
