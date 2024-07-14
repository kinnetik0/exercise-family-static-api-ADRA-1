import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Get all members
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Get a single member by ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"message": "Member not found"}), 404

# Add a new member
@app.route('/member', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"message": "Invalid data"}), 400

    new_member = jackson_family.add_member(data)
    return jsonify(new_member), 200

# Delete a member by ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    result = jackson_family.delete_member(member_id)
    if result["done"]:
        return jsonify(result), 200
    else:
        return jsonify({"message": "Member not found"}), 404

# Update a member by ID
@app.route('/member/<int:member_id>', methods=['PATCH'])
def update_member(member_id):
    data = request.get_json()
    result = jackson_family.update_member(member_id, data)
    if result["done"]:
        return jsonify(result), 200
    else:
        return jsonify({"message": "Member not found"}), 404

# This only runs if $ python src/app.py is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
