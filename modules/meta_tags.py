import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pygsheets
from modules.create_endpoint import client_name

## Setup chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=options)

def get_rendered_source_code(url):
    driver.implicitly_wait(10)
    # Get the URL
    driver.get(url)
    
    # Save the rendered source code
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup


# open the Google spreadsheet and save all the sheets
gc = pygsheets.authorize(client_secret='./credentials/client_secret_martin.json')
sh = gc.open(f'Auditoria-SEO-{client_name}')

def get_audit_sheet(gc):
    sh = gc.open(f'Auditoria-SEO-{client_name}')
    return sh

# Get the title and update it
def seo_title(html, sheet, cell_number):
    # Get the Title Worksheet
    wks_titles = sheet.worksheet('title', 'Títulos')

    try:
        title = html.find('title').get_text()
        wks_titles.update_value(f'C{cell_number+2}', title)
        print(f'Title de la celda E{cell_number + 2} actualizado')
    except:
        wks_titles.update_value(f'C{cell_number+2}', '')
        print(f'Title de la celda E{cell_number + 2} actualizado')


# Get the meta description and update it
def seo_meta_description(html, sheet, cell_number):
    # Get the Meta-description Worksheet
    wks_desc = sheet.worksheet('title', 'Meta-description')

    try:
        meta_description = html.find('meta', {'name':'description'}).get('content')
        wks_desc.update_value(f'C{cell_number+2}', meta_description)
        print(f'Meta-description de la celda E{cell_number + 2} actualizada')
    except:
        wks_desc.update_value(f'C{cell_number+2}', '')
        print(f'Meta-description de la celda E{cell_number + 2} actualizada')


# Get the meta robots value, update it and evaluate.
def seo_noindex_tag(html, sheet, cell_number):
    # Get the Indexacion Worksheet
    wks_indexacion = sheet.worksheet('title', 'Indexación')

    meta_robots_tag = html.find('meta', {'name': 'robots'}).get('content').lower()

    if len(meta_robots_tag) > 0:
        if "noindex" in meta_robots_tag:
            wks_indexacion.update_value(f'C{cell_number+2}', 'No')
            wks_indexacion.update_value(f'D{cell_number+2}', 'Noindex')
        elif "index" in meta_robots_tag:
            wks_indexacion.update_value(f'C{cell_number+2}', 'Si')
            wks_indexacion.update_value(f'D{cell_number+2}', 'Sin bloqueo')
            print(f'Meta robots tag de la celda E{cell_number + 2} actualizada')
    else:
        wks_indexacion.update_value(f'C{cell_number + 2}', 'Si')
        wks_indexacion.update_value(f'D{cell_number + 2}', 'Sin bloqueo')
        print(f'Meta robots tag de la celda E{cell_number + 2} actualizada')

def seo_canonical_tag(html, sheet, cell_number):
    # Get the Canonical Worksheet
    wks_canonicals = sheet.worksheet('title', 'URL Canonicals')

    meta_canonical_tag = html.find('link', {'rel':'canonical'})['href']
    if len(meta_canonical_tag) > 0:
        wks_canonicals.update_value(f'C{cell_number+2}', 'Configurado')
        wks_canonicals.update_value(f'D{cell_number+2}', meta_canonical_tag)
        print(f'Canonical de la celda E{cell_number+2} actualizada')
    else:
        wks_canonicals.update_value(f'C{cell_number+2}', 'No Configurado')
        wks_canonicals.update_value(f'D{cell_number + 2}', '')
        print(f'Canonical de la celda E{cell_number+2} actualizada')

def seo_headings_tags(html, sheet, cell_number):
    # Get the headings Worksheet
    wks_headings = sheet.worksheet('title', 'Etiquetas H')

    h1_tags = html.find_all('h1')
    h2_tags = html.find_all('h2')
    h3_tags = html.find_all('h3')
    h4_tags = html.find_all('h4')
    h5_tags = html.find_all('h5')
    h6_tags = html.find_all('h6')

    h1_values = ''
    h2_values = ''

    for h in range(len(h1_tags)):
        h1 = h1_tags[h]
        h1_values += f'<H1>: {h1.text}\n'

    for j in range(len(h2_tags)):
        h2 = h2_tags[j]
        h2_values += f'<H2>: {h2.text}\n'

    if len(h1_tags) >= 1:
        wks_headings.update_value(f'D{cell_number+2}', h1_values)
        print(f'H1 de la celda D{cell_number + 2} actualizadas')
    elif len(h1_tags) == 0:
        wks_headings.update_value(f'D{cell_number + 2}', '')
        print(f'H1 de la celda D{cell_number + 2} actualizadas')

    if len(h2_tags) > 0:
        wks_headings.update_value(f'E{cell_number + 2}', h2_values)
        print(f'H2 de la celda E{cell_number + 2} actualizadas')
    elif len(h2_tags) == 0:
        wks_headings.update_value(f'E{cell_number + 2}', '')
        print(f'H2 de la celda D{cell_number + 2} actualizadas')

    wks_headings.update_value(f'C{cell_number+2}', f'H1 ({len(h1_tags)}), H2 ({len(h2_tags)}), H3 ({len(h3_tags)}), H4 ({len(h4_tags)}), H5 ({len(h5_tags)}), H6 ({len(h6_tags)})')



def run_meta_tags_test(urls_list, sheet):

    for i in range(len(urls_list)):
        # Render the current URL
        url = get_rendered_source_code(urls_list[i])

        # Get the title and update it
        seo_title(url, sheet, i)

        # Get the meta description and updated
        seo_meta_description(url, sheet, i)

        # Evaluate the meta_robots_tag
        seo_noindex_tag(url, sheet, i)

        # Evaluate the canonical tag
        seo_canonical_tag(url, sheet, i)

        # Update the H2 tags
        seo_headings_tags(url, sheet, i)