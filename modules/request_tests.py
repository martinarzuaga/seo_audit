from modules.create_endpoint import *
from modules.check_test_status import *


def request_tests_mobile(urls):
    """
    Make tests from a list of urls on WebPageTest.

    :param urls: an array with the urls to request the test on WebPageTest.
    :return: a 2D array with the url and the data WebPageTest returns in a JSON format.
    """

    data = []

    for url in urls:

        endpoint = api_base_url + url_param + url + sep + \
                   api_param + api_key + sep + format_param + format_resp + sep + scenario_mobile + sep + mobile + throttle_cpu

        ''' ------------------------
        MAKE THE REQUEST
        ------------------------ '''
        # Start the Test
        r = requests.get(endpoint)
        # Store the response text in a json dictionary
        url_requested = json.loads(r.text)['data']['jsonUrl']

        ''' -------------------------------
        CHECK THE STATUS OF THE TEST
        ------------------------------- '''
        content = check_status_test(url_requested, url)

        data.append([url, content])
    
    return data
    # End the request_tests function


def request_tests_desktop(urls):
    """
    Make tests from a list of urls on WebPageTest.

    :param urls: an array with the urls to request the test on WebPageTest.
    :return: a 2D array with the url and the data WebPageTest returns in a JSON format.
    """

    data = []

    for url in urls:
        endpoint = api_base_url + url_param + url + sep + \
                   api_param + api_key + sep + format_param + format_resp + sep + scenario_desktop + sep + throttle_cpu

        ''' ------------------------
        MAKE THE REQUEST
        ------------------------ '''
        # Start the Test
        r = requests.get(endpoint)
        # Store the response text in a json dictionary
        url_requested = json.loads(r.text)['data']['jsonUrl']

        ''' -------------------------------
        CHECK THE STATUS OF THE TEST
        ------------------------------- '''
        content = check_status_test(url_requested, url)

        data.append([url, content])

    return data
    # End the request_tests function