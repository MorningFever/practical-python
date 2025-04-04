# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_header=True, delimiter=',', silence_errors=False):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성
    '''
    if select is None:
        select = []
    else:
        if not has_header:
            raise RuntimeError("select argument requires column headers")


    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

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
        for rowIndex, row in enumerate(rows, start=1):
            try:
                if not row:  # 데이터가 없는 행을 건너뜀
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
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {rowIndex}: Couldn\'t convert {row}')
                    print(f'Row {rowIndex}: Reason {e}')


    return records