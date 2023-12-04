# task_service.py
from flask import Flask, jsonify,request,render_template
from flask_cors import CORS  # Import the CORS extension
from model import db,Task

app = Flask(__name__)

# Configure your database URI here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()


@app.route('/tasks', methods=['GET'])
def all_tasks():
    tasks = Task.query.all()
    task_list = [task.serialize() for task in tasks]  # Assuming Task has a serialize method

    return jsonify(task_list)


@app.route('/update_task/<int:task_id>', methods=['GET'])
def render_update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        return render_template('update_task.html', task=task)
    return jsonify({"message": "Task not found"}), 404

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.title = request.form.get('title', task.title)
        task.description = request.form.get('description', task.description)
        task.completed = bool(request.form.get('completed', task.completed))
        db.session.commit()
        return jsonify({"message": "Task updated successfully", "task": {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "user_id": task.user_id
        }}), 200
    return jsonify({"message": "Task not found"}), 404


@app.route('/add_task', methods=['GET'])
def add_task_page():
    return render_template('add_task.html')  # Render the HTML file


@app.route('/add_task' , methods = ['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    completed = bool(request.form.get('completed'))

    new_task = Task(title=title, description=description, completed=completed)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task added successfully", "task": {
        "id": new_task.id,
        "title": new_task.title,
        "description": new_task.description,
        "completed": new_task.completed,
        "user_id": new_task.user_id
    }}), 200
@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"message": "Task not found"}), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
