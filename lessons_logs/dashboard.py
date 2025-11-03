import matplotlib.pyplot as plt
from mysql.connector import connect, Error

def plot_log_ip_na():
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="",
            database="logs_db"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT log_date, COUNT(*) FROM logs WHERE ip_address = 'N/A' GROUP BY log_date")
        rows = cursor.fetchall()
        if rows is None:
            rows = []
        dates = [row[0] for row in rows]
        counts = [row[1] for row in rows]
        plt.bar(dates, counts)
        plt.xlabel("Date")
        plt.ylabel("Count")
        plt.title("Log Entries with 'N/A' IP Addresses")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Error as e:
        print(f"Error plotting log IP N/A: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
