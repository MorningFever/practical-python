# report.py
#
# Exercise 2.4
import csv
import sys


def read_portfolio(filename):
    '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")
                continue
            portfolio.append(record)

    return portfolio

def read_prices(filename):
    '''가격정보를 읽기'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for line in rows:
            try:
                prices[line[0]] = float(line[1])
            except IndexError:
                print('IndexError:', line)
                continue
            # print(line)

    return prices

def analyze_portfolio(portfolio, prices):

    portfolio_current_value = 0.0
    total_earned = 0.0
    for asset in portfolio:
        asset_name = asset['name']
        asset_shares = asset['shares']
        asset_price = asset_shares * asset['price']
        asset_current_price = asset_shares * prices[asset_name]
        # print(f'{asset_name} | 구매가치:{asset_price} / 현재가치:{asset_current_price} / 손익:{asset_current_price - asset_price}')
        portfolio_current_value += asset_current_price
        total_earned += asset_current_price - asset_price

    print(f'포트폴리오 현재가치: {portfolio_current_value} / 손익: {total_earned}')

def make_report(portfolio, prices):

    resultList = []

    for asset in portfolio:
        asset_name = asset['name']
        asset_shares = asset['shares']
        asset_price = asset['price']
        asset_current_price = prices[asset_name]
        resultList.append((asset_name, asset_shares, asset_current_price, asset_current_price-asset_price))

    return resultList

def print_report(resultList):

    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{'':->10} {'':->10} {'':->10} {'':->10}')
    for name, shares, price, change in resultList:
        print(f'{name:>10s} {shares:>10d} {'$' + str(round(price, 2)):>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    print_report(make_report(portfolio, prices))

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')

    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)