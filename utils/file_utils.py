import os
import shutil
from pathlib import Path
from datetime import datetime

FILE_TYPE_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Executables": [".exe", ".msi"],
    "Coding": [".py", ".js", ".ts", ".html", ".css", ".cpp", ".java", ".json", ".yaml", ".yml", ".sh", ".bat"]
}

def get_category(extension: str) -> str:
    for category, extensions in FILE_TYPE_MAP.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def move_file_to_folder(file_path: Path, target_dir: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(str(file_path), str(target_dir / file_path.name))

def organize_by_type(source: Path, log_file: Path) -> None:
    for item in source.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            destination = source / category
            move_file_to_folder(item, destination)
            log_file.write_text(log_file.read_text() + f"[TYPE] Moved: {item.name} -> {category}\n")

def organize_by_date(source: Path, log_file: Path) -> None:
    for item in source.iterdir():
        if item.is_file():
            date_folder = datetime.fromtimestamp(item.stat().st_ctime).strftime("%Y-%m-%d")
            destination = source / date_folder
            move_file_to_folder(item, destination)
            log_file.write_text(log_file.read_text() + f"[DATE] Moved: {item.name} -> {date_folder}\n")