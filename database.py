import sqlite3
import random


"""connect = sqlite3.connect('database.sqlite')
cursor = connect.cursor()
cursor.execute("insert into phrases values (1, 'Привет', 'и тебе привет)")
cursor.execute("insert into phrases values (2, 'Kaк дела?', 'Xорошо')")
cursor.execute("insert into phrases values (3, 'Kak дела?', 'Kак твои?')")
connect.commit()
connect.close()"""


def get_member(group):
    group_id = 0
    if group == 'Friends':
        group_id = 1
    elif group == 'Classmates':
        group_id = 2
    elif group == 'Programmers':
        group_id = 3
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT chat_id FROM user WHERE id_group="+str(group_id))
    result = cursor.fetchall()
    conn.close()
    for i in range(0, len(result)):
        result[i] = result[i][0]
    # print(result)
    return result


def get_groups():
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT group_name FROM groups")
    result = cursor.fetchall()
    conn.close()
    for i in range(0, len(result)):
        result[i] = result[i][0]
    return result


def init_db():
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("""
    CREATE table phrases (
        id integer primary key,
        phrase text,
        answer text
        );
    """)
    connect.close()


def insert_db(phrase, answer):
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM phrases")
    print('JJJJJJJJJJJ', cursor.arraysize)
    new_id = str(cursor.fetchall()[-1][0] + 1)
    cursor.execute("insert into phrases values ("+new_id+",'"+phrase+"','"+answer+"')")
    connect.commit()
    connect.close()


def delete_member(chat_id):
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("delete from user where chat_id="+str(chat_id))
    connect.commit()
    connect.close()


def get_db():
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM phrases")
    result = cursor.fetchall()
    connect.close()
    return result


def add_member(group, chat_id):
    group_id = 0
    if group == '{"command":"friends"}':
        group_id = 1
    elif group == '{"command":"classmates"}':
        group_id = 2
    elif group == '{"command":"programmers"}':
        group_id = 3
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM user")
    new_id = str(cursor.fetchall()[-1][0] + 1)
    print(chat_id)
    print(group)
    cursor.execute("insert into user values ("+new_id+","+str(chat_id)+","+str(group_id)+")")
    connect.commit()
    connect.close()


# insert_db("Как тебя зовут?", "А тебя как?")


'''connect = sqlite3.connect('database.sqlite')
cursor = connect.cursor()
req = "delete from phrases where id=5"
cursor.execute(req)
connect.commit()
connect.close()
print(get_db())'''

'''connect = sqlite3.connect('database.sqlite')
cursor = connect.cursor()

cursor.execute("""
CREATE table groups (
  id integer primary key autoincrement,
  group_name text
);
""")

cursor.execute("""
CREATE table user (
  id integer primary key,
  chat_id integer,
  id_group integer,
  FOREIGN KEY (id_group) REFERENCES groups (id)
);
""")

connect.close()

connect = sqlite3.connect('database.sqlite')
cursor = connect.cursor()
cursor.execute("insert into groups values (1,'Friends')")
cursor.execute("insert into groups values (2,'Classmates')")
cursor.execute("insert into groups values (3,'Programmers')")
connect.commit()
connect.close()
print(get_db())'''