# app.py 
 
import flask 
import db 
from flasgger import Swagger, swag_from 
 
# create app 
app = flask.Flask(__name__) 
swagger = Swagger(app) 
 
# default route 
@app.route('/') 
def index(): 
    return flask.jsonify({'message': 'Hello World!'}) 
 
# product catalog 
@app.route('/products', methods=['GET']) 
@swag_from('swagger/products.yml') 
def products(): 
    products = db.get_products() 
    return flask.jsonify(products) 
 
# get single product 
@app.route('/products/<int:product_id>', methods=['GET']) 
@swag_from('swagger/product.yml') 
def product(product_id): 
    product = db.get_product(product_id) 
    return flask.jsonify(product) 
 
# shopping cart 
@app.route('/cart', methods=['GET']) 
@swag_from('swagger/cart.yml') 
def cart(): 
    cart = db.get_cart() 
    return flask.jsonify(cart) 
 
# add product to cart, productId and quantity in body, create cart if needed, else update 
@app.route('/cart/add', methods=['POST']) 
@swag_from('swagger/add_to_cart.yml') 
def add_to_cart(): 
    # get product id and quantity from body 
    product_id = flask.request.json['productId'] 
    quantity = flask.request.json['quantity'] 
 
    db.add_to_cart(product_id, quantity) 
 
    return flask.jsonify({'message': 'Added to cart'}) 
 
# remove product from cart 
@app.route('/cart/remove', methods=['POST']) 
@swag_from('swagger/remove_from_cart.yml') 
def remove_from_cart(): 
    # get product id from body 
    product_id = flask.request.json['productId'] 
 
    db.remove_from_cart(product_id) 
 
    return flask.jsonify({'message': 'Removed from cart'}) 
 
# update quantity of product in cart 
@app.route('/cart/update', methods=['POST']) 
@swag_from('swagger/update_cart.yml') 
def update_cart(): 
    # get product id and quantity from body 
    product_id = flask.request.json['productId'] 
    quantity = flask.request.json['quantity'] 
 
    db.update_cart(product_id, quantity) 
 
    return flask.jsonify({'message': 'Cart updated'}) 
 
# checkout POST, cartId in body 
@app.route('/checkout', methods=['POST']) 
@swag_from('swagger/checkout.yml') 
def checkout(): 
    # get cart id from body 
    cart_id = flask.request.json['cartId'] 
 
    db.checkout(cart_id) 
 
    return flask.jsonify({'message': 'Checkout successful'}) 
 
# start app on port 5000 
if __name__ == '__main__': 
    app.run(debug=True, port=5000) 
