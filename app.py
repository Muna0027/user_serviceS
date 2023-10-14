from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    '1': {'name': 'Alice', 'email': 'alice@example.com'},
    '2': {'name': 'Bob', 'email': 'bob@example.com'}
}


@app.route('/user/<id>')
def get_user(id):
    user_info = users.get(id, {})
    return jsonify(user_info)


@app.route('/user', methods=['POST'])
def create_user():
    data = request.json  
    new_id = str(len(users) + 1)
    users[new_id] = data
    return jsonify({'message': 'User created'})


@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    if id in users:
        data = request.json 
        users[id] = data
        return jsonify({'message': 'User updated'})
    else:
        return jsonify({'error': 'User not found'})


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    if id in users:
        del users[id]
        return jsonify({'message': 'User deleted'})
    else:
        return jsonify({'error': 'User not found'})

if __name__ == '__main__':
    app.run(port=5000)
