""" Game module of the rock paper scissor lizard game"""

class rpsls():

    def __init__(self):
        #initialiser
        self.p1_score=0 #variable to calculate p1 win matches
        self.p2_score=0 #variable to calculate p2 win matches
        self.draw=0 # variable to calculate draw matches
        self.p1_score_collect=[] # list to store the player 1 scores
        self.p2_score_collect=[] # list to store the player 2 scores
        self.winner=None

    def game(self,p1,p2):
        """ The main game sequence : based on the player's choice they will either win or lose"""
        self.p1=p1 # player 1 choice
        self.p2=p2 # player 2 choice

        self.choice={1:"rock",2:"paper",3:"scissor",4:"lizard",5:"spock"}
        self.p1_choice=self.choice[self.p1]
        self.p2_choice=self.choice[self.p2]
        # -----------------------------------------------------------------------------
        # Game logic part
        if (self.p1_choice==self.p2_choice):
            self.p1_score=self.p1_score
            self.p2_score=self.p2_score
            self.draw+=1

        elif ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[3])) or ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[4])):
            self.p1_score+=1

        elif ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[1])) or ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[5])):
            self.p1_score+=1

        elif ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[2])) or ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[4])):
            self.p1_score+=1

        elif ((self.p1_choice==self.choice[4]) and (self.p2_choice==self.choice[2])) or ((self.p1_choice==self.choice[4]) and (self.p2_choice==self.choice[5])):
            self.p1_score+=1

        elif ((self.p1_choice==self.choice[5]) and (self.p2_choice==self.choice[3])) or ((self.p1_choice==self.choice[5]) and (self.p2_choice==self.choice[1])):
            self.p1_score+=1

        elif ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[1])) or ((self.p1_choice==self.choice[4]) and (self.p2_choice==self.choice[1])):
            self.p2_score+=1

        elif ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[2])) or ((self.p1_choice==self.choice[5]) and (self.p2_choice==self.choice[2])):
            self.p2_score+=1

        elif ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[3])) or ((self.p1_choice==self.choice[4]) and (self.p2_choice==self.choice[3])):
            self.p2_score+=1

        elif ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[4])) or ((self.p1_choice==self.choice[5]) and (self.p2_choice==self.choice[4])):
            self.p2_score+=1

        elif ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[5])) or ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[5])):
            self.p2_score+=1
        # -----------------------------------------------------------------------------------
        self.p1_score_collect.append(self.p1_score)
        self.p2_score_collect.append(self.p2_score)
        print("Player one score :",self.p1_score)
        print("Player two score :",self.p2_score)
        print("Draw:",self.draw)
        
    def compute_res(self):
        # To compute the final winner of the game based on total number of runs
        if (self.p1_score > self.p2_score):
            self.winner="Winner is player 1"
        elif (self.p2_score > self.p1_score):
            self.winner="Winner is player 2"
        elif (self.p1_score == self.p2_score):
            self.winner="Match Draw"

        print("Player one Final score :",self.p1_score)
        print("Player two Final score :",self.p2_score)
        #print("Number of matches ends in Draw",self.draw)
        return self.winner,self.p1_score_collect,self.p2_score_collect
