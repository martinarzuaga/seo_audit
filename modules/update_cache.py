
def update_cache(data, wks_cache):
    """Update the Cache to the audit google sheet document.


    Args:
        data (list): the result from get_urls. JSON response in a list format
        wks_velocidad (Worksheet): the Worksheet object to update.
    """
    
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
    
    print('Cache Updated Successfully')
