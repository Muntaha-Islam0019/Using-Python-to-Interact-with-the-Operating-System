#!/usr/bin/env python3
import re
import csv

users = {}
errors = {}

f = open("syslog.log")
for line in f:
    line = line.strip()

    # groups - https://www.tutorialspoint.com/What-is-the-groups-method-in-regular-expressions-in-Python
    username = (re.search(r"\((.*)\)", line)).group(1)
    message = (re.search(r"(ERROR|INFO)", line)).group(1)
    
    if (username not in users):
        user_count = {'INFO': 0, 'ERROR': 0}
        users[username] = user_count
    users[username][message] += 1

    if message == "ERROR":
        err = (re.search(r"ERROR (.*) ", line)).group(1)
        if (err not in errors):
            errors[err] = 0
        errors[err] += 1
f.close()

users_list = []
errors_list = []
for key in sorted(users.keys()):
    users_list.append([key, users[key]["INFO"], users[key]["ERROR"]])

for key, value in sorted(errors.items(), key=lambda item: item[1], reverse=True):
    errors_list.append([key, value])

users_list.insert(0, ["Username", "INFO", "ERROR"])
errors_list.insert(0, ["Error", "Count"])

file_errors = open("error_message.csv", "w")
file_users = open("user_statistics.csv", "w")

writer_1 = csv.writer(file_errors)
writer_2 = csv.writer(file_users)
writer_1.writerows(errors_list)
writer_2.writerows(users_list)

file_errors.close()
file_users.close()
