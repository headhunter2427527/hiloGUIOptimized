import tkinter as tk
import main as m
import Game as gm
import backend

class HighScores:
    def __init__(self, mainArea):
        self.mainArea = mainArea

    def showHighScores(self):
        headingsFrame = tk.Frame(self.mainArea)
        headingsFrame.place(relx = 0.05, rely = 0.1, relheight = 0.1, relwidth = 0.9)

        playerNameLabel = tk.Label(headingsFrame, text = "Player's Name \t", font = ("sans serif", 15, "bold"))
        playerNameLabel.grid(row = 0, column = 1)

        dateTimeLabel = tk.Label(headingsFrame, text="Date & Time \t", font = ("sans serif", 15, "bold"))
        dateTimeLabel.grid(row = 0, column = 2)

        scoreLabel = tk.Label(headingsFrame, text="Score", font = ("sans serif", 15, "bold"))
        scoreLabel.grid(row = 0, column = 3)

        scoresFrame = tk.Frame(self.mainArea)
        scoresFrame.place(relx = 0.05, rely = 0.25, relheight = 0.4, relwidth = 0.9)

        players = backend.getHighScoresList()

        for i in range(len(players)):
            playerName = tk.Label(scoresFrame, text = (str(players[i]["name"]) + " \t "), font = ("sans serif", 13, "bold"))
            playerName.grid(row = i, column = 0)

            playerDateTime = tk.Label(scoresFrame, text = (str(players[i]["datetime"]) + "  "), font = ("sans serif", 13, "bold"))
            playerDateTime.grid(row = i, column = 1)

            playerScore = tk.Label(scoresFrame, text = (str(players[i]["score"]) + " \t "), font = ("sans serif", 13, "bold"))
            playerScore.grid(row = i, column = 2)

        goBackButton = tk.Button(self.mainArea, text="Go to Main Screen", font=("sans serif", 15, "italic"), height=20,
                                 width=30, command=self.goBack, bg="black", fg="crimson")
        goBackButton.place(relx=0.3, rely=0.75, relheight=0.15, relwidth=0.4)

    def goBack(self):
        m.clearFrame(self.mainArea)
        game = gm.Game(self.mainArea)
        game.showMainMenu()