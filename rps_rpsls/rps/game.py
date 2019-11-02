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
        self.p1_score_collect=[] # list to store the player 1 scores
        self.p2_score_collect=[] # list to store the player 2 scores
        self.match_draw_score_collect=[] # list to store draw matches
        self.winner=None

    def game(self,p1,p2):
        # game module
        self.p1=p1 #player 1 choices
        self.p2=p2 #player 2 choices

        self.choice={1:"rock",2:"paper",3:"scissors"}
        self.p1_choice=self.choice[self.p1]
        self.p2_choice=self.choice[self.p2]
        # game logic part ------------------------------------------------------------------------
        if (self.p1_choice==self.p2_choice):
            self.p1_score=self.p1_score
            self.p2_score=self.p2_score
            self.draw+=1
        elif ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[3])) or ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[1])) or ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[2])):
            self.p1_score=self.p1_score+1
        elif ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[2])) or ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[3])) or ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[1])):
            self.p2_score=self.p2_score+1
        # ----------------------------------------------------------------------------------------
        self.p1_score_collect.append(self.p1_score)
        self.p2_score_collect.append(self.p2_score)
        self.match_draw_score_collect.append(self.draw)
        # ----------------------------------------------------------------------------------------
        print("$--------------------------------------------------------$")
        print("Player one score :",self.p1_score)
        print("Player two score :",self.p2_score)
        print("$--------------------------------------------------------$")
        #print("Draw :",self.draw)
        
    def compute_res(self,game_no):
        # compute the result of the game
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
        return self.winner,self.p1_score_collect,self.p2_score_collect,self.match_draw_score_collect,self.p1_score,self.p2_score,self.draw
