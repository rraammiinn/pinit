import desktop_file as d
########################################################################################################
menuPath=d.getMenuPath()
desktopPath=d.getDesktopPath()
########################################################################################################
def createShortCut(path,name,command,icon,terminal=False,categories=None,comment=None):
    shortcut = d.LinuxShortcut.LinuxShortcut(path, name, command)
    shortcut.setTitle(name)
    shortcut.setIcon(icon)
    shortcut.setCategories(categories)
    shortcut.attributes['Terminal'] = str(terminal).lower()
    if comment:
        shortcut.attributes['Comment'] = comment
    shortcut.save()

def createMenuShortCut(name,command,icon,terminal=False,categories=None,comment=None):
    createShortCut(menuPath,name,command,icon,terminal,categories,comment)

def createDesktopShortCut(name,command,icon,terminal=False,categories=None,comment=None):
    createShortCut(desktopPath,name,command,icon,terminal,categories,comment)

