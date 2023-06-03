from shortcut import *
import os

for icon in os.listdir(menuPath):
    if icon.startswith('pinit'):
        os.remove(f'{menuPath}/{icon}')

for icon in os.listdir(desktopPath):
    if icon.startswith('pinit'):
        os.remove(f'{desktopPath}/{icon}')
