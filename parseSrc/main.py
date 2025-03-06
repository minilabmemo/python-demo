import re
import json

def parse_srt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip()
    
    subtitles = []
    pattern = re.compile(r"(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\d+|$)", re.DOTALL)
    
    for match in pattern.finditer(content):
        subtitles.append({
            "index": int(match.group(1)),
            "start": match.group(2),
            "end": match.group(3),
            "text": match.group(4).replace('\n', ' '),
            "chText": ""  # 預留中文字幕欄位
        })
    
    return subtitles

def merge_ch_srt(subtitles, ch_srt_path):
    with open(ch_srt_path, "r", encoding="utf-8") as file:
        content = file.read().strip()
    
    pattern = re.compile(r"(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\d+|$)", re.DOTALL)
    ch_subtitles = {int(match.group(1)): match.group(4).replace('\n', ' ') for match in pattern.finditer(content)}
    
    for sub in subtitles:
        if sub["index"] in ch_subtitles:
            sub["chText"] = ch_subtitles[sub["index"]]
    
    return subtitles

def save_to_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    srt_file = "en.srt"
    ch_srt_file = "ch.srt"
    json_file = "demo.json"
    parsed_data = parse_srt(srt_file)
    merged_data = merge_ch_srt(parsed_data, ch_srt_file)
    save_to_json(merged_data, json_file)
    print(f"Merged {srt_file} and {ch_srt_file} into {json_file} successfully!")