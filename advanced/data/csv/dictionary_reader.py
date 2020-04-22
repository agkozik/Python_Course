import csv

with open('csv_data/persons.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    print('Dialect: ', reader.dialect)
    for row in reader:
        print(reader.line_num -1, row['name'], row['lastname'], row['iq'], sep='\t')