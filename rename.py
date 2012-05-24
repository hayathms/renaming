import sys
import os


# This script removes blank space from all type of
# File names and replaces it with '-' recurssively
# This script also replaces '_' with '-'
# Running this script is easy rename.py 'path to fiolder'
#

path = sys.argv[1]
number_of_dir = 0
number_of_files = 0
number_of_dir = number_of_files = 0


def rename(path):

    elements = os.listdir(path)
    global number_of_dir
    global number_of_files
    number_of_dir += 1
    for ele in elements:
        old_pathname = os.path.join(path, ele)
        if os.path.isdir(old_pathname):
            rename(os.path.join(path, ele))
        else:
            old_filename = ele
            new_filename = ele.strip()
            new_filename = new_filename.replace(' ', '-')
            new_filename = new_filename.replace('_', '-')
            new_filename = new_filename.replace('--', '-')
            new_filename = new_filename.replace('?', '')
            new_filename = new_filename.replace(':', '-')
            new_filename = new_filename.replace("'", "-")


            new_filename = new_filename.lower()
            new_path = os.path.join(path, new_filename)

            if old_pathname != new_path:
                print('----------------------------------------------')
                os.rename(os.path.join(path, ele), new_path)
                print(old_pathname)
                print(new_path)
                number_of_files += 1

if __name__ == '__main__':
    rename(path)
    print('Number of Directories visited = {0}'.format(number_of_dir))
    print('Number of Files Effected = {0}'.format(number_of_files))
    print('Enter Ctr+C to end ')

    while True:
        rename(path)
