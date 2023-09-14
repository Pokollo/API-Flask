from flask import Flask,jsonify
from database.products import products

app = Flask(__name__)

port = 3000

@app.route('/')
def show_status():
    return jsonify(
        { 
            "status": "loves",
            "port": port
        }
    ) 

@app.route('/products')
def get_products():
    return jsonify(
    products
    )

@app.route('/products/<int:id>')
def get_product_by_id(id):
    # Primero la API busca el producto en la lista de productos
    resultado = []
    for product in products:
        if product['id'] == id:
            resultado.append(product)

    # Si encontro un producto con el ID solicitado, nos devuelve el producto en formato JSON, si no, devuelve error
    if resultado:
        return jsonify(resultado[0])
    else:
        return jsonify(
            {
                "Err":"No found"
            }
        )

if __name__ == '__main__':
    app.run(debug= True, port = port)