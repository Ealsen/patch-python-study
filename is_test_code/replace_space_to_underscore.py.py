import os
import time
from colorama import Fore, init


# 脚本功能:
# 批量替换文件名中的空格为下划线
# 日志文件记录替换操作
# 脚本运行前需先确认目标文件夹路径正确
# 脚本运行后需检查日志文件是否存在，并检查日志内容是否正确


# 初始化 Colorama
init(autoreset=True)

# 指定目标文件夹路径
target_dir = r"F:\Multimedia\the_video\BilbilVideoDownload"

# 日志文件路径
log_file_path = os.path.join(target_dir, "replacefilename_spaceto__logger.txt")

# 初始化记录列表
files_to_replace = []

# 遍历目标目录及其子目录
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if " " in file:  # 检查文件名是否包含空格
            old_path = os.path.join(root, file)
            new_file_name = file.replace(" ", "_")  # 替换空格为下划线
            new_path = os.path.join(root, new_file_name)
            files_to_replace.append((old_path, new_path))

# 如果没有需要替换的文件，提示并退出
if not files_to_replace:
    print(Fore.YELLOW + "No files with spaces found in the specified directory.")
    exit()

# 显示即将替换的文件，并统计数量
print(Fore.CYAN + "=" * 50)
print(Fore.GREEN + f"Found {len(files_to_replace)} files with spaces in their names:")
for old_path, new_path in files_to_replace:
    print(Fore.CYAN + f"{old_path} -> {new_path}")

# 用户确认是否继续
confirm = input(Fore.YELLOW + "Do you want to proceed with renaming these files? (yes/no): ").strip().lower()
if confirm not in ['yes', 'y']:
    print(Fore.RED + "Operation cancelled.")
    exit()

# 创建日志文件并记录替换操作
with open(log_file_path, "a", encoding="utf-8") as log_file:  # 使用追加模式
    # 写入日志头部信息
    log_file.write("Replace Space to Underscore Log\n")
    log_file.write("=" * 50 + "\n")
    log_file.write(f"Log Start Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write("=" * 50 + "\n")

    # 替换文件名
    success_count = 0
    for old_path, new_path in files_to_replace:
        try:
            os.rename(old_path, new_path)  # 执行重命名
            success_count += 1
            # 写入日志
            log_file.write(
                f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Renamed: {old_path} -> {new_path}\n"
            )
            print(Fore.GREEN + f"Renamed: {old_path} -> {new_path}")
        except Exception as e:
            log_file.write(
                f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Failed to rename {old_path}: {e}\n"
            )
            print(Fore.RED + f"Failed to rename {old_path}: {e}")

    # 写入统计信息
    log_file.write("=" * 50 + "\n")
    log_file.write(f"Total Files Renamed Successfully: {success_count}\n")
    log_file.write(f"Log End Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write("=" * 50 + "\n")

# 输出总结信息到终端
print(Fore.CYAN + "=" * 50)
print(Fore.GREEN + f"Renaming process completed. Total files renamed: {success_count}")
print(Fore.YELLOW + f"Log saved to: {log_file_path}")
