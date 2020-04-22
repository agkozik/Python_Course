import csv

with open('csv_data/output_csv_file.csv', 'w') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=['name', 'lastname', 'iq'],
        quoting=csv.QUOTE_ALL
    )

    writer.writeheader()
    writer.writerow(
        {
            'name': 'Rick',
            'lastname': 'Sanches',
            'iq': '100'
        }
    )