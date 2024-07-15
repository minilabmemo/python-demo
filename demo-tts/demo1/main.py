# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 


# 在 Python 中，当前工作目录（current working directory, CWD）是指 Python 解释器运行时的目录/Python/simple_py_demo
print("Current working directory:", os.getcwd())    

# 要确保文件路径相对于脚本文件所在的目录，可以使用__file__变量来获取/Python/simple_py_demo/deme-tts
script_dir = os.path.dirname(os.path.abspath(__file__))
print("Current script_dir directory:", script_dir) 

file_path = os.path.join(script_dir, 'test.txt')


# with open("./test1.txt", "w") as fh:
#     fh.write("This is a test file.")

fh = open(file_path, "r")
myText = fh.read().replace("\n", " ")

# Language we want to use 
language = 'en'

output = gTTS(text=myText, lang=language, slow=True)
audio_file_path = os.path.join(script_dir, 'ep1_en.mp3')

output.save(audio_file_path)
fh.close()

# Play the converted file 
if os.path.exists(audio_file_path):
    # 使用 afplay 命令播放音频文件
    os.system(f"afplay {audio_file_path}")
else:
    print(f"File not found: {audio_file_path}")