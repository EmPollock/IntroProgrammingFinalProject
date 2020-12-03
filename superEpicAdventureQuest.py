import time as t
from helpers import getNum
import os
import random as rand

textPauseLen = 3
printBreak = "_"*90

def printStartMenu():
    print("_"*90 + "\n")
    print("1) Load existing save file")
    print("2) Create new save file")
    print("3) Delete a save file")
    print("_"*90)
    choice = getNum("Enter your choice:", 1, 3, float("inf"), True)
    print("_"*90)
    
    if choice == 1:
        saveFile = loadSaveFile()
        print("File loaded")
        return saveFile
    if choice == 2:
        createSaveFile()
        print("File created")
        input("Press Enter to continue...")
        printStartMenu()       
    if choice == 3:
        deleteSaveFile()
        print("File deleted")
        input("Press Enter to continue...")
        printStartMenu()       

def loadSaveFile():
    while True:
        fileName = input("Enter the name of file your save file: ")   
        try:
            saveFile = open(fileName +".txt", "r")
            return saveFile
        except IOError:
            print("Could not find a save file named "+ fileName + ".")
            print("1) Try another name")
            print("2) Go back to start menu")
            choice = getNum("Enter your choice: ", 1, 2, float("inf"), True)
            print("_"*90)
        if choice == 2:
            printStartMenu()

def createSaveFile():
    fileName = input("Enter a name for your save file: ")
    try:
        saveFile = open(fileName + ".txt", "r")
    except IOError:
        saveFile = open(fileName + ".txt", "w")
        print("Save file created." + "\n" + "_"*90)
        return
    else:
        print("A file by that named " + fileName + " already exists.")
        print("Would you like to overwrite it?")
        print("1) Yes"+ " "*20 + "2) No")    
        choice = getNum("Enter your choice: ", 1, 2, float("inf"), True)
        if choice == 1:
            saveFile = open(fileName + ".txt", "w")
            print("Save file created." + "\n" + "_"*90)
        else:
            print("_"*90 + "\n Would you like to...")
            print("1) Create a file by a different name")
            print("2) Go back to the start menu")
            choice = getNum("Enter your choice: ", 1, 2, float("inf"), True)
            if choice == 1:
                createSaveFile()
            else:
                printStartMenu()
    finally:
        return

def deleteSaveFile():
    while True:
        fileName = input("Enter the name of the save file you want to delete: ")    
        if os.path.exists(fileName + ".txt"):
            os.remove(fileName + ".txt")
            return
        else:
            print("_"*90 + "\n Would you like to...")
            print("Could not find a save file by the name of " + fileName + ".")           
            print("1) Create a file by a different name")
            print("2) Go back to the start menu")
            choice = getNum("Enter your choice: ", 1, 2, float("inf"), True)
            if choice == 2:
                printStartMenu()

def printTitleScreen():
    print("\n"+' ' * 40 + "Welcome to...")
    t.sleep(1.25)
    """Ascii art from http://patorjk.com/software/taag/#p=display&f=Epic&t="""
    print(" _______           _______  _______  _______          _______  _______ _________ _______ ")
    print("(  ____ \\|\\     /|(  ____ )(  ____ \\(  ____ )        (  ____ \\(  ____ )\\__   __/(  ____ \\")
    print("| (    \\/| )   ( || (    )|| (    \\/| (    )|        | (    \\/| (    )|   ) (   | (    \\/")
    print("| (_____ | |   | || (____)|| (__    | (____)|        | (__    | (____)|   | |   | |      ")
    print("(_____  )| |   | ||  _____)|  __)   |     __)        |  __)   |  _____)   | |   | |      ")
    print("      ) || |   | || (      | (      | (\\ (           | (      | (         | |   | |      ")
    print("/\\____) || (___) || )      | (____/\\| ) \\ \\__        | (____/\\| )      ___) (___| (____/\\")
    print("\\_______)(_______)|/       (_______/|/   \\__/        (_______/|/       \\_______/(_______/"+"\n")
    t.sleep(1.25)
    print("     _______  ______            _______  _       _________          _______  _______     ")
    print("    (  ___  )(  __  \\ |\\     /|(  ____ \\( (    /|\\__   __/|\\     /|(  ____ )(  ____ \\    ")
    print("    | (   ) || (  \\  )| )   ( || (    \\/|  \\  ( |   ) (   | )   ( || (    )|| (    \\/    ")
    print("    | (___) || |   ) || |   | || (__    |   \\ | |   | |   | |   | || (____)|| (__        ")
    print("    |  ___  || |   | |( (   ) )|  __)   | (\\ \\) |   | |   | |   | ||     __)|  __)       ")
    print("    | (   ) || |   ) | \\ \\_/ / | (      | | \\   |   | |   | |   | || (\\ (   | (          ")
    print("    | )   ( || (__/  )  \\   /  | (____/\\| )  \\  |   | |   | (___) || ) \\ \\__| (____/\\    ")
    print("    |/     \\|(______/    \\_/   (_______/|/    )_)   )_(   (_______)|/   \\__/(_______/    " +"\n")
    t.sleep(1.25)
    print("                       _______           _______  _______ _________                      ")
    print("                      (  ___  )|\\     /|(  ____ \\(  ____ \\\\__   __/                      ")
    print("                      | (   ) || )   ( || (    \\/| (    \\/   ) (                         ")
    print("                      | |   | || |   | || (__    | (_____    | |                         ")
    print("                      | |   | || |   | ||  __)   (_____  )   | |                         ")
    print("                      | | /\\| || |   | || (            ) |   | |                         ")
    print("                      | (_\\ \\ || (___) || (____/\\/\\____) |   | |                         ")
    print("                      (____\\/_)(_______)(_______/\\_______)   )_(                         " + "\n")
    t.sleep(1.25)
    input("Press ENTER to continue...")

def readDialog(fileName):
    onQuestion = False
    inChoice = False
    numOfChoices = 0
    choice = 0
    with open(fileName, "r") as file:
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
                    t.sleep(textPauseLen*.5)
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
                print()
            else:
                print(line)
                t.sleep(textPauseLen)

#Add readSaveFile function

#Add saveProgress function

def readEncounter(fileName):
    enemyStats = {}
    inStats = False
    inDialog = False
    inStrike = False
    inSuccess = False
    inFail = False
    inDefense = False
    inDefeat = False
    inWin = False
    enemyDialog = {"startDialog": [],"strike":{}, "defend":{}}
    with open("encounters/castleEncounter.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "<stats>":
                inStats = True
            elif inStats == True:
                if line[:3] == "atk":
                    enemyStats["atk"] = int(line[5:])
                elif line[:3] == "def":
                    enemyStats["def"] = int(line[5:])
                elif line[:2] == "hp":
                    enemyStats["hp"] = int(line[4:])
                elif line == "</stats>":
                    inStats = False
            elif line == "<dialog>":
                inDialog = True
            elif line == "</dialog>":
                inDialog = False
            elif inDialog == True:
                enemyDialog["startDialog"].append(line)        
            elif line == "<strike>":
                inStrike = True
            elif line == "</strike>":
                inStrike = False
            elif inStrike == True:
                if line == "<success>":
                    inSuccess = True
                elif line == "</success>":
                    inSuccess = False
                elif inSuccess == True:
                    enemyDialog["strike"]["success"] = line
                elif line == "<fail>":
                    inFail = True
                elif line == "</fail>":
                    inFail = False
                elif inFail == True:
                    enemyDialog["strike"]["fail"] = line
                else:
                    enemyDialog["attemptStrike"] = line
            elif line == "<defense>":
                inDefense = True
            elif line == "</defense>":
                inDefense = False
            elif inDefense == True:
                enemyDialog["defense"] = line
            elif line == "<eDefeat>":
                inDefeat = True
            elif line == "</eDefeat>":
                inDefeat = False
            elif inDefeat == True:
                enemyDialog["defeat"] = line
            elif line == "<eWin>":
                inWin = True
            elif line == "</eWin>":
                inWin = False
            elif inWin == True:
                enemyDialog["win"] = line
    return enemyStats, enemyDialog

def fight(fileName, playerStats):
    won = False
    fightPauseLen = 1
    atStart = True
    enemyDefending = False
    playerDefending = False
    enemyStats, enemyDialog = readEncounter(fileName)
    playerTempStats = {}
    enemyTempStats = {}
    turn = 1

    for key in playerStats:
        playerTempStats[key] = playerStats[key]
    for key in enemyStats:
        enemyTempStats[key] = enemyStats[key]
    
    while won == False:
        if atStart == True:
            for line in enemyDialog["startDialog"]:
                print(line)
                t.sleep(fightPauseLen)
            hitOrMiss = rand.randint(1,100)
            if hitOrMiss <= 75:
                print(enemyDialog["strike"]["success"])
                t.sleep(fightPauseLen)
                if playerDefending == False:
                    playerTempStats["hp"] -= enemyTempStats["atk"]
                    print("You weren't defending.")
                    t.sleep(fightPauseLen)
                    print("-"+ str(enemyTempStats["atk"]))
                    t.sleep(fightPauseLen)
                else:
                    playerTempStats["hp"] -= (enemyTempStats["atk"]-playerTempStats["def"])
                    print("You were defending!")
                    t.sleep(fightPauseLen)
                    print("-"+str(enemyTempStats["atk"]-playerTempStats["def"]))
                    t.sleep(fightPauseLen)
            else:
                print(enemyDialog["strike"]["fail"])
                t.sleep(fightPauseLen)
            atStart = False

        if playerTempStats["hp"] <= 0:
            print(enemyDialog["win"])
            for key in playerStats:
                playerTempStats[key] = playerStats[key]
            for key in enemyStats:
                enemyTempStats[key] = enemyStats[key]
            t.sleep(4)
            print(printBreak)
            atStart = True
        elif enemyTempStats["hp"] <= 0:
            print(enemyDialog["defeat"])
            t.sleep(fightPauseLen)
            playerStats["atk"] += 1
            playerStats["def"] += 1
            playerStats["hp"] += 1
            print("You gained 1 attack point")
            t.sleep(fightPauseLen)
            print("You gained 1 defense point")
            t.sleep(fightPauseLen)
            print("You gained 1 health point")
            t.sleep(fightPauseLen)
            return playerStats
        else:
            if turn % 2 != 0:
                #player turn
                print("Enemy Stats: Atk:"+str(enemyTempStats["atk"])+ " Def:"+str(enemyTempStats["def"])+ " hp:"+str(enemyTempStats["hp"])+"/"+str(enemyStats["hp"]))
                print("Your Stats: Atk:"+str(playerTempStats["atk"])+ " Def:"+str(playerTempStats["def"])+ " hp:"+str(playerTempStats["hp"])+"/"+str(playerStats["hp"]))
                t.sleep(fightPauseLen)
                print("What do you do?")
                t.sleep(fightPauseLen)
                print(printBreak + "\n")
                print("1) Attack")
                print("2) Defend")
                choice = getNum("Enter your choice: ",1,2,float("inf"),True)
                if choice == 1:
                    print("You slice at your opponent with your sword!")
                    t.sleep(fightPauseLen)
                    hitOrMiss = rand.randint(1,100)
                    if hitOrMiss <= 75:
                        print("You successfully hit your opponent!")
                        t.sleep(fightPauseLen)
                        if enemyDefending == False:
                            enemyTempStats["hp"] -= playerTempStats["atk"]
                            print("They weren't defending!")
                            t.sleep(fightPauseLen)
                            print("-"+ str(playerTempStats["atk"]))
                            t.sleep(fightPauseLen)
                        else:
                            enemyTempStats["hp"] -= (playerTempStats["atk"]-enemyTempStats["def"])
                            print("They were defending!")
                            t.sleep(fightPauseLen)
                            print("-"+str(playerTempStats["atk"]-enemyTempStats["def"]))
                            t.sleep(fightPauseLen)
                    else:
                        print("You missed.")
                        t.sleep(fightPauseLen)
                if choice == 2:
                    print("You brace yourself for an attack!")
                    t.sleep(fightPauseLen)
                    playerDefending = True
                enemyDefending = False
                turn += 1
            else:
                #enemy turn
                print(printBreak +"\n")
                choice = rand.randint(1, 100)
                if choice <= 75:
                    print(enemyDialog["attemptStrike"])
                    t.sleep(fightPauseLen)
                    hitOrMiss = rand.randint(1,100)
                    if hitOrMiss <= 75:
                        print(enemyDialog["strike"]["success"])
                        t.sleep(fightPauseLen)
                        if playerDefending == False:
                            playerTempStats["hp"] -= enemyTempStats["atk"]
                            print("You weren't defending.")
                            t.sleep(fightPauseLen)
                            print("-"+ str(enemyTempStats["atk"]))
                            t.sleep(fightPauseLen)
                        else:
                            playerTempStats["hp"] -= (enemyTempStats["atk"]-playerTempStats["def"])
                            print("You were defending!")
                            t.sleep(fightPauseLen)
                            print("-"+str(enemyTempStats["atk"]-playerTempStats["def"]))
                            t.sleep(fightPauseLen)
                    else:
                        print(enemyDialog["strike"]["fail"])
                        t.sleep(fightPauseLen)
                if choice > 75:
                    print(enemyDialog["defense"])
                    t.sleep(fightPauseLen)
                    enemyDefending = True
                playerDefending = False
                turn += 1

def main():        
    playerStats = {"atk": 4, "def": 2, "hp": 15}
    zone = "castle"
    completedCutscenes = {"cutscene1":"incomplete", "cutscene2":"incomplete"}
    completedEncounters = {"encounter1":"incomplete"}
    
    printTitleScreen()
    saveFile = printStartMenu()
    if zone == "castle":
        if completedCutscenes["cutscene1"] == "incomplete":
            readDialog("dialogs/cutscene1Castle.txt")
            completedCutscenes["cutscene1"] = "complete"
        if completedCutscenes["cutscene1"] == "complete" and completedEncounters["encounter1"] == "incomplete":
            playerStats = fight("castleEncounter.txt", playerStats)
            completedEncounters["encounter1"] = "complete"

main()