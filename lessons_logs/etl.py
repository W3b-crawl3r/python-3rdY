from multiprocessing import connection
import re
from datetime import datetime, timedelta, timezone
from mysql.connector import connect, Error


def extraction(line:str)->list[tuple[str,...]]:
    data=[]
    pattern_failed=r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+.+Failed password for invalid user\s+(\w+)\s+from\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    pattern_invalid=r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+.+Invalid user\s+(\w+)\s+from\s+(\d{1,3}(?:\.\d{1,3}){3})'
    pattern_unknown =r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+.+pam_unix\(sshd:auth\): check pass; user unknown'
    match_failed = re.search(pattern_failed, line)
    match_unknown = re.search(pattern_unknown, line)
    match_invalid = re.search(pattern_invalid, line)

    if match_failed:
        date = match_failed.group(1)
        user = match_failed.group(2)
        ip = match_failed.group(3)
        data.append((date, user, ip, 'failed_password'))
    elif match_invalid:
        date = match_invalid.group(1)
        user = match_invalid.group(2)
        ip = match_invalid.group(3)
        data.append((date, user, ip, 'invalid_user'))
    elif match_unknown:
        date = match_unknown.group(1)
        data.append((date, 'unknown', 'N/A', 'user_unknown'))
    return data

def translation(data: list[tuple[str, ...]]) -> list[tuple[str, str, str, str]]:
    translated_lines = []
    current_year = datetime.now().year
    tz = timezone(timedelta(hours=1))
    for entry in data:
        date_str, user, ip, status = entry
        try:
            date_obj = datetime.strptime(f"{current_year} {date_str}", "%Y %b %d %H:%M:%S")
            date_obj = date_obj.replace(tzinfo=tz)
            iso_date = date_obj.isoformat()
        except ValueError:
            iso_date = f"{current_year}-01-01T00:00:00+01:00"  # fallback
        level = "INFO" if status == "successful" else "WARNING"
        service = "auth"
        translated_lines.append((iso_date, user, ip, status))
    return translated_lines

def load_data(translated_lines: list[tuple[str, str, str, str]]) -> None:
    """
    Stores parsed SSH log data into MySQL in separate columns:
    (date, user, ip, status)
    """
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="",
            database="logs_db"
        )
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            log_date VARCHAR(50),
            username VARCHAR(100),
            ip_address VARCHAR(45),
            status VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        insert_query = """
        INSERT INTO logs (log_date, username, ip_address, status)
        VALUES (%s, %s, %s, %s)
        """
        cursor.executemany(insert_query, translated_lines)
        connection.commit()
        print(f"{cursor.rowcount} rows inserted successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
