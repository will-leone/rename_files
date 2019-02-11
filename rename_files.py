"""
For all files in the chosen directory, replaces the user-input substring
with another user-input substring in the filenames, within the files'
text, or both based on user input. For intra-file text replacement,
eligibile file types are TXT, CSV, SAS, and SQL.
"""
import os
import datetime

start = datetime.datetime.utcnow()


def file_rename(path=os.getcwd()):
    delta_input_start = datetime.datetime.utcnow()
    str_old = input('Type the current substring you want to replace in every '
                    'filename in this directory, then press Enter. Don\'t add '
                    'extra quotes around the substring.\n')
    str_new = input('Type the new substring you want to insert in place '
                    'of the old substring, then press Enter. Don\'t add '
                    'extra quotes around the substring.\n')
    scope = input('Type "both" (lowercase, no quotes) and press '
                              'Enter if you want to make the substring '
                              'replacement in both the filenames and text '
                              'within the files themselves. Type "filenames" '
                              'to only update the filenames and "files" to '
                              'only update text within the files.\n')
    delta_input_end = datetime.datetime.utcnow()
    global delta
    delta = delta_input_end - delta_input_start
    with os.scandir(os.getcwd()) as mydir:
        for item in mydir:
            if scope.strip() in ('both', 'files') and any(extension in item.name
                    for extension in ['.sas', '.sql', '.csv', '.txt']):
                with open(item.name, 'r') as file:
                    contents = file.read()
                new_contents = contents.replace(str_old, str_new)
                with open(item.name, 'w') as file:
                    file.write(new_contents)
            if (scope.strip() in ('both', 'filenames') and item.is_file()
                    and str_old in item.name):
                new_name = (item.name).replace(str_old, str_new)
                os.rename(item.path, new_name)
    return


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

end = datetime.datetime.utcnow()
total_time = end - start
adjusted_time = total_time - delta
print("\nThis script ran in ", adjusted_time.total_seconds(), " seconds.\n")
raise SystemExit
