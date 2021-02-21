import os
import datetime


def file_date(filename):
    # Create the file in the current directory
    file = open('newfile.txt', 'w')
    timestamp = os.path.getmtime('newfile.txt')
    # Convert the timestamp into a readable format, then into a string
    date = datetime.datetime.fromtimestamp(timestamp).date().strftime("%Y-%m-%d")
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return date


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
