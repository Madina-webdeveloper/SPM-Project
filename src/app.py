from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)

DATA_FILE = 'tasks.json'

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks():
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, default=str)

# Initialize tasks
tasks = load_tasks()

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    new_task_title = request.form["title"]
    if new_task_title.strip():
        task_id = len(tasks) + 1
        tasks.append({"id": task_id, "title": new_task_title, "completed": False, "timestamp": datetime.now(), "edited": False})
        save_tasks()
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    save_tasks()
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks()
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if request.method == "POST":
        task["title"] = request.form["title"]
        task["timestamp"] = datetime.now()
        task["edited"] = True
        save_tasks()
        return redirect(url_for("index"))
    return render_template("edit.html", task=task)

if __name__ == "__main__":
    app.run(debug=True)
