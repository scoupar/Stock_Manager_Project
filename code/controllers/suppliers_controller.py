from flask import Flask, render_template, request, redirect, Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = suppliers)

@suppliers_blueprint.route("/suppliers/new", methods =["GET"])
def new_supplier():
    return render_template("suppliers/new.html")

@suppliers_blueprint.route("/suppliers", methods =['POST'])
def create_supplier():
    supplier_name = request.form['supplier_name']
    contact_info = request.form['contact_info']
    notes = request.form['notes']
    supplier = Supplier(supplier_name, contact_info, notes)
    supplier_repository.save(supplier)
    return redirect('/suppliers')