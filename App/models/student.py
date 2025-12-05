from App.database import db
from App.models.user import User
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date
from App.models.application import Application


# class Shortlist(db.Model):
#     __tablename__ = 'shortlist'
#     studentID = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
#     positionID = db.Column(db.Integer, db.ForeignKey('position.id'), primary_key=True)
#     status = db.Column(db.String(20), nullable=False, default='pending')
#     employer_response = db.Column(db.String(20), nullable=True, default=None)

#     def __init__(self, studentID, positionID):
#         self.studentID = studentID
#         self.positionID = positionID

#     def get_json(self):
#         return {
#             'studentID': self.studentID,
#             'positionID': self.positionID,
#             'status': self.status,
#             'employer_response': self.employer_response
#         }

#     def __repr__(self):
#         return f"Shortlist[studentID= {self.studentID} -> positionID= {self.positionID}, status= {self.status}, employer_response= {self.employer_response}]"


class Student(User):

    __tablename__ = 'student'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    degree = db.Column(db.String(20), nullable=False)
    gpa = db.Column(db.Integer, nullable=False)
    resume = db.Column(db.String(256))
    # shortlists = db.Column(db.String(256)) # temporary placeholder
    shortlists = db.relationship('Position', secondary='shortlist', back_populates='shortlist')

    applications = db.relationship('Application', backref='student', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password, degree, gpa, resume):
        self.username = username
        self.set_password(password)
        self.degree = degree
        self.gpa = gpa
        self.resume = resume

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'degree': self.degree,
            'gpa': self.gpa,
            'resume': self.resume
        }

    def __repr__(self):
        return f"Student[id= {self.id}, username= {self.username}, degree= {self.degree}, gpa= {self.gpa}, resume= {self.resume}]"

    def get_applications(self):
        return self.applications

    # def create_application(self, position_id, application_state):
    #     application = Application(applicant_id=self.id, position_id=position_id, application_state=application_state)
    #     db.session.add(application)
    #     db.session.commit()
    #     return application

#    def update_DOB(self, date):
#        self.DOB = date
#        db.session.commit()
#        return self.DOB
#        
#   @hybrid_property
#   def age(self):
#       if self.DOB is None:
#           return None
#       today = date.today()
#       dob = self.DOB
#       return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
