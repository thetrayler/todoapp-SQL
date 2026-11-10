import sqlite3

# Подключаемся к базе данных
connection = sqlite3.connect("to-do-app.db")

# Получаем курсор для выполнения запросов
cursor = connection.cursor()

# # Добавляем 3 задачи
# cursor.execute(
#     "INSERT INTO tasks (id, name, is_done) VALUES (?, ?, ?)",
#     (1, "My task 1", False))
# cursor.execute(
#     "INSERT INTO tasks (id, name, is_done) VALUES (?, ?, ?)",
#     (2, "My task 2", False))
# cursor.execute(
#     "INSERT INTO tasks (id, name, is_done) VALUES (?, ?, ?)",
#     (3, "My task 3", False))

# # Сохраняем изменения
# connection.commit()

# # Помечаем задачу выполненой
# cursor.execute("UPDATE tasks SET is_done = ? WHERE id = ?", (True, 1))

# # Сохраняем изменения
# connection.commit()

# # Удаляем задачу с идентификатором 2
# cursor.execute("DELETE FROM tasks WHERE id = ?", (2,))

# # Сохраняем изменения
# connection.commit()

# # Читаем список задач из базы
# cursor.execute("SELECT * FROM tasks")
# rows = cursor.fetchall()

# # Каждая запись представлена в виде кортежа.
# # Например, (1, 'My task', 0).
# for row in rows:
#     print(row)

# # Отключаемся от базы данных
# connection.close()

def addtask():
    name = input('Введите название задачи: ')
    cursor.execute(
        "INSERT INTO tasks (name, is_done) VALUES (?, ?)",
        (name, False))
    connection.commit()
    print(f'Задача "{name}" успешно добавлена!')


def command(name):
    match name:
        case 'addtask': addtask()
        case _: print('Такой команды не существует')


while True:
    command(input('Напишите команду: '))