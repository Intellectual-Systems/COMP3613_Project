from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from functools import wraps

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    user = create_user(data['username'], data['password'])
    return jsonify({'message': f"user {user.username} created with id {user.id}"})

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')

'''
Permissions
'''

def requires_permission(perm):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # jwt_current_user is only available after @jwt_required() runs
            user = jwt_current_user

            if not user:
                return jsonify({"error": "User not authenticated"}), 401
            
            print("Permission: " + perm)
            print("User info:\n\n" + user)

            # if perm != "student":
            #     print("Permission denied")
            print("Permission granted")
            # func()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@user_views.route('/permission-test', methods=['GET'])
@jwt_required()
@requires_permission("test-permission")
def permission_test():
    return jsonify({"message": "Test successful"}), 200