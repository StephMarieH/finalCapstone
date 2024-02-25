# Notes: 

# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password

# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.


#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


#=====Defining Functions===========
def line(symbol='-', length=79):
    '''
    Creates a line in the code, 79 characters long to break up the code.
    '''
    return(symbol*length)


def print_heading(title):
    '''
    Print title in the middle of the code.
    '''
    print((' '*(40-(len(title)//2))), title)


def reg_user(username_password):
    '''
    Register a new user and password to the user.txt file.
    '''
    while True:
        # Opens the file for storing usernames, creates one if one doesn't yet exist.
        with open("user.txt", 'r+') as file_obj:
            # Request input of a new username.
            new_username = input("New Username: ")
            user_exists_check = file_obj.read()
        # Adds the new username to file, if it does not yet exist.    
        if new_username not in user_exists_check:
            with open("user.txt", 'a+') as file_obj:
                file_obj.write(f"\n{new_username}")
            break
        else:
            # Error handling, so no 2 usernames are the same.
            print("ERROR: Username already in use, please re-enter:")
            return False
        
    # Request user to input a new password.
    new_password = input("New Password: ")

    # Request user to input password agin to confirm.
    confirm_password = input("Confirm Password: ")

    # Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
    # If they are the same, add them to the user.txt file.
        print("New user added")
        username_password[new_username] = new_password
            
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # Otherwise you present a relevant message, and returns to main menu.
    else:
        print("ERROR: Passwords do no match")


def add_task(task_list, username_password):
    '''
    Allow a user to add a new task to task.txt file.
    Prompt a user for the following: 
    - A username of the person whom the task is assigned to
    - A title of a task
    - A description of the task
    - The due date of the task
    Add the data to the file task.txt and
    Include 'No' to indicate if the task is complete.
    '''
    task_username = input("Name of person assigned to task: ")
    # Ask user for username input, re-ask if input does not match usernames in file.
    if task_username not in username_password.keys():
        print("ERROR: User does not exist. Please enter a valid username")
    # Ask user for task name input.    
    task_title = input("Title of Task: ")
    # Ask user for task description input.
    task_description = input("Description of Task: ")
    while True:
        # Ask user for due date input.
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        # Error handle if input does not match date format.
        except ValueError:
            print("ERROR: Invalid datetime format. Please use the format specified")


    # Save the current date as variable.
    curr_date = date.today()
    # Save task details as a dictionary.
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    # Append new task in list format to the tasks file.
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all(task_list):
    '''Reads the tasks from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling) 
    '''
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_mine(task_list, curr_user):
    '''Reads the tasks from task.txt file and prints to the console the tasks
    assigned to the username the user is currently signed in with, in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    '''
    while True:
        # Gives each task a task number, and formats information to print.
        for i, t in enumerate(task_list, start=1):
            # Checks to see if task is assigned to user.
            if t['username'] == curr_user:
                today = datetime.today().date()
                disp_str = f"Task no: \t\t {i}\n"
                disp_str += f"Task title: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t\t {t['username']}\n"
                disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \t {t['description']}"
                print(line())
                print(disp_str)
                print(line())
            
        try:
            # Asks for user input of which tasks they would like to edit.
            task_number = int(input("Enter the number of the task you want to edit, or -1 for main menu: "))

        except ValueError:
            # Return error if an integer is not entered, run input query again.
            print("ERROR: Please enter a task number: \n")
            continue
                        
        if task_number == -1:
            # Return to main menu if -1 entered.
            break

        elif task_number < 1 or task_number > len(task_list):
            # Return error if task number is not in task list.
            print("ERROR: Please enter a task number: \n")
            continue

        # Referring to an index, so 0 index = 1, 1 index = 2, etc.
        selected_task = task_list[task_number - 1]

        if selected_task['completed']:
            print("\nYou can not edit completed tasks\n")
            continue

        edit_option = input("Do you want to edit this task? (y/n): ").lower()

        # Execute program to edit task and update it in file.
        if edit_option == 'y':
            if edit_task(selected_task, task_list):
                update_task(task_list)
                break
            
        # If user chooses not to edit task, inform them and come back to the menu 
        elif edit_option == 'n':
            print("Task will not be edited.\n")

        else:
            print("ERROR: Invalid option.")

        # Mark task as complete


def edit_task(task, task_list):
    '''
    Function to edit tasks.
    Firstly Check if task is completed or not.
    Secondly give options of modification, ask user for input of selection.
    Then give functionality for options.

    '''
    if task['completed']:
        print("ERROR: This task is already completed. You cannot modify it.\n")
        return

    while True:
        print("1. Mark as completed")
        print("2. Edit username")
        print("3. Edit Due Date")
        print("-1. Return to Main Menu")
        
        task_edit = input("Enter the number referring to the edit you would like to make: ")

        #  Task has been completed.
        if task_edit == '1':
            task['completed'] = True
            print("Task is listed as completed!")
            break

        # Edit the username assigned to the task.
        elif task_edit == '2':
            new_username = input("Enter the new username: ")
            if new_username not in username_password.keys():
                print("ERROR: User does not exist. Please enter a valid username: \n")
                return
            task['username'] = new_username

        # Edit due date of the task.
        elif task_edit == '3':
            while True:
                try:
                    task_due_date = input("Task due date (YYYY-MM-DD): ")

                    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)

                    # Make sure new due date isn't in the past.
                    if due_date_time.date() < date.today():
                        print("ERROR: You need to enter a due date in the future.")
                        # Continue the loop to prompt user for a valid due date.
                        continue
                    # Save new due date and exit loop if due date is in the future.
                    task['due_date'] = due_date_time
                    break
                except ValueError:
                    print("ERROR: Please enter due date using (YYYY-MM-DD) format: \n")
        
        # Return to the main menu.
        elif task_edit == '-1':
            return True

        else:
            print("ERROR: Input invalid.\n")
            continue
        
        # Update the task list in the file
        update_task(task_list)
        break


def update_task(task_list):
    '''
    This function opens the task file and writes over data to update it.
    '''
    with open("tasks.txt", "a") as task_file:
        task_list_to_write = []
        for t in task_list:
            task_str = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(task_str))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully updated.")


def generate_user_report(username_password, task_list):
    '''
    Opens a new file to write to.
    Then performs calculations required in the report as per the project spec.
    Prints these answers in an easy to read format to a file in the folder.
    '''
    print("Report has been generated.")
    users_total = len(username_password)
    tasks_total = len(task_list)
    
    if users_total == 0 or tasks_total == 0:
        print("No users or tasks have been assigned yet.")
        return
    
    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(line())
        user_overview.write('\n')
        user_overview.write("User Report")
        user_overview.write('\n')
        user_overview.write(line())
        user_overview.write('\n')
        user_overview.write(f"Total number of users:\t\t\t\t\t\t\t\t{users_total}\n")
        user_overview.write(f"Total number of tasks:\t\t\t\t\t\t\t\t{tasks_total}\n\n")

        for username, password in username_password.items():
            user_tasks = [task for task in task_list if task['username'] == username]
            user_tasks_total = len(user_tasks)
            user_tasks_completed = sum(task['completed'] for task in user_tasks)
            user_tasks_overdue = sum(1 for task in user_tasks
            if not task['completed'] and task['due_date'].date() < datetime.today().date())
            user_tasks_incomplete = user_tasks_total - user_tasks_completed

            percentage_user_tasks_total = (user_tasks_total/tasks_total)*100 if tasks_total>0 else 0
            percentage_user_tasks_completed = (user_tasks_completed/user_tasks_total)*100 if user_tasks_total>0 else 0
            percentage_must_completed = (user_tasks_incomplete/user_tasks_total)*100 if user_tasks_total>0 else 0
            percentage_user_tasks_overdue = (user_tasks_overdue/user_tasks_total)*100 if user_tasks_total>0 else 0

            user_overview.write(f"User:\t\t\t\t\t\t\t\t\t\t\t\t{username}\n")
            user_overview.write(f"Total number of tasks assigned:\t\t\t\t\t\t{user_tasks_total}\n")
            user_overview.write(f"Percentage of total tasks assigned:\t\t\t\t\t{percentage_user_tasks_total:.2f}%\n")
            user_overview.write(f"Percentage of tasks assigned and completed:\t\t\t{percentage_user_tasks_completed:.2f}%\n")
            user_overview.write(f"Percentage of tasks must be completed:\t\t\t\t{percentage_must_completed:.2f}%\n")
            user_overview.write(f"Percentage of tasks not yet completed and overdue:\t{percentage_user_tasks_overdue:.2f}%\n")
            user_overview.write("\n")


def generate_task_report(task_list):
    '''
    Opens a new file to write to.
    Then performs calculations required in the report as per the project spec.
    Prints these answers in an easy to read format to a file in the folder.
    '''
    today = datetime.today()

    tasks_total = len(task_list)

    tasks_completed = sum(task['completed'] for task in task_list)

    tasks_uncompleted = tasks_total - tasks_completed

    tasks_overdue = sum(1 for task in task_list
    if not task['completed'] and task['due_date'].date() < today.date())

    percentage_incomplete = (tasks_uncompleted / tasks_total) * 100 if tasks_total > 0 else 0

    percentage_overdue = (tasks_overdue / tasks_total) * 100 if tasks_total > 0 else 0

    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(line())
        task_overview.write('\n')
        task_overview.write("Task Report")
        task_overview.write('\n')
        task_overview.write(line())
        task_overview.write('\n')           
        task_overview.write(f"Total number of tasks:\t\t\t\t\t\t\t{tasks_total}\n")
        task_overview.write(f"Total number of completed tasks:\t\t\t\t{tasks_completed}\n")
        task_overview.write(f"Total number of uncompleted tasks:\t\t\t\t{tasks_uncompleted}\n")
        task_overview.write(f"Total number of tasks incomplete and overdue:\t{tasks_overdue}\n")
        task_overview.write(f"Percentage of incomplete tasks:\t\t\t\t\t{percentage_incomplete:.2f}%\n")
        task_overview.write(f"Percentage of overdue tasks:\t\t\t\t\t{percentage_overdue:.2f}%\n\n")

        for index, task in enumerate(task_list, start=1):
            task_overview.write(f"Task\t\t\t{index}:\n")
            task_overview.write(f"Title:\t\t\t{task['title']}\n")
            task_overview.write(f"Assigned to:\t{task['username']}\n")
            task_overview.write(f"Due Date:\t\t"
            f"{task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n")
            task_overview.write(f"Description:\t{task['description']}\n")
            status = 'Completed' if task['completed'] else 'Not Completed'
            task_overview.write(f"Status:\t\t\t{status}\n")
            if task['username'] not in username_password:
                task_overview.write("User deleted\n")
            task_overview.write("\n")



#---------- End of Functions. -----------
                 
#---------- Start of main code. ------------
            
# Create user.txt if it doesn't exist
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass


task_list = []

for t_str in task_list:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''
This code reads usernames and password from the user.txt file to
allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print(line())
    print_heading("LOGIN")
    print(line())
    print()
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    print()
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    # if user is admin:
    print()
    print(line())
    print()
    menu = input('''Select one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - exit
: ''').lower()
    print(line())


    if menu == 'r':
        reg_user(username_password)

    elif menu == 'a':
        add_task(task_list, username_password)

    elif menu == 'va':
        view_all(task_list)
            
    elif menu == 'vm':
        view_mine(task_list, curr_user)

    elif menu == 'gr':
        # Only enable admins to generarte reports.
        if curr_user == 'admin':
            generate_task_report(task_list)
            generate_user_report(username_password, task_list)

        else:
            print("Only admin users can generate reports.")
            # Return to main menu.
            continue  

    elif menu == 'ds':
        '''
        If admin user is logged in, show the display statistics option.
    if admin_rights:
        '''
        if curr_user == 'admin':
            num_users = len(username_password.keys())
            num_tasks = len(task_list)

            print(line())
            print(f"Number of users: \t\t {num_users}")
            print(f"Number of tasks: \t\t {num_tasks}")
            print(line())

        else:
            print("Only admin users can display statistics.")
            # Return to main menu.
            continue  

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


