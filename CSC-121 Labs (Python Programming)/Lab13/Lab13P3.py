#
# Alex Cesar Rosa
# 4/21/2024
# ITS Python Certification Review - Problem 1 (OS and OS.Path modules)
#

import os
import os.path


def show_files_and_dirs():
    print("Files and directories in current directory: ")
    dir_contents = os.listdir()
    for i in dir_contents:
        print(f"\t{i}")
    print()


def main():
    show_files_and_dirs()
    if os.path.isfile("info.txt"):
        os.renames("info.txt", "info.txt")
    else:
        print("File info.txt does not exist. Cannot rename.")

    if not os.path.exists("information"):
        os.mkdir("information")
    else:
        print("Directory information already exists. Cannot create.")

    show_files_and_dirs()


main()
