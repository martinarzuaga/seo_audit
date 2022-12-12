import requests
import json
import base64
import modules.get_audit_urls as get_auditUrls

for i in get_auditUrls.wks_mobileFriendly.range('B2:B100'):
    
    row = i[0]
    
    endpoint = 'https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run'
    
    if 'http' in row.value:
        url_toTest = row.value
    else:
        break
    
    print(f'Empezando a analizar la URL: {url_toTest}.')
    
    params = {
        'url': url_toTest,
        'requestScreenshot': 'true',
        'key': 'AIzaSyAYCP7iSxwNwA9qqdLUZ9X2BpPtA1L0rUY'
    }
    
    x = requests.post(endpoint, data = params)
    data = json.loads(x.text)
    
    reference = get_auditUrls.wks_mobileFriendly.cell(f'A{row.row}')
    
    with open(f'./screenshots/screenshot-{reference.value}.png', 'wb') as fh:
        fh.write(base64.b64decode(data["screenshot"]["data"]))
    
    if data['mobileFriendliness'] == 'MOBILE_FRIENDLY':
        get_auditUrls.wks_mobileFriendly.update_value(f'C{row.row}', 'Bien')
    elif data['mobileFriendliness'] == 'NOT_MOBILE_FRIENDLY':
        get_auditUrls.wks_mobileFriendly.update_value(f'C{row.row}', 'Mal')
    else:
        get_auditUrls.wks_mobileFriendly.update_value(f'C{row.row}', 'N/A')
    
    print(f'URL: {url_toTest} analizada.')
    
