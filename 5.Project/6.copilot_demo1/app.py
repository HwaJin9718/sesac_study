from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/todo', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    if task:
        tasks.append({'task': task, 'completed': False})
        return jsonify({'message': 'Task added', 'tasks': tasks}), 200
    else:
        return 'Invalid input', 400

@app.route('/todo', methods=['PUT'])
def toggle_task_complete():
    data = request.get_json()
    task = data.get('task')
    if task:
        for t in tasks:
            if t['task'] == task:
                t['completed'] = not t['completed']
                return jsonify({'message': 'Task completion toggled', 'tasks': tasks}), 200
        return 'Task not found', 404
    else:
        return 'Invalid input', 400

@app.route('/todo', methods=['DELETE'])
def delete_task():
    data = request.get_json()
    task = data.get('task')
    if task:
        global tasks
        tasks = [t for t in tasks if t['task'] != task]
        return jsonify({'message': 'Task deleted', 'tasks': tasks}), 200
    else:
        return 'Invalid input', 400

if __name__ == '__main__':
    app.run(debug=True)