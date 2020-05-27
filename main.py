import Game as gm
import tkinter as tk

def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def createHeaderArea(root):
    headerFrame = tk.Frame(root, bg = "black")
    headerFrame.place(relx = 0, rely = 0, relheight = 0.2, relwidth = 1)
    headerLabel = tk.Label(headerFrame, text = "Welcome to Hi-Lo", height = 100, fg = "crimson", bg = "black", font = ("sans serif", 25, "bold italic"))
    headerLabel.pack()

def createMainArea(root):
    mainFrame = tk.Frame(root, bg = "crimson")
    mainFrame.place(relx = 0, rely = 0.2, relheight = 0.8, relwidth = 1)
    return mainFrame

def main():
    root = tk.Tk()
    root.geometry("500x500+50+50")

    createHeaderArea(root)
    mainArea = createMainArea(root)
    game = gm.Game(mainArea)
    game.showMainMenu()

    root.mainloop()


if __name__ == "__main__":
    main()