class Product:
    def __init__(self, product_name, details, stock_quantity, buying_cost, selling_price, supplier, id= None):
        self.product_name = product_name
        self.details = details
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.supplier = supplier
        self.id = id

    def markup(self, buy_price, sell_price):
        mark_up = sell_price - buy_price
        return mark_up
        
