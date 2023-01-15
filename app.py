# Import library dan file
from flask import Flask, request, jsonify
from flask_cors import CORS
from crud_handler import create_user, get_all_user, get_user_by_id, edit_user, delete_user

# Flask CORS
app = Flask(__name__)
CORS(app, resources={
    r"/*" : {"origins":"*"}
})

# Route untuk melihar keseluruhan employees
@app.route('/user', methods=['GET'])
def api_get_all_users():
    return jsonify(get_all_user())

# Route untuk melihat salah satu employee
@app.route('/user/<user_id>', methods=['GET'])
def api_get_user_by_id(user_id):
    return jsonify(get_user_by_id(user_id))

# Route untuk menambahkan data employee baru
@app.route('/user/add', methods=['POST'])
def api_create_user():
    user = request.get_json()
    jsonify(create_user(user))
    return "Data Berhasil ditambahkan!"
    
# Route untuk mengedit data employee baru
@app.route('/user/update', methods=['PUT'])
def api_update_user():
    user = request.get_json()
    jsonify(edit_user(user))
    return "Data Berhasil diedit!"

# Route untuk menghapus data employee
@app.route('/user/delete/<user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    jsonify(delete_user(user_id))
    return "Data Berhasil dihapus!"

# Running Apps
if __name__ == '__main__':
    app.run(debug=True)




# Status

# 0 - 200 => berhasil
# 201 - 399 => ada error di koneksi database
# 400 - 599 => database aman tetapi route tidak ada
