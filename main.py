import os
from pathlib import Path
from dotenv import load_dotenv
from utils.file_utils import organize_by_type, organize_by_date

# Load .env as fallback
load_dotenv(dotenv_path="./config/settings.env")

def print_menu():
    print("\nWelcome to Smart Download Organizer 📁")
    print("--------------------------------------")
    print("1. Organize by file type")
    print("2. Organize by date")
    print("3. Exit")

def get_download_path():
    path = input("Enter folder path to organize (leave blank to use .env DOWNLOAD_PATH): ").strip()
    if not path:
        path = os.getenv("DOWNLOAD_PATH", "Downloads")
    folder = Path(path)
    if not folder.exists():
        print(f"[ERROR] Path does not exist: {folder}")
        return None
    return folder

def main():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            folder = get_download_path()
            if folder:
                log_file = Path("logs/activity.log")
                log_file.parent.mkdir(parents=True, exist_ok=True)
                log_file.write_text("=== FILE ORGANIZER LOG ===\n")
                organize_by_type(folder, log_file)
                print("✔ Done organizing by file type.")
        
        elif choice == "2":
            folder = get_download_path()
            if folder:
                log_file = Path("logs/activity.log")
                log_file.parent.mkdir(parents=True, exist_ok=True)
                log_file.write_text("=== FILE ORGANIZER LOG ===\n")
                organize_by_date(folder, log_file)
                print("✔ Done organizing by date.")

        elif choice == "3":
            print("👋 Exiting. Have a clutter-free day!")
            break

        else:
            print("[ERROR] Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()