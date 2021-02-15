import os
import datetime

# os.remove('novel.txt')
# If we try to remove it again it shows an error
# os.remove('novel.txt')

# It changes the name
# os.rename('first_draft.txt', 'final_draft.txt')

# Checks if it is there
print(os.path.exists('first_draft.txt'))

# Returns the size in bytes
print(os.path.getsize('spider.txt'))

# Returns the timestamp of creation
timestamp = os.path.getmtime('spider.txt')
print(datetime.datetime.fromtimestamp(timestamp))

# Returns the absolute path
print(os.path.abspath('spider.txt'))

# Current working directory
print(os.getcwd())

# Make a new directory
# os.mkdir('new_directory')

# Change the directory
os.chdir('new_directory')
print(os.getcwd())

# Remove a directory
os.mkdir('newer_directory')
os.rmdir('newer_directory')
# One need to delete all the files in a directory before to remove the directory
# A directory which consists files, will throw an error if someone tries to remove it

# Listing files in a directory
# os.mkdir('a_dir')
# os.mkdir('another_dir')
os.chdir('..')
# Goes to parent directory
print(os.listdir('new_directory'))

# Joining path names & checking if its a directory
os.chdir('new_directory')
with open('a_text.txt', 'w') as file:
    file.write("Well, it's a line")
os.chdir('..')
dir_name = 'new_directory'
for name in os.listdir(dir_name):
    full_path = os.path.join(dir_name, name)
    if os.path.isdir(full_path):
        print('{} is a directory'.format(full_path))
    else:
        print('{} is a file'.format(full_path))
