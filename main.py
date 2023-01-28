import os
import time


def rm_files(directory, exts):
    for root, dirs, files in os.walk(directory):
        for file in files:
            for ext in exts:
                if file.endswith(ext):
                    os.remove(os.path.join(root, file))


dl_path = "C:/Users/Amélia/Downloads/"
extensions = [".exe", ".zip", ".7z", ".rar"]
os.startfile(dl_path)
time.sleep(5)
rm_files(dl_path, extensions)
