import time

def countdown(sec, url):
    
    while sec:
        mins, secs = divmod(sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        sec -= 1

    print(f'Analizando {url}')
