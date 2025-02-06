"""
@author: <Ealsen>
@file: crawler_tools_kuaishou_video.py
@date: 2025/02/06
@description: 
爬取快手视频py脚本
"""
import random
import string
import time
import requests
import os

# 全局变量，指定视频的下载路径
# 注意：请修改为自己实际的下载路径
# 举例：DOWNLOAD_PATH: str = r"E:\downloadCaches\picturesVideos\savedVideos"

DOWNLOAD_PATH: str = r"E:\downloadCaches\picturesVideos\savedVideos"

target_url: str = r"https://v2.kwaicdn.com/ksc2/ryrww2ZSvFO0YJPsU9dpmSg4-XCZbSgxa0EIikWioOKFMBONre8GKbSiqnbxSbVQ27cYNMBRGAvlAH-cOpYGbNHbH3fbALpLGDd47bMTb0n97iBNakKcqN7zFrNoM9ah.mp4?pkey=AAXQpY-NbnBR0ry6Dp2RobVDe4ILkmo-IOjeeCDtG8f5Waxf1RDlWkfKrgF9KJrGpcz-Vb2wld36iopMpGkAA5cdgJcQjf3kgE-U9yLbb3zPB7N094dRmw6iUpF_dh7yk0M&tag=1-1738843462-unknown-0-1vjrrfvqzc-23a4c35a03187c9b&clientCacheKey=3xj7t2x4s9qx42g_0981a13b&di=JA4DaYz3pgB2DQwx_sd5gQ==&bp=10004&tt=hd15&ss=vp"

def rename_video(target_url: str) -> str:
    """
    重命名视频文件名，从URL中随机取英文字符并结合当前时间戳中的几个数字
    :param target_url: 视频的URL链接
    :return: 重命名后的视频文件名
    """
    # 从URL中提取一部分英文字符
    video_name = target_url.split("/")[-1].split("?")[0]
    letters = ''.join(filter(lambda c: c in string.ascii_letters, video_name))
    
    # 随机选择5个英文字符（允许重复）
    random_chars = ''.join(random.choices(letters, k=min(5, len(letters))))
    
    # 获取当前时间戳并取最后6位数字
    timestamp = str(int(time.time()))[-6:]
    
    # 结合随机字符和时间戳生成新的文件名，并确保长度不超过30字符
    new_video_name = f"{random_chars}_{timestamp}.mp4"
    if len(new_video_name) > 30:
        new_video_name = new_video_name[:26] + ".mp4"
    
    return new_video_name

filename: str = rename_video(target_url)

def download_video(url: str, filename: str) -> None:
    """
    从给定的URL下载视频并保存到文件中
    :param url: 视频的URL链接
    :param filename: 保存的文件名
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 如果响应状态码不是200，抛出异常
        
        # 确保下载路径存在
        if not os.path.exists(DOWNLOAD_PATH):
            os.makedirs(DOWNLOAD_PATH)
        
        with open(os.path.join(DOWNLOAD_PATH, filename), 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"视频已成功下载并保存为 {os.path.join(DOWNLOAD_PATH, filename)}")
    except requests.exceptions.RequestException as e:
        print(f"下载视频时发生错误: {e}")

if __name__ == "__main__":
    download_video(target_url, filename)
