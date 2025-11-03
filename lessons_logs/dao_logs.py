from mysql.connector import connect, Error
from typing import List, Tuple

def read_logs_from_db() -> List[str]:
    logs = []
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="",
            database="logs_db"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT log_message FROM logs")
        rows = cursor.fetchall()
        if rows is not None:
            for row in rows:
                logs.append(row[0])
    except Error as e:
        print(f"Error reading logs from database: {e}")
    finally:
        if connection:
            connection.close()
    return logs