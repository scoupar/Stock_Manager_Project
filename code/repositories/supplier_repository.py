from db.run_sql import run_sql

from models.supplier import Supplier 
from models.product import Product

def save(supplier):
    sql="INSERT INTO suppliers (supplier_name, contact_info, notes) VALUES (%s, %s, %s) RETURNING *"
    values = [supplier.supplier_name, supplier.contact_info, supplier.notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id =id
    return supplier

def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)