import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, open_position, add_student_to_shortlist, decide_shortlist, get_shortlist_by_student, get_shortlist_by_position, get_positions_by_employer)
from App.controllers.student import (get_all_students, create_student, get_student_by_id)


from App.models.student import Student
from App.models.staff import Staff
from App.models.position import Position
from App.models.employer import Employer

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# Configuration Constants
DEFAULT_USERNAME = "rob"
DEFAULT_PASSWORD = "robpass"
DEFAULT_USER_TYPE = "student"
DEFAULT_POSITION_TITLE = "Software Engineer"
DEFAULT_EMPLOYER_ID = 1
DEFAULT_POSITION_NUMBER = 1
DEFAULT_STUDENT_ID = 1
DEFAULT_POSITION_ID = 1
DEFAULT_STAFF_ID = 1
DEFAULT_DECISION = "accepted"
DEFAULT_FORMAT = "string"
DEFAULT_TEST_TYPE = "all"

# Helper functions for consistent output
def print_separator():
    """Prints a separator line for better readability"""
    print("\n\n__________________________________________________________________________\n\n")

def print_success(message):
    """Prints a success message with separator"""
    print(message)
    print_separator()

def print_error(message):
    """Prints an error message with separator"""
    print(message)
    print_separator()

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default=DEFAULT_USERNAME)
@click.argument("password", default=DEFAULT_PASSWORD)
@click.argument("user_type", default=DEFAULT_USER_TYPE)
def create_user_command(username, password, user_type):
    result = create_user(username, password, user_type)
    if result:
        print(f'{username} created!')
    else:
        print("User creation failed")

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default=DEFAULT_FORMAT)
def list_user_command(format):
    # if format == 'string':
    #     print(get_all_users())
    # else:
    print(get_all_users_json())

@user_cli.command("add_position", help="Adds a position")
@click.argument("title", default=DEFAULT_POSITION_TITLE)
@click.argument("employer_id", type=int, default=DEFAULT_EMPLOYER_ID)
@click.argument("number", type=int, default=DEFAULT_POSITION_NUMBER)
def add_position_command(title, employer_id, number):
    if number < 1:
        print_error("Number of positions must be at least 1")
        return
    
    position = open_position(title, employer_id, number)
    if position:
        print(f'{title} created!')
    else:
        print(f'Employer {employer_id} does not exist')

@user_cli.command("add_to_shortlist", help="Adds a student to a shortlist")
@click.argument("student_id", type=int, default=DEFAULT_STUDENT_ID)
@click.argument("position_id", type=int, default=DEFAULT_POSITION_ID)
@click.argument("staff_id", type=int, default=DEFAULT_STAFF_ID)
def add_to_shortlist_command(student_id, position_id, staff_id):
    test = add_student_to_shortlist(student_id, position_id, staff_id)
    if test:
        print_success(f'Student {student_id} added to shortlist for position {position_id}')
    else:
        error_msg = 'One of the following is the issue:\n'
        error_msg += f'    Position {position_id} is not open\n'
        error_msg += f'    Student {student_id} already in shortlist for position {position_id}\n'
        error_msg += f'    There is no more open slots for position {position_id}'
        print_error(error_msg)

@user_cli.command("decide_shortlist", help="Decides on a shortlist")
@click.argument("student_id", type=int, default=DEFAULT_STUDENT_ID)
@click.argument("position_id", type=int, default=DEFAULT_POSITION_ID)
@click.argument("decision", default=DEFAULT_DECISION)
def decide_shortlist_command(student_id, position_id, decision):
    test = decide_shortlist(student_id, position_id, decision)
    if test:
        print_success(f'Student {student_id} is {decision} for position {position_id}')
    else:
        print_error(f'Student {student_id} not in shortlist for position {position_id}')

@user_cli.command("get_shortlist", help="Gets a shortlist for a student")
@click.argument("student_id", type=int, default=DEFAULT_STUDENT_ID)
def get_shortlist_command(student_id):
    list = get_shortlist_by_student(student_id)
    if list:
        for item in list:
            print(f'Student {item.student_id} is {item.status.value} for position {item.position_id}')
        print_separator()
    else:
        print_error(f'Student {student_id} has no shortlists')

@user_cli.command("get_shortlist_by_position", help="Gets a shortlist for a position")
@click.argument("position_id", type=int, default=DEFAULT_POSITION_ID)
def get_shortlist_by_position_command(position_id):
    list = get_shortlist_by_position(position_id)
    if list:
        for item in list:
            print(f'Student {item.student_id} is {item.status.value} for {item.position.title} id: {item.position_id}')
            print(f'    Staff {item.staff_id} added this student to the shortlist')
            print(f'    Position {item.position_id} is {item.position.status.value}')
            print(f'    Position {item.position_id} has {item.position.number_of_positions} slots')
            print(f'    Position {item.position_id} is for {item.position.title}')
            print_separator()
    else:
        print_error(f'Position {position_id} has no shortlists')

@user_cli.command("get_positions_by_employer", help="Gets all positions for an employer")
@click.argument("employer_id", type=int, default=DEFAULT_EMPLOYER_ID)
def get_positions_by_employer_command(employer_id):
    list = get_positions_by_employer(employer_id)
    if list:
        for item in list:
            print(f'Position {item.id} is {item.status.value}')
            print(f'    Position {item.id} has {item.number_of_positions} slots')
            print(f'    Position {item.id} is for {item.title}')
            print_separator()
    else:
        print_error(f'Employer {employer_id} has no positions')
            
app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default=DEFAULT_TEST_TYPE)
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

'''
Student Commands
'''

student_cli = AppGroup('student', help='Student object commands')

@student_cli.command("list", help="Lists all students in the database")
def list_students_command():
    students = get_all_students()

    if not students:
        print("\nNo students found.\n")
        return

    print("")
    for stu in students:
        print(stu)
    print("")

@student_cli.command("create", help="Creates a student")
def create_student_command():
    username = input('\nEnter student username: ')
    password = input('\nEnter student password: ')
    degree = input('\nEnter degree: ')
    gpa = input('\nEnter GPA: ')
    resume = input('\nEnter student resume (example: MyResume.pdf): ')

    s = Student.query.filter_by(username=username, degree=degree, gpa=gpa, resume=resume).first()
    # s = Student.query.filter_by(username=username, faculty=faculty, department=department, degree=degree, gpa=gpa).first()
    if s:
        print('\nThis student already exists.')
        return
    else:
        stu = create_student(username, password, degree, gpa, resume)
        # stu = create_student(username, password, faculty, department, degree, gpa)
        db.session.add(stu)
        db.session.commit()
        print(f'\nStudent {username} created!\n')

# @student_cli.command("view-shortlists", help="View shortlists a specified student was added to")
# def view_shortlists_command():
#     print("\nStudents:\n")
#     students = get_all_students()
#     for stu in students:
#         print(f'ID: {stu.id} Name: {stu.username}')
    
#     student_id = input('\nEnter student ID: ')
#     print("")
#     student = get_student_by_id(student_id)
#     if not student:
#         print('Student not found.')
#         return

#     student = Student_Position.query.filter_by(studentID=student_id).all()
#     if student:
#         for s in student:
#             print(s)
#     else:
#         print('No shortlists found for this student.')
#     print("")

# @student_cli.command("browse-positions", help="Browse available positions")
# def browse_positions_command():
#     positions = get_all_positions()
#     if not positions:
#         print("\nNo positions available.\n")
#         return
    
#     print("\n=== Available Positions ===\n")
#     for pos in positions:
#         employer = get_employer_by_id(pos.employerID)
#         print(f"ID: {pos.id} | {pos.positionTitle}")
#         print(f"  Company: {employer.companyName if employer else 'Unknown'}")
#         print(f"  Department: {pos.department}")
#         print(f"  Description: {pos.description}")
        
#         # Show number of applicants
#         shortlist = view_position_shortlist(pos.id)
#         print(f"  Applicants: {len(shortlist) if shortlist else 0}")
#         print("")
app.cli.add_command(student_cli)