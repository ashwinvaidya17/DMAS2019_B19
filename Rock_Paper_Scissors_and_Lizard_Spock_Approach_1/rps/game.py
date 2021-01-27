"""
Game module of the rock paper scissors game
"""
class rps_game():
    def __init__(self):
        #initialiser
        # variable decleration
        self.p1_score=0 #variable to calculate p1 win matches
        self.p2_score=0 #variable to calculate p2 win matches
        self.draw=0 # variable to calculate draw matches
        # game decision variables --> 1:Rock, 2:Paper, 3: Scissors
        self.p1_decision_choices=[
            (2,1),
            (3,2),
            (1,3)]
        self.p2_decision_choices=[
            (1,2),
            (2,3),
            (3,1)]
        self.winner=None

    def game(self,p1,p2):
        # game module, which computes the result for each round between player 1 and player 2
        self.p1=p1 #player 1 choices
        self.p2=p2 #player 2 choices

        # game logic part ------------------------------------------------------------------------
        self.user_choices=[]
        self.user_choices.append(self.p1)
        self.user_choices.append(self.p2)
        self.user_choices=tuple(self.user_choices)
        if self.user_choices in self.p1_decision_choices:
            self.p1_score+=1
        elif self.user_choices in self.p2_decision_choices:
            self.p2_score+=1
        else:
            self.draw+=1
        # ----------------------------------------------------------------------------------------
        print("$--------------------------------------------------------$")
        print("Player one score :",self.p1_score)
        print("Player two score :",self.p2_score)
        print("$--------------------------------------------------------$")
        #print("Draw :",self.draw)

    # The function compute_res, gives the game summary (result) for the rounds computed between player one and player two.
    def compute_res(self,game_no):
        # compute the final winner of the game
        if (self.p1_score > self.p2_score):
            self.winner="Winner is player 1"
        elif (self.p2_score > self.p1_score):
            self.winner="Winner is player 2"
        elif (self.p1_score == self.p2_score):
            self.winner="Match Draw"

        print("--------------------------------------------------------")
        print("Player one Final score in game "+str(game_no)+" is : ",self.p1_score)
        print("Player two Final score in game "+str(game_no)+" is : ",self.p2_score)
        print("Number of matches ends in draw in game "+str(game_no)+" is : ",self.draw)
        print("--------------------------------------------------------")
        return self.winner,self.p1_score,self.p2_score,self.draw
