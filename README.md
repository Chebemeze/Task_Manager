# Task_Manager
Building a task manager API
This project will focus on a simple Task manager API that helps registered user create tasks
with priority level and deadlines for the task.
It will utilize djangos rest frame work to do it


Achieve CRUD operations with tasks such as:
Listing tasks for a user: GET http://127.0.0.1:8000/api/tasks/
Create task for a logged in user: POST http://127.0.0.1:8000/api/tasks/
Retrieve user task using their ID: GET http://127.0.0.1:8000/api/tasks/{id}/
Update user task using their ID: PUT http://127.0.0.1:8000/api/tasks/{id}/
Delete user task using their ID: DELETE http://127.0.0.1:8000/api/tasks/{id}/

Mark task as complete utilizes the following Api endpoints:
To mark task as complete POST http://127.0.0.1:8000/api/tasks/{id}/Complete

To mark task as incomplete POST http://127.0.0.1:8000/api/tasks/{id}/inComplete

example to register:
{
    "username": "eben",
    "email": "chebemeze@gmail.com",
    "password": "1324dgfadvn!%$#",
    "password2": "1324dgfadvn!%$#",
    "date_of_birth": null,
    "profile_photo": null
}

example to login:
{
    "username": 
        "eben",
    "password": 
        "1324dgfadvn!%$#"
}

example to create task for a user:
{
    "title": "Alx capstone submission",
    "description": "Showcasing knwolege gotten from course",
    "deadine": "2024-09-10",
    "priority": "High",
    "status": "Pending"
}