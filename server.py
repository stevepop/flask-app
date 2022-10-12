from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'task': 'Read Introduction to ECS',
        'done': True
    },
    {
        'task': 'Read Understanding Docker',
        'done': True
    },
    {
        'task': 'Write sample Flask App',
        'done': True
    },
    {
        'task': 'Build container',
        'done': True
    },
    {
        'task': 'Deploy container to ECS',
        'done': False
    },
    {
        'task': 'Test the application',
        'done': False
    }
]


@app.route('/')
def index():
    # return {'message': 'Working fine..'}
    return jsonify(message='It works...')


@app.route('/tasks')
def fetch_items():
    return jsonify(tasks=tasks)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    