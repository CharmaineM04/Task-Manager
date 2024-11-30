# Capstone project - Lists, Functions, and string handling
# Task_24

#=====importing libraries===========
from datetime import datetime

#====Login Section====
# Open text file in reading mode and readlines
# Store in a variable credentials
# Log in into the program, using a while loop
def login():
    credentials = {}
    with open("user.txt", "r") as file:
        for lines in file.readlines():
            key, value = lines.strip().split(", ")
            credentials[key.strip()] = value.strip()
    
    while True:
        username = input("Please enter username: ").lower()
        password = input("Please enter password: ").lower()
        if username in credentials and credentials[username] == password:
            print("Logged in successfully")
            return username
        else:
            print("Incorrect username or password. Please try again")

# Function to present the menu to the user               
def menu():
    while True:
        choice = input('''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit
        : ''').lower()
        if choice in ['r', 'a', 'va', 'vm', 'gr', 'ds', 'e']:
            return choice
        else:
            print("Invalid selection. Please try again")

#Function to add a new user to the user.txt file 
def reg_user():
        new_user = input("Enter a username : ").lower()
        new_password = input("Enter a password : ").lower()
        while True:
            password_confirm = input("Re-enter your password to confirm : ").lower()
            if new_password == password_confirm:
                print("Passwords match\n")
                break
            else :
                 print("Passwords do not match, Please enter matching passwords")      
            
# Check if username already exists
        with open('user.txt', 'r') as file:
            existing_users = [line.split(", ")[0].lower() for line in file.readlines()]
            if new_user in existing_users:
                print("Username is already taken, choose another one")
                return
             
  # Write new user details on file           
        with open('user.txt', 'a') as new_details:
            new_details.write(f"\n{new_user}, {password_confirm}")
            print("New user has been registered\n")
            
# Function to allow a user to add a new task to tasks.txt file
def add_task():
    assignee = input("Enter the username of the person whom the task is assigned to : ").lower()
    title = input("Enter the title of the task : ").lower()
    description = input("Enter the description of the task : ").lower()
    due_date = input("Enter the due date of the task (example : 04 Apr 1998): ").lower()
    current_date = datetime.now().strftime("%d %b %Y")
    
    with open('tasks.txt', 'a') as tasks:
        tasks.write(f"{assignee}, {title}, {description}, {due_date}, {current_date}, No\n")

def view_all():
    with open('tasks.txt', 'r') as tsk:
        task_lines = tsk.readlines()
        for line in task_lines:
            task_file = line.strip().split(", ")
            
             # Skip empty lines
            if not line.strip():
                continue

            # Check if task_file has the expected number of elements
            if len(task_file) == 6:
                print(f" Assigned to:\t{task_file[0]}\n Title:\t\t{task_file[1]}\n Description:\t{task_file[2]}\n Due date:\t{task_file[3]}\n Current date:\t{task_file[4]}\n Completed?:\t{task_file[5]}\n")
            else:
                print(f"Error: Incomplete task entry: {task_file}")
 
# Function to read and display tasks from task.txt file assined to logged in user               
def view_mine ():
    
    # Assiged  user  log in and display tasks assigned  to them
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()

    for index, task in enumerate(tasks):
        split_lines = task.split(", ")
        if username == split_lines[0]:
            print(f''' ---------------Task : {index+1}-------------- 
    Assigned to:\t{split_lines[0]}
    Title:\t\t{split_lines[1]}
    Description:\t{split_lines[2]} 
    Due date:\t\t{split_lines[3]} 
    Current date:\t{split_lines[4]}
    Completed?:\t\t{split_lines[5]}''') 
        
    else:
        print("You can only view your own tasks or you have no tasks assigned.")

            
# Select specific task or enter '-1' to return to main menu
    while True:
        task_choice = input("Enter the number of task you would like to edit or enter '-1' to return to main menu : ")
        if task_choice == "-1":
            print("Return to main menu")
            break
    
# Display selected task based on user imput   
        elif 0 <= int(task_choice) <= len(tasks):
            selected_task = tasks[int(task_choice)-1].split(", ")
            print(f''' ------------Selected task:-------------- 
    Assigned to:\t{selected_task[0]}
    Title:\t\t{selected_task[1]}
    Description:\t{selected_task[2]} 
    Due date:\t\t{selected_task[3]} 
    Current date:\t{selected_task[4]}
    Completed?:\t\t{selected_task[5]}''')

 # Mark task complete if not completed already     
            modify_task = input("Please enter 1 - to mark complete your task or 2 - to edit  : ")
            if modify_task == '1':
                
# Check if the task is completed
                if selected_task[5].strip().lower() == "yes":   
                    print("Task has been already completed, can not be edited")
                else:
                    selected_task[-1] = "Yes"
                    tasks[int(task_choice) - 1] = ", ".join(selected_task) + "\n"
                    print("Task marked as complete")

# Update user and due date                   
            elif modify_task == "2":
                if selected_task[5].strip().lower() == "yes":   
                    print("Task has been already completed, can not be edited")
                    break
                update_user = input("Enter the name of the person whom the task is assigned : ")
                update_due_date = input("Enter the due date of that particular task in the format: dd mmm yyyy: ")
                selected_task[0] = update_user
                selected_task[3] ==  update_due_date
                tasks[int(task_choice) - 1] = ", ".join(selected_task) + "\n"
                print("Task updated successfully")       
            else:
                print("Invalid input. Please enter either 1 or 2.")
        else:
            print("Invalid input. Please enter a valid number or -1 to return to the main menu.")
    
    with open('tasks.txt', 'w') as file:
        file.writelines(tasks)

# Function to generate reports
def generate_reports():
    with open('user.txt', 'r') as file: 
            with open("tasks.txt", "r") as task_file:
                task_data = task_file.readlines()

# Total number of tasks
            total_tasks = len(task_data)

# Total number of completed tasks
            completed_tasks = 0
            incomplete_tasks = 0
            overdue_tasks = 0
            for task in task_data:
                task_status = task.strip().split(", ")        
                if task_status[-1].lower() == "yes":
                    completed_tasks +=1
                elif task_status[-1].lower() == "no":
                    incomplete_tasks +=1
                    if datetime.strptime(task_status[3], "%d %b %Y") < datetime.today():
                        overdue_tasks += 1 

# Percentage of  incomplete and overdue tasks
            percentage_incomplete = (incomplete_tasks / total_tasks) * 100
            percentage_overdue = (overdue_tasks / total_tasks) * 100

# Open task_overview.txt to write task-related data
            with open("task_overview.txt", "w") as task_overview_file:
                task_overview_file.write(f"Total number of tasks : {total_tasks}\n")
                task_overview_file.write(f"Total number of completed tasks: {completed_tasks}\n")
                task_overview_file.write(f"Total number of uncompleted tasks: {incomplete_tasks}\n")
                task_overview_file.write(f"Total number of tasks overdue: {overdue_tasks}\n")
                task_overview_file.write(f"Percentage of incomplete tasks: {percentage_incomplete:.2f}%\n")
                task_overview_file.write(f"Percentage of overdue tasks: {percentage_overdue:.2f}%\n")

# Number of users
            total_users =len(task_data)

# Total number of tasks
            total_tasks = len(task_data)

# Number of tasks assigned to user

            total_user_tasks = 0
            completed_user_tasks = 0
            incomplete_user_tasks = 0
            overdue_user_tasks = 0

            for user in task_data:
                user_details = user.strip().split(", ")
                total_user_tasks += 1
                if user_details[-1].lower()== "yes":
                    completed_user_tasks +=1
                elif user_details[-1].lower() == "no":
                    incomplete_user_tasks +=1
                    if datetime.strptime(user_details[3], "%d %b %Y") < datetime.today():
                            overdue_user_tasks += 1 

# Open task_overview.txt to write task-related data
            with open("user_overview.txt", "w") as user_overview_file:
                user_overview_file.write(f"Total number of tasks {total_user_tasks}\n")
                user_overview_file.write(f"Percentage of the total number of assigned tasks: {(total_user_tasks / total_tasks) * 100:.2f}%\n")
                user_overview_file.write(f"Percentage of completed tasks: {(completed_user_tasks / total_tasks) * 100:.2f}%\n")
                user_overview_file.write(f"Percentage of incomplete tasks: {(incomplete_user_tasks / total_tasks) * 100:.2f}%\n")
                user_overview_file.write(f"Percentage of overdue tasks: {(overdue_user_tasks / total_tasks) * 100:.2f}%\n")

# Function to display statistics from task overview and user overview file      
def display_stats():
            generate_reports()
            with open("task_overview.txt", "r") as task_overview_file:
                print("Task Overview:")
                for line in task_overview_file:
                    print(line.strip())

            with open("user_overview.txt", "r") as user_overview_file:
                print("\nUser-specific Task Overview:")
                for line in user_overview_file:
                    print(line.strip())       
       
# Main program
username = login()
while True:
    choice = menu()
    if choice == "r":
        if username == 'admin':
            reg_user()
        else:
            print("Only admins can register new users.")
    elif choice == "a":
        add_task()
    elif choice == "va":
        view_all()
    elif choice == "vm":
        view_mine()
    elif choice == "gr":
        if username == 'admin':
            generate_reports()
        else:
            print("Only admins can generate reports.")
    elif choice == "ds":
        if username == 'admin':
            display_stats()
        else:
            print("Only admins can display statistics.")
    elif choice == "e":
        print('Goodbye!!!')
        break