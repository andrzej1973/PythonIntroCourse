class Game:
    def __init__(self,newPlayerName):
        self.playerName = newPlayerName
        self.playerHand="NA"
        self.botHand="NA"
        self.winner="No winner yet"
        print("New istance of game class for: "+str(self.playerName))

    def runGame(self):
        print("runGame")
        #botHand: 1- scissors, 2- rock, 3- paper
        if((self.playerHand=='rock' or self.playerHand=='Rock') and self.botHand==1):
            self.winner='You win'
        elif((self.playerHand=='rock' or self.playerHand=='Rock') and self.botHand==2):
            self.winner= 'You tie'
        elif ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 3):
            self.winner='You lose'

        elif((self.playerHand=='paper' or self.playerHand=='Paper') and self.botHand==1):
            self.winner='You lose'
        elif((self.playerHand=='paper' or self.playerHand=='Paper') and self.botHand==2):
            self.winner='You win'
        elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 3):
            self.winner='You tie'

        elif((self.playerHand=='scissors' or self.playerHand=='Scissors') and self.botHand==1):
            self.winner='You tie'
        elif((self.playerHand=='scissors' or self.playerHand=='Scissors') and self.botHand==2):
            self.winner='You lose'
        elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 3):
            self.winner='You win'
        else:
            self.winner='INVALID input. Try again...'
            import time
            time.sleep(2)
            main()

def main():
    myGame=Game('Andrzej')
    print(myGame.playerName)
    print(myGame.playerHand)
    print(myGame.botHand)
    print(myGame.winner)

    myGame.playerHand='scissors'
    myGame.botHand=3 #paper
    myGame.runGame()
    print(myGame.winner)

main()