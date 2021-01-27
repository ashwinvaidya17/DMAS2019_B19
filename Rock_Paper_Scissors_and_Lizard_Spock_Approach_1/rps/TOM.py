"""
Theory of Mind Functionality
"""

import random

class tom():
    # class to compute the player decisions
    def __init__(self):
        self.p1_order=0 # Getting the player 1 order
        self.p2_order=0 # Getting the player 2 order
        self.zero_order_decision=0 # zero order agent decision 
        self.first_order_decision=0 # first order agent decision 
        self.higher_order_decision=0 # higher order agent decision 
        self.zero_flag=0 # variable to check the zero order TOM state
        self.first_flag=0 # variable to check the first order TOM state

    # Assigning agent functionality ------------------------------------------
    def agents_functionality(self,p_name,p_order,p1_ch,p2_ch):

        self.p1_order=None # Getting the player 1 order
        self.p2_order=None# Getting the player 2 order

        # Assigning player names and functionality
        # --------------------------------------------------------------------
        if p_name=="p1":
            self.p1_order=p_order
            if self.p1_order==0:
                self.zero_flag=1
                return self.zero_order(p1_ch,p2_ch)
            elif self.p1_order==1:
                self.first_flag=1
                return self.first_order(p1_ch,p2_ch)
            elif self.p1_order > 1:
                return self.higher_order(self.p1_order,p1_ch,p2_ch)
        # --------------------------------------------------------------------
        elif p_name=="p2":
            self.p2_order=p_order
            if self.p2_order==0:
                self.zero_flag=1
                return self.zero_order(p1_ch,p2_ch)
            elif self.p2_order == 1:
                self.first_flag=1
                return self.first_order(p1_ch,p2_ch)
            elif self.p2_order > 1:
                return self.higher_order(self.p2_order,p1_ch,p2_ch)


    # returning the player's choice based on the opponent choice -------------------
    def response(self,inp):
        """ 1-> Rock 2-> Paper 3-> Scissors """
        res=0 # Response
        # if the input is rock(1) the opponent need to choose Paper(2) to win
        if inp==1:
            res=2
        elif inp==2:
            res=3
        elif inp==3:
            res=1
        return res

    # Determing the choice of players ----------------------------------------
    def compute(self,inp_lst):
        self.final_store=[]
        if (len(inp_lst) >= 1):
            for choices in inp_lst:
                if choices not in self.final_store:
                    self.final_store.append(choices)

        return self.response(random.choice(self.final_store))


    # zero order Theory of mind computation ----------------------------------------------
    def zero_order(self,p1_ch,p2_ch):
        self.zero_order_res=0 # zero order player result
        c_cnt=0         # choice count of the opponent player
        c_lst=[]        # store choice count
        str1=[]         # store opponent choice
        self.zero_flag=1
        # sorting the choice count
        if len(p2_ch) > 1:
            for i in range(0,len(p2_ch)):
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
                    if len(c_lst) > 1: # sorting the highest choices by the player's
                        for k in range(1,len(c_lst)):
                            if c_lst[k-1] == c_cnt:
                                str1.append(p2_ch[i])
        else:
            str1=p2_ch
                                    
        self.zero_order_res = self.compute(str1)
        self.zero_order_decision=self.zero_order_res
        #print("Zero order decision :",self.zero_order_decision)
        return self.zero_order_decision

    # First order TOM computation ------------------------------------------------------------
    def first_order(self,p1_ch,p2_ch):
        if not self.zero_flag==1:
            self.zero_order(p1_ch,p2_ch)
        if len(self.final_store)>=2:
            first_order_res=self.response(random.choice(self.final_store)) # first order result
            first_order_res=self.response(first_order_res) # taking the decision based on zero order
        else:
            first_order_res=self.response(self.zero_order_decision)
        self.first_order_decision=first_order_res
        #print("first order decision :",self.first_order_decision)
        return self.first_order_decision

    # Higher order TOM computation ------------------------------------------------------------
    def higher_order(self,order,p1_ch,p2_ch):
        if not self.zero_flag==1:
            self.zero_order(p1_ch,p2_ch)
        if not self.first_flag==1:
            self.first_order(p1_ch,p2_ch)
        self.higher_order_decision=self.first_order_decision
        while order > 1:
            if len(self.final_store)>=2:
                higher_order_res=self.response(random.choice(self.final_store)) # higher order result
                higher_order_res=self.response(higher_order_res) # taking the decision based on lower order
            else:
                higher_order_res=self.response(self.higher_order_decision)
            self.higher_order_decision=higher_order_res
            #print("order : "+str(order)+" decision : "+str(self.higher_order_decision))
            order=order-1

        return self.higher_order_decision
