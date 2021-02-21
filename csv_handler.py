import csv
import os

script_path = f'{os.path.dirname(os.path.realpath(__file__))}/csvs'
csv_path = f'{script_path}/ark_sheets'
handled_csvs_path = f'{script_path}/handled_csvs'
stocks_path = f'{script_path}/stocks'

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

create_folder(csv_path)
create_folder(handled_csvs_path)
create_folder(stocks_path)

files = os.listdir(csv_path)
paths = [os.path.join(csv_path, basename) for basename in files]

def read_funding_data(path):
    with open(path, 'r') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row

def iterate_rows_for_csv(path):
    csv_time = path.split('.')[0].split('-')[2]
    for idx, row in enumerate(read_funding_data(path)):
        if row['ticker']:
            with open(f'{stocks_path}/{row["ticker"]}', 'a+') as stock_file:
                stock_file.write(f'{csv_time},{row["shares"]}\n')
    os.rename(path, f'{handled_csvs_path}/{os.path.basename(path)}')


if len(paths):
    for path in paths:
        iterate_rows_for_csv(path)

