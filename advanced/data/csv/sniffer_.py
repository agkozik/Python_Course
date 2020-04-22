import csv

sniffer = csv.Sniffer()
dialect = None

print('# пробуем прочитать файл обычным ридером')
with open('csv_data/sniffer_file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print('# определяем диалект')
with open('csv_data/sniffer_file.csv', 'r') as file:
    content = file.read()
    dialect = sniffer.sniff(content)

print(dialect.delimiter, dialect.doublequote, dialect.quoting)

print('# используя полученный диалект, читаем файл')
with open('csv_data/sniffer_file.csv', 'r') as file:
    reader = csv.reader(file, dialect=dialect)
    for row in reader:
        print(row)
