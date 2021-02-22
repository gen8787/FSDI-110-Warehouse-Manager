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

    def print(self):
        print(
            f"ID: {self.id} | {self.name} | Category: {self.cat} | Stock: {self.stock} | Price: {self.price}")
