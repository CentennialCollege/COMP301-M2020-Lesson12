import csv
import random

random.seed(45)
with open('accounts.csv', mode = 'w', newline='') as accounts:
    fieldnames = ['AccountNumber','LastName', 'Balance']
    writer = csv.writer(accounts)
    writer.writerow(fieldnames)
    writer.writerow([random.randrange(1000,5001), 'Parker', random.randrange(1000001)])
    writer.writerow([random.randrange(1000,5001), 'Banner', random.randrange(1000001)])
    writer.writerow([random.randrange(1000,5001), 'Stark', random.randrange(1000001)])
    writer.writerow([random.randrange(1000,5001), 'Strange', random.randrange(1000001)])
    writer.writerow([random.randrange(1000,5001), 'Bond', random.randrange(1000001)])


