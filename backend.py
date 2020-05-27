from os import path
import pickle as pk

def findPlayer(score):
    if path.exists("High Scores"):
        file = open("High Scores", mode = 'rb')
        players = pk.load(file)
        for player in players:
            if player["score"] == score:
                return player
    else:
        return None

def sortplayers(players):
    scores = []
    for player in players:
        scores.append(player["score"])

    scores.sort(reverse = True)
    players = list(map(findPlayer, scores))
    return players

def saveScore(player):
    players = []
    if path.exists("High Scores"):
        file = open("High Scores", mode = 'rb')
        players = pk.load(file)
        file.close()
    else:
        file = open("High Scores", mode = 'wb')
        file.close()
    if len(players) < 5:
        players.append(player)
        file = open("High Scores", mode = 'wb')
        pk.dump(players, file)
        file.close()
        print("score successfully saved...")
    else:
        players = sortplayers(players)
        if player["score"] > players[len(players)-1]["score"]:
            players[len(players)-1] = player
            file = open("High Scores", 'wb')
            pk.dump(players, file)
            file.close()
            print("score successfully saved...")
        else:
            print("List full...")

def getHighScoresList():
    file = open("High Scores", mode = 'rb')
    players = pk.load(file)
    file.close()
    players = sortplayers(players)
    return players