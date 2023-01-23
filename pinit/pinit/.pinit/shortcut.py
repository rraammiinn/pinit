import desktop_file as d
########################################################################################################
menuPath=d.getMenuPath()
desktopPath=d.getDesktopPath()
########################################################################################################
def createShortCut(path,name,command,icon,terminal=False,categories=None):
    shortcut = d.LinuxShortcut.LinuxShortcut(path, name, command)
    shortcut.setTitle(name)
    shortcut.setIcon(icon)
    shortcut.setCategories(categories)
    shortcut.attributes['Terminal'] = str(terminal).lower()
    shortcut.save()

def createMenuShortCut(name,command,icon,terminal=False,categories=None):
    createShortCut(menuPath,name,command,icon,terminal,categories)

def createDesktopShortCut(name,command,icon,terminal=False,categories=None):
    createShortCut(desktopPath,name,command,icon,terminal,categories)

