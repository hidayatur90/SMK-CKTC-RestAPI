# Import Library
import sqlite3 as sql
from db_handler import connect_db

# Fungsi untuk create User/employee baru
def create_user(user):
    data_user = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO employees(name, phone, city)
            VALUES (?, ?, ?)''', (user['name'], user['phone'], user['city']))
        conn.commit()
        data_user = get_user_by_id(cur.lastrowid)
    except:
        conn.rollback()
        
    finally:
        conn.close()
    
    return data_user

# Fungsi untuk menampilkan semua employee
def get_all_user():
    users = []
    try:
        conn = connect_db()
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")

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

# Fungsi untuk menampilkan salah satu employee berdasarkan id nya
def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_db()
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees WHERE user_id=?", (user_id))
        row = cur.fetchone()

        user["user_id"] = row["user_id"]
        user["name"] = row["name"]
        user["phone"] = row["phone"]
        user["city"] = row["city"]

    except:
        user = {}
    
    return user

# Fungsi untuk melakukan edit pada data employee
def edit_user(user):
    data_user = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('''
            UPDATE employees SET name=?, phone=?, city=? WHERE user_id=?''',
            (user['name'], user['phone'], user['city'], user['user_id']))
        conn.commit()
        data_user = get_user_by_id(user['user_id'])
    except:
        conn.rollback()
        data_user = {}
    finally:
        conn.close()

    return data_user

# Fungsi untuk menghapus data employee
def delete_user(user_id):
    try:
        conn = connect_db()
        conn.execute("DELETE FROM employees WHERE user_id=?", (user_id))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

