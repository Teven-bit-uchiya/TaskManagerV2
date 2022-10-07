# ===========importing Libraries=======#
from datetime import date, datetime
from os import path
from tomlkit import value


# Function to add a user to a text file
def add_user():
    # Declare variables to store username and password input
    new_username = input("Enter a username:\n")  # Store username input
    new_password = input("Enter a password:\n")  # Store password input
    confirm_password = input("Confirm password:\n")  # Store password input for confirmation

    # If password and confirm password match
    if new_password == confirm_password:
        with open("user.txt", "r") as f:  # Open the user.txt file in read mode
            for line in f:  # Iterate through each line in the file
                line = line.replace("\n", "").split(
                    ", ")  # Remove the newline at the end of each line and split each line where there is a comma

                if line[
                    0] != new_username:  # If the username from the file does not equal the username entered by the user
                    with open("user.txt", "a") as file:  # Open the user.txt file in append mode
                        file.write(f"\n{new_username}, {new_password}")  # Write the username and password to the file
                        print("User added successfully")  # Print success message to the user
                else:  # If the username from the file equals the username entered by the user
                    print("Username already exists")  # Print error message to the user
    else:
        print("Passwords do not match")  # If passwords do not match, print error message to the user

# here we are creating a function to add a task


def add_task():
    # here we are asking the user to input the username who the task is assigned to
    username_tasked = input("Enter the username whom the task is assigned to:\n")
    # here we are asking the user to input the title of the task
    task_title = input("Enter the title of the task:\n")
    # here we are asking the user to input the description of the task
    task_description = input("Enter the description of the task:\n")
    # here we are asking the user to input the due date of the task
    due_date = input("Enter the due date:\n")
    # here we are getting the current date
    today = date.today()
    # here we are changing the format of the output
    today = str(today.strftime("%d %B %Y"))
    # here we are setting the default value of whether the task has been completed to No
    task_complete = "No"
    # here we are opening the tasks.txt file
    with open("tasks.txt", "a") as f:
        # here we are appending the task to the file
        f.write(
            username_tasked + ", " + task_title + ", " + task_description + ", " + due_date + ", " + today + ", " + task_complete + "\n")


def view_all_tasks():
    """
    - Opens file in read mode
    - For each line of the file
        - Replaces newline character with nothing
        - Splits line at comma and space
        - Prints each line in a formatted way
    """
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "").split(", ")
            print(
                f"\nTask: {line[1]}\nAssigned to: {line[0]} \nDate assigned: {line[4]}\nDue date: {line[3]}\nTask "
                f"complete?: {line[5]}\nTask description: {line[2]}\n")


def view_my_tasks():
    task_numb = 1 #starting task number
    tasks = {}

    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "").split(", ") #separates the line by comma and removes spaces
            tasks[task_numb] = line #creates a dictionary with each task assigned a number, the number is the task number
            if line[0] == username: #the first item in the list is the username, checks if the name matches
                print(
                #prints out the task, task description and due date
                    f"Task number {task_numb}\nTask: {line[1]} \nAssigned to: {line[0]} \nDate assigned: {line[4]} "
                    f"\nDue date: {line[3]} \nTask complete?: {line[5]} \nTask description: {line[2]}\n")
    #asks user to input a number of a task or -1 to retun to the main menu
            task_numb += 1
    task_choice = int(input("Select either a specific task by entering a number or input -1 to the main menu: "))
    mark_edit_task = input('''Select one of the following Options below:
    mc -Mark task as complete
    ed - edit task:
    .lower()''')
    #asks user whether they want to mark the task complete or edit the task, if mark task as complete the task can no longer
    #be edited
    if mark_edit_task == "mc":
        tasks[task_choice][5] = "Yes"
    else: #if the user wants to edit the task
        if line[5] == "No":
            tasks[task_choice][0] = input("Edit user name: ") #edits the username
            tasks[task_choice][3] = input("Edit due date: ") #edits the due date
        else:
            print("You cant edit completed tasks")
    with open("tasks.txt", "w") as f:
        for task in tasks.values(): #saves the file as a text file
            f.write(f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}\n")


def user_overview():

    #Open user file to get number of users
    with open("user.txt", "r") as user_file:
        user_file_content = user_file.readlines()
        no_users = len(user_file_content)

    #Open task file to get number of tasks
    with open("tasks.txt", "r") as task_file:
        task_file_content = task_file.readlines()
        no_of_tasks = len(task_file_content)

    #Open user overview file to write data
    with open("task_overview.txt", "w") as my_file:

        #Loop through user file
        for line in user_file_content:
            #Remove \n and separate user and tasks
            line = line.replace("\n", "").split(", ")

            #Assign user to variable
            user = line[0]

            #Create variables to count users tasks
            user_total_tasks = 0
            user_completed = 0
            user_uncomplete = 0
            user_uncomp_overdue = 0
            #Loop through task file
            for line in task_file_content:


                #Remove \n and separate user, task data

                #Assign task to variable
                line = line.replace("\n", "").split(", ")

                #Check if user and task user match
                task_user = line[0]

                #If match do the following:
                if user == task_user:

                    #Convert todays date and due date to dates
                    todays_date = date.today().strptime(line[-3], "%d %b %Y").date()
                    due_date = datetime.strptime(line[-2], "%d %b %Y").date()

                    #Check if task is completed and count completed, uncompleted and uncompleted and overdue tasks

                    user_total_tasks += 1
                    if line[5] == "Yes":
                        user_completed += 1
                    elif line[5] == "No" and due_date < todays_date:

                    #Calculate task percentages
                        user_uncomp_overdue += 1
                    else:
                        user_uncomplete += 1


            #Write overview to file
            user_task_percentage = round(((user_total_tasks / no_of_tasks) * 100), 2)
            user_task_comp_percent = round(((user_completed / user_total_tasks) * 100), 2)
            user_task_uncomp_percent = round(((user_uncomplete / user_total_tasks) * 100), 2)
            user_task_uncomp_overdue_percent = round(((user_uncomp_overdue / user_total_tasks) * 100), 2)
            my_file.write(f"Number of User: {no_users}\n"
                        f"Number of Tasks: {no_of_tasks}\n"
                        f"Tasks user: {user}\n"
                        f"Total number of user tasks: {user_total_tasks}\n"
                        f"Total number of tasks user completed: {user_completed}\n"
                        f"Total number of tasks user uncompleted: {user_uncomplete}\n"
                        f"Total number of tasks user uncompleted and overdue: {user_uncomp_overdue}\n"
                        f"Percentage of tasks user has: {user_task_percentage}%\n"
                        f"Percentage of tasks user completed: {user_task_comp_percent}%\n"
                        f"Percentage of tasks user uncompleted: {user_task_uncomp_percent}%\n"
                        f"Percentage of tasks user uncompleted and overdue: {user_task_uncomp_overdue_percent}%\n")


def task_overview():
    # declaring the variables
    no_of_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    uncompleted_overdue = 0
    today = date.today()

    # opening the file in read mode
    with open("tasks.txt", "r") as f:
        # looping through each line in the file
        for line in f:
            # removing the new line character and splitting the line into a list
            line = line.replace("\n", "").split(", ")
            no_of_tasks += 1
            due_date = datetime.strptime(line[-2], "%d %b %Y").date()
            # if the task is completed, increase the completed_tasks variable by 1

            if line[-1] == "Yes":
                completed_tasks += 1
            elif line[-1] == "No":
                # if the task is not completed and the due date is today or before, increase the uncompleted_overdue variable by 1
                uncompleted_tasks += 1
                if today > due_date:
                    uncompleted_overdue += 1

    # calculating the percentage of tasks that are incomplete and those that are overdue
    incomplete_percentage = round(((uncompleted_tasks / no_of_tasks) * 100), 2)
    overdue_percentage = round(((uncompleted_overdue / no_of_tasks) * 100), 2)

    # opening the file in write mode
    with open("task_overview.txt", "w") as f:
        f.write(f"The total number of tasks: {no_of_tasks} \n"
                f"The total number  of completed tasks: {completed_tasks} \n"
                f"The total number of  uncompleted tasks: {uncompleted_tasks} \n"
                f"The total number of tasks that have not been completed and overdue: {uncompleted_overdue}%\n"
                f"The percentage of tasks that are incomplete: {incomplete_percentage}% \n"
                f"The percentage of tasks that are overdue: {overdue_percentage}%")


def user_overview():
    # Open user file to get number of users
    with open("user.txt", "r") as user_file:
        user_file_content = user_file.readlines()
        no_users = len(user_file_content)

    # Open task file to get number of tasks
    with open("tasks.txt", "r") as task_file:
        task_file_content = task_file.readlines()
        no_of_tasks = len(task_file_content)

    # Open user overview file to write data
    with open("task_overview.txt", "w") as my_file:

        # Loop through user file
        for line in user_file_content:
            # Remove \n and separate user and tasks
            line = line.replace("\n", "").split(", ")

            # Assign user to variable
            user = line[0]

            # Create variables to count users tasks
            user_total_tasks = 0
            user_completed = 0
            user_uncomplete = 0
            user_uncomp_overdue = 0
            # Loop through task file
            for line in task_file_content:

                # Remove \n and separate user, task data

                # Assign task to variable
                line = line.replace("\n", "").split(", ")

                # Check if user and task user match
                task_user = line[0]

                # If match do the following:
                if user == task_user:

                    # Convert todays date and due date to dates
                    todays_date = date.today().strptime(line[-3], "%d %b %Y").date()
                    due_date = datetime.strptime(line[-2], "%d %b %Y").date()

                    # Check if task is completed and count completed, uncompleted and uncompleted and overdue tasks

                    user_total_tasks += 1
                    if line[5] == "Yes":
                        user_completed += 1
                    elif line[5] == "No" and due_date < todays_date:

                        # Calculate task percentages
                        user_uncomp_overdue += 1
                    else:
                        user_uncomplete += 1

            # Write overview to file
            user_task_percentage = round(((user_total_tasks / no_of_tasks) * 100), 2)
            user_task_comp_percent = round(((user_completed / user_total_tasks) * 100), 2)
            user_task_uncomp_percent = round(((user_uncomplete / user_total_tasks) * 100), 2)
            user_task_uncomp_overdue_percent = round(((user_uncomp_overdue / user_total_tasks) * 100), 2)
            my_file.write(f"Number of User: {no_users}\n"
                          f"Number of Tasks: {no_of_tasks}\n"
                          f"Tasks user: {user}\n"
                          f"Total number of user tasks: {user_total_tasks}\n"
                          f"Total number of tasks user completed: {user_completed}\n"
                          f"Total number of tasks user uncompleted: {user_uncomplete}\n"
                          f"Total number of tasks user uncompleted and overdue: {user_uncomp_overdue}\n"
                          f"Percentage of tasks user has: {user_task_percentage}%\n"
                          f"Percentage of tasks user completed: {user_task_comp_percent}%\n"
                          f"Percentage of tasks user uncompleted: {user_task_uncomp_percent}%\n"
                          f"Percentage of tasks user uncompleted and overdue: {user_task_uncomp_overdue_percent}%\n")

# Write to and read from text files
def display_stats():# Open and read content of 
    with open("task_overview.txt", "r") as f:
        file_content = f.readlines()  # Set file content to file_content variable
         # Loop through each line in file content
        [print(line) for line in file_content]  # print the lines
    with open("task_overview.txt", "r") as fh: # Open and read content of user_overview.txt
        contents = fh.readlines()  # get the lines
        [print(line) for line in contents]


# log in section
user_names = {}

# Read the user file and add each line to a dictionary
with open("user.txt", "r") as f:
    for line in f:
        username_f, password_f = line.replace("\n", "").split(", ")
        user_names[username_f] = password_f

# Ask for username and check if it is in the file
username = input("Enter your username:\n")
while not username in user_names:
    print("Invalid username")
    username = input("Enter your username:\n")

# Ask for password and check if it is right
password = input("Enter your password:\n")
while password != user_names[username]:
    print("Invalid password")
    password = input("Enter your password:\n")

# Infinite loop
while True:

    # If the current user is admin
    if username == "admin":

        # Ask for choice and call the corresponding function
        menu = input("Menu:\n"
                     "r - register user\n"
                     "a - add task\n"
                     "va - view all tasks\n"
                     "vm - view my tasks\n"
                     "e - exit\n").lower()
        if menu == "r":
            add_user()
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all_tasks()
        elif menu == "vm":
            task_overview()
            user_overview()
            display_stats()
        elif menu == "e":
            break

    # If the current user is not admin
    else:

        # Ask for choice and call the corresponding function
        menu = input("Welcome user select an option from the menu below:\n"
                     "a - Add task\n"
                     "va - View all tasks\n"
                     "vm - View my tasks\n"
                     "e - Exit\n"
                     "Enter your choice:\n")
        if menu == "a":
            add_task()
        elif menu == "va":
            view_all_tasks()
        elif menu == "vm":
            view_my_tasks()
        elif menu == "e":
            print("Goodbye user {}".format(username))
            exit()
        else:
            print("Invalid choice not in menu")