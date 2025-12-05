from App.database import db
from App.models.user import User
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date
from App.models.application import Application

class Student(User):

    __tablename__ = 'student'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    degree = db.Column(db.String(20), nullable=False)
    gpa = db.Column(db.Integer, nullable=False)
    resume = db.Column(db.String(256))
    shortlists = db.relationship('Position', secondary='shortlist', back_populates='shortlist')

    applications = db.relationship('Application', backref='student', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password, degree, gpa, resume):
        self.username = username
        self.set_password(password)
        self.role = "student"
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
