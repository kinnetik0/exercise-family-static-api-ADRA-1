import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from src.datastructure import FamilyStructure  # Asegúrate de que la ruta sea correcta

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Crea el objeto de la familia Jackson
jackson_family = FamilyStructure("Jackson")

# Maneja/serializa errores como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Genera el sitemap con todos tus endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Obtener todos los miembros
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Obtener un miembro por ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"message": "Member not found"}), 404

# Agregar un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"message": "Invalid data"}), 400

    new_member = jackson_family.add_member(data)
    return jsonify(new_member), 200

# Eliminar un miembro por ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    result = jackson_family.delete_member(member_id)
    if result["done"]:
        return jsonify(result), 200
    else:
        return jsonify({"message": "Member not found"}), 404

# Actualizar un miembro por ID
@app.route('/member/<int:member_id>', methods=['PATCH'])
def update_member(member_id):
    data = request.get_json()
    result = jackson_family.update_member(member_id, data)
    if result["done"]:
        return jsonify(result), 200
    else:
        return jsonify({"message": "Member not found"}), 404

# Esto solo se ejecuta si se ejecuta $ python src/app.py
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
