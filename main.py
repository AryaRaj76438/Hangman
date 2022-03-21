import hangman_words
import random
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)
word_length = len(chosen_word)

end_of_games = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_games:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter
    print(f"{''.join(display)}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_games = True
            print("You Lose.")
    if "_" not in display:
        end_of_games = True
        print("You Win")

    print(hangman_art.stages[lives])

