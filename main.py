import pyautogui
import time
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch

pyautogui.FAILSAFE = False

icoDiscord = './data/icoDS.png'
serverDiscord = './data/svDS.png'
canalDS = './data/canal.png'
mensajeDS = './data/mensaje.png'

def abrirApp():
    while True:
        pos = imagesearch(icoDiscord, precision=0.5)
        if not pos[0] == -1:
            pyautogui.leftClick(pos[0], pos[1])
            break

def abrirSV():
    while True:
        pos = imagesearch(serverDiscord, precision=0.5)
        if not pos[0] == -1:
            pyautogui.leftClick(pos[0], pos[1])
            break

def canal():
    while True:
        pos = imagesearch(canalDS, precision=0.7)
        if not pos[0] == -1:
            pyautogui.leftClick(pos[0], pos[1])
            break

def intTexto():
    while True:
        pos = imagesearch(mensajeDS, precision=0.5)
        if not pos[0] == -1:
            pyautogui.leftClick(pos[0], pos[1])
            break

def ingTexto():
    while True:
        pyautogui.write('!d bump')
        pyautogui.press('enter', presses=1)
        break

def main():
    print('Ejecutando...')
    discord = True
    abrirApp()
    abrirSV()
    canal()
    intTexto()
    ingTexto()
    time.sleep(7260)
    return main()


if __name__ == '__main__':
    main()

