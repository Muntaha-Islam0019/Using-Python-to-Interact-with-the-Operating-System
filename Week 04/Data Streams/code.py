import os

# To access environment variables:
print("TEMP: " + os.environ.get("TEMP", ""))
# If a variable isn't present, the above line would print a black space. To export a new variable, write "export VAR_NAME = VALUE" in command line

