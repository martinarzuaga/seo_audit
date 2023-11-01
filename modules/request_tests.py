import json
import requests
from modules.check_test_status import check_status_test

f = open('./configuracion.txt', 'r')

configuration = f.readlines()

client_name = configuration[0].replace('\n', '')
location = configuration[1].replace('\n', '')

location_options = ['Sao Paulo', 'Virginia', 'California', 'Paris']

if location == 'Sao Paulo':
    location_test = 'ec2-sa-east-1'
elif location == 'Virginia':
    location_test = 'ec2-us-east-1'
elif location == 'California':
    location_test = 'ec2-us-west-1'
elif location == 'Paris':
    location_test = 'ec2-eu-west-3'

# CREATE THE ENDPOINT

api_base_url = 'https://www.webpagetest.org/runtest.php?'

url_param = 'url='

api_param = 'k='

wpt_api_key_file = open('./wpt_api_key.txt', 'r')

wpt_api_key = wpt_api_key_file.readline()

format_param = 'f='

format_resp = 'json'

# 1 if is mobile, just don't add to the request_tests function
mobile = "mobile=1"

# Throttle CPU to slow the test machine.
throttle_cpu_value = 1

throttle_cpu = f"throttle_cpu={throttle_cpu_value}"

# See the correct location on
# https://www.webpagetest.org/getLocations.php?f=html

browser = "Chrome"

connectivity_mobile = "3GFast"

connectivity_desktop = "Cable"

scenario_mobile = f"location={location_test}.{connectivity_mobile}"

scenario_desktop = f"location={location_test}:{browser}.{connectivity_desktop}"

sep = '&'


def request_tests_mobile(urls):
    """
    Make tests from a list of urls on WebPageTest.

    :param urls: an array with the urls to request the test on WebPageTest.
    :return: a 2D array with the url and the data WebPageTest
    returns in a JSON format.
    """

    data = []

    for url in urls:

        endpoint = api_base_url + url_param + url + sep + \
            api_param + wpt_api_key + sep + \
            format_param + format_resp + sep + \
            scenario_mobile + sep + \
            mobile + throttle_cpu

        # Start the Test
        r = requests.get(endpoint)

        # Store the response text in a json dictionary
        url_requested = json.loads(r.text)['data']['jsonUrl']

        # Check the status test
        content = check_status_test(url_requested, url)

        data.append([url, content])

    return data
    # End the request_tests function


def request_tests_desktop(urls):
    """
    Make tests from a list of urls on WebPageTest.

    :param urls: an array with the urls to request the test on WebPageTest.
    :return: a 2D array with the url and the data WebPageTest
    returns in a JSON format.
    """

    data = []

    for url in urls:
        endpoint = api_base_url + url_param + url + sep + \
            api_param + wpt_api_key + sep + format_param + \
            format_resp + sep + scenario_desktop + sep + throttle_cpu

        # Start the Test
        r = requests.get(endpoint)

        # Store the response text in a json dictionary
        url_requested = json.loads(r.text)['data']['jsonUrl']

        # Check the status test
        content = check_status_test(url_requested, url)

        data.append([url, content])

    return data
    # End the request_tests function
