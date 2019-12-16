import random

# Initialize empty memory for player
p_2_memory = []
p_1_memory = []
# player confidence at the starting of the game between 10% and 90%
#random.seed(1)
p_1_confidence = round(random.uniform(0.1, 0.9), 1)
p_2_confidence = round(random.uniform(0.1, 0.9), 1)
p_confidence = round(random.uniform(0.1, 0.9), 1)

# Initialize global variable = 0
p_loop_number = 0
p_thinks_rock_probability = 0.0
p_thinks_paper_probability = 0.0
p_thinks_scissor_probability = 0.0
p_confidence_on_rock = 0.0
p_confidence_on_paper = 0.0
p_confidence_on_scissor = 0.0
limit = 10


# This function uses Theory of Mind, in which p looks at opponent or own data set and
# calculate the probability of repeating elements
def p_thinks_probability(p_order, catch_order):
    global p_thinks_rock_probability, p_thinks_paper_probability, p_thinks_scissor_probability
    # catch_order = 1, means p 1 will choose first
    if catch_order == 1:
        p_1_order = p_order
        # If p_1_order = even number (0,2,4,6,...) p will look at opponent data set and
        # calculate the probability of repeating elements
        if len(p_1_memory) < limit:
            divideFactor = len(p_1_memory)
        else:
            divideFactor = limit

        if p_1_order % 2 == 0:
            p_thinks_rock_probability = p_2_memory[-divideFactor:].count("Rock") / divideFactor
            p_thinks_paper_probability = p_2_memory[-divideFactor:].count("Paper") / divideFactor
            p_thinks_scissor_probability = p_2_memory[-divideFactor:].count("Scissor") / divideFactor
        # Else p will look at own data set and
        # calculate the probability of repeating elements
        else:
            p_thinks_rock_probability = p_1_memory[-divideFactor:].count("Rock") / divideFactor
            p_thinks_paper_probability = p_1_memory[-divideFactor:].count("Paper") / divideFactor
            p_thinks_scissor_probability = p_1_memory[-divideFactor:].count("Scissor") / divideFactor
            #print(p_1_memory[-divideFactor:])
    # catch_order = 2, means p 2 will choose Second
    elif catch_order == 2:
        p_2_order = p_order
        # If p_1_order = even number (0,2,4,6,...) p will look at opponent data set and
        # calculate the probability of repeating elements
        if len(p_2_memory) < limit:
            divideFactor = len(p_2_memory)
            if p_2_order % 2 == 0:
                # Note:  we need to decrease the length to length--, because till the time p 2 will choose,
                # p 1 has already choosen. Hence, decreasing the length
                # p_thinks_rock_probability = p_1_memory[0:(len(p_1_memory) - 1)].count("Rock") / (
                # len(p_1_memory) - 1)
                p_thinks_rock_probability = p_1_memory[:divideFactor].count("Rock") / divideFactor
                p_thinks_paper_probability = p_1_memory[:divideFactor].count("Paper") / divideFactor
                p_thinks_scissor_probability = p_1_memory[:divideFactor].count("Scissor") / divideFactor
                #print(p_1_memory[:divideFactor])

            else:
                p_thinks_rock_probability = p_2_memory[-divideFactor:].count("Rock") / divideFactor
                p_thinks_paper_probability = p_2_memory[-divideFactor:].count("Paper") / divideFactor
                p_thinks_scissor_probability = p_2_memory[-divideFactor:].count("Scissor") / divideFactor
        else:
            divideFactor = limit
            if p_2_order % 2 == 0:
                # Note:  we need to decrease the length to length--, because till the time p 2 will choose,
                # p 1 has already choosen. Hence, decreasing the length
                # p_thinks_rock_probability = p_1_memory[0:(len(p_1_memory) - 1)].count("Rock") / (
                # len(p_1_memory) - 1)
                p_thinks_rock_probability = p_1_memory[len(p_1_memory)-(limit+1):-1].count("Rock") / divideFactor
                p_thinks_paper_probability = p_1_memory[len(p_1_memory)-(limit+1):-1].count("Paper") / divideFactor
                p_thinks_scissor_probability = p_1_memory[len(p_1_memory)-(limit+1):-1].count("Scissor") / divideFactor
                #print(p_1_memory[len(p_1_memory)-(limit+1):-1])

            else:
                p_thinks_rock_probability = p_2_memory[-divideFactor:].count("Rock") / divideFactor
                p_thinks_paper_probability = p_2_memory[-divideFactor:].count("Paper") / divideFactor
                p_thinks_scissor_probability = p_2_memory[-divideFactor:].count("Scissor") / divideFactor


# This function calculate what element is supposed to choose from probability
def p_choose_from_probability(p_confidence_assume, p_order, p_thinks_rock_probability,
                              p_thinks_paper_probability, p_thinks_scissor_probability):
    global p_choose_rock, p_choose_paper, p_choose_scissor, p_loop_number

    # Suppose the probability of rock is the highest from p_thinks_probability(),
    # then p_choose_paper will have the highest value from below formula, hence p will choose paper
    p_choose_rock = (p_thinks_rock_probability * 0) + (p_thinks_paper_probability * (-1)) + (
            p_thinks_scissor_probability * 1)
    p_choose_paper = (p_thinks_rock_probability * 1) + (p_thinks_paper_probability * 0) + (
            p_thinks_scissor_probability * (-1))
    p_choose_scissor = (p_thinks_rock_probability * (-1)) + (p_thinks_paper_probability * 1) + (
            p_thinks_scissor_probability * 0)
    print(p_choose_rock, p_choose_paper, p_choose_scissor)
    # if p_order == 0, then it will not call p_confidence_from_choice()

    # At the start p_loop_number will be 0, it will increase in p_confidence_from_choice()
    if p_order > p_loop_number:
        p_confidence_from_choice(p_confidence_assume, p_order, p_thinks_rock_probability,
                                 p_thinks_paper_probability, p_thinks_scissor_probability)


# The p uses his confidence to make sure his opponent will choose a perticular element
# This function is only applicable for order of agents > 0
def p_confidence_from_choice(p_confidence_assume, p_order, rock_multiply, paper_multiply,
                             scissor_multiply):
    global p_confidence_on_rock, p_confidence_on_paper, p_confidence_on_scissor, p_loop_number

    # The agent will confirm that his opponent has choosen a perticular elemrnt from his confidence
    # and then will call p_choose_from_probability() to make the decision to what element to choose
    if p_choose_rock > p_choose_paper and p_choose_rock > p_choose_scissor:
        p_confidence_on_rock = ((1 - p_confidence_assume) * rock_multiply) + p_confidence_assume
        p_confidence_on_paper = ((1 - p_confidence_assume) * paper_multiply)
        p_confidence_on_scissor = ((1 - p_confidence_assume) * scissor_multiply)

    elif p_choose_paper > p_choose_rock and p_choose_paper > p_choose_scissor:
        p_confidence_on_rock = ((1 - p_confidence_assume) * rock_multiply)
        p_confidence_on_paper = ((1 - p_confidence_assume) * paper_multiply) + p_confidence_assume
        p_confidence_on_scissor = ((1 - p_confidence_assume) * scissor_multiply)

    elif p_choose_scissor > p_choose_rock and p_choose_scissor > p_choose_paper:
        p_confidence_on_rock = ((1 - p_confidence_assume) * rock_multiply)
        p_confidence_on_paper = ((1 - p_confidence_assume) * paper_multiply)
        p_confidence_on_scissor = ((1 - p_confidence_assume) * scissor_multiply) + p_confidence_assume

    elif p_choose_rock == p_choose_paper and p_choose_rock == p_choose_scissor:
        p_confidence_on_rock = 0
        p_confidence_on_paper = p_confidence_on_rock
        p_confidence_on_scissor = p_confidence_on_rock

    p_loop_number = p_loop_number + 1

    p_choose_from_probability(p_confidence_assume, p_order, p_confidence_on_rock,
                              p_confidence_on_paper, p_confidence_on_scissor)


# if the calculated number from probability/confidence is max for that element then choose that element
# else choose random
def p_chooses_finally():
    global p_choice_is
    if p_choose_rock > p_choose_paper and p_choose_rock > p_choose_scissor:
        p_choice_is = "Rock"

    elif p_choose_paper > p_choose_rock and p_choose_paper > p_choose_scissor:
        p_choice_is = "Paper"

    elif p_choose_scissor > p_choose_rock and p_choose_scissor > p_choose_paper:
        p_choice_is = "Scissor"

    elif p_choose_rock == p_choose_scissor and p_choose_rock == p_choose_paper:
        p_choice_is = random.choice(["Rock", "Paper", "Scissor"])


# From the order the p will return the choice
def p_will_choose(p_order, catch_order):
    global p_loop_number, p_confidence
    p_loop_number = 0
    p_confidence_assume = round(random.uniform(0.1, 0.9), 1)

    # To calculate the probability of repeating elements
    # catch_order will store the value of iteration_order from Rock_paper_Scissor_Game.py
    p_thinks_probability(p_order, catch_order)

    # To calculate what is to be choose from probability
    p_choose_from_probability(p_confidence_assume, p_order, p_thinks_rock_probability,
                              p_thinks_paper_probability, p_thinks_scissor_probability)

    # To calculate which element is benificial to play next
    p_chooses_finally()

    return p_choice_is
