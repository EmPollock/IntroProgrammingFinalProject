from helpers import getNum
import random as rand
import time as t

playerStats = {"atk": 7, "def": 6, "hp": 16}


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
    with open(fileName, "r") as file:
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
    atStart = True
    enemyDefending = False
    playerDefending = False
    enemyStats, enemyDialog = readEncounter(fileName)
    playerTempStats = {}
    enemyTempStats = {}
    turn = 1
    fightPauseLen = 1
    printBreak = "_"*90
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
            input("Press Enter to retry: ")
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
                            if playerTempStats["atk"]-enemyTempStats["def"] > 0:
                                enemyTempStats["hp"] -= (playerTempStats["atk"]-enemyTempStats["def"])
                                print("They were defending!")
                                t.sleep(fightPauseLen)
                                print("-"+str(playerTempStats["atk"]-enemyTempStats["def"]))
                                t.sleep(fightPauseLen)
                            else:
                                print("They were defending!")
                                t.sleep(fightPauseLen)
                                print("-0")
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
                if choice <= 65:
                    print(enemyDialog["attemptStrike"])
                    t.sleep(fightPauseLen)
                    hitOrMiss = rand.randint(1,100)
                    if hitOrMiss <= 65:
                        print(enemyDialog["strike"]["success"])
                        t.sleep(fightPauseLen)
                        if playerDefending == False:
                            playerTempStats["hp"] -= enemyTempStats["atk"]
                            print("You weren't defending.")
                            t.sleep(fightPauseLen)
                            print("-"+ str(enemyTempStats["atk"]))
                            t.sleep(fightPauseLen)
                        else:
                            if enemyTempStats["atk"]-playerTempStats["def"] > 0:
                                playerTempStats["hp"] -= (enemyTempStats["atk"]-playerTempStats["def"])
                                print("You were defending!")
                                t.sleep(fightPauseLen)
                                print("-"+str(enemyTempStats["atk"]-playerTempStats["def"]))
                                t.sleep(fightPauseLen)
                            else:
                                print("You were defending!")
                                t.sleep(fightPauseLen)
                                print("-0")
                                t.sleep(fightPauseLen)
                    else:
                        print(enemyDialog["strike"]["fail"])
                        t.sleep(fightPauseLen)
                if choice > 65:
                    print(enemyDialog["defense"])
                    t.sleep(fightPauseLen)
                    enemyDefending = True
                playerDefending = False
                turn += 1


fight("encounters/encounter3Cave.txt", playerStats)
print(playerStats)