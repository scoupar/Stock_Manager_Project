DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(255),
    contact_info VARCHAR(255),
    notes VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buying_cost FLOAT, 
    selling_price FLOAT,
    supplier_id INT REFERENCES suppliers(id) ON DELETE CASCADE
);