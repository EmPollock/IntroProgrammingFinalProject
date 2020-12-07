def readSaveFile(fileName):
    inZone = False
    inCutscene = False
    inEncounter = False
    inPlayerStats = False
    completedCutscenes = {}
    completedEncounters = {}
    playerStats = {}
    with open(fileName+".txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "<zone>":
                inZone = True
            elif line == "</zone>":
                inZone = False
            elif inZone == True:
                zone = line
            elif line == "<cutscenes>":
                inCutscene = True
                counter = 0
            elif line == "</cutscenes>":
                inCutscene = False
            elif inCutscene == True:
                if counter % 2 != 0:
                    completedCutscenes[key] = line
                else:                    
                    key = line
                counter += 1
            elif line == "<encounters>":
                inEncounter = True
                counter = 0
            elif line == "</encounters>":
                inEncounter = False
            elif inEncounter == True:
                if counter % 2 != 0:
                    completedEncounters[key] = line   
                else:
                    key = line
                counter += 1
            elif line == "<playerStats>":
                inPlayerStats = True
            elif line =="</playerStats>":
                inPlayerStats = False
            elif inPlayerStats == True:
                if line[:4] == "atk:":
                    playerStats["atk"] = int(line[5:])
                elif line[:4] == "def:":
                    playerStats["def"] = int(line[5:])
                elif line[:3] == "hp:":
                    playerStats["hp"] = int(line[4:])
    print(playerStats)
    return zone, completedCutscenes, completedEncounters, playerStats

playerTempStats = {}

zone, completedCutscenes, completedEncounters, playerStats = readSaveFile("Emma")
print(zone)
print(completedCutscenes)
print(completedEncounters)
print(playerStats)
for key in playerStats:
        playerTempStats[key] = playerStats[key]
print(playerTempStats)