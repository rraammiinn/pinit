import eel
from shortcut import *
# from tkinter.filedialog import askopenfilename , askdirectory
from crossfiledialog import open_file, choose_folder
import os
import sys
import time
import shutil
########################################################################################################
cwd=os.path.dirname(__file__)
home=os.getenv('HOME')
########################################################################################################
eel.init(f'{cwd}/ui', allowed_extensions=['.html'])
########################################################################################################
runners = {'python':'python' , 'enaml':'enaml-run','bash':'bash' , 'sh':'sh' , 'xonsh':'xonsh' , 'fish':'fish'}
########################################################################################################
@eel.expose
def getFilePath(filePath=home):
    # filePath = askopenfilename(title='select app',initialdir=filePath)
    filePath = open_file(title='select app')
    return filePath

@eel.expose
def getIconPath(iconPath=home):
    # iconPath = askopenfilename(title='select icon',initialdir=iconPath)
    iconPath = open_file(title='select icon')
    return iconPath

@eel.expose
def getInterpreterPath(interpreterPath=home):
    # interpreterPath = askdirectory(title='select venv',initialdir=interpreterPath)
    interpreterPath = choose_folder(title='select venv')
    return interpreterPath

@eel.expose
def make(name,filePath,iconPath,interpreterPath,cmd,ccmd,typ,runner,is_terminal,categories,places,argv):
    runners['python'] = interpreterPath.removesuffix('/bin')+'/bin/python' if interpreterPath.strip() else 'python'
    command = ccmd if ccmd.strip() else runners[runner]
    command = ccmd if typ == 'binary' else command
    command += ' ' + filePath + ' ' + argv
    command = command.replace('./','/').replace('//','/').strip()

    if 'menu' in places:
        createMenuShortCut(name=name,command=command,icon=iconPath,terminal=is_terminal,categories=categories)
    if 'desktop' in places:
        createDesktopShortCut(name=name,command=command,icon=iconPath,terminal=is_terminal,categories=categories)
########################################################################################################
def init():
    name = 'pinit'+int(time.time())
    command= (os.getcwd()+'/pinit'+' --desktop').replace('//', '/').replace('./','/')
    icon=(home+'/'+'.pinit.svg').replace('//', '/')
    try:
        shutil.copy('.pinit.svg', (home+'/.pinit.svg').replace('//', '/'))
    finally:
        for i in os.listdir(menuPath):
            if 'pinit' in i:
                os.remove(i)
            createMenuShortCut(name, command, icon,title='pinit')

        for i in os.listdir(desktopPath):
            if 'pinit' in i:
                os.remove(i)
            createDesktopShortCut(name, command, icon,title='pinit')
########################################################################################################

if __name__ == "__main__":
    if '--desktop' in sys.argv:
        eel.start('index.html' , size = (300, 650), position = (800, 200))
    else:
        try:
            init()
        finally:
            eel.start('index.html' , size = (300, 650), position = (800, 200))
