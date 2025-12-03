from App.models import db
from abc import ABC, abstractmethod

class ApplicationState(db.Model, ABC):
    __tablename__ = 'application_state'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, state, description=None):
        self.state = state
        self.description = description

    def setState(self, state):
        self.state = state

    @abstractmethod
    def shortlist(self, application):
        pass
    
    @abstractmethod
    def employer_accept(self, application):
        pass
    
    @abstractmethod
    def employer_reject(self, application):
        pass