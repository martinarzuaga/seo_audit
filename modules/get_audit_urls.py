import pygsheets
import requests
from modules.request_tests import client_name

credentials = './credentials/client_secret_dahseo.json'

# Login to Google Sheets
gc = pygsheets.authorize(client_secret=credentials)

# open the Google spreadsheet and save all the sheets
sh = gc.open(f'Auditoria-SEO-{client_name}')

# save all the workseets in variables
wks_cache = sh.worksheet('title', 'Caché')
wks_velocidad = sh.worksheet('title', 'Velocidad')
wks_webVitals = sh.worksheet('title', 'Web Vitals')
wks_pageSpeed = sh.worksheet('title', 'PageSpeed')
wks_mobileFriendly = sh.worksheet('title', 'Web Responsive')

# save all the URLs to check to
urls_list = []

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 \
                Edge/12.246"

for row in wks_velocidad.range('B2:B100'):
    if 'http' in row[0].value:
        url = row[0].value
        request = requests.get(url, headers={"User-Agent": user_agent})
        if request.status_code == 200:
            urls_list.append(row[0].value)
        else:
            continue
    else:
        break
