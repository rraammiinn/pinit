import os
import shutil
import subprocess
import sys
import importlib.metadata as md
###########################################################################################################
cwd=os.path.dirname(__file__)
home=os.getenv('HOME')

src=f'{cwd}/.pinit'
dist=f'{home}/.pinit'
###########################################################################################################
def uninstall():
    try:
        os.chdir(dist)
        subprocess.run(['venv/bin/python', 'uninstall.py'])
    finally:
        try:
            shutil.rmtree(dist)
        except:
            pass


def install():
    try:
        os.chdir(dist)
        subprocess.run(['venv/bin/python', 'upgrade.py'])
    finally:
        try:
            shutil.rmtree(dist)
        finally:
            shutil.copytree(src, dist)
            os.chdir(dist)
            subprocess.run(['python','-m','venv','venv'])
            subprocess.run(['venv/bin/python','-m','pip','install','-r','requirements.txt'])
            subprocess.run(['venv/bin/python', 'install.py'])




def upgrade():
    if '--force' in sys.argv or '-f' in sys.argv:
        subprocess.run(['pip', 'install', '--upgrade', 'pinit'])
        install()
        return
    version = md.version('pinit')
    subprocess.run(['pip','install','--upgrade','pinit'])
    if version != md.version('pinit'):
        print('updating ...')
        install()
        print('updated')
    else:
        print('pinit is up to date')

def update():
    upgrade()

def create():
    try:
        os.chdir(dist)
        subprocess.run(['venv/bin/python', 'cli.py'])
    except:
        pass

def open():
    try:
        os.chdir(dist)
        subprocess.run(['venv/bin/python', 'main.py'])
    except:
        pass

def help():
    print('commands .........................................')
    print('install')
    print('uninstall')
    print('upgrade')
    print('update')
    print('upgrade --force')
    print('update --force')
    print('open')
    print('create')
    print('..................................................')
###########################################################################################################
def main():
    if len(sys.argv) == 1:
        open()
    else:
        exec (f'{sys.argv[1]}()')
