import subprocess

# We use subprocess to run system commands in python

# Shows the date
# subprocess.run(["date"]) 

# Keeps the interpreter idle for 2 seconds
# subprocess.run(["sleep", "2"], shell=True)

# This type of run commands is only useful if we wanna figure out if the command is successful or not
# To obtain the output which can be later used:

# result = subprocess.run(["host", "8.8.8.8"], capture_output=True, shell=True)
# print(result.returncode)
# print(result.stdout) this will generate an array of bytes
# To decode:
# print(result.stdout.decode.split())
# For errors, we should use stderr instead of stdout