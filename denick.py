import time
import requests 
import ctypes
import colorama

ctypes.windll.kernel32.SetConsoleTitleW("Dqrk Denicker - Made by DqrkEvil#5456")
colorama.init()

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
        APIoutput = requests.get(f"https://api.antisniper.net/denick?nick={IGN}&key=1083033b-2c49-4211-82dc-341e72fe1cfb").json()
        denicked = APIoutput["player"]["ign"]
        print('Real IGN:', denicked)
        print ("\n----------------------------------------------------------------")

    except: 
        print('An error has occured, make sure this is a nick and that you spelled it correctly. Contact DqrkEvil#5456 if this happens repeatedly.')
        time.sleep(10)
        break
