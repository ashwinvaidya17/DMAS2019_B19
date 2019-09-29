# Rock paper scissor lizard spock game"

import random
from . import game
from .import TOM

def rpsls_run(total_no_of_runs,p1order,p2order):
    turn=0
    p1=0
    p2=0
    rpsls={1:"rock",2:"paper",3:"scissor",4:"lizard",5:"spock"}
    count=1 # run count
    p1_order=p1order # order of player one here it is zero order
    p2_order=p2order # order of plater two here it is first order
    p1_ch=[] # player 1 choice
    p2_ch=[] # player 2 choice
    tom=TOM.tom() # calling the TOM function
    a=game.rpsls()
    res_limit=10  # limit for the order of agents trails
    t_runs=total_no_of_runs # total number of runs
    file_to_save_result="result.txt"
    print("########--------------------------------------------------------########")
    print("This is an rock paper scissor game ---------- the choice are \
         \n 1:Rock \n 2.scissor \n 3.paper \n 4.lizard \n 5.spock\
        each player need to choose one of the above options  ")
    print("------------------------------------------------------------------------")
    print("For the rest of the game \n 1=Rock \n 2=paper \n 3=scissor \n 4=lizard \n 5=spock")
    print("------------------------------------------------------------------------")
    while (count <= t_runs):
        print("Round :",count)
        while turn < 2:
            if turn == 0:
                print("player one turn -------->")
                if count > res_limit:
                    p1=tom.call_me("p1",p1_order,p1_ch,p2_ch)
                    print("player one ("+str(p1_order)+" order) choice at round "+str(count)+":",rpsls[p1])
                    p1_ch.append(p1)
                else:
                    p1=random.randint(1,5)
                    print("player one choice at round "+ str(count) +":",rpsls[p1])
                    p1_ch.append(p1)
            if turn == 1:
                print("player two turn -------->")
                if count > res_limit:
                    p2=tom.call_me("p2",p2_order,p1_ch,p2_ch)
                    print("player two ("+str(p2_order)+" order) choice at round "+str(count)+":",rpsls[p2])
                    p2_ch.append(p2)
                else:
                    p2=random.randint(1,5)
                    print("player two choice at round "+str(count)+":",rpsls[p2])
                    p2_ch.append(p2)
            turn+=1

        a.game(p1,p2) # game running part

        #print("The winner is : ",a.compute_res())
        count+=1
        turn=0

    game_summary=a.compute_res()
    with open(file_to_save_result,'a') as result:
        result.write("The choices of player 1 :")
        result.write(str(p1_ch))
        result.write("\n")
        result.write("The choices of player 2 :")
        result.write(str(p2_ch))
        result.write("\n")
        result.write("The result of the game :")
        result.write(str(game_summary))
        result.write("\n")

    print("The choices of player 1 :",p1_ch)
    print("The choices of player 2 :",p2_ch)
    print("The result of the game :",game_summary)

#run(50,0,1)
