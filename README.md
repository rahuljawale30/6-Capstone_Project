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

### Screenshot
- Home Page
  ![1 png](https://github.com/user-attachments/assets/7dd25a97-ef78-4cb1-9fe5-1c5975b892cc)
- login Page
  ![2 png](https://github.com/user-attachments/assets/51f533b7-cc5b-4479-a3e1-5e12ed7cb4d4)
- Register Page
  ![3](https://github.com/user-attachments/assets/368ec436-c61e-494a-b072-a12bfcd4d2c0)
- Submit Estimation
  ![4](https://github.com/user-attachments/assets/2efffc4a-dd87-4c97-bd9d-1eb9563f5bc9)

- Estimation tools
  ![5](https://github.com/user-attachments/assets/9e8ba6bf-5732-47f2-9318-cd7bd947ba32)

- Task Estimations
  ![6](https://github.com/user-attachments/assets/9a6207b3-5bab-49cc-bdc3-ff39206f547b)

- Estimations results
  ![7](https://github.com/user-attachments/assets/dcc137a5-72fe-4879-8d79-ec78785f0a50)

- Create Historical Data
  ![12](https://github.com/user-attachments/assets/74f105d2-c63f-47ff-bd76-5d952b0ec0fc)

- View Historical Data
  ![13](https://github.com/user-attachments/assets/5d33e792-5d38-40d4-9452-477469a56b00)

- 
  








