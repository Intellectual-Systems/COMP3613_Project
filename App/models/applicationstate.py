from abc import ABC, abstractmethod

class ApplicationState(ABC):

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