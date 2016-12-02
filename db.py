import sqlite3
import bcrypt


conn = sqlite3.connect("clients.db")
cursor = conn.cursor()


def create_table(tablename="user"):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS {} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL UNIQUE,
            password TEXT
        );
    """.format(tablename))


def create_user(name, password):
    cursor.execute(""" SELECT COUNT(login) FROM user WHERE login = ?; """,(name,))
    result = cursor.fetchone()
    if result[0] == 0:
        cursor.execute("""
            INSERT INTO user (login, password) VALUES(?, ?);
        """, (name, password))
        conn.commit()
        return True
    else:
        return False


def verify_user(name, password, full_verification = None):
    if full_verification == True:
        cursor.execute(""" SELECT login, password from user WHERE login = ?;""", (name,))
        for line in cursor.fetchall():
            if bcrypt.hashpw(password.encode(), line[1]) == line[1]:
                return True
                break
            return False
    else:
        cursor.execute(""" SELECT login from user WHERE login = ?;""", (name,))
        for line in cursor.fetchall():
            if line[0] == name:
                return True
                break
            return False
