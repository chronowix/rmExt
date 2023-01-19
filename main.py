import os
import glob
import time

dl_path = "C:/Users/Amélia/Downloads/"
extension = ("*.exe", "*.zip", "*.7z", "*.rar")

for file in glob.glob(dl_path):
    os.startfile(dl_path)
    time.sleep(5)
    if file.endswith(extension):
        os.remove(file)
        print("files removed!")
    else:
        print("error")
