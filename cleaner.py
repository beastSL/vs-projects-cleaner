import os
from os import path

def check_vs_proj(dirs):
    for s in dirs:
        if len(s) >= 4 and s[-4:] == ".sln":
            return True
    return False

def check_del(filename):
    return (
        (len(filename) < 2 or filename[-2:] != ".h") and
        (len(filename) < 3 or filename[-3:] != ".cs") and 
        (len(filename) < 4 or filename[-4:] != ".cpp")
    )

def dfs(cur_path, restricted_dir, del_mode):
    if os.getcwd() in restricted_dir:
        return
    os.chdir(cur_path)
    ls = os.listdir()
    if not del_mode and check_vs_proj(ls):
        del_mode = True
    for d in ls:
        if path.isdir(d):
            dfs(d, restricted_dir, (del_mode or d == ".vs"))
            if del_mode or d == ".vs":
                try:
                    os.rmdir(d)
                except OSError:
                    pass
        elif path.isfile(d) and del_mode and check_del(d):
            os.remove(d)
    os.chdir("..")


restricted_dir = [
    r"C:\Users\thati\source\repos\work",
    r"C:\Users\thati\source\repos\oop\work_projects",
    r"C:\Users\thati\source\repos\_trashbox"
]
dfs(r"C:\Users\thati\source\repos", restricted_dir, False)