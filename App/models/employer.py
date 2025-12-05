from App.database import db
from App.models.user import User

class Employer(User):

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    companyName = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password, companyName):
        self.username = username
        self.set_password(password)
        self.role = "employer"
        self.companyName = companyName
    
    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'companyName': self.companyName
        }

    def __repr__(self):
        return f"Employer[id= {self.id}, username= {self.username}, companyName= {self.companyName}]"

# class Employer(db.Model):
#     __tablename__ = 'employer'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
#     username =  db.Column(db.String(20), nullable=False, unique=True)
#     positions = db.relationship("Position", back_populates="employer")

#     def __init__(self, username, user_id):
#         self.username = username
#         self.user_id = user_id