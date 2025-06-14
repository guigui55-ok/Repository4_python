from pathlib import Path
import re

def get_new_file_name(file_path: str, add: str) -> Path:
    """既存パスのファイル名にaddを加えて、新しいパスを取得する"""
    original_path = Path(file_path)
    new_file_name = original_path.stem + add + original_path.suffix
    new_file_path = original_path.parent / new_file_name
    
    # 数字付きファイル名が必要な場合
    count = 1
    while new_file_path.exists():
        # ファイル名の最後が既に "_数字" であるかを確認し、カウントアップ
        match = re.match(rf"^(.*{re.escape(add)})(_(\d+))?{re.escape(original_path.suffix)}$", new_file_path.name)
        if match:
            base_name = match.group(1)
            count = int(match.group(3)) + 1 if match.group(3) else 1
            new_file_name = f"{base_name}_{count}{original_path.suffix}"
        else:
            new_file_name = original_path.stem + add + f"_{count}" + original_path.suffix
        
        new_file_path = original_path.parent / new_file_name

    return new_file_path

# 使用例
print("\n*****")
path = r"C:\Users\OK\source\repos\Repository4_python\ffmpeg_test\ffmpeg_tool1.py"
print(get_new_file_name(path, "_new"))
