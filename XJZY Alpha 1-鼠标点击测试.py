import keyboard

def on_key_press(event):
    print(event)
    print(f"Key {event.name} was pressed.")

# 监听所有按键按下事件
keyboard.on_press(on_key_press)

# 保持程序运行，直到按下ESC
keyboard.wait("esc")