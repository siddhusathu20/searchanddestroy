# By Siddharth Jai Gokulan

import customtkinter as ctk
from PIL import Image
import random

currentMap = 0
currentSol = "None"
mapCodes = {1:'catecode', 2:'doggycode', 3:'matrix'}
failCount = 0

caseAlphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
worDict = {
    'catecode':['after', 'once', 'buy', 'come', 'seven',
                'mind', 'computer', 'own', 'excellent', 'ace',
                'trick', 'throne', 'the', 'doctor', 'falls',
                'lava', 'them', 'noble', 'click', 'stone',
                'shack', 'rusty', 'pirate', 'vapour', 'trend'],
    'doggycode':['speck', 'hollow', 'evil', 'race', 'flank',
                 'shelter', 'bus', 'trap', 'decieve', 'laugh',
                 'voice', 'influx', 'cable', 'crank', 'train',
                 'see', 'refuse', 'control', 'lost', 'hope',
                 'love', 'pride', 'hate', 'fear', 'destruction',
                 'all', 'in', 'its', 'dark', 'eyes']
}

def doggycode() :
    global currentSol
    chosenWords = []
    for i in range(5) :
        index = random.randint(0, len(worDict['doggycode'])-1)
        chosenWords.append(worDict['doggycode'][index])
    toEncode = ""
    for i in chosenWords :
        toEncode = toEncode + i + ' '
    toEncode = toEncode[0:len(toEncode)-1]
    currentSol = toEncode
    print(currentSol)
    wordsToEncode = toEncode.split()
    encoded = ""
    encodedWord = ""
    for h in range(len(wordsToEncode)) :
        encodedWord = ""
        encodedWord += alphabets[h]
        for i in wordsToEncode[h] :
            if i in vowels :
                encodedWord = encodedWord + alphabets[vowels.index(i)-1] + "•"
            elif i in consonants :
                encodedWord = encodedWord + alphabets[consonants.index(i)+1] + "-"
            else :
                encodedWord += i
        encodedWord += alphabets[h+1]
        encoded = encoded + encodedWord + " "
    encoded.strip()
    return encoded

def catecode() :
    global currentSol
    chosenWords = []
    for i in range(5) :
        index = random.randint(0, len(worDict['catecode'])-1)
        chosenWords.append(worDict['catecode'][index])
    toEncode = ""
    for i in chosenWords :
        toEncode = toEncode + i + ' '
    toEncode = toEncode[0:len(toEncode)-1]
    currentSol = toEncode
    print(currentSol)
    encoded = ""
    for i in toEncode :
        if i in vowels :
            encoded = encoded + alphabets[vowels.index(i)] + "•"
        elif i in consonants :
            encoded = encoded + alphabets[consonants.index(i)] + "-"
        else :
            encoded += i
    return encoded

def matrix() :
    global currentSol
    toEncode = str(random.randint(10000000, 99999999))
    currentSol = toEncode
    print(currentSol)
    encoded = ""
    for i in range(8) :
        for j in range(8) :
            encoded += caseAlphabets[random.randint(0, 51)]
        encoded += "\n"
    encodedList = list(encoded)
    for k in range(8) :
        if k==0 :
            encodedList[9*k] = alphabets[int(toEncode[k])-1]
        else :
            encodedList[10*k] = alphabets[int(toEncode[k])-1]
    encoded = ""
    for l in encodedList :
        encoded += l
    return encoded

def advance(ans) :
    global currentMap
    global currentStatus
    global failCount
    if currentMap == 1 :
        if ans==currentSol :
            currentMap += 1
            currentStatus = f"{textList[currentMap]}" + doggycode()
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
        else :
            failCount += 1
            currentStatus += f"\n\n[{failCount}] ERROR: File does not match."
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
    elif currentMap == 2 :
        if ans==currentSol :
            currentMap += 1
            currentStatus = f"{textList[currentMap]}" + matrix()
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
        else :
            failCount += 1
            currentStatus += f"\n\n[{failCount}] ERROR: File does not match."
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
    elif currentMap == 3 :
        if str(ans)==str(currentSol) :
            currentMap += 1
            currentStatus = f"{textList[currentMap]}"
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
        else :
            failCount += 1
            currentStatus += f"\n\n[{failCount}] ERROR: File does not match."
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
    elif currentMap == 0 :
        currentMap += 1
        currentStatus = f"{textList[currentMap]}" + catecode()
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert(0.0, currentStatus)
        status.configure(state="disabled")

textList = [
    '''You are a detective and have to find details pertaining to a planned attack from some encrypted files in order to intercept the attack. Get to work!''',
    '''FILE 1
Available information:
The file is an encoded string of words with potential significance to the attack.
A decrypted file that uses the same ciphering or encryption algorithm notes that the word 'hello' is converted to 'f-b•i-i-d•'.
Data:\n''',
    '''FILE 2
Available information:
Similar to the last file, this file is an encoded string of words.
The ciphering algorithm is more complex this time, however. In this one, according to information obtained from a similar deciphered file, 'hello' is converted to 'ag-a•j-j-c•b'.
Data:\n''',
    f'''FILE 3
Available information:
This matrix hides an 8-digit code. Look in spots with equal row numbers and column numbers.
Data:\n''',
    '''ALL ASSIGNMENTS COMPLETE'''
]

currentStatus = f"{textList[currentMap]}"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("800x600")
root.title("Search and Destroy")
title = ctk.CTkLabel(master=root, text="<search and destroy>", font=("Consolas", 30))
title.place(relx=0.5, y=0.1, anchor=ctk.N)
status=ctk.CTkTextbox(master=root, width=600, height=350)
status.configure(state="normal")
status.delete(0.0, "end")
status.insert(0.0, currentStatus)
status.configure(state="disabled")
status.place(relx=0.5, rely=0.125, anchor=ctk.N)
choices = ctk.CTkFrame(master=root)
choices.place(relx=0.5, rely=0.85, anchor=ctk.N)
answer = ctk.CTkEntry(master=choices, placeholder_text="Enter solution here...")
answer.grid(row=0, column=0, padx=10, pady=10, sticky=ctk.NSEW)
next = ctk.CTkButton(master=choices, text="Next", command=lambda: advance(answer.get()))
next.grid(row=0, column=1, padx=10, pady=10, sticky=ctk.NSEW)

root.mainloop()
