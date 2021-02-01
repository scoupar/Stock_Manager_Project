from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository


products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", all_products = products)

@products_blueprint.route("/products/new", methods =['GET'])
def new_product():
    suppliers = supplier_repository.select_all()
    return render_template("products/new.html", all_suppliers = suppliers)

@products_blueprint.route("/products", methods =['POST'])
def create_product():
    product_name = request.form['product_name']
    details = request.form['details']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    supplier = supplier_repository.select(request.form['supplier_id'])
    product = Product(product_name, details, stock_quantity, buying_cost, selling_price, supplier)
    product_repository.save(product)
    return redirect ('/products')

@products_blueprint.route("/products/<id>", methods = ['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html', product = product)

@products_blueprint.route("/products/<id>/edit", methods =["GET"])
def edit_product(id):
    product = product_repository.select(id)
    suppliers = supplier_repository.select_all()
    return render_template('products/edit.html', product =product, all_suppliers = suppliers)

@products_blueprint.route("/products/<id>", methods =['POST'])
def update_product(id):
    product_name = request.form['product_name']
    details = request.form['details']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    supplier = supplier_repository.select(request.form['supplier_id'])
    product = Product(product_name, details, stock_quantity, buying_cost, selling_price, supplier, id)
    product_repository.update(product)
    return redirect('/products')
