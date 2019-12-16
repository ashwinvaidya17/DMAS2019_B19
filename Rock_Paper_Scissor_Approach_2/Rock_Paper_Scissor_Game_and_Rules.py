import random
from datetime import datetime
from tabulate import tabulate
import player_action as pa

# Initialize global variable:
tie_match = 0
player_1_wins = 0
player_2_wins = 0
# Rock paper scissor game have 2 players and 3 options:
player_1_choices = ["Rock", "Paper", "Scissor"]
player_2_choices = ["Rock", "Paper", "Scissor"]

tie_match_array = []
player_1_wins_array = []
player_2_wins_array = []

final_tie_match = []
final_player_1_wins = []
final_player_2_wins = []
change_1 = 0
change_2 = 0


# This function calls the functions for first 5 games and next number of round & at the end it will show results
def rock_paper_scissor(player_1_order, player_2_order, max_rounds):
    global tie_match_array, player_1_wins_array, player_2_wins_array, tie_match, player_2_wins, player_1_wins
    print("This module will be used for rps Game")
    # After each game initialize variable to 0 or empty list
    tie_match = 0
    player_1_wins = 0
    player_2_wins = 0

    pa.player_1_memory = []
    pa.player_2_memory = []
    tie_match_array = []
    player_1_wins_array = []
    player_2_wins_array = []

    first_five_games_rps(player_1_order, player_2_order)
    for numberOfRounds in range(6, max_rounds + 1):
        next_iterative_games_rps(player_1_order, player_2_order, numberOfRounds)
    result_rps(player_1_order, player_2_order)

    # This will plot scatter graph of final result


# This function will be used after 5 games for choosing the choices based on Theory of mind
def next_iterative_games_rps(player_1_order, player_2_order, numberOfRounds):
    print(f"\n-----------------Round {numberOfRounds}-----------------")

    # From iteration_order, player_action.py knows which player is choosing first
    # and in player_action.py, iteration_order is received by catch_order
    iteration_order = 1
    player_1_chooses = pa.p_will_choose(player_1_order, iteration_order)  # Based on order, the choice will be made from player_1_will_choose()
    print(f"last 10 DataSet for player 1: {pa.p_1_memory[-pa.limit:]}")
    pa.p_1_memory.append(player_1_chooses)  # The Choice will be added to the list: player_1_memory
    # print("Player 1 Choice: " + player_1_chooses)
    print(f"Player 1 Choice: {player_1_chooses}")

    iteration_order = 2
    player_2_chooses = pa.p_will_choose(player_2_order, iteration_order)  # Based on order, the choice will be made from player_2_will_choose()
    print(f"last 10 DataSet for player 2: {pa.p_2_memory[-pa.limit:]}")
    pa.p_2_memory.append(player_2_chooses)  # The Choice will be added to the list: player_2_memory
    # print("Player 2 Choice: " + player_2_chooses)
    print(f"Player 2 Choice: {player_2_chooses}")

    # To call rps_rule() which will decide the winner
    rps_rule(player_1_chooses, player_2_chooses, player_1_order, player_2_order)
    print(f"-------------End of Round {numberOfRounds}--------------")
    # time.sleep(end_round_time)


# The first five games are used to collect the player's choices in the player memmory
def first_five_games_rps(player_1_order, player_2_order):
    #random.seed(0)
    for i in range(1, 6):
        print(f"\n-----------------Round {i}-----------------")
        # Player 1 will choose randomly for the first 5 games and will append the choice in the player's memory

        player_1_chooses = random.choice(player_1_choices)
        pa.p_1_memory.append(player_1_chooses)
        print("Player 1 Choice: " + player_1_chooses)

        # Player 2 will choose randomly for the first 5 games and will append the choice in the player's memory

        player_2_chooses = random.choice(player_2_choices)
        pa.p_2_memory.append(player_2_chooses)
        print("Player 2 Choice: " + player_2_chooses)

        # To call rps_rule() which will decide the winner
        rps_rule(player_1_chooses, player_2_chooses, player_1_order, player_2_order)

        print(f"-------------End of Round {i}--------------")
        # time.sleep(end_round_time)


# This function determines the result of the round.
# It is also used to increase the percent of confidence if the player won.
def rps_rule(player_1_chooses, player_2_chooses, player_1_order, player_2_order):
    global tie_match, player_1_wins, player_2_wins, tie_match_array, player_1_wins_array, player_2_wins_array, change_1, change_2

    # Tie match condition
    if player_1_chooses == player_2_chooses:
        print("Its a Tie")
        tie_match += 1

    elif player_1_chooses == "Rock":
        if player_2_chooses == "Scissor":
            print("Player 1 Wins")
            player_1_wins += 1

            # Increase the confidence if player 1 is first order
            if player_1_order >= 1 and pa.p_1_confidence < 1.0:
                pa.p_1_confidence += 0.1
            # Decrease the confidence if player 2 is first order
            if player_2_order >= 1 and pa.p_2_confidence > 0.0:
                pa.p_2_confidence -= 0.1

        else:
            print("Player 2 Wins")
            player_2_wins += 1

            if player_2_order >= 1 and pa.p_2_confidence < 1.0:
                pa.p_2_confidence += 0.1

            if player_1_order >= 1 and pa.p_1_confidence > 0.0:
                pa.p_1_confidence -= 0.1


    elif player_1_chooses == "Paper":
        if player_2_chooses == "Rock":
            print("Player 1 Wins")
            player_1_wins += 1

            if player_1_order >= 1 and pa.p_1_confidence < 1.0:
                pa.p_1_confidence += 0.1

            if player_2_order >= 1 and pa.p_2_confidence > 0.0:
                pa.p_2_confidence -= 0.1

        else:
            print("Player 2 Wins")
            player_2_wins += 1

            if player_2_order >= 1 and pa.p_2_confidence < 1.0:
                pa.p_2_confidence += 0.1

            if player_1_order >= 1 and pa.p_1_confidence > 0.0:
                pa.p_1_confidence -= 0.1


    elif player_1_chooses == "Scissor":
        if player_2_chooses == "Paper":
            print("Player 1 Wins")
            player_1_wins += 1

            if player_1_order >= 1 and pa.p_1_confidence < 1.0:
                pa.p_1_confidence += 0.1

            if player_2_order >= 1 and pa.p_2_confidence > 0.0:
                pa.p_2_confidence -= 0.1

        else:
            print("Player 2 Wins")
            player_2_wins += 1

            if player_2_order >= 1 and pa.p_2_confidence < 1.0:
                pa.p_2_confidence += 0.1

            if player_1_order >= 1 and pa.p_1_confidence > 0.0:
                pa.p_1_confidence -= 0.1

    # If the player 1 confidence Increases after 100%, make it equal to 100%
    if pa.p_1_confidence > 1.0:
        pa.p_1_confidence = 1.0
    # If the player 1 confidence decreases after 0%, make it equal to 0%
    if pa.p_1_confidence < 0.0:
        pa.p_1_confidence = 0.0
    # If the player 2 confidence Increases after 100%, make it equal to 100%
    if pa.p_2_confidence > 1.0:
        pa.p_2_confidence = 1.0
    # If the player 2 confidence decreases after 0%, make it equal to 0%
    if pa.p_2_confidence < 0.0:
        pa.p_2_confidence = 0.0

    # print the confidence in percentage
    if player_1_order > 0:
        print(f"Player 1 confidence: {int(pa.p_1_confidence * 100)}%")
    if player_2_order > 0:
        print(f"Player 2 confidence: {int(pa.p_2_confidence * 100)}%")

    tie_match_array.append(tie_match)
    player_1_wins_array.append(player_1_wins)
    player_2_wins_array.append(player_2_wins)


# This function will show the end result of all rounds
def result_rps(player_1_order, player_2_order):
    print("\n----------------Result------------------")
    print(f"number of tie match: {tie_match}")
    print(f"number of times player 1 won: {player_1_wins}")
    print(f"number of times player 2 won: {player_2_wins}")

    final_tie_match.append(tie_match)
    final_player_1_wins.append(player_1_wins)
    final_player_2_wins.append(player_2_wins)
    # Print the data set of players
    print(pa.p_1_memory)
    print(pa.p_2_memory)

    p_1_order_title = "th"
    if player_1_order == 1:
        p_1_order_title = "st"
    elif player_1_order == 2:
        p_1_order_title = "nd"
    elif player_1_order == 3:
        p_1_order_title = "rd"

    p_2_order_title = "th"
    if player_2_order == 1:
        p_2_order_title = "st"
    elif player_2_order == 2:
        p_2_order_title = "nd"
    elif player_2_order == 3:
        p_2_order_title = "rd"

    results = [(tie_match, player_1_wins, player_2_wins)]
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    dt_object = datetime.fromtimestamp(timestamp)
    f = open(f"rps_approach2_results.txt", "a+")
    f.writelines(f"\n")
    f.writelines(f"RPS Results between Player 1 as {player_1_order}{p_1_order_title}-order & Player 2 as {player_2_order}{p_2_order_title}-order |---| {dt_object}")
    f.writelines(f"\n")
    f.writelines(tabulate(results, headers=["Draw Matches", "Player 1 wins", "Player 2 wins"]))
    f.writelines("\n------------------------------------------------\n")
    f.close()
