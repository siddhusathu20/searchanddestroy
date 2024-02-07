# Search and Destroy
# Version 1.2.2.1
# This is the version I'm submitting as my school project. Thank you to everyone who's played upto this point!
# By Siddharth Jai Gokulan
# Check the project out on GitHub: https://github.com/siddhusathu20/searchanddestroy
# Please don't use my code without giving me credit!

import customtkinter as ctk # Tom Schimansky's customtkinter is used for the UI.
import random

currentMap = 0 # The file the player is currently on. The name 'currentMap' is a remnant of an older version of the game.
currentSol = "None" # The decoded version of the current file.
codeCount = {1:5, 2:5, 3:8, 4:5, 5:5, 6:10, 7:10, 8:8, 9:10, 10:10} # The number of words/numbers in the current file.
failCount = 0
giveUpCount = 0
currentGiveUpCount = 0

# I have different save files for the three counters only because it was the easiest way... I should definitely fix that someday, but I want to complete the save implementation as soon as possible.
try :
    save1 = open("sadsave1.txt", "r+") # Open existing save files.
    save1.seek(0)
    save2 = open("sadsave2.txt", "r+")
    save2.seek(0)
    failCount = int(save2.read())
    save3 = open("sadsave3.txt", "r+")
    save3.seek(0)
    giveUpCount = int(save3.read())
except :
    save1 = open("sadsave1.txt", "w+") # Create save files if they don't already exist.
    save1.write("1")
    save1.close()
    save1 = open("sadsave1.txt", "r+")
    save1.seek(0)
    save2 = open("sadsave2.txt", "w+")
    save2.write("0")
    save2.close()
    save2 = open("sadsave2.txt", "r+")
    save2.seek(0)
    save3 = open("sadsave3.txt", "w+")
    save3.write("0")
    save3.close()
    save3 = open("sadsave3.txt", "r+")
    save3.seek(0)

caseAlphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

# List of words
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

# Algorithm for catecode
# Each letter is represented by a pair of characters - a letter and a symbol.
# A dot (•) after the letter indicates that the represented letter is a vowel, whereas a hyphen (-) indicates that it is a consonant.
# The letter itself indicates the position of the represented letter in the list of vowels (a-e) or consonants (a-u).
def catecode() :
    global currentSol
    global codeCount
    chosenWords = []
    for i in range(codeCount[currentMap]) :
        index = random.randint(0, len(worDict)-1)
        chosenWords.append(worDict[index])
    toEncode = ""
    for i in chosenWords :
        toEncode = toEncode + i + ' '
    toEncode = toEncode[0:len(toEncode)-1]
    currentSol = toEncode
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

# Algorithm for doggycode
# Takes the catecode version of a word, then offsets every vowel pair one letter back and every consonant pair one letter forward.
# Adds letters at the start and end of a word that indicate the word's position in a sentence/sequence.
def doggycode() :
    global currentSol
    global codeCount
    chosenWords = []
    for i in range(codeCount[currentMap]) :
        index = random.randint(0, len(worDict)-1)
        chosenWords.append(worDict[index])
    toEncode = ""
    for i in chosenWords :
        toEncode = toEncode + i + ' '
    toEncode = toEncode[0:len(toEncode)-1]
    currentSol = toEncode
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
    if codeCount[currentMap]==10 :
        encList = encoded.split(" ")
        random.shuffle(encList)
        encoded = ""
        for encodedWord in encList :
            encoded = encoded + encodedWord + " "
    return encoded

# Algorithm for matrix
# The code is simply the positions of the letters in the diagonal from the top-left corner to the bottom-right corner.
def matrix() :
    global currentSol
    toEncode = str(random.randint(10000000, 99999999))
    currentSol = toEncode
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

# Algorithm for penguincode
# Words are split into vowel-consonant pairs (a consonant followed by a vowel) and separated by spaces.
# The number of dots to the left of the brackets indicates the position of the vowel (1-5:a-e).
# The number of dots inside the brackets indicates the tens place of the consonant's position.
# The number to the right of the brackets indicates the units place of the consonant's position.
# Spaces are indicated by the | symbol.
def penguincode() :
    global currentSol
    global codeCount
    chosenWords = []
    for i in range(codeCount[currentMap]) :
        index = random.randint(0, len(worDict)-1)
        chosenWords.append(worDict[index])
    toEncode = ""
    for i in chosenWords :
        toEncode = toEncode + i + ' '
    toEncode = toEncode[0:len(toEncode)-1]
    currentSol = toEncode
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
    return encoded

# Algorithm for antcode
# Takes the penguincode version of a word, converts the dots and numbers to letters whose position in the alphabet conveys the information the dots and numbers previously did.
# Offsets every vowel back one letter and every consonant forward one letter.
# Zero in the tens place is now indicated by 'z' rather than empty brackets.
def antcode() :
    global currentSol
    global codeCount
    chosenWords = []
    for i in range(codeCount[currentMap]) :
        index = random.randint(0, len(worDict)-1)
        chosenWords.append(worDict[index])
    toEncode = ""
    for i in chosenWords :
        toEncode = toEncode + i + ' '
    toEncode = toEncode[0:len(toEncode)-1]
    currentSol = toEncode
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
    if codeCount[currentMap]==10 :
        encList = encoded.split(" | ")
        random.shuffle(encList)
        encoded = ""
        for encodedWord in encList :
            encoded = encoded + encodedWord + " | "
    return encoded

# The function that checks your answers and decides whether to proceed to the next file.
def advance(ans) :
    global currentMap
    global currentStatus
    global failCount
    global giveUpCount
    global currentGiveUpCount
    # Clearing the save files.
    if currentMap == 0 and ans == "clear" :
        currentMap = 1
        save1.seek(0)
        save1.write("1")
        save1.truncate()
        save1.seek(0)
        save2.seek(0)
        save2.write("0")
        save2.truncate()
        save2.seek(0)
        save3.seek(0)
        save3.write("0")
        save3.truncate()
        save3.seek(0)
        currentStatus = f"FILE {currentMap}\n{textList[1]}" + catecode()
        status.configure(state="normal")
        status.delete(0.0, "end")
        status.insert(0.0, currentStatus)
        status.configure(state="disabled")
    # Starting the game
    elif currentMap == 0 :
        save1.seek(0)
        savedMap = save1.read()
        if savedMap == "1" :
            currentMap = 1
            currentStatus = f"FILE {currentMap}\n{textList[1]}" + catecode()
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
        else :
            currentMap = int(savedMap)-1
            advance("None")
    # Checking if the game is already completed.
    elif currentMap >= 11 :
        pass
    # Giving up.
    elif ans == "giveup" :
        if currentGiveUpCount == 0 :
            currentStatus += f"\n\nYOU GAVE UP.\nANSWER: {currentSol}\n{giveUpList[currentMap-1]}"
            status.configure(state="normal")
            status.delete(0.0, "end")
            status.insert(0.0, currentStatus)
            status.configure(state="disabled")
            giveUpCount += 1
            currentGiveUpCount += 1
    # Validating answers and proceeding to the next map.
    else :
        if ans==currentSol :
            currentMap += 1
            currentGiveUpCount = 0
            save1.seek(0)
            save1.write(f"{currentMap}")
            save1.truncate()
            save1.seek(0)
            if currentMap >= 11 :
                currentStatus = currentStatus = f"{textList[6]}\nERROR COUNT: {failCount}\nNUMBER OF TIMES YOU GAVE UP: {giveUpCount}\nCongratulations, and thank you for playing!\nCome back later for a new set of files! Try speedrunning the game!"
                chosenPuzzle = 0
                save1.seek(0)
                save1.write("1")
                save1.truncate()
                save1.seek(0)
                save2.seek(0)
                save2.write("0")
                save2.truncate()
                save2.seek(0)
                save3.seek(0)
                save3.write("0")
                save3.truncate()
                save3.seek(0)
                failCount = 0
                giveUpCount = 0
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
    '''WELCOME TO SEARCH AND DESTROY!\nYou are a detective and have to find details pertaining to a planned attack from some encrypted files in order to intercept the attack. Get to work!\n[Click Next to continue. Type \'clear\' to clear your save file.]\n[If you're stuck on a file, type \'giveup\' into the answer box. Note that this comes with consequences.]''',
    f'''ENCRYPTION TYPE: catecode
Available information:
The file is an encoded string of words with potential significance to the attack.
A decrypted file that uses the same ciphering or encryption algorithm notes that the word \'hello\' is converted to \'f-b•i-i-d•\'.
Enter the decoded data in the text box.
Data:\n''',
    f'''ENCRYPTION TYPE: doggycode
Available information:
This file is an encoded string of words.
In this cipher, according to information obtained from a similar deciphered file, \'hello\' is converted to \'ag-a•j-j-c•b\' and \'the lone wolf\' is converted to \'aq-g-a•b bj-c•l-a•c cs-c•j-e-d\'.
Enter the decoded data in the text box.
Data:\n''',
    f'''ENCRYPTION TYPE: matrix
Available information:
This matrix hides an 8-digit code that may be of importance to the planned attack.
Enter the decoded data in the text box.
Data:\n''',
    f'''ENCRYPTION TYPE: penguincode
Available information:
This file is an encoded string of words. In this cipher, \'hello\' is converted to \'••()6 ()9 ••••()9\'.
Enter the decoded data in the text box.
Data:\n''',
    f'''ENCRYPTION TYPE: antcode
Available information:
This file is a string of words encoded in the most advanced cipher yet. In this cipher, \'hello\' is converted to \'z(z) a(z)g (a)z c(a)z (z)b\' and \'happy republic day\' is converted to \'z(z) z(z)g (a)c (a)c (b)b (z)b | (z)b a(a)e d(a)c (z)b b(z)j (z)c (z)c | (z)c z(z)d (b)b (z)d\'.
Enter the decoded data in the text box.
Data:\n''',
    f'''ALL FILES DECODED'''
]

giveUpList = ["REALLY? ON THE FIRST FILE?",
              "I THOUGHT YOU WERE BETTER THAN THIS.",
              "WHO HIRED YOU AGAIN?",
              "IF YOU CAN'T DO THIS RIGHT NOW, MIGHT AS WELL GO GET SOME FRESH AIR.",
              "YOU KNOW WHAT? THIS TIME... I DON'T BLAME YOU.",
              "OH, COME ON, YOU'VE DONE THIS BEFORE!",
              "SO YOU DIDN'T LEARN A THING FROM FILE 2?",
              "YOU'VE GOT THIS FAR AND YOU COULDN'T DECIPHER THE SIMPLEST ONE?",
              "YOU'VE DONE THIS BEFORE, IT'S JUST LONGER THIS TIME!",
              "COME ON! RIGHT AT THE END? I THOUGHT YOU'D GO OUT WITH A BANG...",
              "SICK OF THE JOB, EH?"]

currentStatus = f"{textList[0]}"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("800x600")
root.title("Search and Destroy")
title = ctk.CTkLabel(master=root, text="<search and destroy>", font=("Consolas", 30)) # Title text
title.place(relx=0.5, y=0.1, anchor=ctk.N)
status=ctk.CTkTextbox(master=root, width=600, height=350, font=("Consolas", 13)) # Data textbox
status.configure(state="normal")
status.delete(0.0, "end")
status.insert(0.0, currentStatus)
status.configure(state="disabled")
status.place(relx=0.5, rely=0.125, anchor=ctk.N)
choices = ctk.CTkFrame(master=root)
choices.place(relx=0.5, rely=0.85, anchor=ctk.N)
answer = ctk.CTkEntry(master=choices, placeholder_text="Type here...") # Answer entry
answer.grid(row=0, column=0, padx=10, pady=10, sticky=ctk.NSEW)
next = ctk.CTkButton(master=choices, text="Next", command=lambda: advance(answer.get())) # Next button
next.grid(row=0, column=1, padx=10, pady=10, sticky=ctk.NSEW)
root.bind("<Return>", lambda ans: advance(answer.get())) # Binding the Enter key to the advance function

root.mainloop()
save2.seek(0)
save2.write(f"{failCount}")
save2.truncate()
save2.seek(0)
save3.seek(0)
save3.write(f"{giveUpCount}")
save3.truncate()
save3.seek(0)
save1.close()
save2.close()
save3.close()