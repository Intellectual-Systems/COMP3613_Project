from abc import ABC, abstractmethod

class ApplicationState(ABC):

    def __init__(self, state):
        self.state = state

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

class AppliedState(ApplicationState):

    def __init__(self):
        super().__init__('Applied')

    def shortlist(self, application):
        application.state = "Shortlisted"
    
    def employer_accept(self, application):
        raise Exception("Applicant must be shortlisted before acceptance.")
    
    def employer_reject(self, application):
        application.state = "Rejected"

class ShortlistedState(ApplicationState):

    def __init__(self):
        super().__init__('Shortlisted')

    def shortlist(self):
        raise Exception("Application is already shortlisted for a position.")
    
    def employer_accept(self, application):
        application.state = "Accepted"
    
    def employer_reject(self, application):
        application.state = "Rejected"

class AcceptedState(ApplicationState):

    def __init__(self):
        super().__init__('Accepted', description)

    def shortlist(self, application):
        raise Exception("Applicant has already been accepted for a position.")
    
    def employer_accept(self, application):
        raise Exception("Applicant has already been accepted for a position.")
    
    def employer_reject(self, application):
        raise Exception("Cannot reject an applicant who has already been accepted.")

class RejectedState(ApplicationState):

    def __init__(self):
        super().__init__('Rejected', description)

    def shortlist(self, application):
        raise Exception("Applicant has already been rejected for this position.")
    
    def employer_accept(self, application):
        raise Exception("Applicant has already been rejected for this position.")
    
    def employer_reject(self, application):
        raise Exception("Applicant has already been rejected for this position.")

STATE_MAP = {
    "Applied": AppliedState,
    "Shortlisted": ShortlistedState,
    "Accepted": AcceptedState,
    "Rejected": RejectedState
}
