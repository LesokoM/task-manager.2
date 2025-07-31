# ===== Importing external modules ===========
import datetime

#  ==== Login Section ====
def login(user_data):
    print("Please login. (user or admin)")
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in user_data and user_data[username] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Try again")

# Function to read users from file
def read_users(filename):
    users = {}
    try:
        with open('user.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
    except FileNotFoundError:
        print("User file not found.")
    return users

# Register a new user
def register_user():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    password_confirmation = input("Confirm your password: ")

    # Checking passwords match and write to file
    if password == password_confirmation:
        with open('user.txt', 'a') as f:
            f.write(f"{username}, {password}\n")
        print("User registered successfully!")
    else:
        print("Passwords do not match.")

# Adding a new task 
def add_task(username):
    username = input("Enter the username of the person assigned to the task: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    created_at = datetime.date.today()
    completed = "No"

    task = [username, title, description, str(created_at), due_date, completed]
    with open('tasks.txt', 'a') as file:
        file.write(", ".join(task) + "\n")
        print("Task added successfully!")

def validate_user(username, password):
    with open('user.txt', 'r') as file:
        users = file.readline()

        # Check if user exits
        for user in users:
            name, passw, role = user.strip().split(',')
            if name == username and passw == password:
                return role # Return the role of the user
            return False
        
def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                tasks.append(line.strip().split(", "))
    except FileNotFoundError:
        print("File not found.")
    return tasks

def view_all(tasks):
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {tasks}")

# Display menu for non admin menu
def display_non_admin_menu():
    print("\nUser Menu")
    print("a - add task")
    print("va - view all my tasks")
    print("vm - view all my tasks")
    print("e - exit")

# Display menu for admin menu
def display_admin_menu():
    print("\naAdmin Menu")
    print("r - register user")    
    print("a - add task")
    print("va - view all my task")
    print("vm - view my task")
    print("vc - view completed task")
    print("del - delete tasks")
    print("ds - display statistics")
    print("e - exit")   

# Main menu interaction
def main_menu():
   while True:
    username = read_users('user.txt')
    tasks = load_tasks('tasks.txt')

    user_data = view_all(username)
    username = login(user_data)
    role = validate_user(username)

    if role == 'admin':
        while True:
            display_admin_menu()
            choice = input("Select an option")
            if choice == 'e':
                break
            # Handle admin actions here
    else: 
        while True:
            display_non_admin_menu()
            choice = input("Select an option: ")
            if choice == 'e':
                break
            # Handle user actions here

if __name__ == "__main__":
    main_menu()