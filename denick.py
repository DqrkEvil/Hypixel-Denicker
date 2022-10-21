import time
import requests 
import ctypes
import colorama
import os

ctypes.windll.kernel32.SetConsoleTitleW("Dqrk Denicker - Made by DqrkEvil#5456")
colorama.init()

git_URL = 'https://github.com/DqrkEvil/Hypixel-Denicker/releases'
version = '1.2.0'

# gets the latest release version
def latest_version():
    from bs4 import BeautifulSoup
    
    data = requests.get(git_URL)

    soup = BeautifulSoup(data.content, 'html.parser')

    data = soup.find('div', id= 'repo-content-pjax-container')

    data = str(data.find('h2', class_='sr-only'))

    data = data.split('v')[-1]

    latest_version = data.split('<')[0]

    return latest_version

# update version
def update():
    import wget
    
    latest_download = (f'https://github.com/DqrkEvil/Hypixel-Denicker/releases/download/{latest_version()}/denick.exe')
    os.rename('denick.exe', 'denick_remove.exe')
    print('New version available')
    wget.download(latest_download)
    os.startfile('denick.exe')
    exit()

# denick loop
def main_loop():

    print(colorama.Fore.RED + "  _____             _      _____             _      _             ")
    print(" |  __ \           | |    |  __ \           (_)    | |            ")
    print(" | |  | | __ _ _ __| | __ | |  | | ___ _ __  _  ___| | _____ _ __ ")
    print(" | |  | |/ _` | '__| |/ / | |  | |/ _ \ '_ \| |/ __| |/ / _ \ '__|")
    print(" | |__| | (_| | |  |   <  | |__| |  __/ | | | | (__|   <  __/ |   ")
    print(" |_____/ \__, |_|  |_|\_\ |_____/ \___|_| |_|_|\___|_|\_\___|_|   ")
    print("            | |                                                   ")
    print("            |_|                                                   ")

    print ('\nCredits to antisniper.net for their API and denicker method.')
    while True: 
        IGN = input('\nNick you want to denick: ')

        time.sleep(1)

        try:
            APIoutput = requests.get(f"https://api.antisniper.net/denick?nick={IGN}&key=b846da83-ff45-49ff-9dab-8c74219b8e8b").json()
            print(f'Real IGN: {APIoutput["player"]["ign"]}')
            print(f'UUID: {APIoutput["player"]["uuid"]}')
            print(f'Latest Nick: {APIoutput["player"]["latest_nick"]}')
            
        except: 
            print('An error has occured, make sure this is a nick and that you spelled it correctly. Contact DqrkEvil#5456 if this happens repeatedly.')
            time.sleep(3)

        print ("\n----------------------------------------------------------------")

# main program
def main():

    if version != latest_version():
        update()
    
    elif version == latest_version():

        # deletes old file
        if os.path.isfile('denick_remove.exe'):
            time.sleep(3)
            os.remove('denick_remove.exe')
        
        main_loop()

# start
if __name__ == '__main__':
    main()
