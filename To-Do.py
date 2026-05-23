print("=== To-Do App ===")

def Add_task():
    try:
        task = input("Enter you task:")
        with open("To-Do_app.txt", "a") as f:
            f.write(f"Task = {task}\n")
    
        print("Task added successfully!")

    except:
        print("Please correctly Enter your task")
    
def View_task():
    print("Here is your task!")

    with open("To-Do_app.txt", "r") as f:
        print(f.read())


def Delete_task():
    with open("To-Do_app.txt", "w") as f:
        f.write("")

    print("Your task successfully Delete!")

def Mark_task_as_completed():

    with open("To-Do_app.txt", "r") as file:
        lines = file.readlines()

    task = input("Enter task name to mark complete: ")

    updated_lines = []

    for line in lines:

        # Match task
        if task.lower() in line.lower():

            # Add tick only once
            if "Done" not in line:
                line = line.strip() + " [Done]\n"
# There may be extra \n (newline characters) or spaces at the end of a line in a file.
# The .strip() function removes those extra spaces and newline characters from the beginning 
# and end of the string.

        # Save every line
        updated_lines.append(line)

    # Rewrite complete file
    with open("To-Do_app.txt", "w") as file:
        file.writelines(updated_lines)

    print("Task marked as completed!")

while(True):
    print("Enter (1) for Add task")
    print("Enter (2) for View task")
    print("Enter (3) for Delete task")
    print("Enter (4) for mark task as completed")
    print("Enter (5) for exit")

    option = int(input("Enter your opttion:"))
    if option == 1:
        Add_task()
    elif option == 2:
        View_task()
    elif option == 3:
        Delete_task()
    elif option == 4:
        Mark_task_as_completed()
    elif option == 5:
        print("Good bye!")
        break
    
    else:
        print("invalid option")