# Human Resources Management System

The Human Resources Management System (HR Management System) is a web application designed to manage employee information, payroll, benefits, and performance evaluations. The system enables efficient administration of HR data, assisting in the organization and analysis of employee information.

## 🔨 Project Features

- **Employee Registration**: Add and manage information about company employees, including name, email, phone, hire date, position, and salary.
- **Payroll**: Record and view information about employee payments, including payment date, gross and net salaries, and deductions.
- **Benefits**: Manage employee benefits such as health plans and bonuses.
- **Performance Evaluations**: Conduct and record employee performance evaluations with ratings and comments.

### Visual Example of the Project
***

## ✔️ Techniques and Technologies Used

- **Python**: Programming language used to develop the application.
- **Django**: Web framework for rapid and clean application development.
- **Microsoft SQL Server**: Database management system used to store application data.
- **django-mssql-backend**: Package for integrating Django with Microsoft SQL Server.
- **pyodbc**: Library for connecting Django to SQL Server.

## 📁 Project Structure

- **`.gitignore`**: File listing files and directories to be ignored by Git, such as local configuration files and cache directories.
- **`LICENSE`**: File containing the license under which the project is distributed.
- **`manage.py`**: Django management script that allows executing administrative commands.
- **`README.md`**: Project documentation file providing an overview and usage instructions.
- **`requirements.txt`**: File listing project dependencies for installation with `pip`.
- **`Human-Resource-Management-System/`**: Main directory of the Django project, containing configuration and initialization files:
   - **`__init__.py`**: Package initializer to make the directory a Python module.
   - **`asgi.py`**: ASGI interface for asynchronous servers.
   - **`settings.py`**: Project settings, such as database and installed apps.
   - **`urls.py`**: Project URL routing file.
   - **`wsgi.py`**: WSGI interface for application servers.
- **`employees/`**: Django application for employee management:
   - **`__init__.py`**: Package initializer to make the directory a Python module.
   - **`admin.py`**: Django admin configurations.
   - **`apps.py`**: Application-specific configurations.
   - **`models.py`**: Data model definitions for the application.
   - **`tests.py`**: Automated tests for the application.
   - **`views.py`**: View logic and request handling.
   - **`migrations/`**: Directory for migration files reflecting changes in data models.
   - **`templates/`**: Directory for application-specific HTML templates, containing:
      - **`employee_list.html`**: Template for listing employees.

## 🛠️ Running the Project

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/Human-Resource-Management-System.git
    cd Human-Resource-Management-System
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the database**:
    - Edit `settings.py` to include your SQL Server credentials.

4. **Run migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Start the development server**:

    ```bash
    python manage.py runserver
    ```

6. **Access the application**:
    - Navigate to `http://127.0.0.1:8000/admin` to access the admin panel.

## 🌐 Deploy

To deploy the project in a production environment:

1. **Set up the production environment** with your chosen web server, such as Nginx or Apache, and a WSGI server like Gunicorn.
2. **Configure the production database** and ensure credentials are correct.
3. **Additional configurations** may include setting up security, backups, and SSL certificates.

For more details on deployment, refer to the [official Django documentation](https://docs.djangoproject.com/en/stable/howto/deployment/).
