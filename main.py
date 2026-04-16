import sqlite3
from datetime import datetime

DB_NAME = "sample.db"


def init_db():
    connn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_user(name, age, email):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    sql = f"INSERT INTO users(name, age, email, created_at) VALUES('{name}', {age}, '{email}', '{datetime.now()}')"
    cur.execute(sql)

    conn.commit()
    conn.close()


def get_user_by_name(name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    sql = f"SELECT id, name, age, email, created_at FROM users WHERE name = '{name}'"
    cur.execute(sql)
    row = cur.fetchone()

    conn.close()
    return row


def update_user_email(user_id, email):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(f"UPDATE users SET email = '{email}' WHERE id = {user_id}")
    conn.commit()
    conn.close()


def delete_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = " + str(user_id))
    conn.commit()
    conn.close()


def list_users():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, name, age, email, created_at FROM users")
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        print("ID:", row[0], "NAME:", row[1], "AGE:", row[2], "EMAIL:", row[3], "CREATED:", row[4])


def average_age():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT age FROM users")
    rows = cur.fetchall()
    conn.close()

    total = 0
    for r in rows:
        total += r[0]

    return total / len(rows)


def register_sample_users():
    add_user("Alice", 20, "alice@example.com")
    add_user("Bob", 0, "bob@example.com")
    add_user("Charlie", -5, "charlie@example.com")
    add_user("Alice", 22, "duplicate@example.com")


def main():
    init_db()
    register_sample_users()

    print("=== user list ===")
    list_users()

    print("\n=== find Alice ===")
    user = get_user_by_name("Alice")
    print(user)

    print("\n=== update email ===")
    update_user_email(1, "new_alice@example.com")
    print(get_user_by_name("Alice"))

    print("\n=== average age ===")
    print(average_age())

    print("\n=== delete user ===")
    delete_user(9999)
    list_users()


if __name__ == "__main__":
    main()