from mysql.connector import connect, Error
from typing import List
from api_service import get_location
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
        cursor.execute("SELECT log_date, username, ip_address, status FROM logs")
        rows = cursor.fetchall()
        if rows:
            with open("auth.log", "w", encoding="utf-8") as file:
                for (date, user, ip, status) in rows:
                    level = "INFO" if status == "successful" else "WARNING"
                    service = "auth"
                    try:
                        location_data = get_location(ip)
                        country = location_data.get("country", "Unknown")
                    except Exception:
                        country = "Unknown"
                    line = f"{date} level={level} service={service} user={user} ip={ip} country={country}"
                    file.write(line + "\n")
                    logs.append(line)
    except Error as e:
        print(f"Error reading logs from database: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return logs