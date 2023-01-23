import eel
from shortcut import *
from tkinter.filedialog import askopenfilename , askdirectory
import os
import sys
from shortcut import *
import shutil
########################################################################################################
rootDir=os.path.dirname(__file__)
argv = sys.argv
cwd = os.path.dirname(os.getcwd() + '/' + argv[0])
home=os.getenv('HOME')
file = argv[0] if argv[0].startswith(home) else (os.getcwd() + '/' + argv[0]).replace('./','/').replace('//','/')
########################################################################################################
eel.init(f'{rootDir}/ui', allowed_extensions=['.js', '.html','.css'])
########################################################################################################
runners = {'python':'python' , 'enaml':'enaml-run','bash':'bash' , 'sh':'sh' , 'xonsh':'xonsh' , 'fish':'fish'}
########################################################################################################
@eel.expose
def getFilePath(filePath=home):
    filePath = askopenfilename(title='select app',initialdir=filePath)
    return filePath

@eel.expose
def getIconPath(iconPath=home):
    iconPath = askopenfilename(title='select icon',initialdir=iconPath)
    return iconPath

@eel.expose
def getInterpreterPath(interpreterPath=home):
    interpreterPath = askdirectory(title='select venv',initialdir=interpreterPath)
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
def setup():
    shutil.copy(f'{rootDir}/.pinit.svg',f'{home}/.pinit.svg')
    createMenuShortCut(name='pinit', command=f'{file} desktop', icon=f'{home}/.pinit.svg',categories='Utility')
    createDesktopShortCut(name='pinit', command=f'{file} desktop', icon=f'{home}/.pinit.svg',categories='Utility')
########################################################################################################
if __name__ == "__main__":
    if len(argv) > 1 and argv[1] == 'desktop':
        eel.start('index.html', size=(300, 650), position = (800, 200))
    else:
        setup()
        eel.start('index.html', size=(300, 650), position=(800, 200))