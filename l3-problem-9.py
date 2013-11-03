print 'Please think of a number between 0 and 100!'

high = 100
low = 0
found = False

while found == False:
    middle = (high + low) / 2
    print('Is your secret number ' + str(middle)+ '?')
    feedback = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if feedback == 'h':
        high = middle
    elif feedback == 'l':
        low = middle
    elif feedback == 'c':
        found = True
    else:
        print 'Sorry, I did not understand your input.'

print('Game over. Your secret number was: ' + str(middle))
