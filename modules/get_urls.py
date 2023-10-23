<<<<<<< HEAD
import pandas as pd
import credentials.loging_to_gs as lgs

gc = lgs.log_to_gs()

# open the Google spreadsheet and save all the sheets
sh = gc.open('Auditoria-Performance-Divino')

# save all the worksheets in variables
wks_velocidad = sh.worksheet('title', 'Velocidad')
wks_cache = sh.worksheet('title', 'Caché')
wks_webVitals = sh.worksheet('title', 'Web Vitals')
wks_pageSpeed = sh.worksheet('title', 'PageSpeed')

# save the worksheets also un data frames
df_velocidad = pd.DataFrame(wks_velocidad)
df_cache = pd.DataFrame(wks_cache)
df_webVitals = pd.DataFrame(wks_webVitals)
df_pageSpeed = pd.DataFrame(wks_pageSpeed)

# save all the URLs to check to
urls_list = []

for url in wks_velocidad.range('B2:B100'):
    if 'http' in url[0].value:
        urls_list.append(url[0].value)
=======
import pandas as pd
import credentials.loging_to_gs as lgs

gc = lgs.log_to_gs()

# open the Google spreadsheet and save all the sheets
sh = gc.open('Copy of Auditoria-SEO-Aliss-CR_y_PA')

# save all the worksheets in variables
wks_velocidad = sh.worksheet('title', 'Velocidad')
wks_cache = sh.worksheet('title', 'Caché')
wks_webVitals = sh.worksheet('title', 'Web Vitals')
wks_pageSpeed = sh.worksheet('title', 'PageSpeed')

# save the worksheets also un data frames
df_velocidad = pd.DataFrame(wks_velocidad)
df_cache = pd.DataFrame(wks_cache)
df_webVitals = pd.DataFrame(wks_webVitals)
df_pageSpeed = pd.DataFrame(wks_pageSpeed)

# save all the URLs to check to
urls_list = []

for url in wks_velocidad.range('B2:B100'):
    if 'http' in url[0].value:
        urls_list.append(url[0].value)
>>>>>>> main
