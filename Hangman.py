

from random import choice

words = choice(['apple', 'alpha', 'africa', 'australia', 'annoying', 'albania', 'algeria', 'alone','cookie', 'camera', 'camero', 'controller',
                'console', 'cropped', 'doctor', 'diamond', 'dime', 'egg', 'eagles', 'ferrari', 'furious', 'frog', 'goat', 'greece', 'hurricane',
                'hawks', 'lamborghini', 'lizard', 'lunar', 'musician', 'monster', 'movie', 'money', 'mime', 'new', 'opal', 'omega',
                'panda', 'potato', 'playstation', 'python', 'rabbit', 'salesianum', 'soccer', 'sony', 'superman', 'sandwich', 'someone', 'sad', 'supper',
                'shark', 'sharp', 'skunk', 'undecided', 'utopia', 'unique', 'stars', 'swan', 'tiger', 'tornado', 'toronto',
                'turkey', 'taco', 'winner', 'wizards', 'warriors', 'walking', 'zebra']) #words in hangman that will be choosed at random

guessed = []
wrong = []

while len(wrong) < 7: #the ammount of attempts given

    out = ''

    for letter in words:
        if letter in guessed:
            out = out + letter
        else:
            out = out + '_'

    if out == words:
        break

    print('Guess the word:',out)
    print(7-len(wrong),'chances left\n')

    guess = input()

    if guess in guessed or guess in wrong:
        print('You already guessed',guess+ '.','Please try another one!')
    elif guess in words:
        print('Yes!',guess,'is in the word!')
        guessed.append(guess)
    else:
        print('Sorry,',guess,'is not in the word. Try again.')
        wrong.append(guess)

    print()

if len(wrong) != 7:
    print('Awesome! You guessed',words + '!')
else:
    print('Sorry you ran out of attempts. The word was',words + '.', 'Try again later.')

quit = input("Do you want to quit? (Yes/No): ").upper()
if quit == "YES" or quit == "Y" or quit=='y':
			Continue = False
print(quit)
def jls_extract_def():
    return print






jls_extract_def()("Thank you for playing Hangman!")