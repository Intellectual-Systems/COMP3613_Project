# from App.models import Position, Employer
from App.database import db
from App.models.position import Position

def create_position(employerID, positionTitle, department, description):
    pos = Position(employerID=employerID, positionTitle=positionTitle, department=department, description=description)
    if not pos:
        return None
    db.session.add(pos)
    db.session.commit()
    return pos

def get_position_by_id(positionID):
    pos = Position.query.filter_by(id=positionID).first()
    if not pos:
        return None
    return pos

def get_all_positions():
    posits = Position.query.all()
    if not posits:
        return None
    return posits

# def open_position(user_id, title, number_of_positions=1):
#     employer = Employer.query.filter_by(user_id=user_id).first()
#     if not employer:
#         return None
    
#     new_position = Position(title=title, number=number_of_positions, employer_id=employer.id)
#     db.session.add(new_position)
#     try:
#         db.session.commit()
#         return new_position
#     except Exception as e:
#         db.session.rollback()
#         return None


# def get_positions_by_employer(user_id):
#     employer = Employer.query.filter_by(user_id=user_id).first()
#     return db.session.query(Position).filter_by(employer_id=employer.id).all()

# def get_all_positions_json():
#     positions = Position.query.all()
#     if positions:
#         return [position.toJSON() for position in positions]
#     return []

# def get_positions_by_employer_json(user_id):
#     employer = Employer.query.filter_by(user_id=user_id).first()
#     positions = db.session.query(Position).filter_by(employer_id=employer.id).all()
#     if positions:
#         return [position.toJSON() for position in positions]
#     return []