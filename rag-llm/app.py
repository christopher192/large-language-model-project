from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask API!'

@app.route('/post-data', methods = ['POST'])
def post_data():
    message = request.json.get('message')
    if message:
        return jsonify({"success": True, "message": "Message received"}), 200
    else:
        return jsonify({"success": False, "error": "No message provided"}), 400

@app.route('/get-data', methods = ['GET'])
def get_data():
    data = {
        "id": 1,
        "name": "Sample Data",
        "description": "This is an example of data returned by a GET request."
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug = True)