import ftplib
import sys
import os
import io

server = "54.38.52.41"
rfactor_dir = "rFactor"
source = "/rFactor/"
destination = "./download/"
interval = 0.05
ftp = ftplib.FTP(server)


def connect_to_ftp_server():
    ftp.login()

    print(ftp.dir(rfactor_dir))


def list_ftp_files(ftp_server, ftp_dir):
    dirs = []
    non_dirs = []

    stream = io.StringIO()
    sys.stdout = stream
    ftp_server.dir(ftp_dir)
    streamed_result = stream.getvalue()

    reduced = [x for x in streamed_result.split(' ') if x != '']

    reduced = [x.split('\n')[0] for x in reduced]

    indexes = [ix + 1 for ix, x in enumerate(reduced) if x == '<DIR>']

    folders = [reduced[ix] for ix in indexes]
    if ftp_dir == rfactor_dir:
        non_folders = [x for x in ftp_server.nlst() if x not in folders]
    else:
        non_folders = [x for x in ftp_server.nlst(ftp_dir) if x not in folders]
        non_folders = [ftp_dir + '/' + x for x in non_folders]
        folders = [ftp_dir + '/' + x for x in folders]

    if not dirs:
        dirs.extend(folders)
    if not non_dirs:
        non_dirs.extend(non_folders)

    if len(folders) > 0:
        for sub_folder in sorted(folders):
            result = list_ftp_files(ftp_server, sub_folder)
            dirs.extend(result[0])
            non_dirs.extend(result[1])

    return dirs, non_dirs


def download_files():
    connect_to_ftp_server()

    folders, files = list_ftp_files(ftp, rfactor_dir)

    file_mapper = {}

    for file in files:
        r = io.BytesIO()
        ftp.retrbinary('RETR ' + file, r.write())

        file_mapper[file] = r
        r.close()

    for key, val in file_mapper.items():
        if not os.path.exists(os.path.dirname(key)):
            os.makedirs(os.path.dirname(key))

    if len(key.split('.txt')) > 1:
        f = open(key, 'w+')
        f.write(val.decode())
        f.close()
    else:
        f = open(key, 'wb+')
        f.write(val)
        f.close()


def download_btn_functionality():
    download_files()
