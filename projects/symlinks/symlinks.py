import os
import ia256utilities.filesystem as fs

dr = "C:"
r = "C:/Users/icearrow256/Dropbox"

replacements = {
    "%icearrow256%": "/Users/icearrow256"
}

def ln(src: str, dst: str):
    if os.path.isdir(dst):
        os.rmdir(dst)
    os.makedirs(src, exist_ok=True)
    os.system("mklink /J {} {}".format(dst, src))

def main():
    symlinks = fs.load_json("symlinks.json", False)
    for symlink in symlinks:
        for replacement in replacements:
            symlink = symlink.replace(replacement, replacements[replacement])
        src = os.path.normpath(r + symlink)
        dst = os.path.normpath(dr + symlink)
        ln(src, dst)
        
if __name__ == "__main__":
    main()