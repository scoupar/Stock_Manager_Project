import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Burger", "6oz Beef Patty", 50, 1.99, 2.58, "Rodgers")

    def test_product_has_name(self):
        self.assertEqual("Burger", self.product.name)

    def test_product_has_description(self):
        self.assertEqual("6oz Beef Patty", self.product.description)
        
    def test_product_has_stock_quantity(self):
        self.assertEqual(50, self.product.stock_quantity)

    def test_product_has_buying_cost(self):
        self.assertEqual(1.99, self.product.buying_cost)

    def test_product_has_selling_price(self):
        self.assertEqual(2.58, self.product.selling_price)

    def test_product_has_supplier(self):
        self.assertEqual("Rodgers", self.product.supplier)

    def test_product_id_starts_none(self):
        self.assertEqual(None, self.product.id)
