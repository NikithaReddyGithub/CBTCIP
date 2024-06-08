import random

def generate_number():
    return str(random.randint(1000, 9999))

def get_clues(secret_number, guess):
    clues = ""
    for i in range(len(secret_number)):
        if secret_number[i] == guess[i]:
            clues += "X"
        elif secret_number[i] in guess:
            clues += "O"
        else:
            clues += "-"
    return clues

def main():
    print("Welcome to Mastermind!")

    # Player 1 sets the number
    player1_number = generate_number()
    print("Player 1 has set the number. Now it's Player 2's turn to guess.")

    # Player 2 guesses
    attempts_player2 = 0
    while True:
        guess = input("Enter your guess (4-digit number): ")
        attempts_player2 += 1
        if guess == player1_number:
            print(f"Congratulations! Player 2 guessed the number {player1_number} in {attempts_player2} attempts. Player 2 wins!")
            break
        else:
            clues = get_clues(player1_number, guess)
            print(f"Clues: {clues}")

    # Player 2 sets the number
    player2_number = input("Player 2, enter your number (4-digit number): ")
    print("Player 2 has set the number. Now it's Player 1's turn to guess.")

    # Player 1 guesses
    attempts_player1 = 0
    while True:
        guess = input("Enter your guess (4-digit number): ")
        attempts_player1 += 1
        if guess == player2_number:
            print(f"Congratulations! Player 1 guessed the number {player2_number} in {attempts_player1} attempts. Player 1 wins!")
            break
        else:
            clues = get_clues(player2_number, guess)
            print(f"Clues: {clues}")

if __name__ == "__main__":
    main()