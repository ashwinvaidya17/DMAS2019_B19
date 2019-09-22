class rpsls():

    def __init__(self,p1,p2):

        self.p1=p1
        self.p2=p2

        self.choice={1:"rock",2:"paper",3:"scissor",4:"lizard",5:"spock"}
        self.p1_choice=self.choice[self.p1]
        self.p2_choice=self.choice[self.p2]
        self.p1_score=0
        self.p2_score=0
        self.winner=None

        print("player one choice :", self.p1_choice)
        print("player two choice : ",self.p2_choice)
        self.game()

    def game(self):

        if (self.p1_choice==self.p2_choice):
            self.p1_score=self.p1_score
            self.p2_score=self.p2_score

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

    def compute_res(self):
        #print(self.p1_score)
        #print(self.p2_score)
        if (self.p1_score > self.p2_score):
            self.winner="player 1"

        elif (self.p2_score > self.p1_score):
            self.winner="player 2"

        else:
            self.winner=None

        return self.winner


if __name__ == "__main__":

    turn=0
    p1=0
    p2=0
    count=1

    print("This is an rock paper scissor game ---------- the choice are \
         \n 1:Rock \n 2.scissor \n 3.paper \n 4.lizard \n 5.spock \
        each player need to choose one of the above options  ")

    while (count <= 20):
        #print("count :",count)
        while turn < 2:

            if turn == 0:
                print("player one turn :")
                p1=int(input(""))
            if turn == 1:
                print("player two turn :")
                p2=int(input(""))
            if (p1 or p2) >=6:
                print("Outside the given parameter try other options ..... ")
                break

            turn+=1

        a=rpsls(p1,p2)

        print("The winner is : ",a.compute_res())
        count+=1
        turn=0
