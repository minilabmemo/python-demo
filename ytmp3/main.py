import yt_dlp

def download_audio(url, save_path="."):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f"{save_path}/%(title)s.%(ext)s"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("音訊下載完成！")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    video_url = input("請輸入YouTube影片網址: ")
    download_audio(video_url)
