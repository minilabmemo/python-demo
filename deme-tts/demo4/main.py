import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# 获取当前工作目录
print("Current working directory:", os.getcwd())

# 获取脚本文件所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
print("Current script_dir directory:", script_dir)

file_path = os.path.join(script_dir, 't1_ed.txt')

# 读取文件内容
with open(file_path, "r") as fh:
    lines = fh.readlines()

# 设置语言
language = 'en'

# 创建一个空的音频段
combined = AudioSegment.empty()

# 生成每行的音频并添加到组合音频中
for line in lines:
    myText = line.strip()
    if myText:
        output = gTTS(text=myText, lang=language, slow=True)
        line_audio_file_path = os.path.join(script_dir, 'line_temp.mp3')
        output.save(line_audio_file_path)

        # 加载生成的音频文件
        line_audio = AudioSegment.from_file(line_audio_file_path)
        combined += line_audio + AudioSegment.silent(duration=1000)  # 添加 1 秒静音

# 保存组合后的音频文件
audio_file_path = os.path.join(script_dir, 'ep1_en.mp3')
combined.export(audio_file_path, format="mp3")

# 播放组合后的音频文件
if os.path.exists(audio_file_path):
    play(combined)
else:
    print(f"File not found: {audio_file_path}")
