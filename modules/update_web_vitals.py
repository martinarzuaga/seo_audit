
def update_web_vitals_mobile(mobile_data, wks_webVitals):
    """Update the Web Vitals data to the audit google sheet document.

    Args:
        data (list): the result from get_urls. JSON response in a list format
        wks_webVitals (Worksheet): the Worksheet object to update.
    """    
    
    for i in range(len(mobile_data)):
        
        lcp = round(int(mobile_data[i][1]['data']['average']['firstView']['chromeUserTiming.LargestContentfulPaint']) / 1000, 2)
        cls = round(float(mobile_data[i][1]['data']['average']['firstView']['chromeUserTiming.CumulativeLayoutShift']), 5)
        tbt = int(mobile_data[i][1]['data']['average']['firstView']['TotalBlockingTime'])
        
        wks_webVitals.update_value(f'C{i+2}', lcp)
        wks_webVitals.update_value(f'D{i+2}', cls)
        wks_webVitals.update_value(f'E{i+2}', tbt)
    
    print('Web Core Vitals Mobile Updated')
        


def update_web_vitals_desktop(desktop_data, wks_webVitals):
    """Update the Web Vitals data to the audit google sheet document.

    Args:
        data (list): the result from get_urls. JSON response in a list format
        wks_webVitals (Worksheet): the Worksheet object to update.
    """    
    
    for i in range(len(desktop_data)):
        
        lcp = round(int(desktop_data[i][1]['data']['average']['firstView']['chromeUserTiming.LargestContentfulPaint']) / 1000, 2)
        cls = round(float(desktop_data[i][1]['data']['average']['firstView']['chromeUserTiming.CumulativeLayoutShift']), 5)
        tbt = int(desktop_data[i][1]['data']['average']['firstView']['TotalBlockingTime'])
        
        wks_webVitals.update_value(f'G{i+2}', lcp)
        wks_webVitals.update_value(f'H{i+2}', cls)
        wks_webVitals.update_value(f'I{i+2}', tbt)

    print('Web Core Vitals Desktop Updated')
