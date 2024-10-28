from flask import Flask, jsonify, request
import redis
import json

# Create a Flask app
app = Flask(__name__)

# Connect to the Redis server
redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

# Helper function to fetch all products from Redis
def get_all_products():
    products = []
    for key in redis_client.scan_iter("product:*"):
        products.append(json.loads(redis_client.get(key)))
    return products

# Route to retrieve all products (GET)
@app.route('/products', methods=['GET'])
def get_products():
    products = get_all_products()
    return jsonify(products)

# Route to retrieve a specific product (GET)
@app.route('/products/<string:product_name>', methods=['GET'])
def get_product(product_name):
    product_key = f"product:{product_name.lower()}"
    product = redis_client.get(product_key)
    if product:
        return jsonify(json.loads(product))
    else:
        return jsonify({"error": "Product not found"}), 404

# Route to add a new product (POST)
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    product_name = new_product.get('name').lower()
    product_key = f"product:{product_name}"
    
    # Store product as a JSON string in Redis
    redis_client.set(product_key, json.dumps(new_product))
    return "Product added successfully."

# Run the Flask app
if __name__ == '__main__':
    print('''
          
          Pour vérifier la connexion : curl http://localhost:5000/products
          
          Post:
            - On Windows: 
                   - Invoke-WebRequest -Uri http://localhost:5000/products -Method 
                     POST -Headers @{"Content-Type"="application/json"} -Body 
                     '{"name": "products", "price": xxx}'
                
            - On Linux: 
                    - curl -X POST http://localhost:5000/products -H "Content-Type: application/json" 
                      -d '{"name": "voiture", "price": 10.99}'

            ''')
    app.run(host='0.0.0.0', port=5000, debug=True)
