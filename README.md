# Capstone_Project
# Effort Estimation Tool

## Overview

The Effort Estimation Tool is a web application designed to provide users with accurate estimates for various tasks based on historical data stored in a MongoDB database. 

## Technical Implementation Steps

### 1. User Registration and Authentication
- Implement a user registration form using HTML and CSS.
- Securely store user credentials in MongoDB.
- Use JSON Web Tokens (JWT) for secure authentication.

### 2. Estimation Submission
- Design an estimation submission form with fields for complexity, size, and type of task using HTML and CSS.
- Use AJAX to send form data asynchronously to the Flask backend.
- Validate and sanitize input data.
- Store estimation details in MongoDB.

### 3. Estimation Calculation
- Develop a formula to calculate new estimates based on historical data and user input.
- Implement estimation calculation logic in Flask.
- Return the calculated new estimate, confidence level and Estimted Range to the frontend.

### 4. Database Interaction
- Establish a connection to MongoDB using Flask-PyMongo.
- Define database models/schema for storing historical estimation data.
- Update historical data with new estimations.

### 5. UI/UX Design
- Design responsive UI components using HTML/CSS and Bootstrap .
- Implement client-side form validation.
- Test the UI across various devices and screen sizes.

### 6. Testing
- Write unit tests for backend APIs using pytest.
- Mock database interactions in unit tests.

### 7. Deployment Using CI/CD (Jenkins and Docker)
- Set up a Jenkins server for continuous integration and deployment.
- Configure Jenkins jobs to pull source code from version control (e.g., GitHub).


### Prerequisites
- Python 3.9
- Flask
- MongoDB

### Installation
- Clone the repository to your local machine.
- Navigate to the project directory.
- Install dependencies using pip install -r requirements.txt.
- Set up MongoDB database and configure connection settings in config.py.
- Run the Flask application using python app.py.
- Access the application in your web browser at http://localhost:5050.


myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
    app1/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        migrations/
            __init__.py
    app2/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        migrations/
            __init__.py
    static/
        css/
        js/
        images/
    templates/
        base.html
        app1/
            template1.html
        app2/
            template2.html
    requirements.txt
    README.md






