import random
import json
import argparse
from datetime import datetime

game="BlottoGame"
implementation = "1v1"
noOfTroops = 8
noOfBattleFields = 3
totalPlayers = 2
memory = 0
strategy = 1

#Will return json with initial configuration of -1 troops at every battlefield
'''
The function gives initial distribution of troops
'''
def initializeDistributionOfTroops(noOfBattleFields):
    distribution = []
    count = 1
    while(count <= noOfBattleFields):
        distribution.append({"battleField":count,"troops":-1})
        count = count + 1
    return distribution

#Return the json like {{index:0,value:2},{index:1,value:3}}. The whole processing of logic will be using the following json structure
def getJsonForDistribution(distribution):
    jsonDistribution = []
    for i in range(0,len(distribution)):
        jsonDistribution.append({'battleField':i+1,'troops':distribution[i]})
    return jsonDistribution

#Sort the distribution of the opponent and get the distribution which beats the oppoenent's distribution.
#Sort opponent's distribution in ascending order of  battlefield witn minimum troops. Send 1 troop extra than then opponent's in a battlefield.
def findDistributionToBeatAsc(sortedDistributionOfTheOpponent,numberOfTroops):
    numberOfTroopsRemaining = numberOfTroops
    distribution = []
    for i in range(0,len(sortedDistributionOfTheOpponent)):
        if((numberOfTroopsRemaining - sortedDistributionOfTheOpponent[i]['troops']) > 1):
            distribution.append({'battleField':sortedDistributionOfTheOpponent[i]['battleField'],'troops':sortedDistributionOfTheOpponent[i]['troops'] + 1})
            numberOfTroopsRemaining = numberOfTroopsRemaining - sortedDistributionOfTheOpponent[i]['troops'] - 1
        else:
            distribution.append({'battleField':sortedDistributionOfTheOpponent[i]['battleField'],'troops':numberOfTroopsRemaining})
            numberOfTroopsRemaining = 0
    return sorted(distribution, key=lambda i: i['battleField'])

#For an agent, it finds out the minimum number of battles that needs to be won.
#And the battleFields to be won are chosen randomly from the given battlefields
def findProbableDistribution(distributionOfOpponent,numberOfTroops,memory,noOfBattleFields):
    numberOfTroopsRemaining = numberOfTroops
    distribution = []

    if(noOfBattleFields%2 == 0):
        battleFieldsToBeWon = (noOfBattleFields/2) + 1
    else:
        battleFieldsToBeWon = (noOfBattleFields+1)/2
    choicesForBattleField=random.sample(range(0, noOfBattleFields), int(battleFieldsToBeWon))
    distribution = initializeDistributionOfTroops(noOfBattleFields)
    for i in choicesForBattleField:

        if ((numberOfTroopsRemaining - distributionOfOpponent[i]['troops']) < 1):
            break
        else:
           distribution[i]['battleField'] = distributionOfOpponent[i]['battleField']
           distribution[i]['troops']  = distributionOfOpponent[i]['troops'] + 1
           numberOfTroopsRemaining = numberOfTroopsRemaining - (distributionOfOpponent[i]['troops'] + 1)
    for i in range(0,noOfBattleFields):
        if(distribution[i]['troops'] == -1):
            distribution[i]['battleField'] = i + 1
            distribution[i]['troops'] = numberOfTroopsRemaining
            numberOfTroopsRemaining = 0
    return distribution

#Sort the distribution of the opponent and get the distribution which beats the oppoenent's distribution.
#Sort opponent's distribution in descending order of battlefield with maximum troops. Send 1 troop extra than then opponent's in a battlefield.
def findDistributionToBeatDesc(sortedDistributionOfTheOpponent, numberOfTroops):
    numberOfTroopsRemaining = numberOfTroops
    distribution = []
    descSortedDistributionOfOpponent = sorted(sortedDistributionOfTheOpponent, key=lambda i: i['troops'],reverse=True)
    for i in range(0, len(descSortedDistributionOfOpponent)):
        if((numberOfTroopsRemaining - descSortedDistributionOfOpponent[i]['troops']) > 1):
            distribution.append({'battleField': sortedDistributionOfTheOpponent[i]['battleField'],
                             'troops': sortedDistributionOfTheOpponent[i]['troops'] + 1})
            numberOfTroopsRemaining = numberOfTroopsRemaining - sortedDistributionOfTheOpponent[i]['troops'] - 1
        else:
            distribution.append(
            {'battleField': sortedDistributionOfTheOpponent[i]['battleField'], 'troops': numberOfTroopsRemaining})
            numberOfTroopsRemaining = 0
    return sorted(distribution, key=lambda i: i['battleField'])

#Returns the troops dostribution for higher order agent
def distributeTroopsForHigherOrderAgent(distributionOfTheOpponent, distributionOfTheUser, orderOfTheAgent, numberOfTroops,noOfBattleFields):
    jsonForDistribution = []
    #distributionReturn = getJsonForDistribution(distributionOfTheUser)
    jsonDistributionForOpponent = distributionOfTheOpponent
    while(orderOfTheAgent > 0):
         #sortedDistributionForOpponent=sorted(jsonDistributionForOpponent, key=lambda i: i['troops'])
         #print("Sorted Distribution of Oppenent ",sortedDistributionForOpponent)
         distributionReturn = findProbableDistribution(jsonDistributionForOpponent, numberOfTroops,1,noOfBattleFields)

         jsonDistributionForOpponent = distributionReturn
         orderOfTheAgent = orderOfTheAgent - 1
    return distributionReturn

#Distribute the troops randomly in given battlefields
def distributeTroopsRandomly(troops, battlefields):
    split=random.sample(range(0, troops+1), battlefields -1)
    split =  sorted(split)
    split.append(troops)
    troops_allocation = []
    prev_val = 0
    count=0
    while( count  < (battlefields)):
          next_val = split[count]
          troops_allocation.append({"battleField":count + 1,"troops":next_val-prev_val})
          count = count + 1
          prev_val = next_val
    return troops_allocation

#Troop distribution strategy for odd theory of mind agent
def distributionStrategyForOdd(agent,distributionInfo,noOfTroops,noOfBattleFields,strategy):
    #Support for both the strategy
    agentName = 'Agent' + str(agent+1)
    distribution = distributionInfo[agentName]['distribution']
    orderOfAgent = int(distributionInfo[agentName]['Order'])
    while(orderOfAgent > 0 ):
        sortedDistributionForOpponent = sorted(distribution, key=lambda i: i['troops'])
        if(strategy==2):
            distribution = findDistributionToBeatAsc(sortedDistributionForOpponent,noOfTroops)
        elif(strategy==3):
            distribution = findProbableDistribution(distribution,noOfTroops,memory,noOfBattleFields)
        orderOfAgent = orderOfAgent - 1
    return distribution

#Troop distribution strategy for even theory of mind agents
def distributionStrategyForEven(agent, distributionInfo, noOfTroops, noOfBattlefields,noOfPlayers,strategy):
    agentName = 'Agent' + str(agent+1)
    distributionOfOpponent = []
    maxBattleField = [0]*noOfBattleFields
    orderOfAgents = int(distributionInfo[agentName]['Order'])
    for i in range(0,noOfPlayers):
        otherPlayerAgentName = 'Agent' + str(i+1)
        if(distributionInfo[otherPlayerAgentName] == distributionInfo[agentName]):
            continue
        else:
            for j in range(0,noOfBattleFields):
                if(maxBattleField[j] < distributionInfo[otherPlayerAgentName]['distribution'][j]['troops']):
                    maxBattleField[j] = distributionInfo[otherPlayerAgentName]['distribution'][j]['troops']

    distribution = getJsonForDistribution(maxBattleField)
    while(orderOfAgents > 0):
        sortedDistributionForOpponent = sorted(distribution, key=lambda i: i['troops'])
        if(strategy==2):
            distribution = findDistributionToBeatAsc(sortedDistributionForOpponent,noOfTroops)
        elif(strategy==3):
            distribution = findProbableDistribution(distribution,noOfTroops,memory,noOfBattleFields)
        orderOfAgents = orderOfAgents - 1
    return distribution

#Get the distribution for the agent
def getDistribution(listAgentInfo,noOfPlayers,noOfBattleFields,strategy):
    updateListAgentInfo = listAgentInfo

    for i in range(noOfPlayers):
        agentName = 'Agent' + str(i+1)
        if(int(listAgentInfo[agentName]['Order']) % 2 == 0):
            if(strategy==1):
                updateListAgentInfo[agentName]['distribution'] = distributeTroopsRandomly(noOfTroops,noOfBattleFields)
            else:
                updateListAgentInfo[agentName]['distribution'] = distributionStrategyForEven(i,listAgentInfo,noOfTroops, noOfBattleFields, noOfPlayers,strategy)
        else:
            if(strategy==1):
                updateListAgentInfo[agentName]['distribution'] = distributeTroopsRandomly(noOfTroops,noOfBattleFields)
            else:
                updateListAgentInfo[agentName]['distribution'] = distributionStrategyForOdd(i,listAgentInfo,noOfTroops,noOfBattleFields,strategy)
    return updateListAgentInfo


#Get the winner of the simulation
def getWinner(listAgentInfo,noOfPlayers,noOfBattleFields):
    winnerList = [0]*noOfPlayers
    for i in range(0,noOfBattleFields):
        distributionList = []
        for j in range(0,noOfPlayers):
            agent = "Agent" + str(j+1)
            distributionList.append(listAgentInfo[agent]['distribution'][i]['troops'])
        #maxIdx is the index of the agent with max troops in a battlefield
        maxIdx = distributionList.index(max(distributionList))
        maxValue = max(distributionList)
        #This check if there are multiwinner. If there are multiwinner that is more than 1 has sent their highest troops, then discard the winner
        checkMultiWinner=distributionList.count(maxValue)
        if(checkMultiWinner == 1):
           winnerList[maxIdx] = winnerList[maxIdx] + 1


    return winnerList

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    #Command line arguments
    parser.add_argument("--troops",type=int,help="number of troops")
    parser.add_argument("--battlefields",type=int,help="number of battlefields")
    #parser.add_argument("--orderofagent1",help="Theory of mind order of the agent1")
    #parser.add_argument("--orderofagent2",help="Theory of mind order of the agent2")
    parser.add_argument("--numberOfPlayers",type=int, help="Total number of players for the game")
    parser.add_argument("--orderOfAgent",nargs="*", help="Theory of mind order of agents")
    parser.add_argument("--strategy",type=int,help="1 for Random Strategy, 2 for Most Optimal Winning Strategy, 3 for Random Winning Strategy")
    #parser.add_argument("--strategy",help="0 for most optimal strategy, 1 for random winning strategy")
    args = parser.parse_args()
    simulation_round = 0
    print (args)
    noOfTroops = int(args.troops)
    noOfBattleFields = int(args.battlefields)
    noOfPlayers = int(args.numberOfPlayers)
    orderOfAgents = (args.orderOfAgent)
    strategy = int(args.strategy)
    #strategy = int(args.strategy)
    simulation_round = 0
    orderOfAgents = orderOfAgents[0].split(",")
    main_winner_list = [0]*(noOfPlayers+1)
    troopsDistribution = []
    listOrderOfAgents = []
    agentWins = []

    listAgentInfo = {}

    #Initializing the datatypes for the initial state. Troops are distributed randomply. Order of agents is defined. Number of wins stored.
    for i in range(0,noOfPlayers):
        agentInfo = {}
        agent = "Agent" + str(i+1)
        agentInfo['distribution'] = distributeTroopsRandomly(noOfTroops,noOfBattleFields)
        orderofAgent = int(orderOfAgents[i])
        if(orderofAgent > 5):
            orderofAgent = 5
        agentInfo['Order'] = orderofAgent
        agentInfo['wins'] = 0
        listAgentInfo[agent] = agentInfo

    winnerList = getWinner(listAgentInfo,noOfPlayers,noOfBattleFields)

    while(simulation_round < 100):
         simulation_round = simulation_round + 1
         #print getJsonForDistribution(agentA)
         
         updateListInfo = getDistribution(listAgentInfo,noOfPlayers,noOfBattleFields,strategy)

         winnerList = getWinner(updateListInfo,noOfPlayers,noOfBattleFields)

         listAgentInfo = updateListInfo

         maxValue = max(winnerList)
         # This check if there are multiwinner. If there are multiwinner that is more than 1 has sent their highest troops, then discard the winner
         checkMultiWinner = winnerList.count(maxValue)
         maxIdx = winnerList.index(max(winnerList))

         if (checkMultiWinner == 1):
             #Updating the winner
             main_winner_list[maxIdx] = main_winner_list[maxIdx] + 1
         else:
             #Updating the draw
             main_winner_list[noOfPlayers] = main_winner_list[noOfPlayers] + 1

         if(checkMultiWinner==1):
             strPrint = "Result of simulation " + str(simulation_round) + " - player " + str(maxIdx+1) + " theory of mind order " + str(orderOfAgents[maxIdx]) + " is the winner"
             print(strPrint)
         else:
             strPrint= "Result of simulation " + str(simulation_round) + " - draw"
             print (strPrint)
    with open("nplayersResult.txt", "a+") as f:
        now = datetime.now()
        current_time = now.strftime("\n%Y-%m-%d %H:%M:%S\n")
        f.write(current_time)
        for i in range(0,noOfPlayers):
            strPrint = "Player" +str(i+1) +" order " + str(orderOfAgents[i]) + " wins - " + str(main_winner_list[i]) + "\n"
            print(strPrint)
            f.write(strPrint)
        strPrint = "Draw - `" + str(main_winner_list[noOfPlayers]) + "\n"
        print(strPrint)
        f.write(strPrint)
        f.close()
