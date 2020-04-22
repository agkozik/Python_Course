import csv

class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "_"
    delimiter = ","
    lineterminator = '\n'
    # _1_,_2_,_3_
    # _4_,_5_,_6_

csv.register_dialect('tester', CustomDialect)

with open('csv_data/custom_dialect_csv.csv', 'w') as file:
    writer = csv.writer(file, dialect='tester')
    writer.writerow(['1', '2', '3'])
    writer.writerow(['4', '5', '6'])