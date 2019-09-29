# DMAS2019_B19
This repository contains the Apha version submission for the Design of Multi-agent systems by the group ``B-19``. 

# Title : "Higher order Agents in zero sum game"

# Instructions 
## Game working principle
### Rock Paper Scissors
#### Approach 1
1. The game demo is between the zero order agent vs first order agent for 't' number of runs/rounds to the 'n' number of games.
2. The agents need to choose between on of the available choices as follows:         
    1. Rock 
    2. Scissor 
    3. Paper 
3. Each player needs to choose one of the above options. Based on the rules the player will win/lose.
4. The winner of the game is computed based on the cumulative score gained by each players in the 't' rounds/runs.
5. Players with the higerst score is determined as the winner.

### Rock Paper Scissors Lizard Spock
1. The game demo is between the zero order agent vs first order agent for 't' number of runs/rounds to the 'n' number of games.
2. The agents need to choose between on of the available choices as follows:         
    1. Rock 
    2. Scissor 
    3. Paper 
    4. Lizard 
    5. Spock
3. Each player needs to choose one of the above options. Based on the rules the player will win/lose.
4. The winner of the game is computed based on the cumulative score gained by each players in the 't' rounds/runs.
5. Players with the higerst score is determined as the winner.

## Running the Game
Both Rock paper scissor game and Rock paper scissor lizard spock game are integrated in the same console.

Follow the below steps to run the Game:

1. Navigate to the folder rps&rpsls in the linux terminal.
2. Run the game by typing ```python3 console.py``` in the linux terminal.
3. First you need to enter the "Game of choice"
    1. rock paper scissors
    2. rock paper scissors lizard spock
4. Then you need to enter the player one order (for this demo enter '0' for the player one).
5. After that, you need to enter the player Two order (for this demo enter '1' for the player two).
(Note : since the test is against the zero order and first order we need to make choices as mentiond in the step 3 and 4).
6.At the next step, you need to enter the number of rounds/runs that the agents need to play for one round (eg, 15 round/runs).
7.Then, you need to enter the number of Games that agents need to play (eg,5 games).
8.After the simulation ends, you find the ``result.txt`` file in the rsp&rpsls folder. which stores the result of the game.


## Blotto-game 
Go through the Readme.md in Blotto_game to run the blotto game. 

