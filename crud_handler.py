import sqlite3 as sql
from db_handler import connect_db

def create_user(user):
    data_user = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO siswa(name, phone, city)
            VALUES (?, ?, ?)''', (user['name'], user['phone'], user['city']))
        conn.commit()
        data_user = get_user_by_id(cur.lastrowid)
    except:
        conn.rollback()
        
    finally:
        conn.close()
    
    return data_user

def get_all_user():
    users = []
    try:
        conn = connect_db()
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM siswa")

        rows = cur.fetchall()
        for i in rows:
            user = {}
            user["user_id"] = i["user_id"]
            user["name"] = i["name"]
            user["phone"] = i["phone"]
            user["city"] = i["city"]
            users.append(user)
    except:
        users = []

    return users

def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_db()
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM siswa WHERE user_id=?", (user_id))
        row = cur.fetchone()

        user["user_id"] = row["user_id"]
        user["name"] = row["name"]
        user["phone"] = row["phone"]
        user["city"] = row["city"]

    except:
        user = {}
    
    return user

def edit_user(user):
    data_user = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('''
            UPDATE siswa SET name=?, phone=?, city=? WHERE user_id=?''',
            (user['name'], user['phone'], user['city'], user['user_id']))
        conn.commit()
        data_user = get_user_by_id(user['user_id'])
    except:
        conn.rollback()
        data_user = {}
    finally:
        conn.close()

    return data_user

def delete_user(user_id):
    try:
        conn = connect_db()
        conn.execute("DELETE FROM siswa WHERE user_id=?", (user_id))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

