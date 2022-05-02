from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    {
    "done": True,
    "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
    ]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

