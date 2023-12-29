from flask import Flask, request, jsonify
import jwt
from flask_cors import CORS
from models import Methods
app = Flask(__name__)

# Assume 'secret_key' is defined somewhere in your code
secret_key = "your_secret_key"
methods_api = Methods()
CORS(app, origins= "http://localhost:3000")

@app.route('/generatetable', methods={"GET"})
def generate_tabel():
    try:
        table = methods_api.generate_table_api()
        return jsonify({"tabel": table}), 200
    except Exception as e:
        return jsonify({"message": 'error-' + str(e)}), 501

@app.route('/getuserbyid', methods=['GET'])
def get_user_by_id():
    try:
        id = request.args.get('user_id')
        print(id)
        if len(id) > 0:
            user = methods_api.get_user_by_id(id)
            if user:
                return jsonify({"user": user}), 200
        else: 
            return jsonify({"message": 'error id is not exist' + str(e)}), 400


    except Exception as e: 
        return jsonify({"message": 'error-' + str(e)}), 501

# google login api
@app.route('/googlelogin', methods=['POST'])
def googlelogin():
    try:
        data = request.json
        if data:
            handle_data = data["data"]
            # Assuming 'methods_api' is defined somewhere in your code
            id_user = methods_api.insert_user(handle_data)
            if len(id_user) > 0:
                token = {
                    "user_id": str(id_user["id"]),
                    "email": handle_data["email"],
                    "verify": handle_data["verify"],
                    "locale": handle_data["locale"],
                    "full_name": handle_data["full_name"],
                    "picture": handle_data["picture"]
                }
                encoded_jwt = jwt.encode(token, secret_key, algorithm='HS256')
                print(encoded_jwt)
                if encoded_jwt:
                    return jsonify({"user": encoded_jwt}), 200
                else:
                    return jsonify({"message": "encoded fail"}), 400
            else:
                return jsonify({"message": "user was not insert"}), 400
        else:
            return jsonify({"message": "fetch failed"}), 400
    except Exception as e:
        return jsonify({"message": 'error-' + str(e)}), 501

# facebook login api
@app.route('/facebooklogin', methods=['POST'])
def facebooklogin():
    try:
        data = request.json
        if data:
            handle_data = data["data"]
            id_user = methods_api.insert_user(handle_data)
            if len(id_user) > 0:
                token = {
                    "user_id": str(id_user["id"]),
                    "email": handle_data["email"],
                    "full_name": handle_data["full_name"],
                    "picture": handle_data["picture"]
                }
                encoded_jwt = jwt.encode(token, secret_key, algorithm='HS256')
                if encoded_jwt:
                    return jsonify({"user": encoded_jwt}), 200
                else:
                    return jsonify({"message": "encoded fail"}), 400
            else:
                return jsonify({"message": "user was not insert"}), 400
        else:
            return jsonify({"message": "fetch failed"}), 400
    except Exception as e:
        return jsonify({"message": 'error-' + str(e)}), 501

if __name__ == '__main__':
    # Use a different port (e.g., 5001) and specify the host as '0.0.0.0'
    app.run(debug=True, host='0.0.0.0', port=9080)
