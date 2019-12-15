""" The main gaming console for the demonstration """

import os
from rps.rps import rps_run
from rpsls.rpsls import rpsls_run

def gen_output(filename,game,p1_order,p2_order,p1_score,p2_score,draw,game_summary,t_rounds):
    # output file generation function
    with open(filename,'a') as result:
        result.write(game+" game result ")
        result.write("\n")
        result.write("\n")
        result.write("Number of rounds in the game :"+str(t_rounds)+"\n")
        result.write("Player one order :"+str(p1_order)+"\n")
        result.write("Player two order :"+str(p2_order)+"\n")
        result.write("The player one final score :"+str(p1_score)+"\n")
        result.write("The player two final score :"+str(p2_score)+"\n")
        result.write("Number of matches ended in draw :"+str(draw)+"\n")
        result.write("The winner of the game :"+str(game_summary)+"\n")


if __name__=="__main__":

    file_to_save_result="result.txt"
    # to remove the old files
    if file_to_save_result in os.listdir():
        os.remove(file_to_save_result)

    print("""Welcome to the Theory Of Mind (TOM) demonstration of Rock-Paper-Scissors and Rock-Paper-Scissors-Lizard-Spock Game
    Enter the Game of choice you want to play ---------------->
    1. rock paper scissors
    2. rock paper scissors lizard spock""")
    read_user=int(input("Enter the Game of your choice 1 or 2 :"))
    p1_order=int(input("Enter the order of agent for player one (Eg : 0) :"))
    p2_order=int(input("Enter the order of agent for player two (Eg : 2) :"))

    if p1_order <= 10 and p2_order <= 10:
        t_round=100 # default
        game_no=1
        if read_user==1:
            game="Rock Paper Scissors"
            game_summary,p1_score,p2_score,draw=rps_run(t_round,p1_order,p2_order,game_no)
            gen_output(file_to_save_result,game,p1_order,p2_order,p1_score,p2_score,draw,game_summary,t_round)

        elif read_user==2:
            game="Rock Paper Scissors Lizard Spock"
            game_summary,p1_score,p2_score,draw=rpsls_run(t_round,p1_order,p2_order,game_no)
            gen_output(file_to_save_result,game,p1_order,p2_order,p1_score,p2_score,draw,game_summary,t_round)
    else:
        print("Order of age more than 10 is not real, Enter the order of agents less than or equal to 10")
        print("To run the simulation again, run the python3 console.py again ----- :) ")
        
        # ---------------------------------------------------------------------------------
