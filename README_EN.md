## 🌐 [Versão em Português do README](README.md)

# Human Resource Management System

The **Human Resource Management System** is a project designed to manage and automate human resources processes such as employee management, payroll, benefits, and performance reviews. The system aims to provide an efficient and practical solution for companies seeking to optimize their HR operations.

## 🔨 Project Features

- **Employee Management**: Create, edit, and delete employee records.
- **Payroll**: Track salaries and generate payroll reports.
- **Benefits**: Manage benefits offered to employees.
- **Performance Reviews**: Record and track employee performance reviews.

### Visual Example of the Project

![image](https://github.com/user-attachments/assets/dbf3ef75-aa1c-4734-8e15-5f4d024077be)
![image](https://github.com/user-attachments/assets/3d9f0dd0-a493-4a17-9272-d922dd3e8e47)
![image](https://github.com/user-attachments/assets/6bae1612-f60b-4cb8-b667-9c442de56e51)

## ✔️ Techniques and Technologies Used

- **Django**: A framework for the rapid and secure development of web applications.
- **SQLite**: A lightweight relational database used for data storage.
- **DRF (Django Rest Framework)**: A framework for building RESTful APIs.
- **drf_yasg**: A library for generating Swagger/OpenAPI documentation for Django APIs.

## 📁 Project Structure

- **db.sqlite3**: SQLite database file.
- **employees/**: Application responsible for employee management.
    - `admin.py`: Administrative panel configurations.
    - `apps.py`: Application configurations.
    - **migrations/**: Database migration files.
        - `0001_initial.py`: Initial migration file.
    - `models.py`: Data models definition.
    - `serializers.py`: Serializers for the API.
    - **templates/**: HTML templates.
        - `employee_list.html`: Template for displaying the employee list.
    - `tests.py`: Automated tests.
    - `urls.py`: Application URLs.
    - `views.py`: View logic.
    - `__init__.py`: Module initialization.
- **Human-Resource-Management-System/**: Main project directory.
    - `asgi.py`: ASGI configuration for the project.
    - `settings.py`: Django settings.
    - `urls.py`: Project URLs.
    - `wsgi.py`: WSGI configuration for the project.
    - `__init__.py`: Module initialization.
- **LICENSE**: License file.
- **manage.py**: Django command-line utility.
- **README.md**: Project instructions document.
- **README_EN.md**: English instructions document.
- **requirements.txt**: Project dependencies list.

## 🛠️ Running the Project

To run the project locally, follow the steps below:

1. **Ensure Python is Installed**:
    - Python is required to run the project. You can check if it is already installed with:

      ```bash
      python --version
      ```

    - If it is not installed, download and install the recommended version.

2. **Clone the Repository**:
    - Copy the repository URL and run the command below in the terminal:

      ```bash
      git clone <REPOSITORY_URL>
      ```

3. **Install Dependencies**:
    - Navigate to the project directory and install the dependencies using pip:

      ```bash
      cd Human-Resource-Management-System
      pip install -r requirements.txt
      ```

4. **Set Up the Database**:
    - Run the migrations to set up the database:

      ```bash
      python manage.py migrate
      ```

5. **Start the Development Server**:
    - Run the Django development server:

      ```bash
      python manage.py runserver
      ```

    - Access the application at `http://127.0.0.1:8000/` in your browser.

## 🌐 Deploy

For information on deploying the application in production environments, refer to the Django documentation for [Deploying Django](https://docs.djangoproject.com/en/stable/howto/deployment/).

[Human Resource Management System](https://human-resource-management-system-l96i.onrender.com)

## 📜 API Documentation

The API documentation is available on Swagger Hub: [Human Resource Management System API Documentation](https://app.swaggerhub.com/apis-docs/FelipeM./Human-Resource-Management-System/1.0.0)
