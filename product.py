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
        print(f"{str(self.id).rjust(3)} | {self.name.ljust(12)} | {self.cat.ljust(12)} | {str(self.stock).ljust(5)} | ${'{:,.2f}'.format(self.price)}")
