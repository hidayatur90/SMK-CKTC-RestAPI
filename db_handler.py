import sqlite3 as sql

def connect_db():
    conn = sql.connect("db_smk_cinta.db")
    return conn


def create_db():
    try:
        conn = connect_db()
        conn.execute('''
            CREATE TABLE siswa(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                city TEXT NOT NULL
            );
        ''')
        conn.commit()
        print("Table siswa berhasil dibuat")
    except:
        print("Ada error, table siswa sudah ada")
    finally:
        conn.close()

create_db()

