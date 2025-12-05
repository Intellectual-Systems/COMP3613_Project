from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user
# from App.controllers import ( add_student_to_shortlist, decide_shortlist, get_shortlist_by_student, get_shortlist_by_position)
from App.controllers.student import get_all_Shortlists_by_id
from App.controllers.staff import addToShortlist
from App.controllers.employer import acceptReject, view_position_shortlist


shortlist_views = Blueprint('shortlist_views', __name__)


@shortlist_views.route('/api/shortlist', methods = ['POST'])
@jwt_required()
def add_student_shortlist():
    if current_user.role != 'staff':
        return jsonify({"message": "Unauthorized user"}), 403

    data = request.json
    request_result = addToShortlist(staffID=current_user.id, studentID=data['student_id'], positionID=data['position_id'])
    
    if request_result:
        return jsonify([p.get_json() for p in request_result]), 200
    else:
        return jsonify({"error": "Failed to add to shortlist"}), 401
     
     

@shortlist_views.route('/api/shortlist/student/<int:student_id>', methods = ['GET'])
@jwt_required()
def get_student_shortlist(student_id):
    print(current_user.role)     
    shortlists = get_all_Shortlists_by_id(student_id)
    if not shortlists:
        return jsonify({"message": "No shortlist found for the student"}), 404
    
    return jsonify([s.get_json() for s in shortlists]), 200
    


@shortlist_views.route('/api/shortlist',methods = ['PUT'] ) 
@jwt_required()
def shortlist_decide():
    if current_user.role != 'employer':
        return jsonify({"message": "Unauthorized user"}), 403
    
    
    data = request.json
    request_result = acceptReject(employerID=current_user.id, studentID=data['student_id'], positionID=data['position_id'], status=data['decision'])
   
    if request_result:
        return jsonify(request_result.get_json()), 200
    else:
     return jsonify({"error": "Failed to update shortlist"}), 400
    

@shortlist_views.route('/api/shortlist/position/<int:position_id>', methods=['GET'])
@jwt_required()
def get_position_shortlist(position_id):
    if current_user.role != 'employer' and current_user.role != 'staff':
        return jsonify({"message": "Unauthorized user"}), 403
    
    
    shortlists = view_position_shortlist(position_id)
    return jsonify([s.get_json() for s in shortlists]), 200 
     