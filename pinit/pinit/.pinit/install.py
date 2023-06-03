from shortcut import *
import os
cwd=os.path.dirname(__file__)


createMenuShortCut(name='pinit', command=f'{cwd}/venv/bin/python {cwd}/main.py', icon=f'{cwd}/pinit.svg', categories='Utility')
createDesktopShortCut(name='pinit', command=f'{cwd}/venv/bin/python {cwd}/main.py', icon=f'{cwd}/pinit.svg', categories='Utility')