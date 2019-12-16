# Rock paper scissor lizard spock game"

import random
from . import game
from .import TOM

def rpsls_run(total_no_of_runs,p1order,p2order,game_no):
    # varaiable declaration
    turn=0
    p1=0 # assign player one
    p2=0 # assign player two
    rpsls={1:"rock",2:"paper",3:"scissors",4:"lizard",5:"spock"} # dictionary initialiser
    count=1 # round count
    p1_order=p1order # order of player one here it is zero order
    p2_order=p2order # order of plater two here it is first order
    p1_ch=[] # player 1 choice
    p2_ch=[] # player 2 choice

    tom=TOM.tom() # calling the TOM function
    a=game.rpsls()
    res_limit=10  # limit for the order of agents trails
    #seed1=res_limit+1 # seed for player 1 random trails
    #seed2=(res_limit*2)+1 # seed for player2 random trails
    t_runs=total_no_of_runs # total number of runs

    print("########--------------------------------------------------------########")
    print("""This is an rock paper scissors lizard spock game ---------- the choice are
         \n 1:Rock \n 2.scissors \n 3.paper \n 4.lizard \n 5.spock
        each player need to choose one of the above options""")
    print("------------------------------------------------------------------------")
    print("For the rest of the game \n 1=Rock \n 2=paper \n 3=scissors \n 4=lizard \n 5=spock")
    print("------------------------------------------------------------------------")

    while (count <= t_runs):
        print("Round :",count)
        while turn < 2:
            if turn == 0:
                print("player one turn -------->")
                if count > res_limit:
                    p1=tom.agents_functionality("p1",p1_order,p1_ch,p2_ch[len(p2_ch)-res_limit:])
                    print("player one ("+str(p1_order)+" order) choice at round "+str(count)+":",rpsls[p1])
                    p1_ch.append(p1)
                else:
                    p1=random.randint(1,5)
                    #random.seed(seed1)
                    print("player one ("+str(p1_order)+" order) choice at round "+ str(count) +":",rpsls[p1])
                    p1_ch.append(p1)
                    #seed1+=1

            if turn == 1:
                print("player two turn -------->")
                if count > res_limit:
                    p2=tom.agents_functionality("p2",p2_order,p2_ch,p1_ch[len(p1_ch)-res_limit:])
                    print("player two ("+str(p2_order)+" order) choice at round "+str(count)+":",rpsls[p2])
                    p2_ch.append(p2)
                else:
                    p2=random.randint(1,5)
                    #random.seed(seed2)
                    print("player two ("+str(p2_order)+" order) choice at round "+str(count)+":",rpsls[p2])
                    p2_ch.append(p2)
                    #seed2+=1
            turn+=1
        a.game(p1,p2) # game running part
        count+=1
        turn=0

    game_summary,p1_score,p2_score,draw=a.compute_res(game_no)

    print("The choices of player 1 in game "+str(game_no)+":",p1_ch)
    print("The choices of player 2 in game "+str(game_no)+":",p2_ch)
    print("The result of the game "+str(game_no)+":",game_summary)

    return game_summary,p1_score,p2_score,draw
