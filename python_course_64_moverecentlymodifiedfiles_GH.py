#   Jeff W. Ferrell 10/10/17
#   Python Course, item 64
#   Moving recently updated (within 24 hours).txt files from one folder to another
#   Made with Python 2.7 using datetime, shutil, and os modules

import datetime as dt
import shutil
import os

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)

source ='\Text_Files'
folder = os.listdir(source)
destination = '\Send_Home'


def MoveRecentlyModified():
    for files in folder:
        path = os.path.join(source, files)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            recents = ('%s modified %s'%(path, mtime))
            if files.endswith('.txt'):
                print files
                shutil.move(os.path.join(source, files), os.path.join(destination))
            
            

MoveRecentlyModified()
