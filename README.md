# The programme Task Manager is the final capstone project for my Software Engineering Bootcamp course with Hyperion Dev.


## The functionality of this programme is a productivity application to allow users to assign tasks to users, mark them when completed and edit when necessary. The admin can generate reports on the activity on the programme and show data on which tasks are completed, incomplete, due dates, who they are assigned to.


**Contents:**
- Installation
- Running the programme
- Maintainance and contribution credits


**Installation:**
- Application can be cloned onto a new constributor's local machine.
- Make sure the folder in downloaded with all 3 fies inside: task_manager.py, user.txt and tasks.txt.


**Running The Programme**
- The first time you run and login to the programme you need to use the username: *admin* and password: *password*
- Choice from a menu to either: register a user, add a task, view all tasks, view tasks assigned to logged in user, if logged in as admin you'd be able to generate reports, display statistics or exit programme
- When registering a new user, the prorgramme with not allow duplicate usernames.
- When adding a task, the programme asking for the following input: assign a user to a task, give the task a title, desciption of the task, and a due date for completing the task. The programme will not let the due date be in the past.
- Viewing all tasks allows users to see all tasks assigned to all users and the task details.
- Viewing my tasks allows users to see tasks assigned to them and all the task details. It also gives the user the option to edit a task.
- When editing a task the user can either: mark task as complete, edit user assigned to task or edit due date.
- Users can not edit the due date of either completed or after due date tasks.
- Admin user can generate reports, other users are not able to do this.
- These reports are opened as new files in the folder with the main code. They are printed in an easy to read format, for reviewing the progess of tasks.
- Display Statistics print on the consol an overview of the Number of Users and the Number of Tasks.
- Each step of the programme with options includes an option to go back in the programme.


*This programme is maintained and contributed by Stephanie Hornby*
