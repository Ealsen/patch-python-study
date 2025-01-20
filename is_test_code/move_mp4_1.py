import os
import shutil
import time
from colorama import Fore, Style

# 脚本功能：
# 遍历脚本目录及其子目录，查找所有 .mp4 文件，并将其移动到脚本目录下。
# 若目标路径已存在文件，则自动重命名文件名。
# 记录日志 move_mp4_log.txt，包括移动成功和失败的文件，以及错误信息。
# 脚本运行结束后，打印总结信息。

# 初始化 Colorama
os.system("")  # 确保颜色代码在 Windows cmd 下生效

# 获取脚本执行目录
# current_dir = os.getcwd()
current_dir = r"F:\Multimedia\the_video\CRTubeGetVideoDownload"
total_mp4_files = 0
moved_mp4_files = 0
error_count = 0

# 日志文件路径
log_file = os.path.join(current_dir, "move_mp4_log.txt")

# 遍历脚本目录及其子目录以统计 .mp4 文件总数
for root, dirs, files in os.walk(current_dir):
    for file in files:
        if file.lower().endswith(".mp4"):
            total_mp4_files += 1

# 如果没有找到任何 .mp4 文件，提示并退出
if total_mp4_files == 0:
    print(Fore.YELLOW + "No .mp4 files found in the directory or its subdirectories.")
    exit()

# 提示用户确认操作
print(Fore.CYAN + f"Found {total_mp4_files} .mp4 files in the directory and its subdirectories.")
confirm = input(Fore.CYAN + "Do you want to proceed with moving them to the current directory? (yes/no): ").strip().lower()
if confirm not in ['yes', 'y']:
    print(Fore.YELLOW + "Operation cancelled.")
    exit()

# 开始记录日志，使用追加模式
with open(log_file, "a", encoding="utf-8") as log:  # 使用追加模式
    log.write("MP4 File Move Log\n")
    log.write("=" * 50 + "\n")

    # 遍历目录并移动 .mp4 文件
    for root, dirs, files in os.walk(current_dir):
        print(Fore.GREEN + f"Processing directory: {root}")
        for file in files:
            if file.lower().endswith(".mp4"):
                file_path = os.path.join(root, file)
                target_path = os.path.join(current_dir, file)

                # 检查目标路径是否已存在文件
                if os.path.exists(target_path):
                    file_name, file_ext = os.path.splitext(file)
                    timestamp = time.strftime("%Y%m%d%H%M%S")
                    target_path = os.path.join(current_dir, f"{file_name}_{timestamp}{file_ext}")

                try:
                    # 移动文件
                    shutil.move(file_path, target_path)
                    moved_mp4_files += 1
                    progress = (moved_mp4_files / total_mp4_files) * 100
                    print(Fore.BLUE + f"Moved: {file_path} -> {target_path} ({progress:.2f}%)")
                    # 每条记录都有当前时间
                    log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Moved: {file_path} -> {target_path}\n")
                except Exception as e:
                    error_count += 1
                    print(Fore.RED + f"Failed to move {file_path}: {e}")
                    # 每条记录都有当前时间
                    log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Failed to move {file_path}: {e}\n")

# 打印总结信息
print(Fore.CYAN + "=" * 50)
print(Fore.GREEN + f"Operation complete. Total files: {total_mp4_files}, Moved files: {moved_mp4_files}, Errors: {error_count}")
print(Fore.CYAN + f"Log file saved to: {log_file}")
