import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
# from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, open_position, add_student_to_shortlist, decide_shortlist, get_shortlist_by_student, get_shortlist_by_position, get_positions_by_employer)
from App.controllers import get_all_users_json, initialize, get_all_positions, get_position_by_id, get_all_staff, get_all_employers, create_employer, get_employer_by_id, create_position, view_positions, view_position_shortlist, acceptReject, create_staff, get_staff_by_id, addToShortlist
from App.controllers.student import (get_all_students, create_student, get_student_by_id)


from App.models.student import Student, Student_Position
from App.models.staff import Staff
from App.models.position import Position
# from App.models.position import Position
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
# @user_cli.command("create", help="Creates a user")
# @click.argument("username", default=DEFAULT_USERNAME)
# @click.argument("password", default=DEFAULT_PASSWORD)
# @click.argument("user_type", default=DEFAULT_USER_TYPE)
# def create_user_command(username, password, user_type):
#     result = create_user(username, password, user_type)
#     if result:
#         print(f'{username} created!')
#     else:
#         print("User creation failed")

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default=DEFAULT_FORMAT)
def list_user_command(format):
    # if format == 'string':
    #     print(get_all_users())
    # else:
    print(get_all_users_json())

# @user_cli.command("add_position", help="Adds a position")
# @click.argument("title", default=DEFAULT_POSITION_TITLE)
# @click.argument("employer_id", type=int, default=DEFAULT_EMPLOYER_ID)
# @click.argument("number", type=int, default=DEFAULT_POSITION_NUMBER)
# def add_position_command(title, employer_id, number):
#     if number < 1:
#         print_error("Number of positions must be at least 1")
#         return
    
#     position = open_position(title, employer_id, number)
#     if position:
#         print(f'{title} created!')
#     else:
#         print(f'Employer {employer_id} does not exist')

# @user_cli.command("add_to_shortlist", help="Adds a student to a shortlist")
# @click.argument("student_id", type=int, default=DEFAULT_STUDENT_ID)
# @click.argument("position_id", type=int, default=DEFAULT_POSITION_ID)
# @click.argument("staff_id", type=int, default=DEFAULT_STAFF_ID)
# def add_to_shortlist_command(student_id, position_id, staff_id):
#     test = add_student_to_shortlist(student_id, position_id, staff_id)
#     if test:
#         print_success(f'Student {student_id} added to shortlist for position {position_id}')
#     else:
#         error_msg = 'One of the following is the issue:\n'
#         error_msg += f'    Position {position_id} is not open\n'
#         error_msg += f'    Student {student_id} already in shortlist for position {position_id}\n'
#         error_msg += f'    There is no more open slots for position {position_id}'
#         print_error(error_msg)

# @user_cli.command("decide_shortlist", help="Decides on a shortlist")
# @click.argument("student_id", type=int, default=DEFAULT_STUDENT_ID)
# @click.argument("position_id", type=int, default=DEFAULT_POSITION_ID)
# @click.argument("decision", default=DEFAULT_DECISION)
# def decide_shortlist_command(student_id, position_id, decision):
#     test = decide_shortlist(student_id, position_id, decision)
#     if test:
#         print_success(f'Student {student_id} is {decision} for position {position_id}')
#     else:
#         print_error(f'Student {student_id} not in shortlist for position {position_id}')

# @user_cli.command("get_shortlist", help="Gets a shortlist for a student")
# @click.argument("student_id", type=int, default=DEFAULT_STUDENT_ID)
# def get_shortlist_command(student_id):
#     list = get_shortlist_by_student(student_id)
#     if list:
#         for item in list:
#             print(f'Student {item.student_id} is {item.status.value} for position {item.position_id}')
#         print_separator()
#     else:
#         print_error(f'Student {student_id} has no shortlists')

# @user_cli.command("get_shortlist_by_position", help="Gets a shortlist for a position")
# @click.argument("position_id", type=int, default=DEFAULT_POSITION_ID)
# def get_shortlist_by_position_command(position_id):
#     list = get_shortlist_by_position(position_id)
#     if list:
#         for item in list:
#             print(f'Student {item.student_id} is {item.status.value} for {item.position.title} id: {item.position_id}')
#             print(f'    Staff {item.staff_id} added this student to the shortlist')
#             print(f'    Position {item.position_id} is {item.position.status.value}')
#             print(f'    Position {item.position_id} has {item.position.number_of_positions} slots')
#             print(f'    Position {item.position_id} is for {item.position.title}')
#             print_separator()
#     else:
#         print_error(f'Position {position_id} has no shortlists')

# @user_cli.command("get_positions_by_employer", help="Gets all positions for an employer")
# @click.argument("employer_id", type=int, default=DEFAULT_EMPLOYER_ID)
# def get_positions_by_employer_command(employer_id):
#     list = get_positions_by_employer(employer_id)
#     if list:
#         for item in list:
#             print(f'Position {item.id} is {item.status.value}')
#             print(f'    Position {item.id} has {item.number_of_positions} slots')
#             print(f'    Position {item.id} is for {item.title}')
#             print_separator()
#     else:
#         print_error(f'Employer {employer_id} has no positions')
            
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
Employer Commands
'''

employer_cli = AppGroup('employer', help='Employer object commands')
@employer_cli.command("list", help="Lists all employers in the database")
def list_employers_command():
    employers = get_all_employers()

    if not employers:
        print("\nNo employers found.\n")
        return

    print("")
    for emp in employers:
        print(emp)
    print("")

app.cli.add_command(employer_cli)

@employer_cli.command("view-positions", help="View positions for a specified employer")
def view_positions_command():
    print("\nEmployers:\n")
    employers = get_all_employers()

    if not employers:
        print('No employers found. Cannot view positions.')
        return

    for emp in employers:
        print(f'ID: {emp.id} Name: {emp.username} Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    print("")
    emp = get_employer_by_id(empID)
    if not emp:
        print('Employer not found.')
        return

    positions =  view_positions(empID)
    if positions:
        for pos in positions:
            print(pos)
    else:
        print('No positions found for this employer.')
    print("")

@employer_cli.command("view-position-shortlist", help="View the shortlist for a specified position")
def view_position_shortlist_command():

    employers = get_all_employers()

    if not employers:
        print('No employers found. Cannot view position shortlist.')
        return

    print("\nEmployers:\n")

    for emp in employers:
        print(f'ID: {emp.id} Name: {emp.username} Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    print("")
    emp = get_employer_by_id(empID)
    if not emp:
        print('Employer not found.')
        return

    print("\nPositions:\n")
    positions = Position.query.filter_by(employerID=empID).all()
    for pos in positions:
        print(f'Position ID: {pos.id} Title: {pos.positionTitle}')
    
    position_id = input('\nEnter position ID: ')
    print("")
    position = get_position_by_id(position_id)
    if not position:
        print('Position not found.')
        return

    student_positions = view_position_shortlist(position_id)
    if student_positions:
        for sp in student_positions:
            print(sp)
    else:
        print('No students found in the shortlist for this position.')
    print("")

@employer_cli.command("create", help="Creates an employer")
def create_employer_command():
    username = input('\nEnter employer username: ')
    password = input('\nEnter employer password: ')
    companyName = input('\nEnter company name: ')

    e = Employer.query.filter_by(username=username, companyName=companyName).first()
    if e:
        print('\nThis employer already exists.')
        return
    else:
        create_employer(username, password, companyName)
        print(f'\nEmployer {username} created!')

@employer_cli.command("create-position", help="Create a new internship position")
def create_position_command():
    employers = get_all_employers()
    if not employers:
        print('No employers found. Cannot create position.')
        return

    print("\nEmployers:\n")
    print("")
    for emp in employers:
        print(f'ID: {emp.id} | Name: {emp.username} | Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    emp = get_employer_by_id(empID)
    if not emp:
        print('Employer not found.')
        return

    title = input('\nEnter position title: ')
    depart = input('\nEnter department: ')
    descr = input('\nEnter description: ')

    p = Position.query.filter_by(positionTitle=title, employerID=empID, department=depart, description=descr).first()
    if p:
        inp = ""
        print('This position already exists for this employer. Would you like to create a duplicate? (y/n): ')

        while inp not in ['y', 'n']:
            inp = input().lower()
            if inp not in ['y', 'n']:
                print('Invalid input. Please enter "y" or "n".')
        if inp == 'n': 
            print('Position creation cancelled.')
            return

    position = create_position(empID, title, depart, descr)
    print(f'\n"{position.positionTitle}" position created for employer {emp.username}.\n')

@employer_cli.command("accept-reject", help="Accept or reject a student application")
def accept_reject_command():
    employers = get_all_employers()

    if not employers:
        print('No employers found. Cannot process applications.')
        return

    print("\nEmployers:\n")
    print("")
    for emp in employers:
        print(f'ID: {emp.id} | Name: {emp.username} | Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    emp = get_employer_by_id(empID)
    if not emp:
        print('Employer not found.')
        return
    
    # Should close positions after a person is accepted, but for simplicity that will not be implemented

    print("\nPositions:\n")
    positions = Position.query.filter_by(employerID=empID).all()
    for pos in positions:
        print(f'ID: {pos.id} Title: {pos.positionTitle}')
    
    position_id = input('\nEnter position ID: ')
    position = get_position_by_id(position_id)
    if not position:
        print('Position not found.')
        return

    print("\nStudents who applied to this position:\n")
    student_positions = Student_Position.query.filter_by(positionID=position_id).all()
    for sp in student_positions:
        student = get_student_by_id(sp.studentID)
        print(f'ID: {student.id} Name: {student.username} Status: {sp.status}')
    
    student_id = input('\nEnter student ID: ')
    sp = Student_Position.query.filter_by(studentID=student_id, positionID=position_id).first()
    if not sp:
        print('This student did not apply to this position.')
        return

    status = input('\nEnter status (accepted/rejected): ').lower()
    while status not in ['accepted', 'rejected']:
        print('Invalid status. Please enter "accepted" or "rejected".')
        status = input('\nEnter new status (accepted/rejected): ').lower()

    message = input('\nEnter an optional message (press Enter to skip): ')
    if message.strip() == '':
        message = None

    if emp.acceptReject(student_id, position_id, status, message):
        print(f'Student application updated to "{status}".')
    else:
        print('Failed to update application status.')

'''
Staff Commands
'''

staff_cli = AppGroup('staff', help='Staff object commands')

@staff_cli.command("list", help="Lists all staff in the database")
def list_staff_command():
    staff = get_all_staff()

    if not staff:
        print("\nNo staff found.\n")
        return

    print("")
    for sta in staff:
        print(sta)
    print("")

@staff_cli.command("create", help="Creates a staff member")
def create_staff_command():
    # print("\nEmployers:\n")
    employers = get_all_employers()

    if not employers:
        print("No employers found. Cannot create staff without an employer.")
        return

    print("Select an employer to associate with the new staff member:\n")
    for emp in employers:
        print(f'ID: {emp.id} Name: {emp.username} Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    emp = get_employer_by_id(empID)
    if not emp:
        print('Employer not found.')
        return

    username = input('\nEnter staff username: ')
    password = input('\nEnter staff password: ')

    s = Staff.query.filter_by(username=username, employerID=emp.id).first()
    if s:
        print('\nThis staff member already exists for this employer.')
        return

    sta = create_staff(username, password, emp.id)
    db.session.add(sta)
    db.session.commit()
    print(f'Staff member {username} created for employer {emp.username}.')

@staff_cli.command("add-to-shortlist", help="Add a student to a position's shortlist")
def add_to_shortlist_command():
    staff = get_all_staff()
    if not staff:
        print('No staff found. Cannot add to shortlist.')
        return
    print("\nStaff:\n")
    print("")
    for sta in staff:
        print(f'ID: {sta.id} Name: {sta.username}')
    
    staff_id = input('\nEnter staff ID: ')
    print("")
    staff =  get_staff_by_id(staff_id)
    if not staff:
        print('Staff not found.')
        return

    print("\nPositions:\n")
    positions = Position.query.filter_by(employerID=staff.employerID).all()
    if not positions:
        print('No positions found for the employer associated with this staff member.')
        return
    for pos in positions:
        print(f'ID: {pos.id} Title: {pos.positionTitle}')
    
    position_id = input('\nEnter position ID: ')
    position = get_position_by_id(position_id)
    if not position:
        print('Position not found.')
        return

    students = get_all_students()

    if not students:
        print('No students found. Cannot add to shortlist.')
        return

    print("\nStudents:\n")
    for stu in students:
        print(f'ID: {stu.id} Name: {stu.username}')
    
    student_id = input('\nEnter student ID: ')
    student = Student.query.filter_by(id=student_id).first()
    if not student:
        print('Student not found.')
        return

    sp = Student_Position.query.filter_by(studentID=student_id, positionID=position_id).first()
    if sp:
        print('Student is already in the shortlist for this position.')
        return

    # if staff.addToShortlist(position_id, student_id):
    if addToShortlist(staff_id, position_id, student_id):
        print(f'\nStudent {student.username} added to shortlist of position {position.positionTitle}.')
    else:
        print('\nFailed to add student to shortlist.')

@staff_cli.command("remove-from-shortlist", help="Remove a student from a position's shortlist")
def remove_from_shortlist_command():
    print("\nStaff:\n")
    staff = get_all_staff()
    for sta in staff:
        print(f'ID: {sta.id} | Name: {sta.username}')
    
    staff_id = input('\nEnter staff ID: ')
    staff_member = get_staff_by_id(staff_id)
    if not staff_member:
        print('Staff not found.')
        return

    print("\nPositions:\n")
    positions = Position.query.filter_by(employerID=staff_member.employerID).all()
    if not positions:
        print('No positions found for this employer.')
        return
    
    for pos in positions:
        print(f'ID: {pos.id} | Title: {pos.positionTitle}')
    
    position_id = input('\nEnter position ID: ')
    position = get_position_by_id(position_id)
    if not position:
        print('Position not found.')
        return

    print("\nShortlisted Students:\n")
    shortlist = view_position_shortlist(position_id)
    if not shortlist:
        print('No students in the shortlist for this position.')
        return
    
    for sp in shortlist:
        student = get_student_by_id(sp.studentID)
        print(f'ID: {student.id} | Name: {student.username} | Status: {sp.status}')
    
    student_id = input('\nEnter student ID to remove: ')
    
    sp = Student_Position.query.filter_by(studentID=student_id, positionID=position_id).first()
    if not sp:
        print('\nStudent not found in this position\'s shortlist.')
        return
    
    confirm = input(f'\nAre you sure you want to remove this student from the shortlist? (y/n): ')
    if confirm.lower() != 'y':
        print('Action cancelled.')
        return
    
    db.session.delete(sp)
    db.session.commit()
    print(f'\nStudent removed from shortlist successfully.\n')

app.cli.add_command(staff_cli)

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

@student_cli.command("view-shortlists", help="View shortlists a specified student was added to")
def view_shortlists_command():
    print("\nStudents:\n")
    students = get_all_students()
    for stu in students:
        print(f'ID: {stu.id} Name: {stu.username}')
    
    student_id = input('\nEnter student ID: ')
    print("")
    student = get_student_by_id(student_id)
    if not student:
        print('Student not found.')
        return

    student = Student_Position.query.filter_by(studentID=student_id).all()
    if student:
        for s in student:
            print(s)
    else:
        print('No shortlists found for this student.')
    print("")

@student_cli.command("browse-positions", help="Browse available positions")
def browse_positions_command():

    # Should only show positions that are open and not shortlisted to yet

    positions = get_all_positions()
    if not positions:
        print("\nNo positions available.\n")
        return
    
    print("\n=== Available Positions ===\n")
    for pos in positions:
        employer = get_employer_by_id(pos.employerID)
        print(f"ID: {pos.id} | {pos.positionTitle}")
        print(f"  Company: {employer.companyName if employer else 'Unknown'}")
        print(f"  Department: {pos.department}")
        print(f"  Description: {pos.description}")
        
        # Show number of applicants
        shortlist = view_position_shortlist(pos.id)
        print(f"  Applicants: {len(shortlist) if shortlist else 0}")
        print("")

app.cli.add_command(student_cli)

'''
Position Commands
'''

position_cli = AppGroup('position', help='Position object commands')

@position_cli.command("list", help="Lists all positions")
def list_positions_command():
    positions = get_all_positions()
    if not positions:
        print("\nNo positions found.\n")
        return
    
    print("\n=== All Positions ===\n")
    for pos in positions:
        employer = get_employer_by_id(pos.employerID)
        print(f"ID: {pos.id} | {pos.positionTitle}")
        print(f"  Company: {employer.companyName if employer else 'Unknown'}")
        print(f"  Department: {pos.department}")
        print(f"  Description: {pos.description}\n")

@position_cli.command("view", help="View a specific position")
def view_position_command():
    positions = get_all_positions()
    if not positions:
        print("\nNo positions available.\n")
        return
    
    print("\nAvailable Positions:\n")
    for pos in positions:
        employer = get_employer_by_id(pos.employerID)
        print(f"ID: {pos.id} | {pos.positionTitle} - {employer.companyName if employer else 'Unknown'}")
    
    pos_id = input("\nEnter position ID: ")
    position = get_position_by_id(pos_id)
    
    if not position:
        print(f"\nPosition {pos_id} not found.\n")
        return
    
    employer = get_employer_by_id(position.employerID)
    shortlist = view_position_shortlist(pos_id)
    
    print(f"\n=== Position Details ===")
    print(f"Title: {position.positionTitle}")
    print(f"Company: {employer.companyName if employer else 'Unknown'}")
    print(f"Department: {position.department}")
    print(f"Description: {position.description}")
    print(f"Shortlisted Students: {len(shortlist) if shortlist else 0}\n")

@position_cli.command("delete", help="Delete a position")
def delete_position_command():
    print("\nPositions:\n")
    positions = get_all_positions()
    if not positions:
        print("No positions available.\n")
        return
    
    for pos in positions:
        employer = get_employer_by_id(pos.employerID)
        print(f"ID: {pos.id} | {pos.positionTitle} - {employer.companyName if employer else 'Unknown'}")
    
    pos_id = input("\nEnter position ID to delete: ")
    position = get_position_by_id(pos_id)
    
    if not position:
        print(f"\nPosition {pos_id} not found.\n")
        return
    
    confirm = input(f"\nAre you sure you want to delete '{position.positionTitle}'? (y/n): ")
    if confirm.lower() != 'y':
        print("Deletion cancelled.\n")
        return
    
    # Check if there are students in shortlist
    shortlist = view_position_shortlist(pos_id)
    if shortlist:
        print(f"\nWarning: This position has {len(shortlist)} student(s) in the shortlist.")
        confirm2 = input("Delete anyway? (y/n): ")
        if confirm2.lower() != 'y':
            print("Deletion cancelled.\n")
            return
    
    # Delete associated student positions first
    Student_Position.query.filter_by(positionID=pos_id).delete()
    db.session.delete(position)
    db.session.commit()
    print(f"\nPosition '{position.positionTitle}' deleted successfully.\n")

app.cli.add_command(position_cli)