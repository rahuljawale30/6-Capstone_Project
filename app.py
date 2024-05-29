from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_jwt_extended import JWTManager,create_access_token, get_jwt_identity, jwt_required
from flask_pymongo import MongoClient
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = '1287A@^#&DS(@&$*#GHFSY&$&$SFFasrsfd4'
jwt = JWTManager(app)
# Configuration
client = MongoClient("mongodb://localhost:27017/")
db = client['effort']
users_collection = db['users']
estimation_collection = db['estimations']
task_collection = db['task_details']
estimation_collection.create_index("created_at")

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash((password))
        print(hashed_password)

        # to check the user is already exits
        if users_collection.find_one({'email': email}):
            return render_template('register.html', message='Email is already registered')

        # to save the user and password
        users_collection.insert_one({'username': username, 'email': email, 'password': hashed_password})
        return redirect(url_for('login'))
    return render_template('register.html',message='User registered Successfully')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users_collection.find_one({'email': email})
        if user and check_password_hash(user['password'],password):
            access_token = create_access_token(identity={'email':user['email'],'password': user['password']})  #add 27
            return render_template('dashboard.html',access_token=access_token)
        else:
            return render_template('login.html', message='Invalid email or password')

    return render_template('login.html')

def calculate_effort_and_range(complexity, size):
    effort_lookup = {
        'Low': {'Small': 10, 'Medium': 20, 'Large': 30},
        'Medium': {'Small': 20, 'Medium': 40, 'Large': 60},
        'High': {'Small': 30, 'Medium': 60, 'Large': 90},
    }

    effort = effort_lookup.get(complexity, {}).get(size, 0)
    range_lower = effort * 0.9
    range_upper = effort * 1.1
    return effort, (range_lower, range_upper)


# Create an estimation and calculate result
@app.route('/submit_estimation', methods=['POST'])
def submit_estimation():
    task_name = request.form.get('task_name')
    complexity = request.form.get('complexity')
    size = request.form.get('size')
    task_type = request.form.get('task_type')
    additional_notes = request.form.get('additional_notes')

    # Save to MongoDB
    estimation_data = {
        'task_name': task_name,
        'complexity': complexity,
        'size': size,
        'task_type': task_type,
        'additional_notes': additional_notes,
        'created_at': datetime.utcnow()
    }
    estimation_collection.insert_one(estimation_data)

    # Calculate the estimation
    effort, effort_range = calculate_effort_and_range(complexity, size)

    if effort < 40:
        confidence_level = "High"
    elif 20 < effort < 40:
        confidence_level = "Medium"
    else:
        confidence_level = "Low"

    result = {
        "new_estimate": effort,
        "confidence_level": confidence_level,
        "confidence_range": effort_range,
    }
    task_collection.insert_one(result)
    return render_template('result.html', result=result)

@app.route('/view_estimations')
def view_estimations():
    # Retrieve all documents from the collection
    estimations = estimation_collection.find()

    # Pass the data to the template for rendering
    return render_template('view_estimations.html', estimations=estimations)

@app.route('/task_details')
def historical_data():
    # Retrieve all documents from the collection
    records = task_collection.find()

    # Pass the data to the template for rendering
    return render_template('historical_data_record.html', records=records)



if __name__ == '__main__':
    app.run(debug=True,port=5050)