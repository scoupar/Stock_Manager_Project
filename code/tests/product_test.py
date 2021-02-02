import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Burger", "6oz Beef Patty", 50, 2.00, 3.50, "Rodgers")

    def test_product_has_name(self):
        self.assertEqual("Burger", self.product.product_name)

    def test_product_has_details(self):
        self.assertEqual("6oz Beef Patty", self.product.details)
        
    def test_product_has_stock_quantity(self):
        self.assertEqual(50, self.product.stock_quantity)

    def test_product_has_buying_cost(self):
        self.assertEqual(2.00, self.product.buying_cost)

    def test_product_has_selling_price(self):
        self.assertEqual(3.50, self.product.selling_price)

    def test_product_has_supplier(self):
        self.assertEqual("Rodgers", self.product.supplier)

    def test_product_id_starts_none(self):
        self.assertEqual(None, self.product.id)

    def test_mark_up(self):
        mark_up =self.product.markup(self.product.buying_cost, self.product.selling_price)
        self.assertEqual(1.50, mark_up)
        
