import random

# Initialize empty memory for player
p_2_memory = []
p_1_memory = []

# player confidence at the starting of the game between 10% and 90%
p_1_confidence = round(random.uniform(0.5, 0.9), 1)
p_2_confidence = round(random.uniform(0.5, 0.9), 1)

# Initialize global variable = 0
p_loop_number = 0
p_confidence_on_rock = 0.0
p_confidence_on_paper = 0.0
p_confidence_on_scissor = 0.0
limit = 10


# This function uses Theory of Mind, in which player looks at opponent or own data-set and
# calculate the probability of repeating elements
def p_thinks_probability(p_order, catch_order):
    # catch_order = 1, means player 1 will choose first
    if catch_order == 1:
        p_1_order = p_order

        # divideFactor is used to set the memory limit from which player will calculate the probability
        if len(p_1_memory) < limit:
            divideFactor = len(p_1_memory)
        else:
            divideFactor = limit

        # If p_1_order is even number (0,2,4,6,...) player will look at opponent data-set and
        # calculate the probability of repeating elements
        if p_1_order % 2 == 0:
            p_thinks_rock_probability = p_2_memory[-divideFactor:].count("Rock") / divideFactor
            p_thinks_paper_probability = p_2_memory[-divideFactor:].count("Paper") / divideFactor
            p_thinks_scissor_probability = p_2_memory[-divideFactor:].count("Scissor") / divideFactor
        # Else player will look at own data set and
        # calculate the probability of repeating elements
        else:
            p_thinks_rock_probability = p_1_memory[-divideFactor:].count("Rock") / divideFactor
            p_thinks_paper_probability = p_1_memory[-divideFactor:].count("Paper") / divideFactor
            p_thinks_scissor_probability = p_1_memory[-divideFactor:].count("Scissor") / divideFactor

    # catch_order = 2, means player 2 will choose Second
    elif catch_order == 2:
        p_2_order = p_order
        if len(p_2_memory) < limit:
            divideFactor = len(p_2_memory)
            # If p_1_order = even number (0,2,4,6,...) p will look at opponent data set and
            # calculate the probability of repeating elements
            if p_2_order % 2 == 0:
                p_thinks_rock_probability = p_1_memory[:divideFactor].count("Rock") / divideFactor
                p_thinks_paper_probability = p_1_memory[:divideFactor].count("Paper") / divideFactor
                p_thinks_scissor_probability = p_1_memory[:divideFactor].count("Scissor") / divideFactor
            # Else player will look at own data set and
            # calculate the probability of repeating elements
            else:
                p_thinks_rock_probability = p_2_memory[-divideFactor:].count("Rock") / divideFactor
                p_thinks_paper_probability = p_2_memory[-divideFactor:].count("Paper") / divideFactor
                p_thinks_scissor_probability = p_2_memory[-divideFactor:].count("Scissor") / divideFactor
        else:
            divideFactor = limit
            if p_2_order % 2 == 0:
                # Note:  here we are using "p_1_memory[len(p_1_memory)-(limit+1):-1]" to calculate probability
                # because the time player 2 chooses an element player 1 has already chosen, hence we need not to
                # consider last element from player 1 list and then calculate the probability
                p_thinks_rock_probability = p_1_memory[len(p_1_memory) - (limit + 1):-1].count("Rock") / divideFactor
                p_thinks_paper_probability = p_1_memory[len(p_1_memory) - (limit + 1):-1].count("Paper") / divideFactor
                p_thinks_scissor_probability = p_1_memory[len(p_1_memory) - (limit + 1):-1].count("Scissor") / divideFactor

            else:
                p_thinks_rock_probability = p_2_memory[-divideFactor:].count("Rock") / divideFactor
                p_thinks_paper_probability = p_2_memory[-divideFactor:].count("Paper") / divideFactor
                p_thinks_scissor_probability = p_2_memory[-divideFactor:].count("Scissor") / divideFactor

    return p_thinks_rock_probability, p_thinks_paper_probability, p_thinks_scissor_probability


# This function calculate what element is supposed to choose from probability
def p_choose_from_probability(confidence_level, p_order, p_thinks_rock_probability,
                              p_thinks_paper_probability, p_thinks_scissor_probability):
    global p_choose_rock, p_choose_paper, p_choose_scissor, p_loop_number

    # Suppose the probability of "rock" is the highest from p_thinks_probability(), then p_choose_paper will have the
    # highest value from below formula, hence player will choose paper if p_order is 0 order
    p_choose_rock = (p_thinks_rock_probability * 0) + (p_thinks_paper_probability * (-1)) + (
            p_thinks_scissor_probability * 1)
    p_choose_paper = (p_thinks_rock_probability * 1) + (p_thinks_paper_probability * 0) + (
            p_thinks_scissor_probability * (-1))
    p_choose_scissor = (p_thinks_rock_probability * (-1)) + (p_thinks_paper_probability * 1) + (
            p_thinks_scissor_probability * 0)

    # if p_order is 0 order, then it will not call p_confidence_from_choice(), as 0 order does not any level of
    # confidence. At the start p_loop_number will be 0, it will increase in p_confidence_from_choice()
    if p_order > p_loop_number:
        p_confidence_from_choice(confidence_level, p_order, p_choose_rock, p_choose_paper, p_choose_scissor)


# The player uses his confidence to make sure his opponent will choose a particular element, i.e. integrating the
# belief of lower order agent.
# This function is only applicable for order of agents > 0
def p_confidence_from_choice(confidence_level, p_order, rock_multiply, paper_multiply,
                             scissor_multiply):
    global p_confidence_on_rock, p_confidence_on_paper, p_confidence_on_scissor, p_loop_number

    # if loop_number reached that player order than use player_confidence ...
    # else assume the level of confidence of lower order agent
    if p_loop_number == p_order + 1:
        p_confidence_assume = confidence_level
    else:
        p_confidence_assume = round(random.uniform(0.1, 0.4), 1)

    # The agent will confirm that his opponent has chosen a particular element from his level of confidence
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
    if p_choose_rock > p_choose_paper and p_choose_rock > p_choose_scissor:
        p_choice_is = "Rock"

    elif p_choose_paper > p_choose_rock and p_choose_paper > p_choose_scissor:
        p_choice_is = "Paper"

    elif p_choose_scissor > p_choose_rock and p_choose_scissor > p_choose_paper:
        p_choice_is = "Scissor"

    elif p_choose_rock == p_choose_scissor and p_choose_rock == p_choose_paper:
        p_choice_is = random.choice(["Rock", "Paper", "Scissor"])

    return p_choice_is


# From the order the p will return the choice
def p_will_choose(p_order, catch_order):
    global p_loop_number
    p_loop_number = 0

    if catch_order == 1:
        p_confidence = p_1_confidence
    else:
        p_confidence = p_2_confidence

    # This function returns the probability of highest repeating element
    rock_prob, paper_prob, scissors_prob = p_thinks_probability(p_order, catch_order)

    # This function calculates, what to choose from probability and uses theory of mind decision
    p_choose_from_probability(p_confidence, p_order, rock_prob, paper_prob, scissors_prob)

    # This function returns the final element to choose
    p_choice_is = p_chooses_finally()

    return p_choice_is
