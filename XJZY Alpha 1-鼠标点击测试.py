# -*- coding: utf-8 -*-
from pynput import mouse, keyboard

# 定义鼠标点击事件的回调函数
def on_click(x, y, button, pressed):
    if pressed:
        # 根据点击位置模拟键盘输入
        if button == mouse.Button.left:
            handle_game_click('left', x, y)
        elif button == mouse.Button.right:
            handle_game_click('right', x, y)

# 游戏内处理点击事件的函数
def handle_game_click(button, x, y):
    # 根据点击按钮执行原本的键盘操作
    if button == 'left':
        # 模拟左键点击对应的键盘操作
        if x < 640:  # 假设屏幕左半部分对应数字键1-5
            if y < 240:  # 假设屏幕上方对应数字键1
                keyboard.press(keyboard.KeyCode(char='1'))
                keyboard.release(keyboard.KeyCode(char='1'))
            # ...以此类推，根据x和y坐标范围确定具体按键
    elif button == 'right':
        # 模拟右键点击对应的键盘操作，例如退出
        keyboard.press(keyboard.KeyCode(char='e'))
        keyboard.release(keyboard.KeyCode(char='e'))
        keyboard.press(keyboard.KeyCode(char='x'))
        keyboard.release(keyboard.KeyCode(char='x'))
        keyboard.press(keyboard.KeyCode(char='i'))
        keyboard.release(keyboard.KeyCode(char='i'))
        keyboard.press(keyboard.KeyCode(char='t'))
        keyboard.release(keyboard.KeyCode(char='t'))

# 启动鼠标监听器的函数
def start_mouse_listener():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()