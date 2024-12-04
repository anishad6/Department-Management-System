
# Department Management System

A web-based application built with Django that allows users to manage departments. The application supports features like adding, updating, deleting, and viewing departments.

## Features
- **View Departments**: Display a list of active departments.
- **Add Department**: Add new departments with descriptions.
- **Update Department**: Modify details of existing departments.
- **Delete Department**: Soft delete departments by marking them inactive.

## Prerequisites
- Python 3.12
- Django 5.1.1 or above
- Mysql 

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/department-management-system.git
   cd department-management-system
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Folder Structure
```
.
├── dashapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│       ├── index.html
│       ├── add.html
│       ├── update.html
│   ├── migrations/
│   └── tests.py
├── manage.py
├── requirements.txt
└── README.md
```

## Models
### Department Model
The `Department` model includes the following fields:
- **dept_id**: Primary Key
- **DepartmentName**: Name of the department
- **Description**: Description of the department
- **status**: Boolean field indicating if the department is active

## Views
### `home(request)`
- Fetches all active departments and displays them on the `index.html` page.

### `addDepartment(request)`
- Handles GET and POST requests for adding a new department.

### `deleteDepartment(request, deptid)`
- Soft deletes a department by setting its status to `False`.

### `updateDepartment(request, deptid)`
- Updates the details of an existing department.

## Routes
| URL Pattern           | Method | Description              |
|-----------------------|--------|--------------------------|
| `/`                   | GET    | Displays all departments |
| `/add/`               | GET/POST | Adds a new department    |
| `/update/<deptid>/`   | GET/POST | Updates a department     |
| `/delete/<deptid>/`   | GET    | Deletes a department     |

## Usage
1. Visit the home page to view the list of departments.
2. Use the **Add Department** option to create new entries.
3. Edit or delete existing departments using the respective actions.

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: mysql

## Author
-Abhishek Nishad (https://github.com/anishad6)

## License
This project is licensed under the [MIT License](LICENSE).
