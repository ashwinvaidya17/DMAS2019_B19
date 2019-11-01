# DMAS2019_B19
This repository contains the Final version submission for the Design of Multi-agent systems project by the group ``B-19``. 

# Title : "Higher Order Theory of Mind in RPS, RPLS and Blotto Game"

# Instructions 
## Game working principle
#### Probability Approach
### Rock Paper Scissors
1. The game demo is between the n order agent vs n order agent, in 't' number of runs/rounds for the 'n' number of games.
2. The agents need to choose between on of the available choices as follows:         
    1. Rock 
    2. Scissor 
    3. Paper 
3. Each player needs to choose one of the above options. Based on the rules the player will win/lose.
4. The winner of the game is computed based on the cumulative score gained by each players in the 't' rounds/runs.
5. Players with the higerst score is determined as the winner.

### Rock Paper Scissors Lizard Spock
1. The game demo is between n order agent vs n order agent, in 't' number of runs/rounds for the 'n' number of games.
2. The agents need to choose between on of the available choices as follows:         
    1. Rock 
    2. Scissor 
    3. Paper 
    4. Lizard 
    5. Spock
3. Each player needs to choose one of the above options. Based on the rules the player will win/lose.
4. The winner of the game is computed based on the cumulative score gained by each players in the 't' rounds/runs.
5. Players with the higerst score is determined as the winner.

### Running the Game
Both Rock paper scissor game and Rock paper scissor lizard spock game are integrated in the same console.

Follow the below steps to run the Game:

1. Navigate to the folder rps&rpsls by typing ```cd 'rps&rpsls' ``` in the linux terminal.
2. Run the game by typing ```python3 console.py``` in the linux terminal.
3. First you need to enter the "Game of choice"
    1. rock paper scissors
    2. rock paper scissors lizard spock
4. Then you need to enter the order of agent for player one as prompted in the console.
5. After that, you need to enter the order of agent for player Two as prompted in the console.
6. At the next step, you need to enter the number of rounds/runs that the agents need to play for one round (eg, 50 round/runs).
7. Then, you need to enter the number of Games that agents need to play (eg,5 games).
8. After the simulation ends, you find the ``result.txt`` file in the rsp&rpsls folder, which stores the result of the game.
#### Note: Please enter the number of games of less than five since the code generates graph 

## Rock Paper Scissors - Probability and Elemental Analysis approach

Follow the steps to run the game:
1. Navigate to the directory Rock_Paper_Scissor_Approach_2 in the linux terminal.
2. Run the file ```Launch_RPS_Game_approach_2.py``` in the linux terminal.
3. Choose the order of player 1 (You can choose any order).
4. Choose the order of player 2 (You can choose any order).



## Blotto-game 
  Go to Blotto_game folder to run the Blotto Game simulation
  # Blotto Game(for 2 players)
 Follow steps given below to run 2 player simulation of Blotto Game. Blotto Game for 2 players can also be run with frontend.

## Running without frontend 
### The simulation will run for 100 rounds 
   
   To run the code without UI simulation
   Default command
   
   python 2playerssimulation.py --troops 8 --battlefields 3 --orderofagent1 3 --orderofagent2 1  --simulation 0 --strategy 3

These are compulsory command line arguments.

- troops -> Number of troops

- battlefields -> Number of battlefields

- orderofagent1 -> Theory of mind order of the agent1  (Order of agent1 should be higher than agent2 for this experiment)

- orderofagent2 -> Theory of mind order of agent2

- simulation =  0 if you don't want to see UI simulation.
                1 if you want to see UI simulation
                
- strategy =    1 for Random Strategy
                2 for Most Optimal Winning Strategy
                3 for Random Winning Strategy
                
 ## Running with frontend    
 ### The simulation will run for 1 round 
 #### Requirements linux 64 bit system
 #### Steps
 1. Go to main folder.
 2. Copy Linux.tar.xz to the current folder  
 3. Extract the contents using the command tar -xvzf Linux.tar.xz
 4. Copy blotto_game.x86_64 from Linux folder (This is the Linux build for the Frontend) and keep it current folder.
 5. Make sure blotto_game.x86_64 has executable permissions.
 6. run in the terminal command 'sh run.sh' 

# Blotto Game(for n players)
Follow the steps given below to run n player simulation for Blotto game. Blotto game for n players.
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
   
   



