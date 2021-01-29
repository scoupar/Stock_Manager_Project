import pdb
from models.product import Product
from models.supplier import Supplier

import repositories.supplier_repository as supplier_repository

supplier_repository.delete_all()

supplier1 = Supplier("Dunns", "0141 1234567", "must order before 5PM")
supplier_repository.save(supplier1)

pdb.set_trace()