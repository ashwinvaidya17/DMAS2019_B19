# DMAS2019_B19
This repository contains the Final version submission for the Design of Multi-agent systems project by the group ``B-19``. 

# Title : "Higher Order Theory of Mind in RPS, RPLS and Blotto Game"

# Instructions 

### ROCK-PAPER-SCISSORS/LIZARD-SPOCK PROBABILITY APPROACH
Both Rock paper scissor game and Rock paper scissor lizard spock game are integrated in the same console.

Follow the below steps to run the Game:

1. Navigate to the folder rps_rpsls by typing ```cd 'rps_rpsls' ``` in the linux terminal\windows cmd prompt.
2. Run the game by typing ```python3 console.py``` in the linux terminal.
3. First you need to enter the "Game of choice"
    1. rock paper scissors
    2. rock paper scissors lizard spock
4. Then you need to enter the order of agent for player one as prompted in the console.
5. After that, you need to enter the order of agent for player two as prompted in the console.
6. At the next step, you need to enter the number of rounds/runs that the agents need to play for one round (eg, 50 round/runs).
7. Then, you need to enter the number of Games that agents need to play (eg,5 games).
8. After the simulation ends, you find the ``result.txt`` file in the rsp_rpsls folder, which stores the result of the game.
#### Note: Please enter the number of games of less than five since the code generates graph for each individual game

## Rock Paper Scissors - Probability and Elemental Analysis approach

Follow the steps to run the game:
1. Navigate to the directory Rock_Paper_Scissor_Approach_2 in the linux terminal.
2. Run the file ```Launch_RPS_Game_approach_2.py``` in the linux terminal.
3. Choose the order of player 1 (You can choose any order).
4. Choose the order of player 2 (You can choose any order).
5. Choose total number of games (eg: 5).
6. Choose total number of rounds per game, should be greater than 5 (eg: 15).
7. After each game a line graph will appear, which will show player's score with respect to rounds.
8. After the simulation ends, results of each game will appear in the form of scatter plot.

# Blotto-game 
  Go to Blotto_game folder to run the Blotto Game simulation.
  #### Note: For the pratical purposes we have consider TOM order of agents to be <=5. If you give the TOM order >5, then it will consider the max i.e. 5.
  ## Blotto Game(for 2 players)
 Follow steps given below to run 2 player simulation of Blotto Game.
### The simulation will run for 100 rounds
   Default command
   
   python 2playerssimulation.py --troops 8 --battlefields 3 --orderofagent1 3 --orderofagent2 1 --strategy 3

These are compulsory command line arguments.
- troops -> Number of troops
- battlefields -> Number of battlefields
- orderofagent1 -> Theory of mind order of the agent1  (Order of agent1 should be higher than agent2 for this experiment)
- orderofagent2 -> Theory of mind order of agent2
- strategy =    1 for Random Strategy
                2 for Most Optimal Winning Strategy
                3 for Random Winning Strategy
#### Results are also added to 2playersResult.txt file                
## Blotto Game(for n players)
Follow the steps given below to run n player simulation for Blotto game.
### The simulation will run for 100 rounds
Default command 

   python nplayersimulation.py --troops 16 --battlefields 6 --numberOfPlayers 4 --orderOfAgent 2,2,1,1  --strategy 3
   
   These are compulsory command line arguments
   - troops -> Number of troops
   - battlefields -> Number of battlefields
   - numberOfPlayers -> Number of Players 
   - orderOfAgent -> comma seperated theory of mind order of agents
   - strategy =    1 for Random Strategy
                   2 for Most Optimal Winning Strategy
                   3 for Random Winning Strategy
#### Results are also added to nplayersResult.txt file                 
   
   



