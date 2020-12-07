playerStats = {"atk": 4, "def": 2, "hp": 15}
zone = "castle"
completedCutscenes = {"cutscene1":"incomplete", "cutscene2":"incomplete"}
completedEncounters = {"encounter1":"incomplete"}
saveFile = "Emma"

def saveProgress(fileName, zone, completedCutscenes, completedEncounters, playerStats, autoSave):
    if autoSave == True:
        print("Auto saving progress...")
    else:
        print("Saving progress...")
    with open(fileName+".txt", "w") as file:
        file.write("<zone>\n")
        file.write(zone+"\n")
        file.write("</zone>\n")
        file.write("<cutscenes>\n")
        for key in completedCutscenes:
            file.write(key+"\n")
            file.write(completedCutscenes[key]+"\n")
        file.write("</cutscenes>\n")
        file.write("<encounters>\n")
        for key in completedEncounters:
            file.write(key+"\n")
            file.write(completedEncounters[key]+"\n")
        file.write("</encounters>\n")
        file.write("<playerStats>\n")
        file.write("atk: "+str(playerStats["atk"])+"\n")
        file.write("def: "+str(playerStats["def"])+"\n")
        file.write("hp: "+str(playerStats["hp"])+"\n")
        file.write("</playerStats>\n")
    print("Finished saving.")

saveProgress(saveFile, zone, completedCutscenes, completedEncounters, playerStats, True)