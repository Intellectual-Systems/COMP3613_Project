from abc import ABC, abstractmethod

class ApplicationState(ABC):

    def _init_(self, state, description=None):
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

class ShortlistedState(ApplicationState):

    def _init_(self, description=None):
        super()._init_('Shortlisted', description)

    def shortlist(self, application):
        raise Exception("Application is already shortlisted for a position.")
    
    def employer_accept(self, application):
        application.state = "Accepted"
    
    def employer_reject(self, application):
        application.state = "Rejected"

class AppliedState(ApplicationState):

    def _init_(self, description=None):
        super()._init_('Applied', description)

    def shortlist(self, application):
        application.state = "Shortlisted"
    
    def employer_accept(self, application):
        raise Exception("Applicant must be shortlisted before acceptance.")
    
    def employer_reject(self, application):
        raise Exception("Applicant must be shortlisted before rejection.")

class AcceptedState(ApplicationState):

    def _init_(self, description=None):
        super()._init_('Accepted', description)

    def shortlist(self, application):
        raise Exception("Applicant has already been accepted for a position.")
    
    def employer_accept(self, application):
        raise Exception("Applicant has already been accepted for a position.")
    
    def employer_reject(self, application):
        raise Exception("Cannot reject an applicant who has already been accepted.")

class RejectedState(ApplicationState):

    def _init_(self, description=None):
        super()._init_('Rejected', description)

    def shortlist(self, application):
        raise Exception("Applicant has already been rejected for this position.")
    
    def employer_accept(self, application):
        raise Exception("Applicant has already been rejected for this position.")
    
    def employer_reject(self, application):
        raise Exception("Applicant has already been rejected for this position.")