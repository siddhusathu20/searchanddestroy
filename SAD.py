# By Siddharth Jai Gokulan

import customtkinter as ctk
from PIL import Image

currentMap = 1
mazePath = ''
correctPath = 'LLRRRLRRLLLRLRL'
timer = 60

textList = [
    '''What are you doing in my code?''',
    '''You have been given orders to investigate a research facility and find and destroy a lethal secret weapon.''',
    '''You find yourself at a lift that can go up or down, with a few bloodstains on the floor. The up button has a faint bloodstain on it.''',
    f'''You ride the lift down and emerge in a room that looks like a maze.
There's a sign at the entrance that reads: \'{correctPath}\'.
You step into the entrance and an alarm goes off. A voice on a loudspeaker says \'Detonation in sixty seconds.\'
You have to make it out of the maze alive before it blows up.''',
    '''You have to make it out of the maze alive before it blows up.''',
    '''You\'re walking down a hall, when you see a guard point a pistol at you. He says \'You will not interfere. You shall be silenced.\'.'''
]

choiceList = [
    ("You're not supposed to see this", "Don't steal my code!"),
    ("Go forward", "'I'm not paid enough for this!'"),
    ("Go up", "Go down"),
    ("Left", "Right"),
    ("Run past him", "Surrender")
]

gameOverList = [
    '''GAME OVER
You aborted the mission.''',
    '''GAME OVER
The bloodstain was a warning...
You found a failed \'experiment\' that injured you too badly to continue the mission.
You retreated to seek medical attention.''',
    '''GAME OVER
You broke your fist.
And you're not the Doctor.''',
    '''GAME OVER
You didn't make it out of the maze in time.''',
    '''GAME OVER
You got lost in the maze.''',
    '''GAME OVER
You got shot.''',
    '''GAME OVER
You surrendered.'''
]

def useItem(item) :
    global inventory
    global status
    global currentStatus
    global currentMap
    if inventory[item] > 1 :
        inventory[item] -= 1
        currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}"
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert(0.0, currentStatus)
        status.configure(state="disabled")
    elif item=='Fist' :
        mapImage.configure(dark_image=Image.open(f"./map/go{currentMap}.png"))
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert("end", f"{gameOverList[2]}")
        status.configure(state="disabled")
        if currentMap == 5 :
            currentMap += 1
            currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}"
            mapImage.configure(dark_image=Image.open(f"./map/map{currentMap}.png"))
            choice1.configure(text=choiceList[currentMap][0])
            choice2.configure(text=choiceList[currentMap][1])
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
    elif inventory[item] == 1 :
        inventory[item] == 'Broken'
        currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}"
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert(0.0, currentStatus)
        status.configure(state="disabled")

def timeUpdate() :
    global timer
    global currentMap
    if timer > 0 and len(mazePath)!=len(correctPath) :
        timer -= 1
        currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}\nPATH: {mazePath}\nSECONDS TO DETONATION: {timer}"
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert(0.0, currentStatus)
        status.configure(state="disabled")
        root.after(1000, timeUpdate)
    elif len(mazePath)==len(correctPath) and mazePath!=correctPath :
        mapImage.configure(dark_image=Image.open("./map/go3.png"))
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert(0.0, f"{gameOverList[4]}")
        status.configure(state="disabled")
    else :
        mapImage.configure(dark_image=Image.open("./map/go3.png"))
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert(0.0, f"{gameOverList[3]}")
        status.configure(state="disabled")

def progress(choice) :
    global currentMap
    global status
    global currentStatus
    global mazePath
    global correctPath
    global timer
    if currentMap == 1 :
        if choice=='2' :
            mapImage.configure(dark_image=Image.open("./map/go1.png"))
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, f"{gameOverList[0]}")
            status.configure(state="disabled")
            currentMap = 1
        else :
            currentMap += 1
            currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}"
            mapImage.configure(dark_image=Image.open(f"./map/map{currentMap}.png"))
            choice1.configure(text=choiceList[currentMap][0])
            choice2.configure(text=choiceList[currentMap][1])
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
    elif currentMap == 2 :
        if choice=='1' :
            mapImage.configure(dark_image=Image.open("./map/go2.png"))
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, f"{gameOverList[1]}")
            status.configure(state="disabled")
            currentMap = 1
        else :
            currentMap += 1
            currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}"
            mapImage.configure(dark_image=Image.open(f"./map/map{currentMap}.png"))
            choice1.configure(text=choiceList[currentMap][0])
            choice2.configure(text=choiceList[currentMap][1])
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
            root.after(1000, timeUpdate)
    elif currentMap == 3 :
        if choice=='1' :
            currentMap += 1
            mazePath += 'L'
            currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}\nPATH: {mazePath}\nSECONDS TO DETONATION: {timer}"
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
        else :
            currentMap += 1
            mazePath += 'R'
            currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}\nPATH: {mazePath}\nSECONDS TO DETONATION: {timer}"
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
    elif currentMap == 4 :
        if choice=='1' :
            mazePath += 'L'
            currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}\nPATH: {mazePath}\nSECONDS TO DETONATION: {timer}"
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
        else :
            mazePath += 'R'
            currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}\nPATH: {mazePath}\nSECONDS TO DETONATION: {timer}"
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
        if len(mazePath) == len(correctPath) :
            if mazePath == correctPath :
                currentMap += 1
                currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}"
                mapImage.configure(dark_image=Image.open(f"./map/map{currentMap}.png"))
                choice1.configure(text=choiceList[currentMap][0])
                choice2.configure(text=choiceList[currentMap][1])
                status.configure(state="normal")
                status.delete(0.0, "end")
                status.insert(0.0, currentStatus)
                status.configure(state="disabled")
            else :
                mapImage.configure(dark_image=Image.open("./map/go3.png"))
                status.configure(state="normal")
                status.delete(0.0, "end")
                status.insert(0.0, f"{gameOverList[4]}")
                status.configure(state="disabled")
                currentMap = 1
    elif currentMap == 5 :
        if choice == 1 :
            mapImage.configure(dark_image=Image.open("./map/go5.png"))
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, f"{gameOverList[5]}")
            status.configure(state="disabled")
            currentMap = 1
        elif choice == 2 :
            mapImage.configure(dark_image=Image.open("./map/go5.png"))
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, f"{gameOverList[6]}")
            status.configure(state="disabled")
            currentMap = 1

inventory = {"Fist":10}

currentStatus = f"{textList[currentMap]}\nINVENTORY: {inventory}"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("640x480")
root.title("Search and Destroy")
title = ctk.CTkLabel(master=root, text="<search and destroy>", font=("Consolas", 30))
title.place(relx=0.5, y=0.1, anchor=ctk.N)
mapFrame = ctk.CTkFrame(master=root)
mapFrame.place(relx=0.5, rely=0.125, anchor=ctk.N)
mapImage = ctk.CTkImage(dark_image=Image.open(f"./map/map1.png"), size=(200, 200))
map = ctk.CTkLabel(master=mapFrame, text="", image=mapImage)
map.place(relx=0.5, y=0.5, anchor=ctk.N)
status=ctk.CTkTextbox(master=root, width=600, height=100)
status.configure(state="normal")
status.delete(0.0, "end")
status.insert(0.0, currentStatus)
status.configure(state="disabled")
status.place(relx=0.5, rely=0.6, anchor=ctk.N)
choices = ctk.CTkFrame(master=root)
choices.place(relx=0.5, rely=0.85, anchor=ctk.N)
choice1 = ctk.CTkButton(master=choices, text=choiceList[currentMap][0], command=lambda: progress('1'))
choice1.grid(row=0, column=0, sticky=ctk.NSEW, padx=5)
choice2 = ctk.CTkButton(master=choices, text=choiceList[currentMap][1], command=lambda: progress('2'))
choice2.grid(row=0, column=1, sticky=ctk.NSEW, padx=5)
inv = ctk.CTkOptionMenu(master=choices, values=list(inventory.keys()), command=useItem)
inv.grid(row=0, column=2, sticky=ctk.NSEW, padx=5)
inv.set("Use item...")

root.mainloop()
