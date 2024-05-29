import pytest
from flask import url_for
from werkzeug.security import generate_password_hash
from app import app, db, users_collection

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
            yield client
def test_register_user(client):
    """Test user registration"""
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@gmail.com',
        'password': 'StrongPassword123'
    }, follow_redirects=True)

    # Check redirects to the login page
    assert response.status_code == 200
    assert b'Login' in response.data

    # Verify the user is actually created in the database
    user = users_collection.find_one({'email': 'test@gmail.com'})
    assert user is not None
    assert user['username'] == 'testuser'
def test_register_existing_user(client):
    with app.app_context():
        users_collection.insert_one({
            'username': 'existinguser',
            'email': 'existinguser@example.com',
            'password': generate_password_hash('password')
        })

    rv = client.post('/register', data={
        'username': 'existinguser',
        'email': 'existinguser@example.com',
        'password': 'password'
    }, follow_redirects=True)

    assert rv.status_code == 200
    assert b'Email is already registered' in rv.data



def test_login_page(client):
    """Test the login page"""
    rv = client.get('/login')
    assert rv.status_code == 200
    assert b'Login' in rv.data


def test_login_user(client):
    """Test user login"""
    with app.app_context():
        users_collection.insert_one({
            'username': 'loginuser',
            'email': 'loginuser@example.com',
            'password': generate_password_hash('password')
        })

    rv = client.post('/login', data={
        'email': 'loginuser@example.com',
        'password': 'password'
    }, follow_redirects=True)

    assert rv.status_code == 200
    assert b'Submit Estimation' in rv.data
    assert b'Title:' in rv.data
    assert b'Complexity:' in rv.data


def test_invalid_login(client):
    """Test invalid login"""
    response=client.post('/login', data={'email':'test_user','password':'test_password'})
    assert b' ' in response.data


