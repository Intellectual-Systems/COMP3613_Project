from App.models.student import Student
from App.models.student import Shortlist
from App.database import db

# def create_student(username, degree, gpa):#, password, faculty, department, degree, gpa):
#     stu = Student(username, degree, gpa)#, password, faculty, department, degree, gpa)
#     db.session.add(stu)
#     db.session.commit()
#     return stu

def create_student(username, password, degree, gpa, resume):
    stu = Student(username, password, degree, gpa, resume)
    db.session.add(stu)
    db.session.commit()
    return stu

def get_student_by_id(studentID):
    stu = Student.query.filter_by(id=studentID).first()
    if not stu:
        return None
    return stu

def get_Shortlist_by_id(studentID):
    stu = Shortlist.query.filter_by(id=studentID).first()
    if not stu:
        return None
    return stu.positions

def get_all_Shortlists():
    stu_pos = Shortlist.query.all()
    if not stu_pos:
        return None
    return stu_pos

def get_all_students():
    students = Student.query.all()
    if not students:
        return None
    return students