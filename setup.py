from modules import log


def getOS():
    log('[SETUP] What operating system are you running? Please, insert L for Linux and W for Windows.')
    OS = input().upper()
    if(OS not in ['L', 'W']):
        log('[SETUP] Insert L for Linux, and W for Windows.')
        return getOS()
    return OS




def getInfos():
    print(getOS())



getInfos()