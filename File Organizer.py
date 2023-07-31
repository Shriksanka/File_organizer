import os
from pathlib import Path

DIRECTORIES = {
    "HTML_Folder": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES_Folder": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "VIDEOS_Folder": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".3gp"],
    "DOCUMENTS_Folder": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
    "ARCHIVES_Folder": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO_Folder": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT_Folder": [".txt", ".in", ".out"],
    "PDF_Folder": [".pdf"],
    "PYTHON_Folder": [".py", ".ipynb"],
    "XML_Folder": [".xml"],
    "EXE_Folder": [".sh", ".exe"],
    "LABEL_Folder": [".lnk"],
    "EXCEL_Folder": [".csv"],
    "ACCESS_Folder": [".accdb", ".laccdb"],
    "TORRENT_Folder": [".torrent"],
    "MINECRAFT_MODS_Folder": [".jar"]
}


FILE_FORMATS = {file_format: directory
               for directory, file_formats in DIRECTORIES.items()
               for file_format in file_formats}


def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok = True)
            file_path.rename(directory_path.joinpath(file_path))
            
        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass


if __name__ == "__main__":
    organize_junk()






