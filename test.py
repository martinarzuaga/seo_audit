import urllib.request, json

psi_api_key = 'key=AIzaSyAYCP7iSxwNwA9qqdLUZ9X2BpPtA1L0rUY'

mobile_strategy = 'strategy=mobile'

desktop_strategy = 'strategy=desktop'

sep = '&'

locale = 'locale=en'

url_test_endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?'


def update_psi_desktop(urls, wks_pagespeed):

    for i in range(len(urls)):
        endpoint = url_test_endpoint + 'url=' + urls[i] + sep + mobile_strategy + sep + locale + sep + psi_api_key
        response = urllib.request.urlopen(endpoint)
        data = json.loads(response.read())
        overall_score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
        wks_pagespeed.update_value(f'C{i+2}', overall_score)


def update_psi_desktop(urls, wks_pagespeed):

    for i in range(len(urls)):
        endpoint = url_test_endpoint + 'url=' + urls[i] + sep + mobile_strategy + sep + locale + sep + psi_api_key
        response = urllib.request.urlopen(endpoint)
        data = json.loads(response.read())
        overall_score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
        wks_pagespeed.update_value(f'C{i+2}', overall_score)
