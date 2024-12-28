import sqlite3

# Создаем и подключаемся к базе данных SQLite
def create_database():
    conn = sqlite3.connect('weather.db')  # База данных будет создана в текущей папке
    cursor = conn.cursor()

    # Создаем таблицу для хранения данных о погоде
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        datetime TEXT,
        temperature REAL
    )''')

    conn.commit()  # Подтверждаем изменения
    conn.close()   # Закрываем соединение

# Вызовем функцию для создания базы данных
create_database()
