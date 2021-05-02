# This code would only work in Unix-like computer operating systems
import sys
import re

logfile  = sys.argv[1]
with open(logfile) as f:
    # Log files may be large, so it's better to read them line by line
    for line in f:
        # CRON is a time-based job scheduler in Unix-like computer operating systems
        # Here, we're just implementing what we would do if something had gone wrong while using CRON
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result[1])
