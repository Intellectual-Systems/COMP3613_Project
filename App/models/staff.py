from App.database import db
from App.models.user import User
# from App.models.shortlist import Shortlist

class Staff(User):
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    employerID = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)

    def __init__(self, username, password, employerID):
        self.username = username
        self.set_password(password)
        self.role = "staff"
        self.employerID = employerID

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'employerID': self.employerID
        }

    def __repr__(self):
        return f"Staff[id= {self.id}, username= {self.username}, employerID= {self.employerID}]"
