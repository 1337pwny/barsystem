from machine import I2C, Pin, SPI, UART
from time import sleep
from pico_i2c_lcd import I2cLcd
from datahandler import DataHandler


def checkForDrinkPress():
    while True:
        for i in range(0, 7):
            if not drinkButtons[i].value():
                return i


def readNFC():
    while True:
        if uart.any():
            b = uart.readline()
            if b is not None:
                try:
                    line = b.decode('utf-8')
                    if "UID" in line:
                        line = line.replace(' ', ':').replace("UID:", "").replace("\r\n", "")
                        return line
                    sleep(0.1)
                except:
                    print("Error reading Card")


uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13), bits=8, parity=None, stop=1)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
print(I2C_ADDR)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
dataHandler = DataHandler("clients.csv")
lcd.blink_cursor_on()
card = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
drinkButtons = []
drinkButtons.append(machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP))
drinkButtons.append(machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP))
drinkButtons.append(machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP))
drinkButtons.append(machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP))
drinkButtons.append(machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP))
drinkButtons.append(machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_UP))
drinkButtons.append(machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP))
lcd.putstr("Ferrox Barsystem\n")
lcd.putstr("Version 1.2")
sleep(2)
lcd.clear()
lcd.putstr("Loaded Users:\n")
lcd.putstr(str(dataHandler.userCount))
sleep(2)
lcd.clear()
lcd.putstr("Writing Backlog\n")
lcd.putstr(".....")
dataHandler.accumulate()

while True:
    # ToDo Check Card here
    lcd.clear()
    lcd.putstr("Bitte Karte\n")
    lcd.putstr("vorhalten")
    cardID = readNFC()
    guest = dataHandler.getGuestByCard(cardID)

    if not guest == None:
        nick = guest.nickname
        if guest.alcAllowed == "NO":
            lcd.clear()
            lcd.putstr("Gast Alkohol\n")
            lcd.putstr("gesperrt!!!")
            sleep(1)
            lcd.clear()
            lcd.putstr(nick + "\n")
            lcd.putstr("Getraenk?")
            if checkForDrinkPress() == 6:
                dataHandler.addWaterToGuest(cardID)
                lcd.clear()
                lcd.putstr("Wasser\n")
                lcd.putstr("Hinzugefuegt")
                sleep(1)
            elif checkForDrinkPress() == 5:
                dataHandler.addSoftdrinkToGuest(cardID)
                lcd.clear()
                lcd.putstr("Softdrink\n")
                lcd.putstr("Hinzugefuegt")
                sleep(1)
            else:
                lcd.clear()
                lcd.putstr("Gast Alkohol\n")
                lcd.putstr("gesperrt!!!")
                sleep(1)
        else:
            lcd.clear()
            lcd.putstr(nick + "\n")
            lcd.putstr("Getraenk?")
            if checkForDrinkPress() == 6:
                dataHandler.addWaterToGuest(cardID)
                lcd.clear()
                lcd.putstr("Wasser\n")
                lcd.putstr("Hinzugefuegt")
                sleep(1)
            elif checkForDrinkPress() == 5:
                dataHandler.addSoftdrinkToGuest(cardID)
                lcd.clear()
                lcd.putstr("Softdrink\n")
                lcd.putstr("Hinzugefuegt")
                sleep(1)
            elif checkForDrinkPress() == 4:
                dataHandler.addBeerToGuest(cardID)
                lcd.clear()
                lcd.putstr("Bier\n")
                lcd.putstr("Hinzugefuegt")
                sleep(1)
            elif checkForDrinkPress() == 3:
                dataHandler.addCiderToGuest(cardID)
                lcd.clear()
                lcd.putstr("Cider\n")
                lcd.putstr("Hinzugefuegt")
                sleep(1)
            elif checkForDrinkPress() == 2:
                dataHandler.addLongdrinkToGuest(cardID)
                lcd.clear()
                lcd.putstr("Longdrink\n")
                lcd.putstr("Hinzugefuegt")
                sleep(1)
            elif checkForDrinkPress() == 1:
                dataHandler.addShotToGuest(cardID)
                lcd.clear()
                lcd.putstr("Shot\n")
                lcd.putstr("Hinzugefuegt")
                sleep(1)
            elif checkForDrinkPress() == 0:
                dataHandler.addCocktailToGuest(cardID)
                lcd.clear()
                lcd.putstr("Cocktail\n")
                lcd.putstr("Hinzugefuegt")
                sleep(1)
    else:
        lcd.clear()
        lcd.putstr("Karte nicht\n")
        lcd.putstr("gerfunden")
        sleep(5)