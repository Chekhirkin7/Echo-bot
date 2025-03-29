def insert_user(conn, id, username):
    cursor = conn.cursor()
    query = "INSERT INTO users (id, username) VALUES  (%s, %s)"
    cursor.execute(query, (id, username))
    conn.commit()
    cursor.close()


def user_exists(conn, id):
    cursor = conn.cursor()
    query = "SELECT id FROM users WHERE id = %s"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def insert_message(conn, user_id, message_text):
    cursor = conn.cursor()
    query = "INSERT INTO messages (user_id, message_text) VALUES (%s, %s)"
    cursor.execute(query, (user_id, message_text))
    conn.commit()
    cursor.close()


def insert_email(conn, id, email):
    cursor = conn.cursor()
    query = """
    INSERT INTO users (id, email)
    VALUES (%s, %s)
    ON CONFLICT(id)
    DO UPDATE SET email = %s
    """
    cursor.execute(query, (id, email, email))
    conn.commit()
    cursor.close()


def insert_phone(conn, id, phone):
    cursor = conn.cursor()
    query = """
    INSERT INTO users (id, phone)
    VALUES (%s, %s)
    ON CONFLICT(id)
    DO UPDATE SET phone = %s
    """
    cursor.execute(query, (id, phone, phone))
    conn.commit()
    cursor.close()
