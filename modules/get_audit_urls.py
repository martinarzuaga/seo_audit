import pandas as pd
import pygsheets
import requests
from modules.create_endpoint import client_name

# Login to Google Sheets
gc = pygsheets.authorize(client_secret='./credentials/client_secret_martin.json')

# open the Google spreadsheet and save all the sheets
# sh = gc.open(f'Auditoria-SEO-{client_name}')
# Activate this line below when you are doing a review
# sh = gc.open(f'Auditoria-SEO-{client_name}-Revision')
# Activate this line below when you are doing another task
sh = gc.open(f'Auditoria-Performance-{client_name}')
# Activate this line below when you are doing another task
# sh = gc.open(f'Auditoria-Performance-{client_name}-Revision')

# save all the workseets in variables
wks_velocidad = sh.worksheet('title', 'Velocidad')
wks_cache = sh.worksheet('title', 'Caché')
wks_webVitals = sh.worksheet('title', 'Web Vitals')
wks_pageSpeed = sh.worksheet('title', 'PageSpeed')
# wks_mobileFriendly = sh.worksheet('title', 'Web Responsive')

# save all the URLs to check to
urls_list = []

for row in wks_velocidad.range('B2:B100'):
    if 'http' in row[0].value:
        url = row[0].value
        request = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"})
        if request.status_code == 200:
            urls_list.append(row[0].value)
        else:
            continue
    else:
        break