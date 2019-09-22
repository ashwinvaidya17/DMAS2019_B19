###### Rock papaer scissor ###########
import random
import math

class rps_game():
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        self.choice={1:"rock",2:"paper",3:"scissor"}
        self.p1_choice=self.choice[self.p1]
        self.p2_choice=self.choice[self.p2]
        self.p1_score=0
        self.p2_score=0
        self.winner=None
        self.game()

    def game(self):
        if (self.p1_choice==self.p2_choice):
            self.p1_score=self.p1_score
            self.p2_score=self.p2_score
        if ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[3])) or ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[1])) or ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[2])):
            self.p1_score=self.p1_score+1
        if ((self.p1_choice==self.choice[1]) and (self.p2_choice==self.choice[2])) or ((self.p1_choice==self.choice[2]) and (self.p2_choice==self.choice[3])) or ((self.p1_choice==self.choice[3]) and (self.p2_choice==self.choice[1])):
            self.p2_score=self.p2_score+1

    def compute_res(self):
        if (self.p1_score > self.p2_score):
            self.winner="player 1"
        elif (self.p2_score > self.p1_score):
            self.winner="player 2"
        else:
            self.winner=None
        return self.winner

    # compute the final winner
    def score_calc(self):
        if self.p1_score > self.p2_score:
            return ("player 1 wins")
        else:
            return ("player 2 wins")

class tom():
    def __init__(self):
        self.p1_decision=0
        self.p2_decision=0

    def call_me(self,p_name,p_order,p1_ch,p2_ch):
        print("player 1 choice @ each round ",p1_ch)
        print("player 2 choice @ each round",p2_ch)
        self.p1_order=None
        self.p2_order=None
        if p_name=="p1":
            self.p1_order=p_order
        elif p_name=="p2":
            self.p2_order=p_order
        if self.p1_order==0:
            return self.zero_order(p1_ch,p2_ch)
        if self.p2_order==1:
            return self.first_order()

    # returning the player's choice based on the opponent choice
    def response(self,inp):
        res=0
        if inp==1:
            res=2
        elif inp==2:
            res=3
        elif inp==3:
            res=1
        return res

    def compute(self,inp_lst):
        # calculate maximum of five trails
        init_val=0
        f_val=0
        self.f_str=[]
        self.randflag=0
        #print("compute list :",inp_lst)
        if (len(inp_lst) > 1):
            for elem in inp_lst:
                if elem not in self.f_str:
                    self.f_str.append(elem)
        #print("Final store list",self.f_str)
        if len(self.f_str) ==1:
            return self.response(self.f_str[0])
            self.randflag=0
        elif len(self.f_str)==2 or len(self.f_str)==3:
            return self.response(random.choice(self.f_str))
            self.randflag=1

    # saving the player's choices for each round
    def zero_order(self,p1_ch,p2_ch):
        self.zero_order_res=0
        c_cnt=0         # choice count of the opponent player
        c_lst=[]        # store choice count
        str1=[]         # store opponent choice
        if self.p1_order == 0:
            if len(p1_ch) == len(p2_ch):
                # sorting the choice count
                for i in range(0,len(p1_ch)):
                    c_cnt=p2_ch.count(p2_ch[i])
                    c_lst.append(c_cnt)
                    if (len(c_lst) > 1):
                        z=0  # support variable
                        for j in range(1,len(c_lst)):
                            if c_lst[z] > c_lst[z+1]:
                                c_lst.remove(c_lst[z+1])
                            elif c_lst[z] == c_lst[z+1]:
                                c_lst=c_lst
                                z=z+1
                            else:
                                c_lst.remove(c_lst[z])
                        if len(c_lst) > 1:
                            # sorting the highest choices by the player's
                            for k in range(1,len(c_lst)):
                                if c_lst[k-1] == c_cnt:
                                    str1.append(p2_ch[i])

                print("Final choice count @ the end of each round",c_lst)
                print("player 2 most trails :",str1)

        """ uncomment it if the player 2 is to set to zero order
        elif self.p2_order==0:
            if len(p1_ch) == len(p2_ch):
                # sorting the choice count
                for i in range(0,len(p2_ch)):
                    c_cnt=p1_ch.count(p1_ch[i])
                    print("choice :",p1_ch[i])
                    print("choice count :",c_cnt)
                    c_lst.append(c_cnt)
                    if (len(c_lst) > 1):
                        for j in range(1,len(c_lst)):
                            if c_lst[j-1] > c_lst[j]:
                                c_lst.remove(c_lst[j])
                            elif c_lst[j-1] == c_lst[j]:
                                c_lst=c_lst
                            else:
                                c_lst.remove(c_lst[j-1])
                        if len(c_lst) > 1:
                            # sorting the highest choices by the player's
                            for k in range(1,len(c_lst)):
                                if c_lst[k-1] == c_cnt:
                                    str1.append(p1_ch[i])


                print("Final choice count @ the end of each round",c_lst)
                print("player 2 most trails :",str1)   """

        self.zero_order_res = self.compute(str1)
        print("zero order try :",self.zero_order_res)
        self.p1_decision=self.zero_order_res
        return self.p1_decision


    def first_order(self):
        first_order_res=0
        if self.randflag==1:
            first_order_res=self.response(random.choice(self.f_str)) # random choice of zero order
            first_order_res=self.response(first_order_res) # taking the decision opposite to zero order
        else:
            first_order_res=self.p1_decision
        print("zero order guess",first_order_res)
        first_order_res=self.response(first_order_res)
        print("first order try :",first_order_res)
        self.p2_decision=first_order_res
        return self.p2_decision

if __name__=="__main__":
    turn=0
    p1=0
    p2=0
    count=1
    p1_order=0 # order of player one here it is zero order
    p2_order=1 # order of plater two here it is first order
    p1_ch=[]
    p2_ch=[]
    tom=tom()
    res_limit=5 # limit for the order of agents trails
    t_runs=11
    print("This is an rock paper scissor game ---------- the choice are \
         \n 1:Rock \n 2.scissor \n 3.paper \n \
        each player need to choose one of the above options  ")
    while (count <= t_runs):
        print("count :",count)
        while turn < 2:
            if turn == 0:
                #print("player one turn :")
                if count > res_limit:
                    p1=tom.call_me("p1",p1_order,p1_ch,p2_ch)
                    #print("By zero order :",p1)
                    p1_ch.append(p1)
                    #print("zero ch1",p1_ch)
                else:
                    p1=random.randint(1,3)
                    p1_ch.append(p1)
            if turn == 1:
                #print("player two turn :")
                if count > res_limit:
                    p2=tom.call_me("p2",p2_order,p1_ch,p2_ch)
                    #print("By firt order :",p2)
                    p2_ch.append(p2)
                    #print("first ch2",p2_ch)
                else:
                    p2=random.randint(1,3)
                    p2_ch.append(p2)
            turn+=1
        a=rps_game(p1,p2)

        #print("The winner is : ",a.compute_res())
        count+=1
        turn=0

    print("The choices of player 1 :",p1_ch)
    print("The choices of player 2 :",p2_ch)
    print("The final winner is :",a.score_calc())
