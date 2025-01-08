**Technical Assignment: Flask To-Do Application**

**Project Title:** To-Do List

Design and implement a Flask-based To-Do web application that allows users to create, edit, complete, and delete tasks with data persistence across server restarts. Tasks should include timestamps and indicate whether they have been edited.

**1. Features:**
1. **Add Tasks:**
   - Allows users to add new tasks.
   - Each task includes a title, completion status, timestamp, and edited status.

2. **Edit Tasks:**
   - Enables users to edit existing tasks.
   - Updates the timestamp and marks the task as edited.

3. **Mark Tasks as Complete/Incomplete:**
   - Users can toggle task completion status.

4. **Delete Tasks:**
   - Users can delete specific tasks from the list.

5. **Persistence:**
   - Tasks are saved in a JSON file, ensuring changes persist across server restarts.

6. **User Interface:**
   - Bootstrap-based responsive UI with forms and buttons for task management.
   - Indicators for edited tasks.

**2. Technical Requirements:**
1. **Backend:**
   - Framework: Flask (Python)
   - JSON file for data persistence.

2. **Frontend:**
   - HTML templates rendered with Jinja2.
   - CSS framework: Bootstrap 5.

3. **Dependencies:**
   - Flask
   - Python standard libraries (datetime, os, json)

4. **Routes:**
   - `/` - Display all tasks.
   - `/add` - Add a new task (POST).
   - `/complete/<int:task_id>` - Toggle task completion.
   - `/delete/<int:task_id>` - Delete a task.
   - `/edit/<int:task_id>` - Edit an existing task (GET/POST).




