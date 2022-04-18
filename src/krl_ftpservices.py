import ftplib
import sys
import os
import io
from datetime import datetime

import wget as wget

server = "54.38.52.41"
rfactor_dir = ""
ftp = ftplib.FTP(server)


def connect_to_ftp_server():
    ftp.login()

    files = ftp.nlst(rfactor_dir)
    print(files[0])
    files1 = ftp.nlst(rfactor_dir + "/" + files[0])
    print(files1)
    files2 = ftp.nlst(rfactor_dir + files1[2])
    print(files2)
    files3 = ftp.nlst(files2[1])
    print(files3)


def download_files():
    ftp_link = "ftp://" + server + "/" + rfactor_dir
    wget.download(ftp_link)


def download_btn_functionality():
    download_files()
