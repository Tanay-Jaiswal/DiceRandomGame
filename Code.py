import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

while True:
    rounds = input("Enter the number of rounds you want to play: ")
    if rounds.isdigit():
        rounds = int(rounds)
        if rounds > 0:
            break
        else:
            print("Number of rounds must be positive.")
    else:
        print("Invalid input. Please enter a number.")

player_scores = [0 for _ in range(players)]

for round_num in range(1, rounds + 1):
    print(f"\n🎲 Round {round_num} of {rounds}")
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "'s turn!")
        print("Current total score:", player_scores[player_idx])
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Current round score:", current_score)

        player_scores[player_idx] += current_score
        print("New total score:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\n🏆 Player", winning_idx + 1, "wins with a score of", max_score)
