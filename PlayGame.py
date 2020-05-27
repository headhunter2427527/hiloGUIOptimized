import tkinter as tk
import datetime as dt
import random as rd
import Game as gm
import backend
import main as m

class PlayGame():
    def __init__(self, mainArea):
        self.mainArea = mainArea
        self.name = tk.StringVar()
        self.player = {}
        self.playerLost = False
        self.randomNumberString = tk.StringVar()
        self.randomNumber = -1
        self.result = tk.StringVar()

    def createPlayer(self, name):
        self.player["name"] = self.name.get()
        self.player["score"] = 0
        self.player["datetime"] = dt.datetime.today()



    def showEnterDetailsMenu(self):
        enterDetailsLabel = tk.Label(self.mainArea, text = "Enter your name", bg = "crimson", fg = "black", font = ("sans serif", 15, "italic"))
        enterDetailsLabel.place(relx = 0.3, rely = 0.15, relheight = 0.15, relwidth = 0.4)

        textEntry = tk.Entry(self.mainArea, textvariable = self.name, font = ("sans serif", 20, "italic"))
        textEntry.place(relx = 0.3, rely = 0.35, relheight = 0.15, relwidth = 0.4)

        beginButton = tk.Button(self.mainArea, text = "Begin Game", font = ("sans serif", 15, "italic"), bg = "black", fg = "crimson", command = self.startGame)
        beginButton.place(relx = 0.3, rely = 0.55, relheight = 0.15, relwidth = 0.4)

    def startGame(self):
        self.createPlayer(self.name)
        m.clearFrame(self.mainArea)

        if self.randomNumber == -1:
            self.randomNumber = rd.randint(1,15)
            self.randomNumberString.set(str(self.randomNumber))


        labelArea = tk.Frame(self.mainArea, bg = "crimson")
        labelArea.place(relx = 0.3, rely = 0.15, relheight = 0.4, relwidth = 0.4)

        guessLabel = tk.Label(labelArea, text = "The Number is", bg = "crimson", fg = "black", font = ("sans serif", 15, "bold italic"))
        guessLabel.place(relx = 0.1, rely = 0.2, relheight = 0.3, relwidth = 0.8)

        guessNumber = tk.Label(labelArea, textvariable = self.randomNumberString, font = ("sans serif", 25, "bold"), bg = "crimson", fg = "black")
        guessNumber.place(relx = 0.4, rely = 0.5, relheight = 0.2, relwidth = 0.2)

        buttonArea = tk.Frame(self.mainArea, bg = "crimson")
        buttonArea.place(relx = 0.1, rely = 0.55, relheight = 0.15, relwidth = 0.8)

        highButton = tk.Button(buttonArea, text = "High", font = ("sans serif", 15, "italic"), bg = "black", fg = "crimson", command = self.high)
        highButton.place(relx = 0, rely = 0.1, relwidth = 0.25)

        sameButton = tk.Button(buttonArea, text="Same", font=("sans serif", 15, "italic"), bg="black", fg="crimson", command = self.same)
        sameButton.place(relx=0.375, rely=0.1, relwidth = 0.25)

        lowButton = tk.Button(buttonArea, text = "Low", font = ("sans serif", 15, "italic"), bg = "black", fg = "crimson", command = self.low)
        lowButton.place(relx = 0.75, rely = 0.1, relwidth = 0.25)

        resultLabel = tk.Label(self.mainArea, textvariable = self.result, font = ("sans serif", 25, "bold"), bg = "crimson", fg = "black")
        resultLabel.place(relx = 0.2, rely = 0.75, relwidth = 0.6, relheight = 0.2)

    def high(self):
        nextRandomNumber = rd.randint(1, 15)
        if self.playerLost == False:
            if nextRandomNumber > self.randomNumber:
                self.player["score"] += 1
                self.result.set("Correct Guess!!!\nScore : " + str(self.player["score"]))
                self.randomNumber = nextRandomNumber
                self.randomNumberString.set(self.randomNumber)
            else:
                self.result.set("Wrong Guess!!!\nScore : " + str(self.player["score"]))
                self.playerLost = True
                self.lostScreen()

    def low(self):
        nextRandomNumber = rd.randint(1, 15)
        if self.playerLost == False:
            if nextRandomNumber < self.randomNumber:
                self.player["score"] += 1
                self.result.set("Correct Guess!!!\nScore : " + str(self.player["score"]))
                self.randomNumber = nextRandomNumber
                self.randomNumberString.set(self.randomNumber)
            else:
                self.result.set("Wrong Guess!!!\nScore : " + str(self.player["score"]))
                self.playerLost = True
                self.lostScreen()

    def same(self):
        nextRandomNumber = rd.randint(1, 15)
        if self.playerLost == False:
            if nextRandomNumber == self.randomNumber:
                self.player["score"] += 2
                self.result.set("Correct Guess!!!\nScore : " + str(self.player["score"]))
                self.randomNumber = nextRandomNumber
                self.randomNumberString.set(self.randomNumber)
            else:
                self.result.set("Wrong Guess!!!\nScore : " + str(self.player["score"]))
                self.playerLost = True
                self.lostScreen()

    def lostScreen(self):
        backend.saveScore(self.player)
        m.clearFrame(self.mainArea)

        gameOver = tk.Label(self.mainArea, text = ("Game Over!!!\n" + str(self.player["name"]) + " your score is : " + str(self.player["score"])), font = ("sans serif", 15, "bold italic"), bg = "crimson", fg = "black")
        gameOver.place(relx = 0.2, rely = 0.3, relheight = 0.4, relwidth = 0.6)

        goBackButton = tk.Button(self.mainArea, text="Go to Main Screen", font=("sans serif", 15, "italic"), height=20, width=30, command = self.goBack, bg = "black", fg = "crimson")
        goBackButton.place(relx=0.3, rely=0.65, relheight=0.15, relwidth=0.4)

    def goBack(self):
        m.clearFrame(self.mainArea)
        game = gm.Game(self.mainArea)
        game.showMainMenu()