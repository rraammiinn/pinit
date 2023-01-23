from shortcut import *
import os
cwd=os.path.dirname(__file__)


createMenuShortCut(name='sc', command=f'{cwd}/venv/bin/python {cwd}/main.py', icon=f'{cwd}/pinit.svg', categories='Utility')
createDesktopShortCut(name='sc', command=f'{cwd}/venv/bin/python {cwd}/main.py', icon=f'{cwd}/pinit.svg', categories='Utility')