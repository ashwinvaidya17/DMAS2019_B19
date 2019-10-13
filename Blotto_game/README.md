# Blotto Game(for 2 players)
This folder contains the necessary steps required to run simulation for Blotto game. Follow steps given below to run 2 player simulation of Blotto Game. Blotto Game for 2 players can also be run with frontend.

## Running without frontend 
### The simulation will run for 100 rounds 
   
1. To run the code without UI simulation
   Default command
   
   python 2playerssimulation.py --troops 8 --battlefields 3 --orderofagent1 3 --orderofagent2 1  --simulation 0

These are compulsory command line arguments.

- troops -> Number of troops

- battlefields -> Number of battlefields

- orderofagent1 -> Theory of mind order of the agent1  (Order of agent1 should be higher than agent2 for this experiment)

- orderofagent2 -> Theory of mind order of agent2

- simulation =  0 if you don't want to see UI simulation.
                1 if you want to see UI simulation
                
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

   python nplayersimulation.py --troops 16 --battlefields 6 --numberOfPlayers 4 --orderOfAgent 4,4,3,3 --simulation 0
   These are compulsory command line arguments
   - troops -> Number of troops
   
   - battlefields -> Number of battlefields
   
   - numberOfPlayers -> Number of Players 
   
   - orderOfAgent -> comma seperated theory of mind order of agents
   
   - simulation -> should be kept to 0
   
   

