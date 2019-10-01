""" The main gamming console for the demonstration """

import os
from rps.rps import rps_run
from rpsls.rpsls import rpsls_run

if __name__=="__main__":

	# to remove the old files 
	file_to_save_result="result.txt" # output file
	if file_to_save_result in os.listdir():
		os.remove(file_to_save_result)
	
	print("Welcome the Higher order TOM perform better than lower order TOM demonstration \n \
	Enter the Game of choice you want to play ----------------> \n \
	1. rock paper scissor \n \
	2. rock paper scissor lizard spock \n")

	read_user=int(input("Enter your Game of choice 1 or 2:"))
	p1_order=int(input("Enter the player one order Eg : 0 (Means zero order agent) :"))
	p2_order=int(input("Enter the player two order Eg : 1 (Means first order agent") :"))
	t_run=int(input("Enter the total number of runs player need to compete (not less than 10 runs for rpsls and not less than 5 for rps game) eg: 20 :"))
	read_games=int(input("Enter the number of games players need to play eg: 5 :"))

	while read_games > 0:
		if read_user==1:
			with open("result.txt",'a') as result:
				result.write("\n")
				result.write("Rock paper scissor Game " +str(read_games)+" result ")
				result.write("\n")
			print("\nRock paper scissor Game :",read_games)	
			rps_run(t_run,p1_order,p2_order)

		elif read_user==2:
			with open("result.txt",'a') as result:
				result.write("Rock paper scissor lizard spock Game " +str(read_games)+" result ")
				result.write("\n")
			print("\nRock paper scissor lizard spock Game :",read_games)	
			rpsls_run(t_run,p1_order,p2_order)
		read_games-=1
