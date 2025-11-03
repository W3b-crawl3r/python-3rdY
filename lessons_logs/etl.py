from multiprocessing import connection
import re
from datetime import datetime, timedelta, timezone
from mysql.connector import connect, Error


def extraction(line:str)->list[tuple[str,...]]:
    data=[]
    pattern_failed=r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+.+Failed password for invalid user\s+(\w+)\s+from\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    patten_invalid=r''
    match=re.search(pattern_failed,line)
    if match :
        date=match.group(1)
        user=match.group(2)
        
        ip=match.group(3)
        data.append((date,user,ip,'failed'))
    return data

def translation(data: list[tuple[str, ...]]) -> list[str]:
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
        formatted_line = f"{iso_date} level={level} service={service} user={user} ip={ip}"
        translated_lines.append(formatted_line)
    return translated_lines

def load_data(translated_lines: list[str]) -> None:
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
            log_line TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)

        for line in translated_lines:
            cursor.execute("INSERT INTO logs (log_line) VALUES (%s)", (line,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
