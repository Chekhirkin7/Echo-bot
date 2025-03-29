def insert_user(conn, id, username):
    """Insert a new user into the users table"""
    cursor = conn.cursor()
    query = "INSERT INTO users (id, username) VALUES (?, ?)"
    cursor.execute(query, (id, username))
    conn.commit()
    cursor.close()


def user_exists(conn, id):
    """Check if the user already exists in the users table"""
    cursor = conn.cursor()
    query = "SELECT id FROM users WHERE id = ?"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def insert_message(conn, user_id, message_text):
    """Insert a new message into the messages table"""
    cursor = conn.cursor()
    query = "INSERT INTO messages (user_id, message_text) VALUES (?, ?)"
    cursor.execute(query, (user_id, message_text))
    conn.commit()
    cursor.close()


# def insert_email(conn, email, user_id):
#     """Insert a email into the users table"""
#     cursor = conn.cursor()
#     query = "SELECT email FROM users WHERE id = ?"
#     cursor.execute(query, (user_id,))
#     result = cursor.fetchone()

#     if result is None:
#         query = "UPDATE users SET email = ? WHERE id = ?"
#         cursor.execute(query, (email, user_id))
#         conn.commit()
#     cursor.close()


def insert_email(conn, email, user_id):
    """Insert or update an email in the users table"""
    cursor = conn.cursor()

    # Використовуємо `INSERT OR REPLACE` або `INSERT ON CONFLICT`
    query = """
    INSERT INTO users (id, email) 
    VALUES (?, ?)
    ON CONFLICT(id) 
    DO UPDATE SET email = ?
    """

    cursor.execute(query, (user_id, email, email))
    conn.commit()
    cursor.close()


# def insert_phone(conn, phone, user_id):
#     """Insert a phone into the users table"""
#     cursor = conn.cursor()
#     query = "SELECT phone FROM users WHERE id = ?"
#     cursor.execute(query, (user_id,))
#     result = cursor.fetchone()

#     if result is None:
#         query = "UPDATE users SET phone = ? WHERE id = ?"
#         cursor.execute(query, (phone, user_id))
#         conn.commit()
#     cursor.close()


def insert_phone(conn, phone, user_id):
    """Insert or update a phone in the users table"""
    cursor = conn.cursor()

    query = """
    INSERT INTO users (id, phone) 
    VALUES (?, ?)
    ON CONFLICT(id) 
    DO UPDATE SET phone = ?
    """

    cursor.execute(query, (user_id, phone, phone))
    conn.commit()
    cursor.close()
