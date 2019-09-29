import random
import player_1_action as p1a

player_2_memory = []
# player confidence at the starting of the game between 10% and 90% (but only first order will use)
player_2_confidence = round(random.uniform(0.1,0.9), 1)
player_2_thinks_rock_probability = 0.0
player_2_thinks_paper_probability = 0.0
player_2_thinks_scissor_probability = 0.0

# From the order the player will return the choise
def player_2_will_choose(player_order):
    if player_order == 0:
        zero_order_player_2_thinks_probability()    # To calculate the probability of repeating elements
        player_2_choose_from_probability()  # To calculate what is to be choose from probability
        player_2_chooses_finally()  # To calculate which element is benificial to play next
        return player_2_choice_is

    elif player_order == 1:
        first_order_player_2_thinks_probability()   # To calculate the probability of repeating elements
        player_2_choose_from_probability()  # To calculate what is to be choose from probability
        player_2_confidence_from_choice()   # To calculate what opponent will choose
        player_2_choose_from_confidence()   # To calculate what is to be choose from Confidence
        player_2_chooses_finally()   # To calculate which element is benificial to play next
        return player_2_choice_is

# This function uses zeroth order Theory of Mind, in which player looks at opponent data set and 
# calculate the probability of repeating elements
def zero_order_player_2_thinks_probability():
    # we have to decrase the length of data set, as at the time this functions gets invoked 
    # the opponent's data set lenght gets inceased by 1
    global player_2_thinks_rock_probability, player_2_thinks_paper_probability, player_2_thinks_scissor_probability
    player_2_thinks_rock_probability = p1a.player_1_memory[0:(len(p1a.player_1_memory)-1)].count("Rock") / (len(p1a.player_1_memory)-1)
    player_2_thinks_paper_probability = p1a.player_1_memory[0:(len(p1a.player_1_memory)-1)].count("Paper") / (len(p1a.player_1_memory)-1)
    player_2_thinks_scissor_probability = p1a.player_1_memory[0:(len(p1a.player_1_memory)-1)].count("Scissor") / (len(p1a.player_1_memory)-1)

# This function uses first order Theory of Mind, in which player looks at their own data set and 
# calculate the probability of repeating elements
def first_order_player_2_thinks_probability():
    global player_2_thinks_rock_probability, player_2_thinks_paper_probability, player_2_thinks_scissor_probability
    player_2_thinks_rock_probability = player_2_memory.count("Rock") / len(player_2_memory)
    player_2_thinks_paper_probability = player_2_memory.count("Paper") / len(player_2_memory)
    player_2_thinks_scissor_probability = player_2_memory.count("Scissor") / len(player_2_memory)

# This function calculate what element is supposed to choose from probability
def player_2_choose_from_probability():
    global player_2_choose_rock, player_2_choose_paper, player_2_choose_scissor
    player_2_choose_rock = (player_2_thinks_rock_probability*0)+(player_2_thinks_paper_probability*(-1))+(player_2_thinks_scissor_probability*1) 
    player_2_choose_paper = (player_2_thinks_rock_probability*(1))+(player_2_thinks_paper_probability*(0))+(player_2_thinks_scissor_probability*(-1))
    player_2_choose_scissor = (player_2_thinks_rock_probability*(-1))+(player_2_thinks_paper_probability*(1))+(player_2_thinks_scissor_probability*0)

# The player uses his confidence to make sure his opponent will choose a perticular element
def player_2_confidence_from_choice():
    global player_2_confidence_on_rock, player_2_confidence_on_paper, player_2_confidence_on_scissor
    if player_2_choose_rock > player_2_choose_paper and player_2_choose_rock > player_2_choose_scissor:
        player_2_confidence_on_rock = ((1-player_2_confidence)*p1a.player_1_thinks_rock_probability) + player_2_confidence
        player_2_confidence_on_paper = ((1-player_2_confidence)*p1a.player_1_thinks_paper_probability)
        player_2_confidence_on_scissor = ((1-player_2_confidence)*p1a.player_1_thinks_scissor_probability)

    elif player_2_choose_paper > player_2_choose_rock and player_2_choose_paper > player_2_choose_scissor:
        player_2_confidence_on_rock = ((1-player_2_confidence)*p1a.player_1_thinks_rock_probability)
        player_2_confidence_on_paper = ((1-player_2_confidence)*p1a.player_1_thinks_paper_probability) + player_2_confidence
        player_2_confidence_on_scissor = ((1-player_2_confidence)*p1a.player_1_thinks_scissor_probability)

    elif player_2_choose_scissor > player_2_choose_rock and player_2_choose_scissor > player_2_choose_paper:
        player_2_confidence_on_rock = ((1-player_2_confidence)*p1a.player_1_thinks_rock_probability)
        player_2_confidence_on_paper = ((1-player_2_confidence)*p1a.player_1_thinks_paper_probability)
        player_2_confidence_on_scissor = ((1-player_2_confidence)*p1a.player_1_thinks_scissor_probability) + player_2_confidence

    elif player_2_choose_rock == player_2_choose_paper and player_2_choose_rock == player_2_choose_scissor:
        player_2_confidence_on_rock = 0
        player_2_confidence_on_paper = player_2_confidence_on_rock
        player_2_confidence_on_scissor = player_2_confidence_on_rock

# This function calculate what element will the first order player will choose from confidence
def player_2_choose_from_confidence():
    global player_2_choose_rock, player_2_choose_paper, player_2_choose_scissor
    player_2_choose_rock = (player_2_confidence_on_rock*0)+(player_2_confidence_on_paper*(-1))+(player_2_confidence_on_scissor*1) 
    player_2_choose_paper = (player_2_confidence_on_rock*(1))+(player_2_confidence_on_paper*(0))+(player_2_confidence_on_scissor*(-1))
    player_2_choose_scissor = (player_2_confidence_on_rock*(-1))+(player_2_confidence_on_paper*(1))+(player_2_confidence_on_scissor*0)

# if the calculated number from probability/confidence is max for that element then choose that element
# else choose random 
def player_2_chooses_finally():
    global player_2_choice_is
    if player_2_choose_rock > player_2_choose_paper and player_2_choose_rock > player_2_choose_scissor:
        player_2_choice_is = "Rock"

    elif player_2_choose_paper > player_2_choose_rock and player_2_choose_paper > player_2_choose_scissor:
        player_2_choice_is = "Paper"

    elif player_2_choose_scissor > player_2_choose_rock and player_2_choose_scissor > player_2_choose_paper:
        player_2_choice_is = "Scissor"

    elif player_2_choose_rock == player_2_choose_scissor and player_2_choose_rock == player_2_choose_paper:
        player_2_choice_is = random.choice(["Rock", "Paper", "Scissor"])
        