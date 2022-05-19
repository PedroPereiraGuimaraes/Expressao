
from tkinter import *
import cv2

def reproduzirVideo(nome):
    capture = cv2.VideoCapture(nome)


    while (capture.isOpened()):
        ret, frame = capture.read()

        if ret == True:
            cv2.imshow("Video", frame)
            if cv2.waitKey(23) & 0xFF == ord('q'):
                break
        else:
            break



root = Tk()
root.geometry('100x100')
btn = Button(root, text='Click me !', bd='5',
             command=lambda: reproduzirVideo('./videos/consoantes/b.mp4'))
btn.pack(side='top')

root.mainloop()