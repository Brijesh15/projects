from flask import Flask, jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
@app.route('/todo/api/v1.0/tasks',methods=['GET'])
def index():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:id>', methods=['GET'])
def get_tasks(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task)== 0:
        return 'URL Not Found'
    return jsonify({'tasks': task[0]})

@app.route('/todo/api/v1.0/tasks1', methods=['POST'])
def create_task():
#    if not request.json or not 'title' in request.json:
#        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', "hello"),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')

