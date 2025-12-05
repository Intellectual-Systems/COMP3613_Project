from .user import create_user
from .position import create_position
from .staff import addToShortlist
from .application import create_application
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass', user_type="student", degree="BSc Computer Science", gpa=3.5, resume="Bob's Resume")
    create_user('frank', 'frankpass', user_type="employer", companyName="Frank's Company")
    create_user('john', 'johnpass', user_type="staff", employerID=2)
    create_position(employerID=2, positionTitle='Data Analyst', department='IT', description='Analyze data trends.')
    create_position(employerID=2, positionTitle='Web Developer', department='IT', description='Develop and maintain websites.')
    create_application(student_id=1, position_id=1)
    addToShortlist(staffID=3, positionID=1, studentID=1)