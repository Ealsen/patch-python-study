import os
import shutil
import time
from colorama import Fore

# 脚本功能
# 遍历指定目录及其子目录，删除其中没有 .mp4 文件的目录，并记录删除的目录及其子目录路径、发现的 .mp4 文件路径。
# 日志文件会记录删除的目录及其子目录路径、发现的 .mp4 文件路径，并输出总结信息。
# 脚本执行目录为脚本所在目录，日志文件会保存至脚本所在目录下的 directory_cleanup_log.txt 文件

# 初始化 Colorama
os.system("")  # 确保颜色代码在 Windows cmd 下生效

# 指定要遍历的目录路径
current_dir = r"F:\Multimedia\the_video\BilbilVideoDownload"

# 排除目录列表（白名单）
exclude_dirs = ['.temp', '.thumb', 'cache', 'eg_exclude_dir1', 'eg_exclude_dir2', 'eg_exclude_dir3']  # 在这里添加你不希望删除的目录名

# 日志文件路径
log_file_path = os.path.join(current_dir, "directory_cleanup_log.txt")

# 初始化计数器
deleted_dirs = 0  # 记录删除的空目录数量
found_mp4_files = 0  # 记录发现的 .mp4 文件数量
checked_dirs = 0  # 记录检查的目录数量
directories_to_delete = []  # 记录需要删除的目录路径

# 打开日志文件，并指定使用 utf-8 编码以处理特殊字符
with open(log_file_path, "a", encoding="utf-8") as log_file:  # 使用追加模式
    log_file.write("Directory Cleanup Log\n")
    log_file.write("=" * 50 + "\n")
    log_file.write(f"Log started at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write("=" * 50 + "\n")

    # 遍历脚本执行目录及其子目录，从子目录向上遍历（topdown=False）
    # 这样可以确保在删除空目录时，先处理子目录，再处理父目录
    for root, dirs, files in os.walk(current_dir, topdown=False):
        checked_dirs += 1  # 增加检查的目录数量

        # 提取当前目录的名称
        dir_name = os.path.basename(root)

        # 检查当前目录是否在排除目录列表中，如果是则跳过
        if dir_name in exclude_dirs:
            continue

        mp4_files = [f for f in files if f.lower().endswith(".mp4")]  # 找到目录中所有的 .mp4 文件

        # 如果目录中没有 .mp4 文件，记录目录路径
        if not mp4_files:
            directories_to_delete.append(root)
        else:
            # 如果目录中有 .mp4 文件，记录文件信息
            for file in mp4_files:
                log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Found .mp4 File: {os.path.join(root, file)}\n")  # 记录发现的 .mp4 文件路径到日志文件
                found_mp4_files += 1  # 增加发现的 .mp4 文件数量

# 输出检查结果
print("=" * 50)
print(f"操作完成：检查了 {checked_dirs} 个目录。")  # 打印检查的目录数量
print(f"发现了 {found_mp4_files} 个 .mp4 文件。")  # 打印发现的 .mp4 文件数量
print(f"发现了 {len(directories_to_delete)} 个没有 .mp4 文件的子目录。")  # 打印没有 .mp4 文件的子目录数量

# 提示用户确认操作
if directories_to_delete:
    print(Fore.CYAN + "以下目录将被删除：")
    for root in directories_to_delete:
        print(Fore.CYAN + root)
else:
    print(Fore.GREEN + "没有发现需要删除的空目录。")

confirm = input(Fore.CYAN + "Do you want to proceed with deleting these directories? (yes/no): ").strip().lower()
if confirm not in ['yes', 'y']:
    print(Fore.YELLOW + "Operation cancelled.")
    exit()

# 打开日志文件，并指定使用 utf-8 编码以处理特殊字符
with open(log_file_path, "a", encoding="utf-8") as log_file:  # 使用追加模式
    # 遍历需要删除的目录列表并删除它们
    for root in directories_to_delete:
        try:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Deleting Directory: {root}\n")
            shutil.rmtree(root)  # 删除整个目录及其子目录
            deleted_dirs += 1  # 增加删除的空目录数量
        except Exception as e:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Failed to delete directory {root}: {e}\n")  # 记录删除失败的目录及其错误信息到日志文件

# 输出总结信息
print("=" * 50)
print(f"操作完成：检查了 {checked_dirs} 个目录。")  # 打印检查的目录数量
print(f"删除了 {deleted_dirs} 个空目录。")  # 打印删除的空目录数量
print(f"发现了 {found_mp4_files} 个 .mp4 文件。")  # 打印发现的 .mp4 文件数量
print(f"日志已保存至 {log_file_path}。")  # 打印日志文件的保存路径
