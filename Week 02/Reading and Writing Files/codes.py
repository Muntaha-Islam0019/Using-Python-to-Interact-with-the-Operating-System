file = open('spider.txt')
# Read reads all lines together
print(file.read())
file.close()

# File opening and closing can be done by with too
with open('spider.txt') as file:
    # Readline just reads one line and add the cursor to next line
    print(file.readline())

# We can read line by line by loops, though it puts a newline after every line and therefore 2 newlines get printed
with open('spider.txt') as file:
    for line in file:
        print(line.strip())

# We can save a file of lines in a list
file = open('spider.txt')
lines = file.readlines()
file.close()
print(lines)

# To write, we use 'w' in the parameter
with open('novel.txt', 'w') as file:
    file.write('Once in a stormy night, I was lying in a camp on mountain Tibi-tabu.')

