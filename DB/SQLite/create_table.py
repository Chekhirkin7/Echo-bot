import logging
from sqlite3 import DatabaseError

from connect import create_connection


def create_table(conn, sql_expression: str):
    """create a table from the create_table_sql statement
    :param sql_expression:
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as err:
        logging.error(err)
        conn.rollback()
    finally:
        c.close()


if __name__ == "__main__":

    sql_delete_users = "DROP TABLE IF EXISTS users;"
    sql_delete_messages = "DROP TABLE IF EXISTS messages;"

    sql_create_table_users = """
	CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY,
	username VARCHAR (120),
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP
	);
	"""

    sql_create_table_messages = """
	CREATE TABLE IF NOT EXISTS messages (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_id INTEGER,
	message_text VARCHAR,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY(user_id) REFERENCES users(id)
	);
	"""

    # sql_add_column_phone = """
    # ALTER TABLE users ADD COLUMN phone VARCHAR(20);
    # """

    # sql_add_column_email = """
    # ALTER TABLE users ADD COLUMN email VARCHAR(120);
    # """

    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, sql_delete_users)
                create_table(conn, sql_delete_messages)
                create_table(conn, sql_create_table_users)
                create_table(conn, sql_create_table_messages)
                # create_table(conn, sql_add_column_email)
                # create_table(conn, sql_add_column_phone)
            else:
                print("Error! Cannot creat the database connection.")
    except Exception as err:
        logging.error(err)
