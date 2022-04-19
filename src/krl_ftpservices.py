import ftplib
import os

server = "54.38.52.41"
rfactor_dir = "/rFactor/"
ftp = ftplib.FTP(server)
list_of_files = []
list_of_folders = []


def connect_to_ftp_server():
    ftp.login()
    print("Logged in FTP server: " + server)


def download_files():
    ftp_link = "ftp://" + server + rfactor_dir
    os.system('wget -r -np -nH ' + ftp_link + ' -P ./download/')


def download_btn_functionality():
    download_files()
