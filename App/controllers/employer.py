from App.models.employer import Employer
from App.models.position import Position
from App.models.shortlist import Shortlist


# from App.models.student import Shortlist



from App.models.application import Application

from App.controllers.staff import create_staff
from App.controllers.position import create_position
from App.controllers.student import create_student
from App.controllers.staff import addToShortlist
from App.controllers.application import create_application


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

    print("Beginning accept rject process...")

    # Get employer

    emp = Employer.query.filter_by(id=employerID).first()

    # Verify employer exists

    if not emp:
        print("Employer not found (in function)")
        return False

    # Get shortlist entry

    sh = Shortlist.query.filter_by(studentID=studentID, positionID=positionID).first()

    # If shortlist doesnt exist return

    if not sh:
        print("Shortlist entry not found")
        return False
    

    # Get the application from the student and update the state depending on accept/reject

    application = Application.query.filter_by(student_id=studentID, position_id=positionID).first()

    if not application:
        print("Application not found")
        return False
    
    if status.lower() == "accepted":
        print("Accepting application...")
        application.set_state('Accepted')
        sh.status = "accepted"
    elif status.lower() == "rejected":
        application.set_state('Rejected')
        sh.status = "rejected"
    else:
        return False

    # sh.status = status
    sh.employer_response = message

    # Automatically reject every other student who was shortlisted for this position
    if status.lower() == 'accepted':
        otherStudents = Shortlist.query.filter_by(positionID=positionID).all()
        for os in otherStudents:
            if os.studentID != sh.studentID:
                os.status = 'rejected'
                os_app = Application.query.filter_by(student_id=os.studentID, position_id=positionID).first()
                os_app.set_state('Rejected')
    print("Application state: " + application.application_state)
    db.session.commit()
    return True


    # return False

def create_template():

    emp = create_employer("King", "kingpass", "King Wing")
    pos = create_position(emp.id, "Software Engineer", "Engineering", "Develop software solutions.")
    sta = create_staff("Alice", "alicepass", 1)
    stu = create_student("Bob", "bobpass", "Computer Science", 3.8, "bob_resume.pdf")
    app = create_application(position_id=pos.id, student_id=stu.id)
    addToShortlist(staffID=sta.id, positionID=pos.id, studentID=stu.id)