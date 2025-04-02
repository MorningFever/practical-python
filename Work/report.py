# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in rows:
            row = {
                'name': line[0],
                'shares': int(line[1]),
                'price': float(line[2])
            }
            portfolio.append(row)

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
            print(line)

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
