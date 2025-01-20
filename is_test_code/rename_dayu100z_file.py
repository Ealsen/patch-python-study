import os
import random
import time
import string

# 脚本功能：
# 1. 遍历指定目录下的所有文件，查找文件名长度大于100字符的文件
# 2. 对于这些文件，生成新的文件名，并确保文件名不重复
# 3. 重命名文件，并记录重命名日志
# 4. 输出重命名日志和统计信息

# 指定目录路径
target_dir = r"F:\Multimedia\the_video\BilbilVideoDownload"

# 日志文件路径
log_file_path = os.path.join(target_dir, "rename_dayu100z_log.txt")

# 定义生成器
def generate_timerandom():
    """生成基于当前时间的10字符随机字符串"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def generate_randmodkey(original_name):
    """从原文件名前30字符中随机抽取5字符"""
    original_name = original_name[:30]  # 截取原文件名前30字符
    return ''.join(random.sample(original_name, min(5, len(original_name))))

def generate_unique_suffix(existing_names):
    """生成不重复的2字符随机后缀"""
    while True:
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=2))
        if suffix not in existing_names:
            return suffix

# 初始化计数器
files_to_rename = []
success_count = 0
failure_count = 0

# 检查文件名长度
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if len(file) > 100:
            files_to_rename.append((root, file))  # 记录待重命名的文件

# 如果没有需要重命名的文件，退出程序
if not files_to_rename:
    print("No files with names longer than 100 characters found.")
    exit()

# 列出需要重命名的文件并统计数量
print("=" * 50)
print(f"Found {len(files_to_rename)} files with names longer than 100 characters:")
for root, file in files_to_rename:
    print(os.path.join(root, file))

# 用户确认是否继续
confirm = input("Do you want to proceed with renaming these files? (yes/no): ").strip().lower()
if confirm not in ['yes', 'y']:
    print("Operation cancelled.")
    exit()

# 开始重命名并记录日志
with open(log_file_path, "a", encoding="utf-8") as log_file:  # 使用追加模式
    log_file.write("Rename Log for Files > 100 Characters\n")
    log_file.write("=" * 50 + "\n")
    log_file.write(f"Log Start Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write("=" * 50 + "\n")

    # 重命名文件
    renamed_files = []  # 记录已重命名的文件，用于确保唯一性
    for root, file in files_to_rename:
        file_name, file_ext = os.path.splitext(file)

        # 生成新文件名
        timerandom = generate_timerandom()
        randmodkey = generate_randmodkey(file_name)
        notsame = generate_unique_suffix(renamed_files)  # 确保不重复
        new_name = f"{file_name[:20]}-{timerandom}-{randmodkey}-{notsame}{file_ext}"

        # 确保新文件名不会超过100字符
        if len(new_name) > 100:
            new_name = new_name[:100 - len(file_ext)] + file_ext

        # 构造完整路径
        old_path = os.path.join(root, file)
        new_path = os.path.join(root, new_name)

        # 执行重命名
        try:
            os.rename(old_path, new_path)
            success_count += 1
            renamed_files.append(new_name)  # 保存新文件名

            # 记录日志
            log_file.write(
                f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Renamed: {old_path} -> {new_path}\n"
            )
            print(f"Renamed: {old_path} -> {new_path}")
        except Exception as e:
            failure_count += 1
            log_file.write(
                f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Failed to rename {old_path}: {e}\n"
            )
            print(f"Failed to rename {old_path}: {e}")

    # 写入统计信息
    log_file.write("=" * 50 + "\n")
    log_file.write(f"Total Files Renamed Successfully: {success_count}\n")
    log_file.write(f"Total Rename Failures: {failure_count}\n")
    log_file.write(f"Log End Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write("=" * 50 + "\n")

# 输出总结信息到终端
print("=" * 50)
print(f"Renaming process completed. Total Success: {success_count}, Total Failures: {failure_count}")
print(f"Log saved to: {log_file_path}")
