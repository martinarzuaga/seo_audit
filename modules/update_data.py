from modules.request_tests import *
from modules.get_audit_urls import *


def update_velocidad(data):

    for i in range(len(data)):

        speed_index = round(int(data[i][1]['data']['average']
                            ['firstView']['SpeedIndex']) / 1000)

        sh.worksheet('title', 'Velocidad').update_value(f'C{i+2}', speed_index)


def update_cache(data):

    for i in range(len(data)):
        # Add KB first and repeat view to the spreadsheet
        kb_first_view = round(int(
            data[i][1]['data']['average']['firstView']['bytesIn']) / 1024)

        wks_cache.update_value(f'C{i + 2}', kb_first_view)

        kb_repeat_view = round(int(
            data[i][1]['data']['average']['repeatView']['bytesIn']) / 1024)

        wks_cache.update_value(f'D{i + 2}', kb_repeat_view)

        # Add REQUESTS first and repeat view to the spreadsheet
        requests_first_view = int(
            data[i][1]['data']['average']['firstView']['requestsFull'])

        wks_cache.update_value(f'F{i + 2}', requests_first_view)

        requests_repeat_view = int(
            data[i][1]['data']['average']['repeatView']['requestsFull'])

        wks_cache.update_value(f'G{i + 2}', requests_repeat_view)
