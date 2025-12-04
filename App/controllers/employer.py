from App.models.employer import Employer
from App.models.position import Position
from App.models.student import Shortlist
from App.database import db

def create_employer(username, password, companyName):
    emp = Employer(username, password, companyName)
    db.session.add(emp)
    db.session.commit()
    return emp

def get_employer_by_id(employerID):
    emp = Employer.query.filter_by(id=employerID).first()
    if not emp:
        return None
    return emp

def get_all_employers():
    emps = Employer.query.all()
    if not emps:
        return None
    return emps

def view_positions(employerID):
    positions = Position.query.filter_by(id=employerID).all()
    if not positions:
        return None
    return positions

def view_position_shortlist(positionID):
    shortlist = Shortlist.query.filter_by(positionID=positionID).all()
    if not shortlist:
        return None
    return shortlist

def create_position(employerID, positionTitle, department, description):
    pos = Position(employerID=employerID, positionTitle=positionTitle, department=department, description=description)
    db.session.add(pos)
    db.session.commit()
    return pos

def acceptReject(employerID, studentID, positionID, status, message=None):
    emp = Employer.query.filter_by(id=employerID).first()
    if not emp:
        return False
    sp = Shortlist.query.filter_by(studentID=studentID, positionID=positionID).first()
    if sp:
        sp.status = status
        sp.employer_response = message

        # Automatically reject every other student who was shortlisted for this position
        if status.lower() == 'accepted':
            otherStudents = Shortlist.query.filter_by(positionID=positionID).all()
            for os in otherStudents:
                if os.studentID != sp.studentID:
                    os.status = 'rejected'

        db.session.commit()
        return True
    return False