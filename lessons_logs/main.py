from api_service import get_location
from etl import extraction
from etl import translation
from etl import load_data
from dao_logs import read_logs_from_db
from dashboard import plot_log_ip_na
line='Oct  6 00:06:32 ns sshd[3371605]: Failed password for invalid user plex from 170.64.193.177 port 33664 ssh2'
#line2='Oct  6 00:05:43 ns sshd[3371574]: Invalid user vbox from 170.64.193.177 port 41040'
#line3='Oct  6 00:05:48 ns sshd[3371578]: pam_unix(sshd:auth): check pass; user unknown'
if __name__=='__main__':
    print(get_location('210.100.100.1'))
    print(extraction(line))
    #print(translation(extraction(line)))
    #load_data(translation(extraction(line)))
    #read_logs_from_db()
    plot_log_ip_na()
    #with open('auth.log.5', 'r', encoding='utf-8') as f:
        #for log_line in f:
            #data = extraction(log_line)
            #translated = translation(data)
            #load_data(translated)