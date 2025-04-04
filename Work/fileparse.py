# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_header=True):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성
    '''
    if select is None:
        select = []
    with open(filename) as f:
        rows = csv.reader(f)

        # 헤더를 읽음
        if has_header:
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select.copy()
            else:
                indices = []
        else:
            headers = None

        records = []
        for row in rows:
            if not row:    # 데이터가 없는 행을 건너뜀
                continue

            if has_header:
                if indices:
                    row = [row[index] for index in indices]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                record = dict(zip(headers, row))

            else:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                    record = tuple(row)

            records.append(record)

    return records