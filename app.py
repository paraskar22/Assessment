from flask import Flask, jsonify, request, abort

# Initialize the Flask application
app = Flask(__name__)

# In-memory data storage (acting like a database) using a dictionary
data_store = {}

# Helper function to find an item by its ID
def find_item(item_id):
    """Return the item corresponding to the given ID, or None if not found."""
    return data_store.get(item_id)

# Health check endpoint to verify if the API is running
@app.route('/health', methods=['GET'])
def health_check():
    """Return the health status of the API."""
    return jsonify({"status": "API is running"}), 200

# Endpoint to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    """Create a new item and store it in the data store."""
    # Check if the request is JSON and contains a 'name'
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid input: 'name' is required")

    # Generate a new ID based on the current number of items
    item_id = str(len(data_store) + 1)
    item = {
        'id': item_id,
        'name': request.json['name'],
        'description': request.json.get('description', "")
    }

    # Store the new item in the data store
    data_store[item_id] = item
    return jsonify(item), 201

# Endpoint to retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    """Return a list of all items in the data store."""
    return jsonify(list(data_store.values())), 200

# Endpoint to retrieve a specific item by ID
@app.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    """Return the item with the specified ID."""
    item = find_item(item_id)
    if item is None:
        abort(404, description="Item not found")

    return jsonify(item), 200

# Endpoint to update an existing item by ID
@app.route('/items/<string:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update the item with the specified ID."""
    item = find_item(item_id)
    if item is None:
        abort(404, description="Item not found")

    # Ensure the request is JSON formatted
    if not request.json:
        abort(400, description="Invalid input: JSON data expected")

    # Update the item's fields based on the request data
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item.get('description', ""))

    # Store the updated item back into the data store
    data_store[item_id] = item
    return jsonify(item), 200

# Endpoint to delete an item by ID
@app.route('/items/<string:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete the item with the specified ID from the data store."""
    item = find_item(item_id)
    if item is None:
        abort(404, description="Item not found")

    # Remove the item from the data store
    del data_store[item_id]
    return jsonify({"message": "Item deleted"}), 200

# Error handler for bad requests (400)
@app.errorhandler(400)
def bad_request(error):
    """Return a JSON response for bad request errors."""
    return jsonify({"error": str(error)}), 400

# Error handler for not found (404)
@app.errorhandler(404)
def not_found(error):
    """Return a JSON response for not found errors."""
    return jsonify({"error": str(error)}), 404

# Run the Flask application
if __name__ == '__main__':
    # Set to debug=True during development for detailed error messages
    app.run(host='0.0.0.0', port=5010, debug=False)
