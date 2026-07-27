# File Organizer

import os
import shutil

folder = input("Enter the path of the folder you want to organize: ")

def check_folder(folder):
    print("Checking folder.....")
    if os.path.isdir(folder):
        print("Folder Exists ✔️")
        check_subfolders(folder)
    else:
        print("This folder does not exist. Please check the path and try again.")

required_folders = [
    "MyImages",
    "MyVideos",
    "MyDocuments",
    "MyMusic",
    "MyPrograms",
    "MyArchives",
    "MyOthers"
    ]
def check_subfolders(folder):
    print("Checking for required subfolders.....")
    items = os.listdir(folder)
    for subfolder in required_folders:
        if subfolder not in items:
            os.mkdir(os.path.join(folder, subfolder))
            print(f"Made {os.path.join(folder, subfolder)} ✔️")
    scan_new_items(folder)

image_ext = [
    ".jpg", ".jpeg", ".png", ".gif",
    ".bmp", ".webp", ".svg", ".tiff",
    ".ico", ".heic", ".avif"
]
video_ext = [
    ".mp4", ".mkv", ".avi", ".mov",
    ".wmv", ".flv", ".webm", ".mpeg",
    ".mpg", ".3gp", ".m4v"
]
document_ext = [
    ".pdf", ".doc", ".docx", ".txt",
    ".ppt", ".pptx", ".xls", ".xlsx",
    ".csv", ".odt", ".rtf", ".md"
]
music_ext = [
    ".mp3", ".wav", ".flac", ".aac",
    ".ogg", ".m4a", ".wma"
]
program_ext = [
    ".exe", ".msi", ".bat", ".cmd",
    ".apk", ".jar", ".py", ".ps1"
]
archive_ext = [
    ".zip", ".rar", ".7z", ".tar",
    ".gz", ".bz2", ".xz"
]
image_count = 0
video_count = 0
document_count = 0
music_count = 0
program_count = 0
archive_count = 0
other_count = 0
image_files = []
video_files = []
document_files = []
music_files = []
program_files = []
archive_files = []
other_files = []
def scan_new_items(folder):
    global image_count, video_count, document_count
    global music_count, program_count, archive_count, other_count
    global image_files, video_files, document_files
    global music_files, program_files, archive_files, other_files
    print("Scanning for new items.....")
    items = os.listdir(folder)
    for item in items:
        item_path = os.path.join(folder, item)
        if item not in required_folders and os.path.isfile(item_path):
            name, ext = os.path.splitext(item)
            ext = ext.lower()
            if ext in image_ext:
                image_count += 1
                image_files.append(item)
            elif ext in video_ext:
                video_count += 1
                video_files.append(item)
            elif ext in document_ext:
                document_count += 1
                document_files.append(item)
            elif ext in music_ext:
                music_count += 1
                music_files.append(item)
            elif ext in program_ext:
                program_count += 1
                program_files.append(item)
            elif ext in archive_ext:
                archive_count += 1
                archive_files.append(item)
            else:
                other_count += 1
                other_files.append(item)
    print("Scan complete ✔️")
    show_summary(folder)

def show_summary(folder):
    total_items_count = image_count + video_count + document_count + music_count + program_count + archive_count + other_count
    print(f"{total_items_count} new items found.")
    print(f"Images :      {image_count}")
    print(f"Videos :      {video_count}")
    print(f"Documents :   {document_count}")
    print(f"Music :       {music_count}")
    print(f"Programs :    {program_count}")
    print(f"Archives :    {archive_count}")
    print(f"Other :       {other_count}")
    get_confirmation(folder)

def get_confirmation(folder):
    confirmation = input("Proceed to move files? (Enter):")
    if get_confirmation == "":
        organize_files(folder)
    else:
        print("...INTERRUPTED...")

def organize_files(folder):
    for item in image_files:
        shutil.move((os.path.join(folder, item)),(os.path.join(folder, "MyImages", item)))
    print("Images moved ✔️")
    for item in video_files:
        shutil.move((os.path.join(folder, item)),(os.path.join(folder, "MyVideos", item)))
    print("Videos moved ✔️")
    for item in document_files:
        shutil.move((os.path.join(folder, item)),(os.path.join(folder, "MyDocuments", item)))
    print("Documents moved ✔️")
    for item in music_files:
        shutil.move((os.path.join(folder, item)),(os.path.join(folder, "MyMusic", item)))
    print("Music moved ✔️")
    for item in program_files:
        shutil.move((os.path.join(folder, item)),(os.path.join(folder, "MyPrograms", item)))
    print("Programs moved ✔️")
    for item in archive_files:
        shutil.move((os.path.join(folder, item)),(os.path.join(folder, "MyArchives", item)))
    print("Archives moved ✔️")
    for item in other_files:
        shutil.move((os.path.join(folder, item)),(os.path.join(folder, "MyOthers", item)))
    print("Others moved ✔️")


def main():
    check_folder(folder)

main()