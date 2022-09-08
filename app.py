from flask import Flask, request, jsonify
from flask_cors import CORS
from crud_handler import create_user, delete_user, get_all_user, get_user_by_id, edit_user, delete_user

app = Flask(__name__)
CORS(app, resources={
    r"/*" : {"origins":"*"}
})

@app.route('/user', methods=['GET'])
def api_get_all_users():
    return jsonify(get_all_user())

@app.route('/user/<user_id>', methods=['GET'])
def api_get_user_by_id(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/user/add', methods=['POST'])
def api_create_user():
    user = request.get_json()
    jsonify(create_user(user))
    return "Data Berhasil ditambahkan!"
    
@app.route('/user/update', methods=['PUT'])
def api_update_user():
    user = request.get_json()
    jsonify(edit_user(user))
    return "Data Berhasil diedit!"

@app.route('/user/delete/<user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    jsonify(delete_user(user_id))
    return "Data Berhasil dihapus!"



app.run(debug=True)