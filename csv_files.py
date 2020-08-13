'''
import csv
import random

random.seed(45)
with open('accounts.csv', mode = 'w', newline='') as accounts:
    fieldnames = ['Account Number','Last Name', 'Balance']
    writer = csv.writer(accounts)
    writer.writerow(fieldnames)
    writer.writerow([random.randrange(1000,5001), 'Parker', random.randrange(1000001)])
    writer.writerow([random.randrange(1000,5001), 'Banner', random.randrange(1000001)])
    writer.writerow([random.randrange(1000,5001), 'Stark', random.randrange(1000001)])
    writer.writerow([random.randrange(1000,5001), 'Strange', random.randrange(1000001)])
    writer.writerow([random.randrange(1000,5001), 'Bond', random.randrange(1000001)])


with open('accounts.csv', mode='r', newline='') as accounts:
    reader = csv.reader(accounts)
    for row in reader:
        accountNumber, lastName, balance = row
        print(f'{accountNumber:<15} {lastName:<15} {balance:>15}')

'''

import pandas as pd
import matplotlib.pyplot as plt

'''
frame = pd.read_csv('accounts.csv')

Tframe = frame.T
series = Tframe.iloc[1]
frame.index = series

frame.to_csv('frame_accounts.csv', index=False)



print(frame)
'''

'''
titanic = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv")

titanic.columns = ['Name', 'Survived', 'Gender', 'Age', 'Class']

print(titanic.head(10))

print((titanic.Survived == 'yes').describe())

titanic.hist()

plt.show()
'''

salaries = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/carData/Salaries.csv")
salaries.columns = ['X', 'Rank', 'Discipline', 'PHD_Years', 'Service_Years', 'Gender', 'Salary']


salaries = salaries.drop(columns=['X'])

print(salaries.describe())

print((salaries.Gender == 'Female').describe())

salaries.hist()
plt.show()
