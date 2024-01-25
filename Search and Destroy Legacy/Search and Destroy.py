# By Siddharth Jai Gokulan

import customtkinter as ctk
from PIL import Image

currentMap = 0

decrypted = {
    1:"time",
    2:"7:54",
    3:"date",
    4:"15/5"
}

textList = [
    '''You are a detective and have to find the time and date of a planned attack from some encrypted files in order to intercept the attack. Get to work!''',
    '''FILE 1
Available information:
The required data is in the first line.
Line 4 is not encrypted, and can therefore be used as a reference to figure out the encryption algorithm.''',
    '''FILE 2
Available information:
Some of this data has already been decoded thanks to a vulnerability in a server exposing a partially decrypted version of the file. It appears to be an 8-character code:
_ 7 e _ _ 3 _ _
In the same server, and as part of the same file, this string of text was found:
[8]:[7][5]
This suggests that the information might be a timestamp.''',
    '''FILE 3
Available information:
Two of the three lines in this file are already decrypted - but the required information is in the third line.''',
    '''FILE 4
Available information:
This file seems to lack any kind of encryption - rather, the data is hidden in the figure.
A string of text found in the file's metadata reads:
[D]/[E]''',
    f'''DATA DECODED
{decrypted[1]}
{decrypted[2]}
{decrypted[3]}
{decrypted[4]}

You have succesfully found the required information.
ASSIGNMENT COMPLETE'''
]

def progress(answer) :
    global currentMap
    global status
    global currentStatus
    if currentMap == 0 :
        currentMap += 1
        currentStatus = f"{textList[currentMap]}"
        mapImage.configure(dark_image=Image.open(f"./map/map{currentMap}.png"))
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert(0.0, currentStatus)
        status.configure(state="disabled")
    elif currentMap == 4 :
        if answer==decrypted[currentMap] :
            currentStatus = f"{textList[5]}"
            mapImage.configure(dark_image=Image.open(f"./map/mapSolved.png"))
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
        choices.destroy()
    else :
        if answer==decrypted[currentMap] :
            currentMap += 1
            currentStatus = f"{textList[currentMap]}"
            mapImage.configure(dark_image=Image.open(f"./map/map{currentMap}.png"))
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
        else :
            currentStatus = f"{textList[currentMap]}\n\nDECRYPTION ERROR: Hash does not match"
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")

currentStatus = f"{textList[currentMap]}"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("800x600")
root.title("Search and Destroy")
title = ctk.CTkLabel(master=root, text="<search and destroy>", font=("Consolas", 30))
title.place(relx=0.5, y=0.1, anchor=ctk.N)
mapFrame = ctk.CTkFrame(master=root, width=250, height=250)
mapFrame.place(relx=0.5, rely=0.125, anchor=ctk.N)
mapImage = ctk.CTkImage(dark_image=Image.open(f"./map/mapMain.png"), size=(250, 250))
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
answer = ctk.CTkEntry(master=choices, placeholder_text="Enter solution here...")
answer.grid(row=0, column=0, padx=10, pady=10, sticky=ctk.NSEW)
next = ctk.CTkButton(master=choices, text="Next", command=lambda: progress(answer.get()))
next.grid(row=0, column=1, padx=10, pady=10, sticky=ctk.NSEW)

root.mainloop()
