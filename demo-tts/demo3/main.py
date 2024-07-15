import os
import re
from gtts import gTTS

# 获取当前脚本文件的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 定义正则表达式用于匹配 <ch> 和 <en> 标签
ch_pattern = re.compile(r'<ch>(.*?)</ch>')
en_pattern = re.compile(r'<en>(.*?)</en>')

# 打开 Markdown 文件并逐行处理
markdown_file = os.path.join(script_dir, 'test.md')

with open(markdown_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化一个空的音频文件路径
output_file = os.path.join(script_dir, 'combined_audio.mp3')

# 逐行生成语音并写入文件
with open(output_file, 'wb') as audio_file:
    for line in lines:
        # 匹配中文标签 <ch>
        ch_match = ch_pattern.search(line)
        if ch_match:
            chinese_text = ch_match.group(1).strip()
            print(f"Chinese: {chinese_text}")
            tts = gTTS(chinese_text, lang='zh-tw')
            tts.write_to_fp(audio_file)

        # 匹配英文标签 <en>
        en_match = en_pattern.search(line)
        if en_match:
            english_text = en_match.group(1).strip()
            print(f"English: {english_text}")
            tts = gTTS(english_text, lang='en')
            tts.write_to_fp(audio_file)

# 播放合并后的音频文件（仅适用于 macOS，其他系统需要相应命令）
os.system(f"afplay {output_file}")
