from flask import Flask, render_template

from controllers.stock_controller import stock_blueprint

app = Flask(__name__)

app.register_blueprint(stock_blueprint)

if __name__=='__main__':
    app.run(debug=True)