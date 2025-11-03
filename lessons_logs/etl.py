import re
from datetime import datetime, timedelta, timezone


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
    tz = timezone(timedelta(hours=1))  # +01:00 timezone

    for entry in data:
        date_str, user, ip, status = entry

        # Parse the syslog-style date (e.g. "Oct 26 10:30:12")
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
