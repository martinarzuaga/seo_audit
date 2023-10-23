import pygsheets as gs
import pathlib

credentials = './credentials/client_secret_dahseo.json'

# Authorization
def log_to_gs():
    # Authorization
    try:
<<<<<<< HEAD
        gs.authorize(client_secret='./credentials/client_secret.json')
=======
        gc = gs.authorize(client_secret=credentials)
>>>>>>> main
        print('Google Sheets Logged\n')
    except:
        print('Google Sheets TOKEN expired.\nRemoving the old token and creating a new one.')
        pathlib.Path('sheets.googleapis.com-python.json').unlink()
<<<<<<< HEAD
        gs.authorize(client_secret='./credentials/client_secret.json')
=======
        gc = gs.authorize(client_secret=credentials)

    return gc
>>>>>>> main
