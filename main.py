import os
import time


def rm_files(directory, exts):
    for root, dirs, files in os.walk(directory):
        for file in files:
            for ext in exts:
                if file.endswith(ext):
                    os.remove(os.path.join(root, file))


path = "C:/Users/user_name/Downloads/"
extensions = [".exe", ".zip", ".7z", ".rar", ".msi"] # types of files you want to delete
os.startfile(path)
time.sleep(2)
rm_files(path, extensions)

