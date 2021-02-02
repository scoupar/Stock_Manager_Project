from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository


def save(product):
    sql = "INSERT INTO products (product_name, details, stock_quantity, buying_cost, selling_price, supplier_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.product_name, product.details, product.stock_quantity, product.buying_cost, product.selling_price, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product


def select_all():
    products =[]
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        product = Product(row['product_name'], row['details'], row['stock_quantity'], row['buying_cost'], row['selling_price'], supplier, row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        supplier = supplier_repository.select(result['supplier_id'])
        product = Product(result['product_name'], result['details'], result['stock_quantity'], result['buying_cost'], result['selling_price'], supplier, result['id'])
    return product

def delete_all():
    sql ="DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id =%s"
    values =[id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (product_name, details, stock_quantity, buying_cost, selling_price, supplier_id) = (%s, %s, %s, %s, %s, %s) WHERE id =%s"
    values = [product.product_name, product.details, product.stock_quantity, product.buying_cost, product.selling_price, product.supplier.id, product.id]
    run_sql(sql, values)

def update_stock(product):
    sql = "UPDATE products SET (stock_quantity) = (%s) WHERE id =%s"
    values = [product.stock_quantity]
    run_sql(sql, values)