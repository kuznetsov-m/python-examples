# https://python-scripts.com/sqlite
# https://stackoverflow.com/questions/13880786/python-sqlite3-string-variable-in-execute

import sqlite3

table_name = 'Songs'

# Подключение к БД
conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Проверить наличие таблицы с транзакциями
# https://stackoverflow.com/questions/1601151/how-do-i-check-in-sqlite-whether-a-table-exists
sql = """SELECT name FROM sqlite_master WHERE type='table' AND name=?;"""
cursor.execute(sql, [(table_name)])

# Если таблица отсутствует, то создать новую 
if not cursor.fetchall():
    # Создание таблицы
    try:
        sql = """CREATE TABLE %s
            (title text, artist text, release_date text,
            publisher text, media_type text)
            """ % (table_name)
        cursor.execute(sql)
    except Exception as e:
        print('Error: ' + str(e))

try:
    sql = 'INSERT INTO %s VALUES (?, ?, ?, ?, ?);' % (table_name)
    cursor.execute(sql, ['Top Song', 'Famouse artist', '27/02/2020', "undeground label 1'23", 'x-type'])
    conn.commit()
    conn.close()
except Exception as e:
    print('Error: ' + str(e))