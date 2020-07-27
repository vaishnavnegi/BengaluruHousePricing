from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "First Flask Hello"

if __name__ == "__main__":
    app.run(debug=True)