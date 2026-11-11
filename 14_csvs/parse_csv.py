import csv

# Read a CSV file
with open('names.csv', 'r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the first line
    next(csv_reader)

    for line in csv_reader:
        print(line[2])

# Write to a new file
with open('names.csv', 'r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w', encoding='utf-8', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

# Read a CSV with correct delimiter
with open('new_names.csv', 'r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)

# Dictionary Reader
with open('names.csv', 'r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['email'])

# Dictionary Writer
with open('names.csv', 'r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_dict_names.csv', 'w', encoding='utf-8', newline='') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            # removing an email
            del line['email']
            csv_writer.writerow(line)
