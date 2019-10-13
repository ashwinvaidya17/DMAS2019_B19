""" The main gamming console for the demonstration """

import os
from rps.rps import rps_run
from rpsls.rpsls import rpsls_run
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def data_plot(game_no,score_p1,score_p2,runs,p1_order,p2_order,game_choice):
	""" plotting the graph """
	game=""
	if game_choice==1:
		game="Rock Paper Scissor"
	elif game_choice==2:
		game="Rock Paper Scissor Lizard Spock"

	fig=plt.figure()
	ax=fig.add_subplot(111)
	r=np.arange(runs)
	ax.plot(r,score_p1,c='b',marker="^",ls='--',label="player1 (order: "+str(p1_order)+")",fillstyle='none')
	ax.plot(r,score_p2,c='m',marker="o",ls='-',label="player2 (order: "+str(p2_order)+")",fillstyle='none')
	ax.set_title(game +" "+"Game :"+str(game_no)+" result chart")
	ax.set_xlabel("Number of runs")
	ax.set_ylabel("player scores")
	plt.legend(loc=2)
	plt.show()



if __name__=="__main__":
 	# to remove the old files
	file_to_save_result="result.txt"
	temp1=1
	if file_to_save_result in os.listdir():
		os.remove(file_to_save_result)

	print("Welcome the Higher order TOM perform better than lower order TOM demonstration \n \
	Enter the Game of choice you want to play ----------------> \n \
	1. rock paper scissor \n \
	2. rock paper scissor lizard spock \n")
	read_user=int(input("Enter the Game of your choice 1 or 2:"))
	p1_order=int(input("Enter the player one order of agent (Eg : 0) :"))
	p2_order=int(input("Enter the player two order of agent (Eg : 2):"))
	t_run=int(input("Enter the total number of runs player need to compete (not less than 10 runs) eg: 20 :"))
	read_games=int(input("Enter the number of games players need to play eg: 5 :"))

	while temp1 <= read_games:
		if read_user==1:
			with open("result.txt",'a') as result:
				result.write("\n")
				result.write("Rock paper scissor Game " +str(temp1)+" result ")
				result.write("\n")
			print("\nRock paper scissor Game :",temp1)
			score_p1,score_p2=rps_run(t_run,p1_order,p2_order)

		elif read_user==2:
			with open("result.txt",'a') as result:
				result.write("Rock paper scissor lizard spock Game " +str(temp1)+" result ")
				result.write("\n")
			print("\nRock paper scissor lizard spock Game :",temp1)
			score_p1,score_p2=rpsls_run(t_run,p1_order,p2_order)

		data_plot(temp1,score_p1,score_p2,t_run,p1_order,p2_order,read_user) # graph plotting
		temp1+=1
