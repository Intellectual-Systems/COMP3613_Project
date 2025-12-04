from App.database import db
from App.models.user import User
# from App.models.shortlist import Shortlist

class Staff(User):
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    employerID = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)

    def __init__(self, username, password, employerID):
        self.username = username
        self.set_password(password)
        self.employerID = employerID

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'employerID': self.employerID
        }

    def __repr__(self):
        return f"Staff[id= {self.id}, username= {self.username}, employerID= {self.employerID}]"

# class Staff(db.Model):
#     __tablename__ = 'staff'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
#     username =  db.Column(db.String(20), nullable=False, unique=True)

#     def __init__(self, username, user_id):
#         self.username = username
#         self.user_id = user_id

    # def add_to_shortlist(self, student_id, position_id):
    #     shortlist = Shortlist(student_id=student_id, position_id=position_id, staff_id=self.id)
    #     db.session.add(shortlist)
    #     db.session.commit()
    #     return shortlist