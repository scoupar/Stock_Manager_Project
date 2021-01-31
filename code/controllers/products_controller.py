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

# @products_blueprint.route("/products", methods =['POST'])
# def create_product():


