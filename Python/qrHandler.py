import qrcode
from tkinter import *

from pyngrok import ngrok


def showQR(window):
    window.title("Scan this QR in the app")
    window = Canvas(window, width=300, height=300)
    window.pack()

    qrImg = PhotoImage(file="qr.jpg")
    window.create_image(0, 0, anchor=NW, image=qrImg)
    window.mainloop()



def createQR(link):
    strL = (link.replace("http://", '')).replace(".ngrok.io", "")
    print("Shortened : ", strL)
    img = qrcode.make(strL)
    img.save("qr.jpg")
    showQR(window)


def startNgrok(port):
    url = ngrok.connect(port)
    print("Teeu > Full Url : ", url)
    print("Teeu > Tunnel Url : ", url.public_url)
    createQR((url.public_url))


window = Tk()

def remov():
    window.quit()

def init():
    startNgrok(7777)



init()
