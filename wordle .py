import random # SO YOU CAN GET A RANDOM WORD. RANDOM IS A LIBRARY :P
word = ["apple", "fruit", "stale", "front"]

def random_word():
    return random.choice(word)

print('OK HERE"S THE WORDLE PART TIME TO GET THIS SHITSHOW ON THE ROAD!!!!!')
print()
print('ENTER A GUESS (5 words long!)')
for attempt in range(1,7):
    guess = input('==> ').lower()

    for i in range (min(len(guess))):
        if guess[i] == word[i]:
            print('[',[i], ']', end='')
        elif guess[i] == word:
            print('{',[i], '}', end='')
        else:
            print('(',[i], ')', end='')
        
        if guess == word:
            print('YOU GOT THE WORD!!! YAY!!!!')