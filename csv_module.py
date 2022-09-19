import csv


csv_file = open('people.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['id', 'name', 'username', 'email'])
csv_writer.writerow(['1', 'Usman Musa', 'Shehu', 'UsmanMusa@python.org'])
csv_writer.writerow(['2', 'Yusuf Musa', 'Myusuf', 'YusufMusa@python.org'])
csv_writer.writerow(['3', 'Aisha Musa', 'Mami', 'AishaMusa@python.org'])
csv_file.close()


with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
