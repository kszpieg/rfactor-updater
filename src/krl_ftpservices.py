import ftplib
import os
from dateutil import parser
from datetime import datetime

server = "54.38.52.41"
logfile = "krl_update.log"
ftp = ftplib.FTP(server)


def connect_to_ftp_server():
    ftp.login()
    print("Logged in FTP server: " + server)


def check_updates():
    updates = {}
    files = []
    ftp.dir("", files.append)
    print(files)
    for file in files:
        tokens = file.split(maxsplit=4)
        time_str = tokens[0] + " " + tokens[1]
        time = parser.parse(time_str)
        updates[tokens[3]] = datetime.strftime(time, "%Y-%m-%d %H:%M")

    ordered_updates = (sorted(updates.items(), key=lambda t: t[1], reverse=False))
    return ordered_updates


def download_files(update_dir):
    ftp_link = "ftp://" + server + '/' + update_dir
    os.system('wget -r -np -nH --cut-dirs=1 ' + ftp_link + ' -P ./download/' + ' -o ' + logfile)
    with open(logfile, "r+") as file:
        new_file = file.readlines()
        file.seek(0)
        for line in new_file:
            if "anonymous" not in line:
                file.write(line)
        file.truncate()
