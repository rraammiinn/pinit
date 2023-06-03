import desktop_file as d
########################################################################################################
menuPath=d.getMenuPath()
desktopPath=d.getDesktopPath()
########################################################################################################
def createShortCut(path,name,command,icon,terminal=False,categories=None,title=name):
    shortcut = d.LinuxShortcut.LinuxShortcut(path, name, command)
    shortcut.setTitle(title)
    shortcut.setIcon(icon)
    shortcut.setCategories(categories)
    shortcut.attributes['Terminal'] = str(terminal).lower()
    shortcut.save()

def createMenuShortCut(name,command,icon,terminal=False,categories=None,title=name):
    createShortCut(menuPath,name,command,icon,terminal,categories)

def createDesktopShortCut(name,command,icon,terminal=False,categories=None,title=name):
    createShortCut(desktopPath,name,command,icon,terminal,categories)

