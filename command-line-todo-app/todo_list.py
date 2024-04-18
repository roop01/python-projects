import argparse
import os

#Set up Argument Parser
def cmd_parser():
    parser = argparse.ArgumentParser(description="To Do List App")
    parser.add_argument("-a", "--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by index")
    return parser

#Add task to todo list
def add_tasks(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

#List tasks
def list_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    else: 
        print("No Task Found")

#Remove Task
def remove_task(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            with open("tasks.txt", "w") as file:
                 for i, task in enumerate(tasks, start=1):
                     if i != index:
                         file.write(task)
            print('Tasks Updated Successfully')
    else:
        print("No Tasks Found")

#Parse Command Line Arguments
def main():
    parser = cmd_parser()
    args = parser.parse_args()
    if args.add:
        add_tasks(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()




