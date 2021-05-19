import json


def show_menu():
    print('1. Add task')
    print('2. Remove task')
    print('3. View tasks')
    print('4. Exit program')


try:
    with open('tasks.json', 'x+') as f:
        tasks = []
except FileExistsError:
    with open('tasks.json') as f:
        try:
            tasks = json.load(f)
        except json.decoder.JSONDecodeError:
            tasks = []


while True:
    show_menu()
    input_ = input('Enter an option from above menu to perform an action: ')

    if input_ == '1':
        task = input('Enter your task to add into the tasks list: ')
        tasks.append(task)
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f)
        print(f'"{task}" added successfully to the tasks list.')

    elif input_ == '2':
        task = input('Enter your task to remove from the tasks list: ')
        if task in tasks:
            tasks.remove(task)
            with open('tasks.json', 'w') as f:
                json.dump(tasks, f)
            print(f'"{task}" removed successfully from the tasks list.')
        else:
            print(f'"{task}" does not exist in the tasks list.')

    elif input_ == '3':
        print(tasks)

    elif input_ == '4':
        break

    else:
        print('Invalid option, try again!')

    print()
