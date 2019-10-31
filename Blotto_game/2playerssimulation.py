import random
import json
import zmq
import argparse
import math
import numpy as np


game = "BlottoGame"
implementation = "1v1"
noOfTroops = 8
noOfBattleFields = 3
totalPlayers = 2
memory = 0

# Will return json with initial configuration of -1 troops at every battlefield
def initializeDistributionOfTroops(noOfBattleFields):
    distribution = []
    count = 1
    while (count <= noOfBattleFields):
        distribution.append({"battleField": count, "troops": -1})
        count = count + 1
    return distribution


# Read Config Parameters from config File
def readConfig(fileName):
    with open('config.txt') as json_file:
        print (json_file)
        config = json.load(json_file)
        game = config['game']
        implementation = config['implementation']
        noOfTroops = config['noOfTroops']
        noOfBattleFields = config['noOfBattleFields']
        totalPlayers = config['totalPlayers']
        memory = config['memory']
        print ("Config Parameters are \n", game, implementation, noOfTroops, noOfBattleFields, totalPlayers, memory)


# Return 1 if winner is playerA, 0 if it is a draw and -1 if playerB is the winner
# Also return the the difference of troops A and B on the battlefields
def getWinner(player1, player2):
    player1_wins = 0
    player2_wins = 0
    difference_troops = []
    for i in range(0, len(player1)):
        difference_troops.append(
            {"battleField": player1[i]['battleField'], "troopsDifference": player1[i]['troops'] - player2[i]['troops']})
        if player1[i]['troops'] > player2[i]['troops']:
            player1_wins = player1_wins + 1
        elif player1[i]['troops'] == player2[i]['troops']:
            continue
        else:
            player2_wins = player2_wins + 1
    if (player1_wins > player2_wins):
        return 1, difference_troops
    elif (player1_wins == player2_wins):
        return 0, difference_troops
    else:
        return -1, difference_troops


# Return the json like {{index:0,value:2},{index:1,value:3}}.  The complete logic will be implemented on the given json
def getJsonForDistribution(distribution):
    jsonDistribution = []
    for i in range(0, len(distribution)):
        jsonDistribution.append({'battleField': i, 'troops': distribution[i]})
    return jsonDistribution


#Sort the distribution of the opponent and get the distribution which beats the oppoenent's distribution.
#Sort opponent's distribution in ascending order of  battlefield witn minimum troops. Send 1 troop extra than then opponent's in a battlefield.
def findDistributionToBeatAsc(sortedDistributionOfTheOpponent, numberOfTroops):
    numberOfTroopsRemaining = numberOfTroops
    distribution = []
    for i in range(0, len(sortedDistributionOfTheOpponent)):
        if ((numberOfTroopsRemaining - sortedDistributionOfTheOpponent[i]['troops']) > 1):
            distribution.append({'battleField': sortedDistributionOfTheOpponent[i]['battleField'],
                                 'troops': sortedDistributionOfTheOpponent[i]['troops'] + 1})
            numberOfTroopsRemaining = numberOfTroopsRemaining - sortedDistributionOfTheOpponent[i]['troops'] - 1
        else:
            distribution.append(
                {'battleField': sortedDistributionOfTheOpponent[i]['battleField'], 'troops': numberOfTroopsRemaining})
            numberOfTroopsRemaining = 0
    return sorted(distribution, key=lambda i: i['battleField'])


#For an agent, it finds out the minimum number of battles that needs to be won.
#And the battleFields to be won are chosen randomly from the given battlefields
def findProbableDistribution(distributionOfOpponent, numberOfTroops, memory, noOfBattleFields):
    numberOfTroopsRemaining = numberOfTroops
    distribution = []
    '''
    Battles to be won, tells for a battlefields minimum number of battles to be won. 
    And the battleFields to be won are chosen randomly from the given battlefields 
    '''
    if (noOfBattleFields % 2 == 0):
        battleFieldsToBeWon = (noOfBattleFields / 2) + 1
    else:
        battleFieldsToBeWon = (noOfBattleFields + 1) / 2
    choicesForBattleField = random.sample(range(0, noOfBattleFields), int(battleFieldsToBeWon))
    distribution = initializeDistributionOfTroops(noOfBattleFields)
    # print("Initialize distribution",distribution)
    for i in choicesForBattleField:

        if ((numberOfTroopsRemaining - distributionOfOpponent[i]['troops']) < 1):

            break
        else:

            distribution[i]['battleField'] = distributionOfOpponent[i]['battleField']
            distribution[i]['troops'] = distributionOfOpponent[i]['troops'] + 1

            numberOfTroopsRemaining = numberOfTroopsRemaining - (distributionOfOpponent[i]['troops'] + 1)
    for i in range(0, noOfBattleFields):

        if (distribution[i]['troops'] == -1):
            '''
            distributing the remaining troops to a battlefield that has no troops.
            Rest all battlefields which are not necessary to be won to win the round still will have 0 troops 
            '''

            distribution[i]['battleField'] = i + 1
            distribution[i]['troops'] = numberOfTroopsRemaining

            numberOfTroopsRemaining = 0

    return distribution


#Sort the distribution of the opponent and get the distribution which beats the oppoenent's distribution.
#Sort opponent's distribution in descending order of battlefield with maximum troops. Send 1 troop extra than then opponent's in a battlefield.
def findDistributionToBeatDesc(sortedDistributionOfTheOpponent, numberOfTroops):
    numberOfTroopsRemaining = numberOfTroops
    distribution = []
    descSortedDistributionOfOpponent = sorted(sortedDistributionOfTheOpponent, key=lambda i: i['troops'], reverse=True)
    for i in range(0, len(descSortedDistributionOfOpponent)):
        if ((numberOfTroopsRemaining - descSortedDistributionOfOpponent[i]['troops']) > 1):
            distribution.append({'battleField': sortedDistributionOfTheOpponent[i]['battleField'],
                                 'troops': sortedDistributionOfTheOpponent[i]['troops'] + 1})
            numberOfTroopsRemaining = numberOfTroopsRemaining - sortedDistributionOfTheOpponent[i]['troops'] - 1
        else:
            distribution.append(
                {'battleField': sortedDistributionOfTheOpponent[i]['battleField'], 'troops': numberOfTroopsRemaining})
            numberOfTroopsRemaining = 0
    return sorted(distribution, key=lambda i: i['battleField'])


# Will return the troops dostribution for higher order agent
def distributeTroopsForHigherOrderAgent(distributionOfTheOpponent, distributionOfTheUser, orderOfTheAgent,
                                        numberOfTroops, noOfBattleFields,strategy):
    jsonForDistribution = []
    # distributionReturn = getJsonForDistribution(distributionOfTheUser)
    jsonDistributionForOpponent = distributionOfTheOpponent
    distributionReturn = distributionOfTheUser
    while (orderOfTheAgent > 0):
        sortedDistributionForOpponent=sorted(jsonDistributionForOpponent, key=lambda i: i['troops'])
        # print("Sorted Distribution of Oppenent ",sortedDistributionForOpponent)
        if(strategy==2):
            distributionReturn = findDistributionToBeatAsc(sortedDistributionForOpponent,noOfTroops)
        elif(strategy==3):
            distributionReturn = findProbableDistribution(jsonDistributionForOpponent, numberOfTroops,1,noOfBattleFields)
        jsonDistributionForOpponent = distributionReturn
        orderOfTheAgent = orderOfTheAgent - 1
    return distributionReturn

# Distribute the troops randomly in given battlefields
def distributeTroopsRandomly(troops, battlefields):
    print("Random distribution")
    split = random.sample(range(0, troops + 1), battlefields - 1)
    split = sorted(split)
    split.append(troops)
    troops_allocation = []
    prev_val = 0
    count = 0
    while (count < (battlefields)):
        next_val = split[count]
        troops_allocation.append({"battleField": count + 1, "troops": next_val - prev_val})
        count = count + 1
        prev_val = next_val
    return troops_allocation

#Creates the JSON to send to unity engine for frontend simulation
def getJsonToSend(game, implementation, noOfTroops, noOfBattleFields, totalPlayers, maxWins, agent1Distribution,
                  agent2Distribution, afterBattleDistribution):
    infoJson = {}
    infoJson["Game"] = game
    infoJson["Implementation"] = implementation
    infoJson["battle_fields"] = noOfBattleFields
    infoJson["total_troops"] = noOfTroops
    infoJson["total_players"] = totalPlayers
    infoJson["max_wins"] = maxWins
    distributionOfTroops = []

    distributionJson = {}
    distributionJson["Name_of_the_Agent"] = "Agent" + str(1)
    distributionJson["distribution"] = agent1Distribution
    distributionOfTroops.append(distributionJson)
    distributionJson = {}
    distributionJson["Name_of_the_Agent"] = "Agent" + str(2)
    distributionJson["distribution"] = agent2Distribution
    distributionOfTroops.append(distributionJson)
    infoJson["distribution_of_troops"] = distributionOfTroops
    afterBattleResults = []
    for i in range(0, noOfBattleFields):
        infoBattleField = {}
        infoBattleField["battle_field"] = afterBattleDistribution[i]["battleField"]
        # print("AfterBattleDistribution",afterBattleDistribution)
        if (afterBattleDistribution[i]["troopsDifference"] > 0):
            winner = "Agent1"
            troops_remaining = afterBattleDistribution[i]["troopsDifference"]
        elif (afterBattleDistribution[i]["troopsDifference"] == 0):
            winner = "Draw"
            troops_remaining = 0
        else:
            winner = "Agent2"
            troops_remaining = -1 * afterBattleDistribution[i]["troopsDifference"]
        infoBattleField["winner"] = winner
        infoBattleField["troops_remaining"] = troops_remaining
        afterBattleResults.append(infoBattleField)
    infoJson["After_battle_results"] = afterBattleResults
    return infoJson

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Command line arguments
    parser.add_argument("--troops", help="number of troops")
    parser.add_argument("--battlefields", help="number of battlefields")
    parser.add_argument("--orderofagent1", help="Theory of mind order of the agent1")
    parser.add_argument("--orderofagent2", help="Theory of mind order of the agent2")
    parser.add_argument("--simulation", help="1 to unable simulation, 0 to disable simulation")
    parser.add_argument("--strategy",help="1 for Random Strategy, 2 for Most Optimal Winning Strategy, 3 for Random Winning Strategy")
    # parser.add_argument("--strategy",help="0 for most optimal strategy, 1 for random winning strategy")
    args = parser.parse_args()
    simulation_round = 0
    print (args)
    noOfTroops = int(args.troops)
    noOfBattleFields = int(args.battlefields)
    agent1_order = int(args.orderofagent1)
    agent2_order = int(args.orderofagent2)
    simulation = int(args.simulation)
    strategy = int(args.strategy)
    # strategy = int(args.strategy)
    if (simulation):
        simulationToRun = 1
    else:
        simulationToRun = 100
    agent1 = distributeTroopsRandomly(noOfTroops, noOfBattleFields)
    agent2 = distributeTroopsRandomly(noOfTroops, noOfBattleFields)
    agent1_wins = 0
    agent2_wins = 0
    simulation_round = 0
    while (simulation_round < simulationToRun):
        simulation_round = simulation_round + 1
        winner, val = getWinner(agent1, agent2)
        # print getJsonForDistribution(agentA)

        #If theory of mind order of the agent is 0, then the agent uses the same distribution
        if(agent2_order==0):
          agent2_higherOrder = agent2
        else:
          #If the strategy is 1-Random, 2 - Most Optimal Winning Strategy, 3 - Random Winning Strategy
          if(strategy==1):
             agent2_higherOrder = distributeTroopsRandomly(noOfTroops,noOfBattleFields)
          else:
             agent2_higherOrder = distributeTroopsForHigherOrderAgent(agent1, agent2, agent2_order, noOfTroops,
                                                                 noOfBattleFields,strategy)

        if(agent1_order==0):
            agent1_higherOrder = agent1
        else:
            if(strategy==1):
                agent1_higherOrder = distributeTroopsRandomly(noOfTroops,noOfBattleFields)
            else:
                agent1_higherOrder = distributeTroopsForHigherOrderAgent(agent1, agent2, agent1_order, noOfTroops,
                                                                 noOfBattleFields,strategy)

        print("Agent 1 higher order",agent1_higherOrder)

        winner, afterBattleDistribution = getWinner(agent1_higherOrder, agent2_higherOrder)
        if (winner == 1):
            maxWins = "Agent1"
            agent1_wins = agent1_wins + 1
        elif (winner == -1):
            maxWins = "Agent2"
            agent2_wins = agent2_wins + 1
        else:
            maxWins = "Draw"
        if ((simulation_round % 10) == 0):
            strng_to_prnt = "Wins after " + str(simulation_round) + " games are: "
            print(strng_to_prnt)
            print("Agent1 ", agent1_wins)
            print("Agent2 ", agent2_wins)

        agent1 = agent1_higherOrder
        agent2 = agent2_higherOrder
    print("Agent1 wins are ", agent1_wins)
    print("Agent2 wins are ", agent2_wins)
    print("Draws are ",(100 - (agent1_wins+agent2_wins)))
    if (simulation):
        msgJson = getJsonToSend(game, implementation, noOfTroops, noOfBattleFields, totalPlayers, maxWins,
                                agent1_higherOrder, agent2_higherOrder, afterBattleDistribution)
        # print("Msg Json",msgJson)
        '''
        zmq sending msg to the frontend
        '''

        context = zmq.Context()
        #  Socket to talk to server
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")
        print(socket.recv())
        socket.send_json(msgJson)
