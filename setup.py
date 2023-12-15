from modules import log
from requests import get
config = dict()

def getOS():
    OS = input('\n--> ').upper()
    if(OS not in ['L', 'W']):
        log('[SETUP] Insert L for Linux, and W for Windows.')
        return getOS()
    return OS

def setTelegram():
    log('[SETUP] Insert your Telegram BOT API. Make sure it is correct before you proceed.')
    TelegramAPI = input('\n--> ')
    return TelegramAPI

def getChatID(API):
    log('[SETUP] Start a conversation with your bot by clicking Start.')
    log(f'The program will temporarily stop until you start a conversation with the bot with this API:{API}. Click Enter if that has already been done.')
    input()
    try:
        return get(f'https://api.telegram.org/bot{API}/getUpdates').json()['result'][0]['message']['chat']['id']
    except:
        return getChatID(API)


def getInfos():
    log('[SETUP] What operating system are you running? Please, insert L for Linux and W for Windows.')
    config['OS'] = getOS()
    config['TelegramAPI'] = setTelegram()
    config['chatID'] = getChatID(config['TelegramAPI'])
    with open('config.py', 'w') as configpy:
        configpy.write(f'config = {str(config)}')


getInfos()