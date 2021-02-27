import re

# re.search() finds out the first match
# Here r stands for raw, and that means all the special characters in this string will be ignored by python
# Returns none if no match found

# . stands for any character
print(re.search(r"ho.e", "HOPE", re.IGNORECASE))
# ^ indicates start of line with character
print(re.search(r"^m", "muntaha", re.IGNORECASE))
# $ indicates end of line with character
print(re.search(r"m$", "muntaha", re.IGNORECASE))
# [] means any of the between
print(re.search(r"[vVp]o", "powel"))
# - defines a range
print(re.search(r"[g-z]ue", "guerrila"))
# [^] means not in
print(re.search(r"[^a-zA-Z ]", "What a gloomy day!"))

# re.findall() finds out all the matches once
# | indicates or
print(re.findall(r"dogs|babies|you", "I like dogs and babies. They both bite."))

# * means specified character for as many time as I want
print(re.search(r"py.*n", "python programming"))

# + means one or more
print(re.search(r"o+f", "roof"))

# ? indicates 0 or 1
print(re.search(r"o?f", "rf"))

# \ is escape character, it's used for giving raw input of special characters like . ? [] etc.
print(re.search(r"\.com", "my.com"))

# \w indicates all alphaneumeric characters and underscore, \d is digits, \s for whitespace characters, \b for word bounderies, etc.
print(re.search(r"\w*", "my.com"))