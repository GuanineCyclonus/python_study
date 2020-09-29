import sys
sys.path.insert(0, './')

import pyautogui
import pyperclip


pyautogui.FAILSAFE = True
width, height = pyautogui.size()
word = pyautogui.prompt(text='请输入你要轰炸发送的文字:', title='BOOM!!!', default='')

pyperclip.copy(word)
location = pyautogui.prompt(text=('请输入你输入栏的位置(坐标)宽度为%d,高度为%d(格式:Width+空格+Height)' % (width, height)), title='BOOM!!!')
location_width, location_height = location.split(' ')
location_width = int(location_width)
location_height = int(location_height)
times = int(pyautogui.prompt(text='请输入轰炸次数:', title='BOOM!!!', default=''))
Hotkey = pyautogui.confirm(text='请输入发送键:', title='BOOM!!!', buttons=['enter', 'enter+ctrl', 'return', 'return+command'])
Hotkey = Hotkey.split('+')
try:
    hotkeyf = Hotkey[0]
    hotkeys = Hotkey[1]
except Exception:
    hotkeyf = Hotkey[0]

pyautogui.moveTo(location_width, location_height)
pyautogui.click(location_width, location_height, 1, 0, 'left')

for time in range(times):
    time += 1
    if hotkeyf == 'enter':
        pyautogui.hotkey('ctrl', 'v')
    if hotkeyf == 'return':
        pyautogui.hotkey('command', 'v')

    try:
        pyautogui.hotkey(hotkeys, hotkeyf)
    except Exception:
        pyautogui.hotkey(hotkeyf)
