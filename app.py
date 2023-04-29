from flask import Flask, jsonify, request

app = Flask(__name__)

comida = [
    {"id": 1, "comida": "mel"},
    {"id": 2, "comida": "bolacha"},
    {"id": 3, "comida": "carne"},
]

@app.route('/comida', methods=['GET'])
def get_data():
    return jsonify(comida)

@app.route('/comida', methods=['POST'])
def add_data():
    new_data = request.json
    data.append(new_data)
    return jsonify(new_data)

@app.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    for d in data:
        if d['id'] == data_id:
            data.remove(d)
            return jsonify(d)
    return jsonify({"error": "Data not found"}), 405

if __name__ == '__main__':
    app.run(debug=True)