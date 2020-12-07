from helpers import getNum
import random as rand
enemyStats = {}
inStats = False
inDialog = False
inStrike = False
inSuccess = False
inFail = False
inDefense = False
inDefeat = False
inWin = False
enemyDialog = {"startDialog": [],"strike":{} }

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

print(enemyStats)
print(enemyDialog)
print(enemyDialog["strike"]["success"])