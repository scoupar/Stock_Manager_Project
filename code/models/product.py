class Product:
    def __init__(self, product_name, description, stock_quantity, buying_cost, selling_price, supplier, id =None):
        self.product_name = product_name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.supplier = supplier
        self.id = id
