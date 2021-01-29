import unittest
from models.supplier import Supplier

class TestSupplier(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("Dunns", "0141 123456", "order before 5PM")


    def test_supplier_has_name(self):
        self.assertEqual("Dunns", self.supplier.name)

    def test_supplier_has_contact_info(self):
        self.assertEqual("0141 123456", self.supplier.contact_info)

    def test_supplier_has_notes(self):
        self.assertEqual("order before 5PM", self.supplier.notes)

    def test_supplier_id_starts_none(self):
        self.assertEqual(None, self.supplier.id)