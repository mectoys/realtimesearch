from flask import Blueprint, render_template, request, jsonify

from src.models.model_product import model_product

main = Blueprint('product_call_bp', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/busquedaajax', methods=["POST", "GET"])
def busquedajax():
    if request.method == 'POST':
        busqueda = request.form.get('query', '')

        productos, numrows = model_product.get_products(busqueda)

    return jsonify({'htmlresponse': render_template('response.html', productos=productos, numrows=numrows)})
