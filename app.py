 #Building a to do list
task = []


def addTask():
    task = input("Enter Task : " )
    task.append(task)
    print(f"Task '{task}' added to the list .")


def listTasks():
    if not task:
        print("There are no tasks currently. ")
    else:
        print("Current Tasks : ")
        for index , task in enumerate(task):
            print(f"Task # {index} . {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the #  to delete : " ))
        if taskToDelete >= 0 and taskToDelete < len(task):

            task.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed. ")

        else:
            print(f"Tasks #{taskToDelete} was not found ")
    except:
        print("Invalid Input . ")

if __name__  == "__main__":
    
    print("Welcome to the to do list app :)")
    while True :
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task ")
        print("2.  Delete a task")
        print("3.  List tasks")
        print("4. Quit ")


        choice =  input("Enter your choice :")

        if (choice == "1"):
           addTask()

        elif(choice == "2"):
            deleteTask()
   
        elif(choice == "3"):
            listTasks()

        elif(choice == "4"):
            quit

        else:
            print("Invalid Input . Please try again")

        print("Goodbye ")