# from sqlalchemy import false, or_
# from App.models import Shortlist, Position, Staff, Student, PositionStatus
# from App.models.shortlist import DecisionStatus
# from App.database import db

# def add_student_to_shortlist(student_id, position_id, staff_id):
#     # The student_id and staff_id might be either user_id OR the internal Student/Staff id
#     # Try both approaches
    
#     # First try: assume student_id is the internal Student table id
#     student = db.session.query(Student).filter_by(id=student_id).first()
#     if not student:
#         # Second try: assume student_id is user_id
#         student = db.session.query(Student).filter_by(user_id=student_id).first()
    
#     # First try: assume staff_id is the internal Staff table id
#     teacher = db.session.query(Staff).filter_by(id=staff_id).first()
#     if not teacher:
#         # Second try: assume staff_id is user_id
#         teacher = db.session.query(Staff).filter_by(user_id=staff_id).first()
    
#     if student == None or teacher == None:
#         return False
    
#     # Check for existing shortlist entry
#     list = db.session.query(Shortlist).filter_by(student_id=student.id, position_id=position_id).first()
    
#     # Query position - handle both string "open" and enum PositionStatus.open
#     position = db.session.query(Position).filter(
#         Position.id == position_id,
#         Position.number_of_positions > 0,
#         or_(Position.status == "open", Position.status == PositionStatus.open)
#     ).first()
    
#     if teacher and not list and position:
#         shortlist = Shortlist(student_id=student.id, position_id=position.id, staff_id=teacher.id, title=position.title)
#         db.session.add(shortlist)
#         db.session.commit()
#         return shortlist
    
#     return False

# def decide_shortlist(student_id, position_id, decision):
#     # Validate decision first
#     if decision not in ["accepted", "rejected"]:
#         return False
    
#     # Try both: student_id might be internal id or user_id
#     student = db.session.query(Student).filter_by(id=student_id).first()
#     if not student:
#         student = db.session.query(Student).filter_by(user_id=student_id).first()
    
#     if not student:
#         return False
    
#     # Find the shortlist entry
#     shortlist = db.session.query(Shortlist).filter_by(student_id=student.id, position_id=position_id, status=DecisionStatus.pending).first()
#     if not shortlist:
#         return False
    
#     # Only decrement position if decision is "accepted"
#     if decision == "accepted":
#         position = db.session.query(Position).filter(Position.id==position_id, Position.number_of_positions > 0).first()
#         if position:
#             shortlist.update_status(decision)
#             position.update_number_of_positions(position.number_of_positions - 1)
#             return shortlist
#         else:
#             return False
#     else:
#         # For "rejected", just update status without checking position count
#         shortlist.update_status(decision)
#         return shortlist


# def get_shortlist_by_student(student_id):
#     # Try both: student_id might be internal id or user_id
#     student = db.session.query(Student).filter_by(id=student_id).first()
#     if not student:
#         student = db.session.query(Student).filter_by(user_id=student_id).first()
    
#     if not student:
#         return []
    
#     return db.session.query(Shortlist).filter_by(student_id=student.id).all()

# def get_shortlist_by_position(position_id):
#     return db.session.query(Shortlist).filter_by(position_id=position_id).all()