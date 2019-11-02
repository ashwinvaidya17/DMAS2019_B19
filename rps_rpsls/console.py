""" The main gaming console for the demonstration """

import os
from rps.rps import rps_run
from rpsls.rpsls import rpsls_run
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def data_plot(game_no,score_p1,score_p2,match_draw,runs,p1_order,p2_order,game_choice):
    """ plotting the graph """
    game="" # Assigning the Games
    if game_choice==1:
	    game="Rock Paper Scissors"
    elif game_choice==2:
	    game="Rock Paper Scissors Lizard Spock"

    fig=plt.figure()
    ax=fig.add_subplot(111)
    r=np.arange(runs)
    ax.plot(r,score_p1,c='r',ls='-',label="Player1 (order: "+str(p1_order)+")",fillstyle='none')
    ax.plot(r,score_p2,c='b',ls='-.',label="Player2 (order: "+str(p2_order)+")",fillstyle='none')
    ax.plot(r,match_draw,c='k',ls='--',label="Draw matches",fillstyle='full')
    ax.set_title(game+" -- Game : "+str(game_no)+" result chart")
    ax.set_xlabel("Number of runs in Game "+str(game_no))
    ax.set_ylabel("player scores")
    ax.legend(loc='best')
    plt.show()

def result_plot(game_list,p1_scores,p2_scores,draws,p1_order,p2_order,game_choice,read_games,t_run):
    """ plotting the final result """
    if len(game_list) !=1:
        game=""
        if game_choice==1:
    	    game="Rock Paper Scissors"
        elif game_choice==2:
    	    game="Rock Paper Scissors Lizard Spock"

        fig=plt.figure()
        ax=fig.add_subplot(1, 1, 1)
        g=game_list
        ax.scatter(g,p1_scores,alpha=0.8,marker='X',c='g',edgecolors='none',s=30,label="Player1 (order: "+str(p1_order)+")")
        ax.scatter(g,p2_scores,alpha=0.8,marker='o',c='c',edgecolors='face',s=30,label="Player2 (order: "+str(p2_order)+")")
        ax.scatter(g,draws,alpha=0.8,marker='^',c='m',edgecolors='face',s=30,label="Draw matches")
        ax.set_title(game +" -- Final result chart For "+str(read_games)+" Games")
        ax.set_xlabel("Number of Games")
        ax.set_ylabel("player scores")
        ax.legend(loc='best')
        plt.show()

if __name__=="__main__":

    # to remove the old files
    temp1=1
    game_list=[]
    p1_score_list=[]
    p2_score_list=[]
    match_draw_list=[]
    file_to_save_result="result.txt"

    if file_to_save_result in os.listdir():
        os.remove(file_to_save_result)

    print("""Welcome to the Theory Of Mind (TOM) demonstration of Rock-Paper-Scissors and Rock-Paper-Scissors-Lizard-Spock Game
    Enter the Game of choice you want to play ---------------->
    1. rock paper scissors
    2. rock paper scissors lizard spock""")

    read_user=int(input("Enter the Game of your choice 1 or 2 :"))
    p1_order=int(input("Enter the order of agent for player one (Eg : 0) :"))
    p2_order=int(input("Enter the order of agent for player two (Eg : 2) :"))
    #p2_order=input("Enter the order of agent for player two (type : random) :")  # uncomment this line if the player2 is random player
    t_run=int(input("Enter the total number of runs/rounds players need to compete (not less than 20) eg: 50 :"))
    read_games=int(input("Enter the number of games players need to play (eg: 5) :"))
    while temp1 <= read_games:
        if read_user==1:
            with open("result.txt",'a') as result:
                result.write("\n")
                result.write("Rock paper scissors Game " +str(temp1)+" result ")
                result.write("\n")
            print("\nRock paper scissors Game :",temp1)
            score_p1,score_p2,match_draw,p1_score,p2_score,draw=rps_run(t_run,p1_order,p2_order,temp1)
        elif read_user==2:
            with open("result.txt",'a') as result:
                result.write("\n")
                result.write("Rock paper scissors lizard spock Game " +str(temp1)+" result ")
                result.write("\n")
            print("\nRock paper scissors lizard spock Game :",temp1)
            score_p1,score_p2,match_draw,p1_score,p2_score,draw=rpsls_run(t_run,p1_order,p2_order,temp1)

        game_list.append(temp1)
        p1_score_list.append(p1_score)
        p2_score_list.append(p2_score)
        match_draw_list.append(draw)
        data_plot(temp1,score_p1,score_p2,match_draw,t_run,p1_order,p2_order,read_user) # graph plotting for each game
        temp1+=1

    """print("Games list :",game_list)
    print("Player 1 score:",p1_score_list)
    print("Player 2 score :",p2_score_list)
    print("Draw matches :",match_draw_list)"""
    result_plot(game_list,p1_score_list,p2_score_list,match_draw_list,p1_order,p2_order,read_user,read_games,t_run) # Final result graph plot
