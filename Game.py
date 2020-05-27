import PlayGame as pg
import HighScores as hs
import tkinter as tk
import main as m

class Game:
    def __init__(self, mainArea):
        self.mainArea = mainArea

    def playGame(self):
        play = pg.PlayGame(self.mainArea)
        m.clearFrame(self.mainArea)
        play.showEnterDetailsMenu()

    def viewHighScores(self):
        highScores = hs.HighScores(self.mainArea)
        m.clearFrame(self.mainArea)
        highScores.showHighScores()

    def exit(self):
        exit(0)

    def showMainMenu(self):
        playButton = tk.Button(self.mainArea, text = "Play Game", font = ("sans serif", 15, "italic"), height = 20, width = 30, command = self.playGame, bg = "black", fg = "crimson")
        playButton.place(relx = 0.3, rely = 0.15, relheight = 0.15, relwidth = 0.4)

        viewHighScoresButton = tk.Button(self.mainArea, text="View High Scores", font=("sans serif", 15, "italic"), height=20, width=30, command = self.viewHighScores, bg = "black", fg = "crimson")
        viewHighScoresButton.place(relx=0.3, rely=0.4, relheight=0.15, relwidth=0.4)

        exitButton = tk.Button(self.mainArea, text="Exit Game", font=("sans serif", 15, "italic"), height=20, width=30, command = self.exit, bg = "black", fg = "crimson")
        exitButton.place(relx=0.3, rely=0.65, relheight=0.15, relwidth=0.4)