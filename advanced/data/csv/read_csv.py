import csv

with open('csv_data/persons.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    print('Lines number: ', reader.line_num)
    print('Dialect', reader.dialect)
    for row in reader:
        print(reader.line_num - 1, row, sep=' ')
