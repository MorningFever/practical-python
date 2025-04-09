# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    'csv 파일 이름을 넣으면 포트폴리오 총 비용을 부동소수점으로 반환'
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")
                continue

    return total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')

    cost = portfolio_cost(argv[1])
    print("Total cost", cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)


