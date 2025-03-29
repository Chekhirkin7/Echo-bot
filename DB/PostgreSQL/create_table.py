import logging
from psycopg2 import DatabaseError

from connect import create_connection

def create_table(conn, sql_expressions: str):
	c = conn.cursor()
	try:
		c.execute(sql_expressions)
		conn.commit()
	except DatabaseError as err:
		logging.error(err)
		conn.rollback()
	finally:
		c.close()

if __name__ == '__main__':
	sql_delete_table_users = """
	DROP TABLE IF EXISTS users CASCADE;
	"""

	sql_delete_table_messages = """
	DROP TABLE IF EXISTS messages CASCADE;
	"""

	sql_create_table_users = """
	CREATE TABLE IF NOT EXISTS users (
	id BIGINT PRIMARY KEY,
	username VARCHAR(120),
	email VARCHAR(120),
	phone VARCHAR(20),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);
	"""
	
	sql_create_table_messages = """
	CREATE TABLE IF NOT EXISTS messages (
	id SERIAL PRIMARY KEY,
	user_id BIGINT,
	message_text VARCHAR,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY(user_id) REFERENCES users(id)
	);
	"""

	try:
		with create_connection() as conn:
			if conn is not None:
				create_table(conn, sql_delete_table_users)
				create_table(conn, sql_delete_table_messages)
				create_table(conn, sql_create_table_users)
				create_table(conn, sql_create_table_messages)
			else:
				print("Error! Cannot create the database connection.")
	except Exception as err:
		logging.error(err)