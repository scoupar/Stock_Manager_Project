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

def select_all():
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)
    for row in results:
        supplier = Supplier(row['supplier_name'], row['contact_info'], row['notes'], row['id'])
        suppliers.append(supplier)
    return suppliers

def select(id):
    supplier = None
    sql ="SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        supplier = Supplier(result['supplier_name'], result['contact_info'], result['notes'], result['id'])
    return supplier

def update(supplier):
    sql ="UPDATE suppliers SET (supplier_name, contact_info, notes) = (%s, %s, %s) WHERE id =%s"
    values = [supplier.supplier_name, supplier.contact_info, supplier.notes, supplier.id]
    run_sql(sql, values)



def delete(id):
    sql = "DELETE FROM suppliers WHERE id =%s"
    values =[id]
    run_sql(sql, values)
