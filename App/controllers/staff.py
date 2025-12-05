from App.models.staff import Staff
from App.models.shortlist import Shortlist
# from App.models.student import Shortlist
from App.models.position import Position
from App.models.student import Student
from App.models.application import Application
from App.database import db


def create_staff(username, password, employerID):
    sta = Staff(username, password, employerID)
    db.session.add(sta)
    db.session.commit()
    return sta

def get_staff_by_id(staffID):
    sta = Staff.query.filter_by(id=staffID).first()
    if not sta:
        return None
    return sta

def get_all_staff():
    staff = Staff.query.all()
    if not staff:
        return None
    return staff

def addToShortlist(staffID, positionID, studentID):

    # Find staff member

    staff = Staff.query.filter_by(id=staffID).first()

    # If not found return

    if not staff:
        print("Staff not found")
        return False
    print("Staff found")
    # Find position 
    
    position = Position.query.filter_by(id=positionID).first()

    if not position:
        print("Position not found")
        return False
    print("Position found")

    student = Student.query.filter_by(id=studentID).first()

    if not student:
        print("Student not found")
        return False
    print("Student found. Appending to shortlist...")

    # if position != None and student != None:

    # Add the student to the position's shortlist

    position.shortlist.append(student)
    print("Finding application...")
    # Get the application from the student and update the state

    application = Application.query.filter_by(student_id=studentID, position_id=positionID).first()

    if not application:
        print("Application not found")
        return False
    
    print("Setting application state...")
    
    application.set_state('Shortlisted')
    
    db.session.commit()

    print("Student added to shortlist successfully! Application state: " + application.application_state)
    return True