from App.models import User, Student, Employer, Staff, Application
from App.database import db

def get_application(student_id, position_id):
    return db.session.query(Application).filter_by(student_id=student_id, position_id=position_id).first()

def create_application(position_id, student_id, status):
    try:
        # Check if Application already exists
        existing_app = get_application(position_id, student_id)
        if existing_app:
            return False
        

        newApp = Application(student_id, position_id=position_id, status=status)
        db.session.add(newApp)
        db.session.commit()

        return newApp

    except Exception as e:
        db.session.rollback()
        print(f"Error creating application: {e}")
        return False
    