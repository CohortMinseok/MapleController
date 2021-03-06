import os, shutil
import sys

sys.path.append('..')
sys.path.append('..\\Dependencies')
from Dependencies import admin

if not admin.isUserAdmin():
    admin.runAsAdmin(wait=False)
    sys.exit()

hiddenimports = [
    'numpy',
    'os',
    'subprocess',
    'itertools',
    'ctypes',
    'win32gui',
    'win32com',
    'pyautogui',
    'keyboard',
    'json',
    'datetime',
    'psutil',
    'time',
    'PIL',
    "mss",
    "cv2",
    "shutil",
    "re"
]




os.makedirs('../compile', exist_ok=True)
with open('../compile/controller imports.py', 'w') as fd:
    fd.write('hiddenimports = ' + str(hiddenimports))

shutil.copyfile("../Dependencies/admin.py", '../compile/admin.py')
shutil.copyfile("Bot.py", '../compile/Bot.py')

os.system('pyinstaller "../compile/bot.py" --onefile --specpath="../compile/" --distpath="../compile/" --workpath="../compile/" --additional-hooks-dir="../compile/hook-data.py"')

shutil.copyfile('../compile/bot.exe', 'bot.exe')
shutil.rmtree('../compile')
#