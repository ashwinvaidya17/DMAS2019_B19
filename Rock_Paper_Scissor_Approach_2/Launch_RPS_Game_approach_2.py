import time
import Rock_Paper_Scissor_Game_and_Rules as rps

print("Rock-Paper-Scissor Game")
order_limit = 6
# The terminal will ask you to choose the order for player 1 & player 2 (For now choose 0 or 1)
player_1_order = int(input("Now, choose the order of thinking for Player 1 (less than 6): "))
player_2_order = int(input("Similarly, choose the order of thinking for Player 2 (less than 6): "))
max_rounds = 100


if player_1_order >= order_limit:
    player_1_order = order_limit-1

if player_2_order >= order_limit:
    player_2_order = order_limit-1

# The Game will begins after 3 Seconds
print("\nGame begins in:")
time.sleep(0.5)
for i in range(3, 0, -1):
    print(i)
    time.sleep(1.0)
print("-----------------------------------------")
# This function will call rock_paper_scissor function from Rock_Paper_Scissor_Game module
rps.rock_paper_scissor(player_1_order, player_2_order, max_rounds)
