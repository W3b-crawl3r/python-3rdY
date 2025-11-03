from api_service import get_location
from etl import extraction
from etl import translation
from etl import load_data
line='Oct  6 00:06:32 ns sshd[3371605]: Failed password for invalid user plex from 170.64.193.177 port 33664 ssh2'
if __name__=='__main__':
    #print(get_location('210.100.100.1'))
    print(extraction(line))
    print(translation(extraction(line)))
    load_data(translation(extraction(line)))