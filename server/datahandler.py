from guest import Guest
import time
import machine


class DataHandler:
    def loadCSV(self):
        csvFile = open(self.filename, 'r')
        lines = csvFile.readlines()
        for line in lines:
            if line.startswith('#'):
                print("Comment, skipping....")
            else:
                # Nick;CardID;AlcAllowed;numberOfWater;numberOfSoftdrinks;numberOfBeer;numberOfCider;numberOfLongdrink;numberOfShot;numberOfCocktails
                elements = line.split(';')
                print(elements[0])
                self.guestList.append(
                    Guest(elements[0], elements[1], elements[2], int(elements[3]), int(elements[4]), int(elements[5]),
                          int(elements[6]), int(elements[7]), int(elements[8]), int(elements[9])))
        csvFile.close()

    def __init__(self, filename):
        self.guestList = []
        self.filename = filename
        self.loadCSV()
        self.userCount = len(self.guestList)

    def writeLog(self, action, state):
        logger = open("log.txt", 'a')
        logger.write(action + " -> " + state + "\n")
        logger.close()

    def writeCSV(self):
        for element in self.guestList:
            csvFile = open(self.filename, 'w')
            csvFile.write(
                "# Nick;CardID;AlcAllowed;numberOfWater;numberOfSoftdrinks;numberOfBeer;numberOfCider;numberOfLongdrink;numberOfShot;numberOfCocktails\n")
            for guest in self.guestList:
                print(guest.nickname)
                csvFile.write(guest.nickname + ";" + guest.cardID + ";" + guest.alcAllowed + ";" + str(
                    guest.numberOfWater) + ";" + str(guest.numberOfSoftdrinks) + ";" + str(
                    guest.numberOfBeer) + ";" + str(guest.numberOfCider) + ";" + str(
                    guest.numberOfLongdrink) + ";" + str(guest.numberOfShot) + ";" + str(
                    guest.numberOfCocktails) + "\n")
            csvFile.close()

    def writeAccumulate(self):
        for element in self.guestList:
            csvFile = open("accumulated.csv", 'w')
            csvFile.write(
                "# Nick;CardID;AlcAllowed;numberOfWater;numberOfSoftdrinks;numberOfBeer;numberOfCider;numberOfLongdrink;numberOfShot;numberOfCocktails\n")
            for guest in self.guestList:
                # print(guest.nickname)
                csvFile.write(guest.nickname + ";" + guest.cardID + ";" + guest.alcAllowed + ";" + str(
                    guest.numberOfWater) + ";" + str(guest.numberOfSoftdrinks) + ";" + str(
                    guest.numberOfBeer) + ";" + str(guest.numberOfCider) + ";" + str(
                    guest.numberOfLongdrink) + ";" + str(guest.numberOfShot) + ";" + str(
                    guest.numberOfCocktails) + "\n")
            csvFile.close()

    def writeBacklog(self, cardID, drink):
        backlog = open("backlog.txt", 'a')
        backlog.write(cardID + ";" + drink + "\n")
        backlog.close()

    def accumulate(self):
        backlog = open("backlog.txt", 'r')
        lines = backlog.readlines()
        for line in lines:
            if line.startswith('#'):
                print("Comment, skipping....")
            else:
                elements = line.split(';')
                guest = self.getGuestByCard(elements[0])
                drink = elements[1].replace("\r\n", "").replace("\n", "")
                if guest is not None:
                    if drink == "water":
                        guest.numberOfWater = guest.numberOfWater + 1
                    elif drink == "softdrink":
                        guest.numberOfSoftdrinks = guest.numberOfSoftdrinks + 1
                    elif drink == "beer":
                        guest.numberOfBeer = guest.numberOfBeer + 1
                    elif drink == "cider":
                        guest.numberOfCider = guest.numberOfCider + 1
                    elif drink == "longdrink":
                        guest.numberOfLongdrink = guest.numberOfLongdrink + 1
                    elif drink == "shot":
                        guest.numberOfShot = guest.numberOfShot + 1
                    elif drink == "cocktail":
                        guest.numberOfCocktails = guest.numberOfCocktails + 1
                    else:
                        print("drink not found: " + elements[1])
                else:
                    print("Guest not found: " + line)
        self.writeCSV()
        backlog.close()
        backlog = open("backlog.txt", 'w')
        backlog.close()

    def getGuestByCard(self, cardID):
        for guest in self.guestList:
            # print("Searched: "+cardID)
            # print("Elem: "+guest.cardID)
            if guest.cardID == cardID:
                return guest
        return None

    def addLongdrinkToGuest(self, cardID):
        for guest in self.guestList:
            if guest.cardID == cardID:
                guest.numberOfLongdrink = guest.numberOfLongdrink + 1
                # self.writeCSV()
                self.writeBacklog(cardID, "longdrink")
                self.writeLog("Adding Longdrink to Guest " + guest.nickname, "Success")
                return True
        self.writeLog("Adding Longdrink to Guest " + guest.nickname, "Error, guest not found")
        return False

    def addShotToGuest(self, cardID):
        for guest in self.guestList:
            if guest.cardID == cardID:
                guest.numberOfShot = guest.numberOfShot + 1
                # self.writeCSV()
                self.writeBacklog(cardID, "shot")
                self.writeLog("Adding Shot to Guest " + guest.nickname, "Success")
                return True
        self.writeLog("Adding Cider to Shot " + guest.nickname, "Error, guest not found")
        return False

    def addCiderToGuest(self, cardID):
        for guest in self.guestList:
            if guest.cardID == cardID:
                guest.numberOfCider = guest.numberOfCider + 1
                # self.writeCSV()
                self.writeBacklog(cardID, "cider")
                self.writeLog("Adding Cider to Guest " + guest.nickname, "Success")
                return True
        self.writeLog("Adding Cider to Guest " + guest.nickname, "Error, guest not found")
        return False

    def addSoftdrinkToGuest(self, cardID):
        for guest in self.guestList:
            if guest.cardID == cardID:
                guest.numberOfSoftdrinks = guest.numberOfSoftdrinks + 1
                # self.writeCSV()
                self.writeBacklog(cardID, "softdrink")
                self.writeLog("Adding Softdrink to Guest " + guest.nickname, "Success")
                return True
        self.writeLog("Adding Softdrink to Guest " + guest.nickname, "Error, guest not found")
        return False

    def addBeerToGuest(self, cardID):
        for guest in self.guestList:
            if guest.cardID == cardID:
                guest.numberOfBeer = guest.numberOfBeer + 1
                # self.writeCSV()
                self.writeBacklog(cardID, "beer")
                self.writeLog("Adding Beer to Guest " + guest.nickname, "Success")
                return True
        self.writeLog("Adding Beer to Guest " + guest.nickname, "Error, guest not found")
        return False

    def addWaterToGuest(self, cardID):
        for guest in self.guestList:
            if guest.cardID == cardID:
                guest.numberOfWater = guest.numberOfWater + 1
                # self.writeCSV()
                self.writeBacklog(cardID, "water")
                self.writeLog("Adding Water to Guest " + guest.nickname, "Success")
                return True
        self.writeLog("Adding Water to Guest " + guest.nickname, "Error, guest not found")
        return False

    def addCocktailToGuest(self, cardID):
        for guest in self.guestList:
            if guest.cardID == cardID:
                guest.numberOfCocktails = guest.numberOfCocktails + 1
                # self.writeCSV()
                self.writeBacklog(cardID, "cocktail")
                self.writeLog("Adding Cocktail to Guest " + guest.nickname, "Success")
                return True
        self.writeLog("Adding Cocktail to Guest " + guest.nickname, "Error, guest not found")
        return False

    def setAlcForGuest(self, cardID, state):
        for guest in self.guestList:
            if guest.cardID == cardID:
                guest.alcAllowed = state
                self.writeCSV()
                return True
        return False