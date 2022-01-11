import datetime
from threading import Thread
import os
import time
import sys


def updateFile(_file):
    print("update file " + _file + "\n")
    time_now = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
    text_file = open(_file, "w+")
    text_file.write("current time: %s\n" % time_now)
    text_file.close()


def updateDirectory(_dir):
    print("update all file in " + _dir + "\n")
    for _curFD in os.listdir(_dir):
        f = os.path.join(_dir, _curFD)
        if os.path.isfile(f):
            updateFile(f)
        else:
            updateDirectory(f)


def writeThrd():
    _dir = sys.argv[1]
    while 1:
        time.sleep(1)
        try:
            print("update all file in " + _dir)
            if(os.path.isfile(_dir)):
                updateFile(_dir)
            elif (os.path.isdir(_dir)):
                updateDirectory(_dir)
        except Exception as e:
            # print("Something else went wrong." + e.)
            print(getattr(e, 'message', repr(e)))


if __name__ == '__main__':
    cnt = 0
    while cnt < 10:
        print(cnt)
        cnt += 1
        t = Thread(target=writeThrd)
        t.daemon = True
        t.start()

t.join()
