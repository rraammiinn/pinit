import eel
from shortcut import *

# from tkinter.filedialog import askopenfilename , askdirectory
from crossfiledialog import open_file, choose_folder
import os
import sys
import random

########################################################################################################
cwd = os.path.dirname(__file__)
home = os.getenv("HOME")

menuIcons = []
desktopIcons = []
########################################################################################################
eel.init(f"{cwd}/ui", allowed_extensions=[".html"])
########################################################################################################
runners = {
    "python": "python",
    "enaml": "enaml-run",
    "bash": "bash",
    "sh": "sh",
    "xonsh": "xonsh",
    "fish": "fish",
}


########################################################################################################
@eel.expose
def getFilePath(filePath=home):
    # filePath = askopenfilename(title='select app',initialdir=filePath)
    filePath = open_file(title="select app")
    return filePath


@eel.expose
def getIconPath(iconPath=home):
    # iconPath = askopenfilename(title='select icon',initialdir=iconPath)
    iconPath = open_file(title="select icon")
    try:
        os.link(iconPath, f'{cwd}/ui/icons/{iconPath.split("/")[-1]}')
    finally:
        return iconPath


@eel.expose
def getInterpreterPath(interpreterPath=home):
    # interpreterPath = askdirectory(title='select venv',initialdir=interpreterPath)
    interpreterPath = choose_folder(title="select venv")
    return interpreterPath


@eel.expose
def make(
    name,
    filePath,
    iconPath,
    interpreterPath,
    cmd,
    ccmd,
    typ,
    runner,
    is_terminal,
    categories,
    places,
    argv,
    comment,
    getPermissions
):
    runners["python"] = (
        interpreterPath.removesuffix("/bin") + "/bin/python"
        if interpreterPath.strip()
        else "python"
    )
    command = ccmd if ccmd.strip() else runners[runner]
    command = ccmd if typ == "binary" else command
    command += " " + filePath + " " + argv
    command = command.replace("./", "/").replace("//", "/").strip()

    if "menu" in places:
        createMenuShortCut(
            name=name,
            command=command,
            icon=iconPath,
            terminal=is_terminal,
            categories=categories,
            comment=comment
        )
    if "desktop" in places:
        createDesktopShortCut(
            name=name,
            command=command,
            icon=iconPath,
            terminal=is_terminal,
            categories=categories,
            comment=comment
        )

    if getPermissions:
        try:
            subprocess.run(['chmod', 'a+rwx', filePath])
        except:
            pass


########################################################################################################
@eel.expose
def getMenuIconDetails(path):
    with open(path, "r") as fp:
        details = fp.read()
    return details


@eel.expose
def getDesktopIconDetails(path):
    with open(path, "r") as fp:
        details = fp.read()
    return details


@eel.expose
def change(path, details):
    newPath = path.replace(".desktop", f"{random.randint(0, 1000)}.desktop")
    with open(newPath, "w") as fp:
        fp.write(details)
    os.remove(path)


@eel.expose
def delete(path):
    os.remove(path)


@eel.expose
def changeTheme(theme):
    d = ""
    for iconName in os.listdir(menuPath):
        if iconName.startswith("pinit"):
            menuIconPath = f"{menuPath}/{iconName}"
            newPath = menuIconPath.replace(
                ".desktop", f"{random.randint(0, 1000)}.desktop"
            )
            with open(menuIconPath, "r") as fp:
                d = fp.read()
            d = (
                d.replace("light", "")
                .replace("dark", "")
                .replace("main.py", f"main.py {theme}")
            )
            with open(newPath, "w") as fp:
                fp.write(d)
            os.remove(menuIconPath)

    for iconName in os.listdir(desktopPath):
        if iconName.startswith("pinit"):
            desktopIconPath = f"{desktopPath}/{iconName}"
            newPath = desktopIconPath.replace(
                ".desktop", f"{random.randint(0, 1000)}.desktop"
            )
            with open(desktopIconPath, "r") as fp:
                d = fp.read()
            d = (
                d.replace("light", "")
                .replace("dark", "")
                .replace("main.py", f"main.py {theme}")
            )
            with open(newPath, "w") as fp:
                fp.write(d)
            os.remove(desktopIconPath)


@eel.expose
def getTheme():
    return "dark" if ("dark" in sys.argv) else "light"


@eel.expose
def loadMenu():
    global menuIcons
    menuIcons = []

    for iconName in os.listdir(menuPath):
        if iconName.endswith(".desktop"):
            menuIconPath = f"{menuPath}/{iconName}"
            try:
                with open(menuIconPath, "r") as fp:
                    details = fp.readlines()
                    for detail in details:
                        if "Name=" in detail:
                            name = detail.replace("Name=", "").replace("\n", "")
                        elif "Icon=" in detail:
                            icon = detail.replace("Icon=", "").replace("\n", "")
                if os.path.exists(icon):
                    menuIcons.append(
                        f"{menuIconPath},,,{name},,,{os.path.basename(icon)}"
                    )
                    dist = f"{cwd}/ui/menu/{os.path.basename(icon)}"
                    try:
                        os.link(icon, dist)
                    except:
                        pass
            except:
                print("error")
    return ";;;".join(menuIcons)


@eel.expose
def loadDesktop():
    global desktopIcons
    desktopIcons = []

    for iconName in os.listdir(desktopPath):
        if iconName.endswith(".desktop"):
            desktopIconPath = f"{desktopPath}/{iconName}"
            try:
                with open(desktopIconPath, "r") as fp:
                    details = fp.readlines()
                    for detail in details:
                        if "Name=" in detail:
                            name = detail.replace("Name=", "").replace("\n", "")
                        elif "Icon=" in detail:
                            icon = detail.replace("Icon=", "").replace("\n", "")
                if os.path.exists(icon):
                    desktopIcons.append(
                        f"{desktopIconPath},,,{name},,,{os.path.basename(icon)}"
                    )
                    dist = f"{cwd}/ui/desktop/{os.path.basename(icon)}"
                    try:
                        os.link(icon, dist)
                    except:
                        pass
            except:
                print("error")
    return ";;;".join(desktopIcons)


########################################################################################################

if __name__ == "__main__":
    try:
        os.makedirs(f"{home}/.pinit/ui/menu")
    except:
        pass
    try:
        os.makedirs(f"{home}/.pinit/ui/desktop")
    except:
        pass
    try:
        os.makedirs(f"{home}/.pinit/ui/icons")
    except:
        pass

    eel.start("index.html", size=(300, 690), position=(800, 200))
