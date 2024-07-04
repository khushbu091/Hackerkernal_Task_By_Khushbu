# User and Task Management Application

This Django application allows an admin to manage users and their tasks. Users can be added with basic information, and tasks can be assigned to them. Additionally, the admin has the capability to export user and task data to an Excel sheet.

## Features

- **Models**: Defines `User` and `Task` models to store user information and task assignments respectively.
- **Forms**: Provides forms for adding users and tasks with appropriate validations.
- **Views**: Implements views to handle adding users, adding tasks, and displaying paginated lists of users and tasks.
- **Pagination**: Utilizes Django's built-in pagination feature for user and task lists.
- **Export to Excel**: Enables exporting of user and task data to separate sheets in an Excel file using Django utilities.

## Setup Instructions

### Prerequisites

- Python (3.x recommended)
- Django framework
- Django extensions (for Excel export, optional)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/khushbu091/Hackerkernal_Task_By_Khushbu.git
   cd project
2. pip install requirements.txt
3. py manage.py makemirgations
4. py manage.py migrate
5. py manage.py runserver

Created by: Khushbu Patel  
