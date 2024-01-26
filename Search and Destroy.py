# By Siddharth Jai Gokulan

import customtkinter as ctk
import random

currentMap = 0
currentSol = "None"
codeCount = {1:5, 2:5, 3:8, 4:5, 5:5}
failCount = 0

caseAlphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
worDict =  ['after', 'once', 'buy', 'come', 'seven',
            'mind', 'computer', 'own', 'excellent', 'ace',
            'trick', 'throne', 'the', 'doctor', 'falls',
            'lava', 'them', 'noble', 'click', 'stone',
            'shack', 'rusty', 'pirate', 'vapour', 'trend',
            'speck', 'hollow', 'evil', 'race', 'flank',
            'shelter', 'bus', 'trap', 'decieve', 'laugh',
            'voice', 'influx', 'cable', 'crank', 'train',
            'see', 'refuse', 'control', 'lost', 'hope',
            'love', 'pride', 'hate', 'fear', 'destruction',
            'all', 'in', 'its', 'dark', 'eyes',
            'class', 'freak', 'blank', 'price', 'gauge',
            'quits', 'pints', 'brink', 'crux', 'efflux',
            'pachinko', 'card', 'graceful', 'landing', 'vessel',
            'broken', 'insane', 'ginger', 'beast', 'green',
            'physics', 'connection', 'resonance', 'person', 'home']

def catecode() :
    global currentSol
    global codeCount
    chosenWords = []
    for i in range(codeCount[1]) :
        index = random.randint(0, len(worDict)-1)
        chosenWords.append(worDict[index])
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
    codeCount[1]+=5
    return encoded

def doggycode() :
    global currentSol
    global codeCount
    chosenWords = []
    for i in range(codeCount[2]) :
        index = random.randint(0, len(worDict)-1)
        chosenWords.append(worDict[index])
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
    encoded = encoded[0:-1]
    if codeCount[2]==10 :
        encList = encoded.split(" ")
        random.shuffle(encList)
        encoded = ""
        for encodedWord in encList :
            encoded = encoded + encodedWord + " "
    codeCount[2]+=5
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

def penguincode() :
    global currentSol
    global codeCount
    chosenWords = []
    for i in range(codeCount[4]) :
        index = random.randint(0, len(worDict)-1)
        chosenWords.append(worDict[index])
    toEncode = ""
    for i in chosenWords :
        toEncode = toEncode + i + ' '
    toEncode = toEncode[0:len(toEncode)-1]
    currentSol = toEncode
    print(currentSol)
    encoded = ""
    for i in range(len(toEncode)) :
        if toEncode[i] in vowels :
            if i==0 or toEncode[i-1] not in consonants :
                vowelPosition = vowels.index(toEncode[i])+1
                encoded = encoded + "•"*vowelPosition + "() "
        elif toEncode[i] in consonants :
            consonantPosition = consonants.index(toEncode[i])+1
            if i < len(toEncode)-1 and toEncode[i+1] in vowels :
                vowelPosition = vowels.index(toEncode[i+1])+1
                encoded = encoded + "•"*vowelPosition + "(" + "•"*(consonantPosition//10) + ")" + str(consonantPosition%10) + " "
            else :
                encoded = encoded + "(" + "•"*(consonantPosition//10) + ")" + str(consonantPosition%10) + " "
        elif toEncode[i]== ' ' :
            encoded += '| '
        else :
            encoded += toEncode[i]
    codeCount[4]+=5
    return encoded

def antcode() :
    global currentSol
    global codeCount
    chosenWords = []
    for i in range(codeCount[5]) :
        index = random.randint(0, len(worDict)-1)
        chosenWords.append(worDict[index])
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
        if alphabets[h] in vowels :
            vowelPosition = vowels.index(alphabets[h])-1
            encodedWord = encodedWord + alphabets[vowelPosition] + "(z) "
        elif alphabets[h] in consonants :
            consonantPosition = consonants.index(alphabets[h])+1
            encodedWord = encodedWord + "(" + alphabets[consonantPosition//10-1] + ")" + alphabets[consonantPosition%10] + " "
        for i in range(len(wordsToEncode[h])) :
            if wordsToEncode[h][i] in vowels :
                if i==0 or wordsToEncode[h][i-1] not in consonants :
                    vowelPosition = vowels.index(wordsToEncode[h][i])-1
                    encodedWord = encodedWord + alphabets[vowelPosition] + "(z) "
            elif wordsToEncode[h][i] in consonants :
                consonantPosition = consonants.index(wordsToEncode[h][i])+1
                if i < len(wordsToEncode[h])-1 and wordsToEncode[h][i+1] in vowels :
                    vowelPosition = vowels.index(wordsToEncode[h][i+1])-1
                    encodedWord = encodedWord + alphabets[vowelPosition] + "(" + alphabets[consonantPosition//10-1] + ")" + alphabets[consonantPosition%10] + " "
                else :
                    encodedWord = encodedWord + "(" + alphabets[consonantPosition//10-1] + ")" + alphabets[consonantPosition%10] + " "
            else :
                encodedWord += wordsToEncode[h][i]
        if alphabets[h+1] in vowels :
            vowelPosition = vowels.index(alphabets[h+1])-1
            encodedWord = encodedWord + alphabets[vowelPosition] + "(z) "
        elif alphabets[h+1] in consonants :
            consonantPosition = consonants.index(alphabets[h+1])+1
            encodedWord = encodedWord + "(" + alphabets[consonantPosition//10-1] + ")" + alphabets[consonantPosition%10] + " "
        encoded = encoded + encodedWord + "| "
    encoded = encoded[0:-1]
    if codeCount[5]==10 :
        encList = encoded.split(" | ")
        random.shuffle(encList)
        encoded = ""
        for encodedWord in encList :
            encoded = encoded + encodedWord + " | "
    codeCount[5]+=5
    return encoded

def advance(ans) :
    global currentMap
    global currentStatus
    global failCount
    if currentMap == 0 :
        currentMap += 1
        currentStatus = f"FILE {currentMap}\n{textList[1]}" + catecode()
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert(0.0, currentStatus)
        status.configure(state="disabled")
    elif currentMap == 11 :
        currentStatus = currentStatus = f"{textList[6]}\nERROR COUNT: {failCount}"
    else :
        if ans==currentSol :
            currentMap += 1
            if currentMap == 11 :
                currentStatus = currentStatus = f"{textList[6]}\nERROR COUNT: {failCount}"
                chosenPuzzle = 0
            elif currentMap == 10 :
                chosenPuzzle = 5
            elif currentMap > 5 :
                chosenPuzzle = currentMap%5
            else :
                chosenPuzzle = currentMap
            if chosenPuzzle==5 :
                currentStatus = f"FILE {currentMap}\n{textList[5]}" + antcode()
            elif chosenPuzzle==4 :
                currentStatus = f"FILE {currentMap}\n{textList[4]}" + penguincode()
            elif chosenPuzzle==3 :
                currentStatus = f"FILE {currentMap}\n{textList[3]}" + matrix() + f"\n\nADDITIONAL NOTES: By comparing it with an older version of the file with weaker encryption, we have determined that the first and last digits are {currentSol[0]} and {currentSol[-1]}"
            elif chosenPuzzle==2 :
                currentStatus = f"FILE {currentMap}\n{textList[2]}" + doggycode()
            elif chosenPuzzle==1 :
                currentStatus = f"FILE {currentMap}\n{textList[1]}" + catecode()
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

textList = [
    '''You are a detective and have to find details pertaining to a planned attack from some encrypted files in order to intercept the attack. Get to work!''',
    f'''ENCRYPTION TYPE: catecode
Available information:
The file is an encoded string of words with potential significance to the attack.
A decrypted file that uses the same ciphering or encryption algorithm notes that the word \'hello\' is converted to \'f-b•i-i-d•\'.
Data:\n''',
    f'''ENCRYPTION TYPE: doggycode
Available information:
This file is an encoded string of words.
In this cipher, according to information obtained from a similar deciphered file, \'hello\' is converted to \'ag-a•j-j-c•b\' and \'the lone wolf\' is converted to \'aq-g-a•b bj-c•l-a•c cs-c•j-e-d\'.
Data:\n''',
    f'''ENCRYPTION TYPE: matrix
Available information:
This matrix hides an 8-digit code that may be of importance to the planned attack.
Data:\n''',
    f'''ENCRYPTION TYPE: penguincode
Available information:
This file is an encoded string of words. In this cipher, \'hello\' is converted to \'••()6 ()9 ••••()9\'.
Data:\n''',
    f'''ENCRYPTION TYPE: antcode
Available information:
This file is a string of words encoded in the most advanced cipher yet. In this cipher, \'hello\' is converted to \'z(z) a(z)g (a)z c(a)z (z)b\' and \'happy republic day\' is converted to \'z(z) z(z)g (a)c (a)c (b)b (z)b | (z)b a(a)e d(a)c (z)b b(z)j (z)c (z)c | (z)c z(z)d (b)b (z)d\'.
Data:\n''',
    f'''ALL ASSIGNMENTS COMPLETE'''
]

currentStatus = f"{textList[currentMap]}"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("800x600")
root.title("Search and Destroy")
title = ctk.CTkLabel(master=root, text="<search and destroy>", font=("Consolas", 30))
title.place(relx=0.5, y=0.1, anchor=ctk.N)
status=ctk.CTkTextbox(master=root, width=600, height=350, font=("Consolas", 13))
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
root.bind("<Return>", lambda ans: advance(answer.get()))

root.mainloop()
