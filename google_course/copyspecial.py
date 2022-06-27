import os
import re
import shutil
import subprocess
import sys


def get_special_paths(given_dir):
    # returns a list of the absolute paths of the special files in the given directory
    allfiles = os.listdir(given_dir)
    special_path = []
    for file in allfiles:
        if re.search(r'__(\w+)__', file):
            special_path.append(os.path.abspath(os.path.join(given_dir, file)))
    return special_path


def copy_to(paths, mydir):
    # given a list of paths, copies those files into the given directory
    if not os.path.exists(mydir):
        os.mkdir(mydir)
    for path in paths:
        shutil.copy(path, os.path.join(mydir))


def zip_to(paths, zippath):
    # (решение скопировала из подсказок, но я его не понимаю, он у меня не работает)
    # given a list of paths, zip those files up into the given zipfile
    cmd = 'zip -j ' + zippath + ' ' + ' '.join(paths)
    print("Command I'm going to do:" + cmd)
    (status, output) = subprocess.getstatusoutput(cmd)
    # здесь заменила модуль commands на subprocess, т.к. в Питоне 3 его нет)
    # If command had a problem (status is non-zero),
    # print its output to stderr and exit.
    if status:
        sys.stderr.write(output)
        sys.exit(1)


def main():
    print('\n'.join(get_special_paths(r'C:\Users\User\Desktop\tasks_from_hacker\google_course')))

    copy_to([r'C:\Users\User\Desktop\tasks_from_hacker\google_course\list1.py',
             r'C:\Users\User\Desktop\tasks_from_hacker\collection_counter2.py'], 'mydirect')


if __name__ == "__main__":
    main()
