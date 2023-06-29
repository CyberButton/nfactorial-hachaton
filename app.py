from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, Flask!")

@app.route('/add', methods=['GET'])
def add():
    # getting parameters from the request
    a = request.args.get('a')
    b = request.args.get('b')

    # converting parameters to float and adding them
    result = float(a) + float(b)

    # returning the result as a JSON
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)
