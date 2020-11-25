import time as t
from helpers import getNum
import os

def printStartMenu():
    print("_"*90+"\n")
    print("1) Load existing save file")
    print("2) Create new save file")
    print("3) Delete a save file")
    print("_"*90)
    choice = getNum("Enter your choice:", 1, 3, float("inf"), True)
    print("_"*90)
    
    if choice == 1:
        saveFile = loadSaveFile()
        print("File loaded")
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

def main():
    printTitleScreen()
    printStartMenu()

main()