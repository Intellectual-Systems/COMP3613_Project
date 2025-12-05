from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user
# from App.controllers import (open_position, get_positions_by_employer, get_all_positions_json, get_positions_by_employer_json)
from App.controllers.employer import view_positions 
from App.controllers.application import create_application
from App.controllers.position import get_all_positions
from App.controllers.position import create_position

position_views = Blueprint('position_views', __name__)

#get all positions
@position_views.route('/api/positions/all', methods = ['GET'])
def get_all_positions():
    if not current_user:
        return jsonify({"message": "Unauthorized user"}), 403
    
    position_list = get_all_positions()
    return jsonify([p.get_json() for p in position_list]), 200

# for opening a position 
@position_views.route('/api/positions/create', methods = ['POST'])
@jwt_required()
def create_new_position():
    if current_user.role != 'employer':
        return jsonify({"message": "Unauthorized user"}), 403
    
    print("Creating position for employer ID:", current_user.id)
    
    data = request.json
    position = create_position(employerID=current_user.id, positionTitle=data['title'], department=data['department'], description=data['description'])
    
    if position:
        return jsonify(position.get_json()), 201
    else:
        return jsonify({"error": "Failed to create position"}), 400
  
  
# # get positions for a given employer
@position_views.route('/api/employer/positions', methods=['GET'])
@jwt_required()
def get_employer_positions():
    print("Current user role:", current_user.role)
    if current_user.role != 'employer':
        return jsonify({"message": "Unauthorized user"}), 403
    
    return jsonify([p.get_json() for p in view_positions(current_user.id)]), 200

@position_views.route('/api/positions/apply', methods=['POST'])
@jwt_required()
def apply_position():
    if current_user.role != 'student':
        return jsonify({"message": "Unauthorized user"}), 403
    
    data = request.json
    new_application = create_application(student_id=current_user.id, position_id=data['position_id'])
    
    if not new_application:
        return jsonify({"error": "Failed to create application"}), 400
    
    return jsonify(new_application.get_json()), 200