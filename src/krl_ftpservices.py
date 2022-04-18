import ftplib
import sys
import os
import io
from datetime import datetime

import wget as wget

server = "54.38.52.41"
rfactor_dir = ""
ftp = ftplib.FTP(server)
list_of_files = []
list_of_folders = []


def connect_to_ftp_server():
    ftp.login()

    # files = ftp.nlst(rfactor_dir)
    # print(files)
    # files1 = ftp.nlst(rfactor_dir + "/" + files[0])
    # print(files1)
    # files2 = ftp.nlst(files1[2])
    # print(files2)
    # files3 = ftp.nlst(files2[1])
    # print(files3)
    ftp_dir = ""
    files = ftp.nlst(ftp_dir)
    temp_path = ftp_dir + "/" + files[0]
    temp_list = create_list_of_files(temp_path)
    print("Files: " + str(temp_list[0]))
    print("Folders: " + str(temp_list[1]))


def create_list_of_files(path):
    files = ftp.nlst(path)
    for file in files:
        if file[-4] == ".":
            list_of_files.append(file)
        else:
            list_of_folders.append(file)
            create_list_of_files(file)

    return list_of_files, list_of_folders


def download_files():
    for file in list_of_files:
        ftp_link = "ftp://" + server + file
        # print(ftp_link)
        wget.download(ftp_link)


def download_btn_functionality():
    download_files()
