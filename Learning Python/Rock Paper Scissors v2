# Rock Paper Scissors v2:
# This is not a joke like v1, this is an actually playable game.

import random

print("Instructions: ")
print("> This is 1 player game against a bot.")
print("> Player choose 1 of 3 plays each round - Rock, Paper, and Scissors.")
print("> Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
print("> Player must type in their play of choice each round.")
print("> If player enters invalid play, bot wins the round.")

player = 0
bot = 0
best_of = input("\nBest of: ")
try:
    best_of = int(best_of)
    if best_of<0:
        print("'Best of' should be more than 0.")
    else:
        for rounds in range(1, best_of+1):
            print("\nRound :", rounds)
            print("Rock/Paper/Scissors")
            print("Bot has chosen play")
            bot_play = random.choice(["rock", "paper", "scissors"])
            play = input("Your play: ").strip().lower() # removes unnesacary spaces, and lowers all letters
            if play!="rock" and play!="paper" and play!="scissors":
                 print("Invalid Play, try again.")
                 bot+=1
                 print("Bot wins this round.")

            else:
                 if play=="rock" and bot_play=="scissors":
                     player+=1
                     print(f"\nYour play: {play} | Bot play: {bot_play}")
                     print("You win!")
                     print("\nScore:")
                     print(f"You: {player} | Bot: {bot}")
                 elif play=="scissors" and bot_play=="paper":
                     player+=1
                     print(f"\nYour play: {play} | Bot play: {bot_play}")
                     print("You win!")
                     print("\nScore:")
                     print(f"You: {player} | Bot: {bot}")
                 elif play=="paper" and bot_play=="rock":
                     player+=1
                     print(f"\nYour play: {play} | Bot play: {bot_play}")
                     print("You win!")
                     print("\nScore:")
                     print(f"You: {player} | Bot: {bot}")
                 elif play==bot_play:
                     print(f"\nYour play: {play} | Bot play: {bot_play}")
                     print("Draw!")
                     print("\nScore:")
                     print(f"You: {player} | Bot: {bot}")
                 else:
                     bot+=1
                     print(f"\nYour play: {play} | Bot play: {bot_play}")
                     print("Bot wins!")
                     print("\nScore:")
                     print(f"You: {player} | Bot: {bot}")
        print("\nFinal Score:")
        print(f"You: {player} | Bot: {bot}")
        if player > bot:
            print("You win the game!")
        elif bot > player:
            print("Bot wins the game!")
        else:
            print("The game is a draw!")
except ValueError:
    print("'Best of' must be a natural number.")