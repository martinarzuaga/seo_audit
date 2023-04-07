import requests
import json
from modules.countdown import *

''' ----------------------------------------------------------------

CHECK THE STATUS TEST

---------------------------------------------------------------- '''


def check_status_test(url_req, url):

    # Request the url content
    r_json = requests.get(url_req)
    
    # Store the content in a json dictionary
    cont = json.loads(r_json.text)

    while 'Test Complete' not in cont.values():
        countdown(30, url)

        # Request the url content
        r_json = requests.get(url_req)

        # Store the content in a json dictionary
        cont = json.loads(r_json.text)

    return cont