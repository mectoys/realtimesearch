from flask import Flask
from src.routes import route_product
import os

template_dir = os.path.abspath('src/templates')
app = Flask(__name__, template_folder=template_dir)
if __name__ == '__main__':
    app.register_blueprint(route_product.main, url_prefix='/')
    app.run(debug=True)
