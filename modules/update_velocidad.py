
def update_velocidad_mobile(data, wks_velocidad):
    """Update the speed_index on mobile devices to the audit google sheet document.

    Args:
        data (list): the result from get_urls. JSON response in a list format
        wks_velocidad (Worksheet): the Worksheet object to update.
    """

    for i in range(len(data)):

        speed_index = round(
            int(data[i][1]['data']['average']['firstView']['SpeedIndex']) / 1000, 1)

        wks_velocidad.update_value(f'C{i+2}', speed_index)

    print('Velocidad Mobile Acutalizado')


def update_velocidad_desktop(data, wks_velocidad):
    """Update the speed_index on desktop devices to the audit google sheet document.

    Args:
        data (list): the result from get_urls. JSON response in a list format
        wks_velocidad (Worksheet): the Worksheet object to update.
    """

    for i in range(len(data)):

        speed_index = round(
            int(data[i][1]['data']['average']['firstView']['SpeedIndex']) / 1000, 1)

        wks_velocidad.update_value(f'D{i+2}', speed_index)

    print('Velocidad Desktop Acutalizado')
