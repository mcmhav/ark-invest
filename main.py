import requests
import time
import os

csv_path = f'{os.path.dirname(os.path.realpath(__file__))}/csvs/ark_sheets'
url = 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv'

def get_existing_csv_paths(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return paths

if not os.path.exists(csv_path):
    os.makedirs(csv_path)

paths = get_existing_csv_paths(csv_path)
newest_date = ''
if len(paths) > 0:
    newest_csv = max(paths, key=os.path.getctime)
    newest_csv_time = int(newest_csv.split('.')[0].split('-')[2])

    newest_date = time.strftime('%Y-%m-%d %H', time.localtime(newest_csv_time))

timestamp = int(time.time())
current_date = time.strftime('%Y-%m-%d %H', time.localtime(timestamp))

if newest_date != current_date:
    r = requests.get(url)

    newest_csv = f'{csv_path}/arkw-{timestamp}.csv'

    with open(newest_csv, 'wb') as f:
      f.write(r.content)

