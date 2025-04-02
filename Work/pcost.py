# pcost.py
#
# Exercise 1.27
import csv
import sys
from fileinput import filename


def portfolio_cost(filename):
    'csv 파일 이름을 넣으면 포트폴리오 총 비용을 부동소수점으로 반환'
    total_price = float()
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)

        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total_price = total_price + (shares * price)
            except ValueError:
                print("value error with this line:", row)
                continue

    return total_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("Total cost", cost)






