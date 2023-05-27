
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

""" ----------------------------------------------------------------

CREATE THE ENDPOINT

---------------------------------------------------------------- """

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

# See the correct location on https://www.webpagetest.org/getLocations.php?f=html

# location_test = "ec2-sa-east-1"

browser = "Chrome"

connectivity_mobile = "3GFast"

connectivity_desktop = "Cable"

scenario_mobile = f"location={location_test}.{connectivity_mobile}"

scenario_desktop = f"location={location_test}:{browser}.{connectivity_desktop}"

sep = '&'
