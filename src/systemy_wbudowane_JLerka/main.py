from tkinter import *
from bluetooth import *


mainWindow=Tk()
mainWindow.title("Systemy Wbudowane robot app")
mainWindow.geometry("600x400")

newlabel=Label(text="Connect to Bluetooth: ")
bluetoothButton = Button(text="Connect!")
newlabel.grid(column=0,row=0)
bluetoothButton.grid(column=1,row=0)




#mainloop() blokuje dzialanie skryptu, warto dodac wszystkie elementy itd. przed deklaracja mainloopa, nie wiem dokladnie jak z logika buttona...
mainWindow.mainloop()