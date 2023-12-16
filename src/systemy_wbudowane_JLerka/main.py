import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as ttk
import bluetooth

index=0
nearbyDevices = bluetooth.discover_devices(lookup_names=True)
devicesDictionary={}

#Control window
mainWindow=ttk.Window(themename='darkly')
mainWindow.title("Systemy Wbudowane robot app")
mainWindow.geometry("600x400")

bd_addr = "F4:BC:DA:03:D4:CA"
           #E6:61:64:07:E3:06:5C:29 #In theory adres MAC karty sieciowej z tego robota.. kinda susge
server_sock= None
port=0

#Connection is to a client, not sure how to make the Raspberry as server honestly
def connectToDevice():
    global server_sock, port
    server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    port = bluetooth.get_available_port( bluetooth.RFCOMM )
    server_sock.connect((bd_addr, port))

#Adres MAC JBL Tune100BT - F4:BC:DA:03:D4:CA

def createBluetoothWindow():
    bluetoothWindow=ttk.Window(themename='darkly') #Okno polaczenia do Bluetooth'a
    bluetoothWindow.title("Połączenie Bluetooth")
    bluetoothWindow.geometry("500x250")
    #new_label = ttk.Label(master=bluetoothWindow)
    #new_label.pack(pady=5)
    #label_list.append(new_label)
    for address, name in nearbyDevices:
        devicesDictionary[index+1] = {"address":address, "name":name}
        labelButtonFrame = ttk.Frame(master=bluetoothWindow) #Frame do przetrzymywanie labela i buttona w pojedynczym wierszu
        labelButtonFrame.pack(side="top",pady=5)

        deviceLabel = ttk.Label(master=labelButtonFrame, text="{} - {} - {}".format(address, name, index))
        
        connectButton=ttk.Button(master=labelButtonFrame,text="Connect",command=connectToDevice)
        deviceLabel.pack(side='left',padx=5)
        connectButton.pack(side='left')


#def bluetoothButtonClick():
#    print("Przycisk wcisniety")
#    print("Znalazlem {} urzadzenia".format(len(nearbyDevices))) #Zwraca na konsole ilosc wykrytych urzadzen, baz nazw
#    for addr, name in nearbyDevices:
#        print("{} - {}\n".format(addr, name))
    #messagebox.showinfo("Test popup")
#    createBluetoothWindow()
    

#Data to send on buttons push



#title
titleLabel=tk.Label(master=mainWindow, text="Robot controls",font='Calibri 24 bold')
titleLabel.pack()

#Bluetooth field
bluetoothFrame=ttk.Frame(master=mainWindow)
bluetoothStatus=ttk.Label(master=bluetoothFrame, text="Connected: ")
bluetoothLabel=tk.Label(master=bluetoothFrame, text="Connect to Bluetooth: ")
bluetoothButton =tk.Button(master=bluetoothFrame, text="Connect!", command=createBluetoothWindow)
bluetoothFrame.pack(pady=10)
bluetoothLabel.pack(side='left', padx=10)
bluetoothStatus.pack(side="right",pady=2)
bluetoothButton.pack(side='left',padx=10)


#Arrows field
arrowsFrame=ttk.Frame(master=mainWindow)
upArrow=tk.PhotoImage(file = "src\\resources\\up-arrow-icon-white.png")
#upArrow=upArrow.subsample(5, 5)

rightArrow=tk.PhotoImage(file = "src\\resources\\right-arrow-icon-white.png")
#rightArrow=rightArrow.subsample(5, 5)

leftArrow=tk.PhotoImage(file = "src\\resources\\left-arrow-icon-white.png")
#leftArrow=leftArrow.subsample(5, 5)

downArrow=tk.PhotoImage(file = "src\\resources\\down-arrow-icon-white.png")
#downArrow=downArrow.subsample(5, 5)

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
