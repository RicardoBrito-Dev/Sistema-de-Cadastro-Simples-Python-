import sqlite3

def get_connection():
    """Establishes and returns a connection to the database."""
    return sqlite3.connect('app_data.db')

def initialize_db():
    """Creates the users table if it does not exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_user(name, email, age):
    """Adds a new user to the database."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', (name, email, age))
        conn.commit()
        print(f"User '{name}' added successfully!")
    except sqlite3.IntegrityError:
        print(f"Error: A user with email '{email}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def get_users():
    """Returns a list of all users."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(user_id, name, email, age):
    """Updates a user's information."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users
        SET name = ?, email = ?, age = ?
        WHERE id = ?
    ''', (name, email, age, user_id))
    
    if cursor.rowcount > 0:
        print(f"User ID {user_id} updated successfully!")
    else:
        print(f"User ID {user_id} not found.")
        
    conn.commit()
    conn.close()

def delete_user(user_id):
    """Deletes a user by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    
    if cursor.rowcount > 0:
        print(f"User ID {user_id} deleted successfully!")
    else:
        print(f"User ID {user_id} not found.")
        
    conn.commit()
    conn.close()
