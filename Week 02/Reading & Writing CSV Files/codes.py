import csv

# Reading a CSV
# file_handler = open("csv_file.txt")
# csv_file_handler = csv.reader(file_handler)
# reader returns a list
# DictReader returns a dictionary

# Writing a CSV
types = [["lady bug", "insect"], ["dolphin", "mammal"]]
with open("types.csv", "w") as types_csv:
    writer = csv.writer(types_csv)
    # writerows write multiple rows at a time using a list
    # writerow writes a single row
    # DictWriter writes a csv from a dictionary
    # To use the writerows() function of DictWriter() to write a list of dictionaries to each line of a CSV file write the fieldnames parameter into the first row using writeheader()
    writer.writerows(types)