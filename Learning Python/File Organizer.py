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
    items = os.listdir(folder)
    for subfolder in required_folders:
        if subfolder not in items:
            os.mkdir(os.path.join(folder, subfolder))
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


def main():
    check_folder(folder)

main()