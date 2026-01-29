import csv

# filename = "records.csv"
filename = "records_discount.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    print(dialect.quotechar)

    csv_f.seek(0) # powrót na początek pliku

    # csvreadder = csv.reader(csv_f, delimiter=";")
    csvreadder = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(csvreadder)
    # <_csv.reader object at 0x0000022F01E2BA00> - iterator

    fields = next(csvreadder) # odczyt pierwszego wiersz z danych

    for row in csvreadder: # zaczyna od drugiego wiersza
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]

# Fields: ['sku;exp_date;price']
# Rows: [['1;today;200'], ['2;today;100'], ['3;tomorrow;500'], ['4;today;2000'], ['5;today;1200'], ['6;tomorrow;700']]
# Fields: ['sku', 'exp_date', 'price']