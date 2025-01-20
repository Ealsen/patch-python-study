import os
import time
from colorama import Fore

# 脚本功能：批量删除指定目录下包含指定关键词的文件
# 脚本说明：该脚本会遍历指定目录及其子目录，查找所有文件名包含指定关键词的文件，并将其删除。
# 脚本使用：1. 修改脚本中的 current_dir 变量为要遍历的目录路径；
#          2. 修改脚本中的 wordkey 变量为要查找并删除的文件名关键词列表；
#          3. 修改脚本中的 bai_word 变量为要保留的文件名关键词列表；
#          4. 运行脚本，根据提示输入 yes 确认删除，脚本将自动遍历指定目录及其子目录，查找并删除所有符合条件的文件。
# 脚本日志：该脚本会在脚本执行目录下生成一个名为 del_wordkey_file.txt 的日志文件，记录删除操作的详细信息。
# 脚本注意事项：脚本不会删除目录，只会删除文件。请确认要删除的文件是否是你希望删除的，并且不要删除重要文件。


# 初始化 Colorama
os.system("")  # 确保颜色代码在 Windows cmd 下生效

# 指定要遍历的目录路径
current_dir = r"F:\Multimedia\the_video\BilbilVideoDownload"

# 关键词列表
wordkey = ['eg_keyword1', 'eg_keyword2', 'eg_keyword3']  # 在这里添加你希望查找并删除的关键词

# 白名单关键词列表
bai_word = ['eg_whitelist_keyword1', 'eg_whitelist_keyword2']  # 在这里添加你希望保留的关键词

# 日志文件路径
log_file_path = os.path.join(current_dir, "del_wordkey_file.txt")

# 初始化计数器和文件列表
checked_files = 0  # 记录检查的文件数量
deleted_files = 0  # 记录删除的文件数量
error_count = 0  # 记录删除失败的文件数量
files_to_delete = []  # 记录需要删除的文件路径

# 检查目标目录是否存在
if not os.path.exists(current_dir):
    print(Fore.RED + f"目标目录 {current_dir} 不存在，请检查路径。")
    exit()

# 遍历脚本执行目录及其子目录
for root, dirs, files in os.walk(current_dir):
    for file in files:
        checked_files += 1  # 增加检查的文件数量
        file_path = os.path.join(root, file)

        # 检查文件名是否包含白名单关键词
        if any(keyword.lower() in file.lower() for keyword in bai_word):
            continue  # 如果文件名包含白名单关键词，则跳过该文件

        # 检查文件名是否包含关键词
        if any(keyword.lower() in file.lower() for keyword in wordkey):
            files_to_delete.append(file_path)  # 如果文件名包含关键词，则记录该文件路径

# 如果没有找到任何符合条件的文件，提示并退出
if not files_to_delete:
    print(Fore.YELLOW + "No files found matching the specified keywords.")
    exit()

# 提示用户确认操作
print(Fore.CYAN + "=" * 50)
print(Fore.CYAN + "以下文件将被删除：")
for file_path in files_to_delete:
    print(Fore.CYAN + file_path)  # 列出所有将要删除的文件路径

# 用户确认删除
confirm = input(Fore.CYAN + "是否继续删除这些文件？(yes/no): ").strip().lower()
if confirm not in ['yes', 'y']:
    print(Fore.YELLOW + "操作已取消。")
    exit()  # 如果用户不确认，则取消操作并退出

# 打开日志文件，并指定使用 utf-8 编码以处理特殊字符
with open(log_file_path, "a", encoding="utf-8") as log_file:  # 使用追加模式
    log_file.write("File Deletion Log\n")
    log_file.write("=" * 50 + "\n")
    log_file.write(f"Log started at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write("=" * 50 + "\n")

    # 遍历需要删除的文件列表并删除它们
    for file_path in files_to_delete:
        try:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Deleting File: {file_path}\n")
            os.remove(file_path)  # 删除文件
            deleted_files += 1  # 增加删除的文件数量
        except Exception as e:
            error_count += 1  # 增加错误计数
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Failed to delete {file_path}: {e}\n")  # 记录删除失败的文件及其错误信息到日志文件

# 打印总结信息
print(Fore.CYAN + "=" * 50)
print(Fore.GREEN + f"操作完成：总计检查文件 {checked_files} 个，成功删除 {deleted_files} 个文件，删除失败 {error_count} 个。")
print(Fore.CYAN + f"日志已保存至 {log_file_path}。")  # 打印日志文件的保存路径
