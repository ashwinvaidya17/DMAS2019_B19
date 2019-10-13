import random, time
import player_action as pa

# Initialize global variable:
end_round_time = 0.5 # How much time at the end of each round, the user waits (1->1 seconds)
end_of_games = 16 # Number of rounds
tie_match = 0
player_1_wins = 0
player_2_wins = 0
# Rock paper scissor game have 2 players and 3 options:
player_1_choices = ["Rock", "Paper", "Scissor"]
player_2_choices = ["Rock", "Paper", "Scissor"]

# This function calls the functions for first 5 games and next number of round & at end it will show results
def rock_paper_scissor(player_1_order, player_2_order):
    print("This module will be used for rps Game")
    first_five_games_rps(player_1_order, player_2_order)
    for numberOfGames in range (6, end_of_games):
        next_iterative_games_rps(player_1_order, player_2_order, numberOfGames)
    result_rps()

# This function will beused after 5 games for choosing the choises based on Theory of mind
def next_iterative_games_rps(player_1_order, player_2_order, numberOfGames):
    print(f"\n-----------------Round {numberOfGames}-----------------")

    # From iteration_order, player_action.py knows which player is choosing first
    # and in player_action.py, iteration_order is received by catch_order
    iteration_order = 1
    player_1_chooses = pa.player_will_choose(player_1_order, iteration_order) # Based on order, the choice will be made from player_1_will_choose()
    pa.player_1_memory.append(player_1_chooses) # The Choice will be added to the list: player_1_memory
    print("Player 1 Choice: " + player_1_chooses)

    iteration_order = 2
    player_2_chooses = pa.player_will_choose(player_2_order, iteration_order) # Based on order, the choice will be made from player_2_will_choose()
    pa.player_2_memory.append(player_2_chooses) # The Choice will be added to the list: player_2_memory
    print("Player 2 Choice: " + player_2_chooses)

    # To call rps_rule() which will decide the winner
    rps_rule(player_1_chooses, player_2_chooses, player_1_order, player_2_order)

    print(f"-------------End of Round {numberOfGames}--------------")
    time.sleep(end_round_time)

# The first five games are used to collect the player's choices in the player memmory
def first_five_games_rps(player_1_order, player_2_order):
    for i in range(1, 6):
        print(f"\n-----------------Round {i}-----------------")
        # Player 1 will choose randomly for the first 5 games and will append the choice in the player's memory
        player_1_chooses = random.choice(player_1_choices)
        pa.player_1_memory.append(player_1_chooses)
        print("Player 1 Choice: " + player_1_chooses)
        
        # Player 2 will choose randomly for the first 5 games and will append the choice in the player's memory
        player_2_chooses = random.choice(player_2_choices)
        pa.player_2_memory.append(player_2_chooses)
        print("Player 2 Choice: " + player_2_chooses)

        # To call rps_rule() which will decide the winner
        rps_rule(player_1_chooses, player_2_chooses, player_1_order, player_2_order)

        print(f"-------------End of Round {i}--------------")
        time.sleep(end_round_time)

# This function determines the result of the round. 
# It is also used to increse the percent of confidence if the player won.
def rps_rule(player_1_chooses, player_2_chooses, player_1_order, player_2_order):
    global tie_match, player_1_wins, player_2_wins
    
    # Tie match condition
    if player_1_chooses == player_2_chooses:
            print("Its a Tie")
            tie_match += 1

    elif player_1_chooses == "Rock":
        if player_2_chooses == "Scissor":
            print("Player 1 Wins")
            player_1_wins += 1
            # Increse the confidence if player 1 is first order
            if player_1_order >= 1 and pa.player_1_confidence < 1.0:
                pa.player_1_confidence += 0.1
            # Decrease the confidence if player 2 is first order    
            if player_2_order >= 1 and pa.player_2_confidence > 0.0:
                pa.player_2_confidence -= 0.1
                
        else:
            print("Player 2 Wins")
            player_2_wins += 1
            if player_2_order >= 1 and pa.player_2_confidence < 1.0:
                pa.player_2_confidence += 0.1
                
            if player_1_order >= 1 and pa.player_1_confidence > 0.0:
                pa.player_1_confidence -= 0.1
                

    elif player_1_chooses == "Paper":
        if player_2_chooses == "Rock":
            print("Player 1 Wins")
            player_1_wins += 1
            if player_1_order >= 1 and pa.player_1_confidence < 1.0:
                pa.player_1_confidence += 0.1
                
            if player_2_order >= 1 and pa.player_2_confidence > 0.0:
                pa.player_2_confidence -= 0.1
                
        else:
            print("Player 2 Wins")
            player_2_wins += 1
            if player_2_order >= 1 and pa.player_2_confidence < 1.0:
                pa.player_2_confidence += 0.1
                
            if player_1_order >= 1 and pa.player_1_confidence > 0.0:
                pa.player_1_confidence -= 0.1 
                

    elif player_1_chooses == "Scissor":
        if player_2_chooses == "Paper":
            print("Player 1 Wins")
            player_1_wins += 1
            if player_1_order >= 1 and pa.player_1_confidence < 1.0:
                pa.player_1_confidence += 0.1
                
            if player_2_order >= 1 and pa.player_2_confidence > 0.0:
                pa.player_2_confidence -= 0.1
                
        else:
            print("Player 2 Wins")
            player_2_wins += 1
            if player_2_order >= 1 and pa.player_2_confidence < 1.0:
                pa.player_2_confidence += 0.1
                
            if player_1_order >= 1 and pa.player_1_confidence > 0.0:
                pa.player_1_confidence -= 0.1
                
    # If the player 1 confidence Increases after 100%, make it equal to 100%
    if pa.player_1_confidence > 1.0:
        pa.player_1_confidence = 1.0
    # If the player 1 confidence decreases after 0%, make it equal to 0%
    if pa.player_1_confidence < 0.0:
        pa.player_1_confidence = 0.0
    # If the player 2 confidence Increases after 100%, make it equal to 100%
    if pa.player_2_confidence > 1.0:
        pa.player_2_confidence = 1.0
    # If the player 2 confidence decreases after 0%, make it equal to 0%
    if pa.player_2_confidence < 0.0:
        pa.player_2_confidence = 0.0
    
    # print the confidence in percentage
    if player_1_order > 0:
        print(f"Player 1 confidence: {int(pa.player_1_confidence*100)}%")
    if player_2_order > 0:
        print(f"Player 2 confidence: {int(pa.player_2_confidence*100)}%")
    
        
# This function will show the end result of all rounds
def result_rps():
    print("\n----------------Result------------------")
    print(f"number of tie match: {tie_match}")
    print(f"number of times player 1 won: {player_1_wins}")
    print(f"number of times player 2 won: {player_2_wins}")

    # Print the data set of players
    print(pa.player_1_memory)
    print(pa.player_2_memory)