"""
Game module of the rock paper scissor game
"""
class rps_game():
    def __init__(self):
        #initialiser
        self.p1_score=0
        self.p2_score=0
        self.draw=0 # no of macthes get draw
        self.winner=None

    def game(self,p1,p2):
        # game module
        self.p1=p1
        self.p2=p2
        self.choice={1:"rock",2:"paper",3:"scissor"}
        self.p1_choice=self.choice[self.p1]
        self.p2_choice=self.choice[self.p2]

        if (self.p1_choice==self.p2_choice):
            self.p1_score=self.p1_score
            self.p2_score=self.p2_score
            self.draw+=1
        elif ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[3])) or ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[1])) or ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[2])):
            self.p1_score=self.p1_score+1
        elif ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[2])) or ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[3])) or ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[1])):
            self.p2_score=self.p2_score+1

        print("Player one score :",self.p1_score)
        print("Player two score :",self.p2_score)

    def compute_res(self):
        # compute the result of the game
        if (self.p1_score > self.p2_score):
            self.winner="Winner is player 1"
        elif (self.p2_score > self.p1_score):
            self.winner="Winner is player 2"
        elif (self.p1_score == self.p2_score):
            self.winner="Match Draw"
        
        print("Player one Final score :",self.p1_score)
        print("Player two Final score :",self.p2_score)
        #print("Number of matches ends in Draw",self.draw)
        return self.winner
