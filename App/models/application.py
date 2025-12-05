from App.database import db
# from App.models.position import Position
from App.models.position import Position
from App.models.applicationstate import ApplicationState, STATE_MAP

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    application_state = db.Column(db.String(50), nullable=False, default='Applied')

    def __init__(self, student_id, position_id):
        self.student_id = student_id
        self.position_id = position_id
        self.application_state = 'Applied'
    
    def __repr__(self):
        return f"Application[id= {self.id}, student_id= {self.student_id}, position_id= {self.position_id}, application_state= {self.application_state}]"
    
    def get_state(self):
        state_class = STATE_MAP.get(self.application_state)
        if state_class:
            return state_class()
        else:
            raise Exception(f"Unknown application state: {self.application_state}")
    
    def set_state(self, new_state):
        if new_state in STATE_MAP:
            self.application_state = new_state
        else:
            raise Exception(f"Invalid state transition to: {new_state}")
    
    def shortlist(self):
        self.get_state().shortlist(self)
    
    def employer_accept(self):
        self.get_state().employer_accept(self)
    
    def employer_reject(self):
        self.get_state().employer_reject(self)

# class Application(ABC):
#     __tablename__ = 'applications'
#     id = Column(Integer, primary_key=True)
#     student_id = Column(Integer, ForeignKey('students.id'))
#     position_id = Column(Integer, ForeignKey('positions.id'))
#     state = Column(String, default='Applied')

#     def __init__(self, student_id, position_id):
#         self.student_id = student_id
#         self.position_id = position_id
#         self._state = "Applied"

#     @property
#     def set_state(self):
#         if self._state is None:
#             state_class = globals()[self.state]
#             self._state = state_class()
#         return self._state

# from sqlalchemy import Column, Integer, String
#     from sqlalchemy.ext.declarative import declarative_base
#     from sqlalchemy.orm import relationship

#     Base = declarative_base()

#     class Document(Base):
#         _tablename_ = 'documents'
#         id = Column(Integer, primary_key=True)
#         title = Column(String)
#         state_name = Column(String, default='DraftState') # Stores the name of the current state class

#         # Relationship to the state object (optional, for direct ORM mapping of state)
#         # current_state = relationship("State", back_populates="document", uselist=False)

#         def _init_(self, title):
#             self.title = title
#             self._state = None # Placeholder for the actual state object

#         @property
#         def state(self):
#             if self._state is None:
#                 # Dynamically load the state object based on state_name
#                 state_class = globals()[self.state_name]
#                 self._state = state_class(self)
#             return self._state

#         @state.setter
#         def state(self, new_state):
#             self._state = new_state
#             self.state_name = new_state._class.name_

#         def edit(self, content):
#             self.state.edit(content)

#         def review(self):
#             self.state.review()

#         def publish(self):
#             self.state.publish()


# s = AppliedState()
# doc = Document("Sample Document")
# doc.state(s)
# doc.edit("New content for the document.")

# doc.state("Applied State")
