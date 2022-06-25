HELP = """
Добро пожаловать в тестовую версию программы todo!
help - напечатать справку по программе
add - добавить задачу в список
show - напечатать все добавленные задачи
exit - выход из программы."""

print(HELP)
tasks = {}

def add(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача", "'", task, "'", "добавлена на", date)

run = True
while run:
    command = input("Введите вашу команду: ").lower().lstrip().rstrip()

    if command == "help":
        print(HELP)

    elif command == 'show':
        for date in tasks:
            print('>', date, ':')
            for task in tasks[date]:
                print('\t-', task)

    elif command == "add":
        task = input("Введите название задачи :").lower().lstrip().rstrip()
        date = input("Введите дату для задачи :").lstrip().rstrip()
        add(date, task)

    elif command == 'exit':
        print("Завершение работы программы. \nДо свидания!")
        break

    else:
        print("Неизвестная команда!")