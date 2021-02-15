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