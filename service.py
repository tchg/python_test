import socket
import threading
import time
import sys
import os
import struct

def socket_service()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 6666))
        s.listen(10)
    except socket.error as msg:
        print msg
        sys.exit(1)
    print 'Waiting connection....'

    while 1:
        fileinfo_size = struct.calcsize('128s1')
        buf = conn.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128s1', buf)
            fn = filename.strip('\00')
            new_filename = os.path.join('./', 'new_' + fn)
            print 'file new name is {0}，filesizeif{1}'.format(new_filename, fileinfo_size)
            