# Nick;CardID;AlcAllowed;NumberOfWater;numberOfSoftdrink;NumberOfBeer;NumberOfCider;NumberOfLongdrink;NumberOfShot;NumberOfCocktails
class Guest:
    def __init__(self, nickname, cardID, alcAllowed, numberOfWater, numberOfSoftdrinks, numberOfBeer, numberOfCider, numberOfLongdrink, numberOfShot, numberOfCocktails):
        self.nickname = nickname
        self.cardID = cardID
        self.alcAllowed = alcAllowed
        self.numberOfWater = numberOfWater
        self.numberOfSoftdrinks = numberOfSoftdrinks
        self.numberOfBeer = numberOfBeer
        self.numberOfCider = numberOfCider
        self.numberOfLongdrink = numberOfLongdrink
        self.numberOfShot = numberOfShot
        self.numberOfCocktails = numberOfCocktails