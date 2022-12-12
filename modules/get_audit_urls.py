import pandas as pd
import pygsheets
from modules.create_endpoint import client_name

# Login to Google Sheets
gc = pygsheets.authorize(client_secret='./credentials/client_secret.json')

# open the Google spreadsheet and save all the sheets
sh = gc.open(f'Auditoria-SEO-{client_name}')

# save all the workseets in variables
wks_velocidad = sh.worksheet('title', 'Velocidad')
wks_cache = sh.worksheet('title', 'Caché')
wks_webVitals = sh.worksheet('title', 'Web Vitals')
wks_pageSpeed = sh.worksheet('title', 'PageSpeed')
wks_webVitals = sh.worksheet('title', 'Web Vitals')
wks_mobileFriendly = sh.worksheet('title', 'Mobile Friendly')

# save all the URLs to check to
urls_list = []

for url in wks_velocidad.range('B2:B100'):
    if 'http' in url[0].value:
        urls_list.append(url[0].value)
