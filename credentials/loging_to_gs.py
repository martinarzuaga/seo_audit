import pygsheets as gs
import pathlib

credentials = './credentials/client_secret_dahseo.json'

# Authorization
def log_to_gs():
    # Authorization
    try:
        gc = gs.authorize(client_secret=credentials)
        print('Google Sheets Logged\n')
    except:
        print('Google Sheets TOKEN expired.\nRemoving the old token and creating a new one.')
        pathlib.Path('sheets.googleapis.com-python.json').unlink()
        gc = gs.authorize(client_secret=credentials)

    return gc