import csv

# Reads first three files
# this works
def read_file(f):
    headers = []
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

    li = []
    for row in file2:
        row = list(row)

    return file_contents # DICTIONARY VALUES NEED TO BE STR -> LIST


def gross_revenue():
    quants = []
    priceper_u = []
    lot_size = []

    gross_rev = []

    for row in whole_df("team_map.csv", "product_master.csv", "sales.csv")["file2"]:
        row = list(row)
        priceper_u.append(float(row[2]))
        lot_size.append(int(row[3]))


    for row in whole_df("team_map.csv", "product_master.csv", "sales.csv")["file3"]:
        row = list(row)
        #quants.append(int(row[3]))

    #print(priceper_u)
    #for item in priceper_u:
        #print(type(item))
    '''for num in quants:
        for num2 in priceper_u:
            first = num * num2
            for num3 in lot_size:
                second = first * num3
                gross_rev.append(second)'''


    return gross_rev

# Combine all proccesses
def main():
    records1 = read_file("team_map.csv")
    records2 = read_file("product_master.csv")
    records3 = read_file("sales.csv")

    for team_id, name in records1:
        pass
