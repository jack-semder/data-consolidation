import csv


headers = []
# Reads first three files
# this works
def read_file(f):
    contents = []
    with open(f, newline='') as csv_f:
        reader = csv.reader(csv_f, delimiter=',')
        headers.append(next(reader)) # One header array per file

        for row in reader:
            contents.append(', '.join(row))

    return contents

# Combines data from all three input files
# Dictionary [header keys, column values] 2-d dictionary?
def whole_df(f1, f2, f3):
    file1 = read_file(f1)
    file2 = read_file(f2)
    file3 = read_file(f3)

# Getting data ready for output files
def organize():
    pass

# Setup and return output files
def outputs():
    pass

# Combine all proccesses
def main():
    pass


