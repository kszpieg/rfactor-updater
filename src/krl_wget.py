import struct

def check_os_version():
    version = struct.calcsize("P") * 8
    return version