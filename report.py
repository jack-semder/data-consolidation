import csv

# Reads first three files
# this works
def read_file(f):
    contents = []
    with open(f, newline='') as csv_f:
        reader = csv.reader(csv_f, delimiter=',')

        for row in reader:
            contents.append(', '.join(row))

    return contents
            #print(', '.join(row))
            #contents[test] = (', '.join(row))
            #test += 1


# Combines data from all three input files
# Dictionary [header keys, column values] 2-d dictionary?
def whole_df(f1, f2, f3):
    file_contents = {}
    file1 = read_file(f1)
    file2 = read_file(f2)
    file3 = read_file(f3)

    file_contents["file1"] = file1
    file_contents["file2"] = file2
    file_contents["file3"] = file3

    return file_contents # three keys 

# Getting data ready for output files
def gross_revenue_calculations():
    
# Setup and return output files
def outputs():
    pass

# Combine all proccesses
def main():
    files = whole_df("team_map.csv", "product_master.csv", "sales.csv")

    with open('team_report.csv', 'w', newline='') as csvf:
        writer = csv.writer(csvf, delimiter=',')

        writer.writerow(files["file1"][0][1] + grossRevenue)

