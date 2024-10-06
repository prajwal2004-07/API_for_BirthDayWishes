from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

# Load the JSON data
def load_wishes():
    with open('wishes.json', 'r') as f:
        data = json.load(f)
    return data['birthday_wishes']

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Birthday Wishes API!"})

@app.route('/wishes', methods=['GET'])
def get_all_wishes():
    wishes = load_wishes()
    return jsonify(wishes)

@app.route('/wishes/<int:index>', methods=['GET'])
def get_wish(index):
    wishes = load_wishes()
    if 0 <= index < len(wishes):
        return jsonify(wishes[index])
    else:
        return jsonify({"error": "Wish not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)