import random

# Initalize empty memory of player
player_2_memory = []
player_1_memory = []
# player confidence at the starting of the game between 10% and 90%
player_1_confidence = round(random.uniform(0.1,0.9), 1)
player_2_confidence = round(random.uniform(0.1,0.9), 1)
player_confidence = round(random.uniform(0.1,0.9), 1)

# Initialize global variable = 0
player_loop_number = 0
player_thinks_rock_probability = 0.0
player_thinks_paper_probability = 0.0
player_thinks_scissor_probability = 0.0
player_confidence_on_rock = 0.0
player_confidence_on_paper = 0.0
player_confidence_on_scissor = 0.0

# This function uses Theory of Mind, in which player looks at opponent or own data set and 
# calculate the probability of repeating elements
def player_thinks_probability(player_order, catch_order):
    global player_thinks_rock_probability, player_thinks_paper_probability, player_thinks_scissor_probability, player_2_order, player_1_order
    
    # catch_order = 1, means Player 1 will choose first
    if catch_order == 1:
        player_1_order = player_order
        
        # If player_1_order = even number (0,2,4,6,...) player will look at opponent data set and
        # calculate the probability of repeating elements
        if player_1_order%2 == 0:
            player_thinks_rock_probability = player_2_memory.count("Rock") / len(player_2_memory)
            player_thinks_paper_probability = player_2_memory.count("Paper") / len(player_2_memory)
            player_thinks_scissor_probability = player_2_memory.count("Scissor") / len(player_2_memory)
        # Else player will look at own data set and 
        # calculate the probability of repeating elements
        else:
            player_thinks_rock_probability = player_1_memory.count("Rock") / len(player_1_memory)
            player_thinks_paper_probability = player_1_memory.count("Paper") / len(player_1_memory)
            player_thinks_scissor_probability = player_1_memory.count("Scissor") / len(player_1_memory)
    
    # catch_order = 2, means Player 2 will choose Second
    elif catch_order == 2:
        player_2_order = player_order
        
        # If player_1_order = even number (0,2,4,6,...) player will look at opponent data set and
        # calculate the probability of repeating elements
        if player_2_order%2 == 0:

            # Note:  we need to decrease the length to length--, because till the time player 2 will choose, 
            # player 1 has already choosen. Hence, decreasing the length
            player_thinks_rock_probability = player_1_memory[0:(len(player_1_memory)-1)].count("Rock") / (len(player_1_memory)-1)
            player_thinks_paper_probability = player_1_memory[0:(len(player_1_memory)-1)].count("Paper") / (len(player_1_memory)-1)
            player_thinks_scissor_probability = player_1_memory[0:(len(player_1_memory)-1)].count("Scissor") / (len(player_1_memory)-1)
        # Else player will look at own data set and 
        # calculate the probability of repeating elements
        else:
            player_thinks_rock_probability = player_2_memory.count("Rock") / len(player_2_memory)
            player_thinks_paper_probability = player_2_memory.count("Paper") / len(player_2_memory)
            player_thinks_scissor_probability = player_2_memory.count("Scissor") / len(player_2_memory)

# This function calculate what element is supposed to choose from probability
def player_choose_from_probability(player_confidence_assume, player_order, player_thinks_rock_probability, player_thinks_paper_probability, player_thinks_scissor_probability):
    global player_choose_rock, player_choose_paper, player_choose_scissor, player_loop_number    
    
    # Suppose the probability of rock is the highest from player_thinks_probability(), 
    # then player_choose_paper will have the highest value from below formula, hence player will choose paper
    player_choose_rock = (player_thinks_rock_probability*0)+(player_thinks_paper_probability*(-1))+(player_thinks_scissor_probability*1) 
    player_choose_paper = (player_thinks_rock_probability*(1))+(player_thinks_paper_probability*(0))+(player_thinks_scissor_probability*(-1))
    player_choose_scissor = (player_thinks_rock_probability*(-1))+(player_thinks_paper_probability*(1))+(player_thinks_scissor_probability*0)
    
    # if player_order == 0, then it will not call player_confidence_from_choice()
    # At the start player_loop_number will be 0, it will increase in player_confidence_from_choice()
    if player_order > player_loop_number:
        player_confidence_from_choice(player_confidence_assume, player_order, player_thinks_rock_probability, player_thinks_paper_probability, player_thinks_scissor_probability)

# The player uses his confidence to make sure his opponent will choose a perticular element
# This function is only applicable for order of agents > 0
def player_confidence_from_choice(player_confidence_assume, player_order, rock_multily, paper_multiply, scissor_multiply):
    global player_confidence_on_rock, player_confidence_on_paper, player_confidence_on_scissor, player_loop_number
    
    # The agent will confirm that his opponent has choosen a perticular elemrnt from his confidence
    # and then will call player_choose_from_probability() to make the decision to what element to choose
    if player_choose_rock > player_choose_paper and player_choose_rock > player_choose_scissor:
        player_confidence_on_rock = ((1-player_confidence_assume)*rock_multily) + player_confidence_assume
        player_confidence_on_paper = ((1-player_confidence_assume)*paper_multiply)
        player_confidence_on_scissor = ((1-player_confidence_assume)*scissor_multiply)

    elif player_choose_paper > player_choose_rock and player_choose_paper > player_choose_scissor:
        player_confidence_on_rock = ((1-player_confidence_assume)*rock_multily)
        player_confidence_on_paper = ((1-player_confidence_assume)*paper_multiply) + player_confidence_assume
        player_confidence_on_scissor = ((1-player_confidence_assume)*scissor_multiply)

    elif player_choose_scissor > player_choose_rock and player_choose_scissor > player_choose_paper:
        player_confidence_on_rock = ((1-player_confidence_assume)*rock_multily)
        player_confidence_on_paper = ((1-player_confidence_assume)*paper_multiply)
        player_confidence_on_scissor = ((1-player_confidence_assume)*scissor_multiply) + player_confidence_assume

    elif player_choose_rock == player_choose_paper and player_choose_rock == player_choose_scissor:
        player_confidence_on_rock = 0
        player_confidence_on_paper = player_confidence_on_rock
        player_confidence_on_scissor = player_confidence_on_rock
    
    player_loop_number = player_loop_number + 1 
    
    player_choose_from_probability(player_confidence_assume, player_order, player_confidence_on_rock, player_confidence_on_paper, player_confidence_on_scissor)
        
# if the calculated number from probability/confidence is max for that element then choose that element
# else choose random 
def player_chooses_finally():
    global player_choice_is
    if player_choose_rock > player_choose_paper and player_choose_rock > player_choose_scissor:
        player_choice_is = "Rock"

    elif player_choose_paper > player_choose_rock and player_choose_paper > player_choose_scissor:
        player_choice_is = "Paper"

    elif player_choose_scissor > player_choose_rock and player_choose_scissor > player_choose_paper:
        player_choice_is = "Scissor"

    elif player_choose_rock == player_choose_scissor and player_choose_rock == player_choose_paper:
        player_choice_is = random.choice(["Rock", "Paper", "Scissor"])
    
# From the order the player will return the choice
def player_will_choose(player_order, catch_order):   
    global player_loop_number, player_confidence
    player_loop_number = 0 
    player_confidence_assume = round(random.uniform(0.1,0.9), 1)

    # To calculate the probability of repeating elements
    # catch_order will store the value of iteration_order from Rock_paper_Scissor_Game.py
    player_thinks_probability(player_order, catch_order)   

    # To calculate what is to be choose from probability
    player_choose_from_probability(player_confidence_assume, player_order, player_thinks_rock_probability, player_thinks_paper_probability, player_thinks_scissor_probability)

    # To calculate which element is benificial to play next
    player_chooses_finally()

    return player_choice_is
