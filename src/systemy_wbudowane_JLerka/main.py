import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as ttk
import bluetooth


nearbyDevices = bluetooth.discover_devices(lookup_names=True)
label_list = []

#Control window
mainWindow=ttk.Window(themename='darkly')
mainWindow.title("Systemy Wbudowane robot app")
mainWindow.geometry("600x400")

def createBluetoothWindow():
    bluetoothWindow=ttk.Window() #Okno polaczenia do Bluetooth'a
    bluetoothWindow.title("Połączenie Bluetooth")
    bluetoothWindow.geometry("500x250")
    #new_label = ttk.Label(master=bluetoothWindow)
    #new_label.pack(pady=5)
    #label_list.append(new_label)
    for addr, name in nearbyDevices:
        label = ttk.Label("{} - {}\n".format(addr, name))
        label.pack(pady=5)
        label_list.append(label)


#def bluetoothButtonClick():
#    print("Przycisk wcisniety")
#    print("Znalazlem {} urzadzenia".format(len(nearbyDevices))) #Zwraca na konsole ilosc wykrytych urzadzen, baz nazw
#    for addr, name in nearbyDevices:
#        print("{} - {}\n".format(addr, name))
    #messagebox.showinfo("Test popup")
#    createBluetoothWindow()
    




#title
titleLabel=tk.Label(master=mainWindow, text="Robot controls",font='Calibri 24 bold')
titleLabel.pack()

#Bluetooth field
bluetoothFrame=ttk.Frame(master=mainWindow)
bluetoothLabel=tk.Label(master=bluetoothFrame, text="Connect to Bluetooth: ")
bluetoothButton =tk.Button(master=bluetoothFrame, text="Connect!", command=createBluetoothWindow)
bluetoothFrame.pack(pady=10)
bluetoothLabel.pack(side='left', padx=10)
bluetoothButton.pack(side='left')


#Arrows field
arrowsFrame=ttk.Frame(master=mainWindow)
upArrow=tk.PhotoImage(file = "src\\resources\\up-arrow-icon.png")
upArrow=upArrow.subsample(5, 5)

rightArrow=tk.PhotoImage(file = "src\\resources\\right-arrow-icon.png")
rightArrow=rightArrow.subsample(5, 5)

leftArrow=tk.PhotoImage(file = "src\\resources\\left-arrow-icon.png")
leftArrow=leftArrow.subsample(5, 5)

downArrow=tk.PhotoImage(file = "src\\resources\\down-arrow-icon.png")
downArrow=downArrow.subsample(5, 5)

arrowsFrame.pack(pady=20)

upButton=tk.Button(master=arrowsFrame, image=upArrow)
upButton.pack()

rightButton=tk.Button(master=arrowsFrame, image=rightArrow)
rightButton.pack(side='right', padx=5)

leftButton=tk.Button(master=arrowsFrame, image=leftArrow)
leftButton.pack(side='left', padx=5)

downButton=tk.Button(master=arrowsFrame, image=downArrow)
downButton.pack(side="bottom")



#mainloop() blokuje dzialanie skryptu, warto dodac wszystkie elementy itd. przed deklaracja mainloopa, nie wiem dokladnie jak z logika buttona...
mainWindow.mainloop()
