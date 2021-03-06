from helpers import getNum
import time as t
onQuestion = False
inChoice = False
numOfChoices = 0
choice = 0
textPauseLen = 3

with open("dialogs/cutscene4Forest.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line[:9] == "<cutscene":
            print()
        elif line == "question:":
            onQuestion = True
        elif line == "choiceQuestion:" and inChoice == True:
            onQuestion = True
        elif onQuestion == True:
            if line[:7] == "choice:":
                print (line[8:])
                numOfChoices += 1
                t.sleep(textPauseLen)
            elif numOfChoices > 0:
                choice = getNum("Enter your choice: ", 1, numOfChoices, float("inf"), True)
                onQuestion = False
                numOfChoices = 0                     
                print("_"*90)
        elif choice == 1:
            if inChoice == False:
                if line[:10] == "<choice 1>":
                    inChoice = True
                if line[:11] == "</choice 2>":
                    choice = 0
            elif line[:11] == "</choice 1>":
                inChoice = False
            else:
                print(line)
                t.sleep(textPauseLen)
        elif choice == 2:
            if inChoice == False:
                if line[:10] == "<choice 2>":
                    inChoice = True
            elif line[:11] == "</choice 2>":
                inChoice = False
                choice = 0
            else:
                print(line)
                t.sleep(textPauseLen)
        elif line == "_"*90 or line == "":
            print(line)
        elif line[:10] == "</cutscene":
            print("")
        else:
            print(line)
            t.sleep(textPauseLen)
        