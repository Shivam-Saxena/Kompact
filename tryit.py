import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['s1', 's2','s3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'s1': '', 's2': '', 's3': 'Spam'})
    writer.writerow({'s1': '', 's2': 'Spam', 's3': ''})
    writer.writerow({'s1': 'Spam', 's2': '', 's3': ''})
