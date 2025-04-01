# pcost.py
#
# Exercise 1.27
import os


total_price = float()

with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        total_price = total_price + (shares*price)

print("Total cost", total_price)