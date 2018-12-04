"""
For all files in the current directory, replaces the user-input substring
with another user-input substring.
"""
import os


def file_rename(path=os.getcwd()):
    str_old = input('Type the current substring you want to replace in every '
                    'filename in this directory, then press Enter. Don\'t add '
                    'extra quotes around the substring.\n')
    str_new = input('Type the new substring you want to insert in place '
                    'of the old substring, then press Enter. Don\'t add '
                    'extra quotes around the substring.\n')
    with os.scandir(os.getcwd()) as mydir:
        for item in mydir:
            if item.is_file() and str_old in item.name:
                new_name = (item.name).replace(str_old, str_new)
                os.rename(item.path, new_name)


dir_location = input('Enter the path of the directory whose files you want to '
                     'rename, then press Enter. If you want to search the '
                     'current directory, press Enter without typing '
                     'anything.\n')

if dir_location == '':
    file_rename()
    print("Rename complete.")
else:
    file_rename(dir_location)
    print("Rename complete.")

raise SystemExit
