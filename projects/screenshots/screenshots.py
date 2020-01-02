import os
import time
import pathlib
import hashlib

root = "C:/Users/icearrow256/Pictures/Screenshots/"


def get_sha256(filename: str) -> str:
    with open(filename,"rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
    return readable_hash

def main():
    files = list()
    for (dirpath, dirnames, filenames) in os.walk(root):
        files += [os.path.join(dirpath, file) for file in filenames]

    for file_path in files:
        if pathlib.Path(file_path).suffix == ".png":
            unix_time = min(os.path.getctime(file_path), os.path.getmtime(file_path))
            if unix_time == 1577141277.0:
                new_path = os.path.normpath("{}/Old/{}.png".format(root, get_sha256(file_path)))
                new_dirs = os.path.dirname(new_path)
                if not os.path.isdir(new_dirs):
                    os.makedirs(new_dirs, True)
                os.rename(file_path, new_path)
            else: 
                lt = time.localtime(unix_time)
                new_path = os.path.normpath("{}/{}.{}/{}.png".format(root, lt.tm_year, lt.tm_mon, float(unix_time)))
                new_dirs = os.path.dirname(new_path)
                if not os.path.isdir(new_dirs):
                    os.makedirs(new_dirs, True)
                if not os.path.exists(new_path):
                    os.rename(file_path, new_path)
                elif not os.path.normpath(file_path) == os.path.normpath(new_path):
                    if (get_sha256(file_path) == get_sha256(new_path)):
                        os.remove(new_path)
                        os.rename(file_path, new_path)
            
if __name__ == "__main__":
    main()