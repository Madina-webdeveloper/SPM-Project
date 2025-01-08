**Technical Assignment: Flask To-Do Application**

**Project Title:** Flask To-Do Application with Data Persistence and Task Management

**Objective:**
Design and implement a Flask-based To-Do web application that allows users to create, edit, complete, and delete tasks with data persistence across server restarts. Tasks should include timestamps and indicate whether they have been edited.

---

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

---

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

---

**3. Implementation Details:**
1. **Data Model:**
   - Task structure:
     ```json
     {
         "id": 1,
         "title": "Sample Task",
         "completed": false,
         "timestamp": "2023-01-01T10:00:00",
         "edited": false
     }
     ```

2. **Task Persistence:**
   - Tasks are stored in a `tasks.json` file.
   - Data is loaded during server startup and saved after each modification.

3. **Error Handling:**
   - Handles missing templates or data files gracefully.
   - Validates input to prevent errors.

4. **UI Elements:**
   - Task list displays completion status, edit status, and timestamps.
   - Buttons for editing, deleting, and toggling completion.

---

**4. Deliverables:**
1. Source code for Flask application.
2. HTML template files (index.html and edit.html).
3. Sample JSON file (tasks.json) with initial data.
4. README file with setup instructions.

---

**5. Optional Features (Future Scope):**
1. Use SQLite instead of JSON for data storage.
2. Implement user authentication for personalized task lists.
3. Add task categories or priorities.
4. Enable search and filter options.

---

**6. Timeline:**
- Day 1-2: Setup Flask environment and implement basic routes.
- Day 3: Develop template files for UI.
- Day 4: Integrate data persistence using JSON.
- Day 5: Test and refine features.

---

**7. Tools and Libraries:**
- Python 3.x
- Flask framework
- Bootstrap 5 for styling

---

**8. Testing and Validation:**
1. Verify routes and form submissions.
2. Test JSON file read/write operations.
3. Ensure UI responsiveness and functionality across devices.

---

**9. Deployment:**
1. Run application locally with Flask development server.
2. Optional: Deploy using services like Heroku or PythonAnywhere.

---

**10. References:**
- Flask Documentation: https://flask.palletsprojects.com/
- Bootstrap Documentation: https://getbootstrap.com/



