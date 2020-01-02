import os
import ia256utilities.filesystem as fs

r = "C:"
dr = "C:/Users/icearrow256/Dropbox"
gr = "C:/Users/icearrow256/Google Drive"

replacements = {
    "%icearrow256%": "/Users/icearrow256"
}

def ln(src: str, dst: str):
    if os.path.exists(dst):
        os.rmdir(dst)
    os.makedirs(src, exist_ok=True)
    print(src)
    os.system("mklink /J \"{}\" \"{}\"".format(dst, src))

def main():
    symlinks = fs.load_json("symlinks.json", False)
    for symlink in symlinks["Dropbox"]:
        for replacement in replacements:
            symlink = symlink.replace(replacement, replacements[replacement])
        src = os.path.normpath(dr + symlink)
        dst = os.path.normpath(r + symlink)
        ln(src, dst)
    for symlink in symlinks["Google Drive"]:
        for replacement in replacements:
            symlink = symlink.replace(replacement, replacements[replacement])
        src = os.path.normpath(gr + symlink)
        dst = os.path.normpath(r + symlink)
        ln(src, dst)
        
if __name__ == "__main__":
    main()