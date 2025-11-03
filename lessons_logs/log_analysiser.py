import re


try:
    with open('app.log', 'r') as file:
        for line in file:
            # Process each line here
            processed_line = line.strip()
            pattern = r'(\S+)\s+level=(\S+)\s+service=(\S+)\s+user=(\S+)\s+ip=(\S+)'
            match = re.match(pattern, processed_line)
            if match:
                timestamp = match.group(1)
                level = match.group(2)
                service = match.group(3)
                user = match.group(4)
                ip = match.group(5)
                print(f"Timestamp: {timestamp}, Level: {level}, Service: {service}, User: {user}, IP: {ip}")
except FileNotFoundError:
    print("Log file not found!")
except IOError:
    print("Error reading the file!")