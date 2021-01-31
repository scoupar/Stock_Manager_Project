import pdb
from models.product import Product
from models.supplier import Supplier
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository


supplier_repository.delete_all()
product_repository.delete_all()

supplier1 = Supplier("Dunns", "0141 1234567", "must order before 5PM")
supplier_repository.save(supplier1)

supplier2 = Supplier("Rodgers", "0141 234546", "no deliveries on a Sunday")
supplier_repository.save(supplier2)

# print(supplier_repository.select_all())

# print(supplier_repository.select(3))


product1 = Product("Burger", "6oz Beef Patty", 50, 1.99, 2.48, supplier2)
product_repository.save(product1)

product2 = Product("Bun", "Brioche burger bun", 50, 0.79, 1.20, supplier2)
product_repository.save(product2)

# print(product_repository.select_all())
# print(product_repository.select(14))
# supplier1 = Supplier("Dunns Drinks", "0141 1234568", "order tues and friday only")
# supplier_repository.save(supplier1)
# product2 = Product("Coke", "case of 24 cans", 2, 5.45, 15, supplier1)
# product_repository.save(product2)
