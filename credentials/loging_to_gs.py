import pygsheets as gs
import pathlib

# Authorization
def log_to_gs():
    # Authorization
    try:
        gs.authorize(client_secret='./credentials/client_secret.json')
        print('Google Sheets Logged\n')
    except:
        print('Google Sheets TOKEN expired.\nRemoving the old token and creating a new one.')
        pathlib.Path('sheets.googleapis.com-python.json').unlink()
        gs.authorize(client_secret='./credentials/client_secret.json')