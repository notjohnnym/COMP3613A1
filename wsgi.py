import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize,
                                create_course, get_all_courses_json )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

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
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


'''
Course Commands
'''

course_cli = AppGroup('course', help='Course object commands') 

@course_cli.command("create", help="Creates a course")
@click.argument("code", default="COMP3613")
@click.argument("title", default="SEII")
@click.argument("credit", default=3)
@click.argument("semester", default=1)
@click.argument("faculty", default="FST")
def create_course_command(code, title, credit, semester, faculty):
    create_course(code, title, credit, semester, faculty)
    print(get_all_courses_json())

# this command will be flask course create args


@course_cli.command("view", help="View Course Staff")
def view_course_staff():
    pass

# this command will be flask course view

app.cli.add_command(course_cli)


'''
Lecturer Commands
'''

lecturer_cli = AppGroup('lecturer', help='Lecturer object commands') 

@lecturer_cli.command("create", help="Creates a lecturer")
def create_lecturer_command():
    pass

# this command will be flask lecturer create args


@lecturer_cli.command("assign", help="Assigns a lecturer to a course")
def assign_lecturer_command():
    pass

# this command will be flask lecturer assign args

app.cli.add_command(lecturer_cli)


'''
TA Commands
'''

ta_cli = AppGroup('ta', help='TA object commands')

@ta_cli.command("create", help="Creates a ta")
def create_ta_command():
    pass

# this command will be flask ta create args


@ta_cli.command("assign", help="Assigns a ta to a course")
def assign_ta_command():
    pass

# this command will be flask ta assign args

app.cli.add_command(ta_cli)


'''
Tutor Commands
'''

tutor_cli = AppGroup('tutor', help='Tutor object commands')

@tutor_cli.command("create", help="Creates a tutor")
def create_tutor_command():
    pass

# this command will be flask tutor create args


@tutor_cli.command("assign", help="Assigns a tutor to a course")
def assign_tutor_command():
    pass

# this command will be flask ta assign args

app.cli.add_command(tutor_cli)



'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)