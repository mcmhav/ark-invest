import requests
import pandas as pd
import time
import os

csv_path = './ark_sheets'
url = 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv'

def newest_file(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

newest_csv = newest_file(csv_path)
newest_csv_time = int(newest_csv.split('.')[1].split('-')[1])

newest_date = time.strftime('%Y-%m-%d', time.localtime(newest_csv_time))
timestamp = int(time.time())
current_date = time.strftime('%Y-%m-%d', time.localtime(timestamp))

if newest_date != current_date:
    r = requests.get(url)

    if not os.path.exists(csv_path):
        os.makedirs(csv_path)

    newest_csv = f'{csv_path}/arkw-{timestamp}.csv'

    with open(newest_csv, 'wb') as f:
      f.write(r.content)

df = pd.read_csv(newest_csv)
df = df[df['company'].notna()]

df_formated = pd.DataFrame(data=[df['shares'].values], columns=df['company'])
print(df_formated.head())

