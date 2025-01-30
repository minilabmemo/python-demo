# 程式說明 v2.0
# sanitize_filename 避免影片命名太長太複雜造成錯誤
# download_video 可以下載 但是mac內建播放器無法開啟
# convert_to_quicktime_compatible 轉換成mac內建播放器quicktime可以開啟的影片 以利剪裁



import os
import subprocess
import yt_dlp
import re

def sanitize_filename(filename, max_length=20):
    # 移除非法字符，並替換空白和加號
    filename = re.sub(r'[<>:"/\\|?*\s+]', '_', filename)  # 將非法字符、空白字符及加號替換為下劃線
    # 截取最大長度
    if len(filename) > max_length:
        filename = filename[:max_length]
    return filename

def download_video(url, save_path="."):
    try:
        ydl_opts = {
            'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',  # 確保下載 H.264 + AAC
            'merge_output_format': 'mp4',  # 合併成 MP4
            'outtmpl': f"{save_path}/%(id)s.%(ext)s",  # 使用 ID 儲存臨時檔案名稱
            'noplaylist': True,  # 防止下載播放清單
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_title = info.get('title', 'downloaded_video')
            sanitized_title = sanitize_filename(video_title)

            # 確定下載的影片檔案名稱
            temp_downloaded_file = f"{save_path}/{info['id']}.mp4"  # 這是 `yt_dlp` 下載的臨時檔案名稱
            downloaded_file = f"{save_path}/{sanitized_title}.mp4"  # 使用處理後的檔案名稱

            # 重新命名檔案
            if os.path.exists(temp_downloaded_file):
                os.rename(temp_downloaded_file, downloaded_file)

        print(f"下載完成！檔案名稱：{downloaded_file}")
        return downloaded_file
    except Exception as e:
        print(f"下載失敗: {e}")
        return None

def convert_to_quicktime_compatible(input_file):
    if not input_file or not os.path.exists(input_file):
        print(f"檔案不存在: {input_file}")
        return
    
    output_file = input_file.replace(".mp4", "_converted.mp4")
    
    command = [
        "ffmpeg",
        "-i", input_file,  # 讀取輸入影片
        "-c:v", "libx264",  # 轉為 H.264
        "-c:a", "aac",  # 轉為 AAC
        "-b:a", "192k",  # 設定音質
        "-movflags", "+faststart",  # 讓影片可以快速播放
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"轉檔完成！輸出檔案：{output_file}")
    except subprocess.CalledProcessError as e:
        print(f"轉檔失敗: {e}")

if __name__ == "__main__":
    video_url = input("請輸入 YouTube 影片網址: ").strip()
    downloaded_video = download_video(video_url)
    if downloaded_video:
        convert_to_quicktime_compatible(downloaded_video)
