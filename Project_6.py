import random
from hangman_word import word_list
from hangman_art import logo,stages 

chosen_word = random.choice(word_list) 
lives = 6
print(logo)

display = ['_' for _ in chosen_word]
print(' '. join(display))

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f'You have already guessed {guess}')

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You loose.')
            print(f'The word was {chosen_word}')

    print(' '.join(display))

    if '_' not in display:
        end_of_game = True
        print('You win!')

    print(stages[lives])