# Employee Management System

This is a backend API for managing employees, departments, roles, and projects using FastAPI. The system includes authentication and authorization mechanisms.

## Features

- Employee management (CRUD operations)
- Department management (CRUD operations)
- Role management (CRUD operations)
- Project management (CRUD operations)
- User authentication and authorization

## Endpoints

### Employees

- **GET** `/employees/` - Read all employees
- **POST** `/employees/` - Create a new employee
- **GET** `/employees/{employee_id}` - Read an employee by ID
- **PUT** `/employees/{employee_id}` - Update an employee by ID
- **DELETE** `/employees/{employee_id}` - Delete an employee by ID

### Departments

- **GET** `/departments/` - Read all departments
- **POST** `/departments/` - Create a new department
- **GET** `/departments/{department_id}` - Read a department by ID
- **PUT** `/departments/{department_id}` - Update a department by ID
- **DELETE** `/departments/{department_id}` - Delete a department by ID

### Roles

- **GET** `/roles/` - Read all roles
- **POST** `/roles/` - Create a new role
- **GET** `/roles/{role_id}` - Read a role by ID
- **PUT** `/roles/{role_id}` - Update a role by ID
- **DELETE** `/roles/{role_id}` - Delete a role by ID

### Projects

- **GET** `/projects/` - Read all projects
- **POST** `/projects/` - Create a new project
- **GET** `/projects/{project_id}` - Read a project by ID
- **PUT** `/projects/{project_id}` - Update a project by ID
- **DELETE** `/projects/{project_id}` - Delete a project by ID

### Authentication

- **POST** `/token` - Login to get an access token
- **POST** `/users/` - Register a new user
- **GET** `/users/me/` - Read the current user's information
- **GET** `/users/me/profile` - Get the current user's profile

## Setup

### Prerequisites

- Python 3.9+
- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic (for database migrations)
- JWT tokens for authentication
