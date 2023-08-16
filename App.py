from random import randint, choice

def clue(answer):
    options = [answer - 1, answer +1]
    return choice(options)

def run_guess(guess, answer, attempts):

    counter = attempts
    if 0 < guess < 11:
        if guess == answer:
            if attempts > 3:
                print('You got the correct answer in', attempts, 'attempts! Well done!')
            elif attempts <= 2:
                print('You got the correct answer in', attempts, 'attempts! You\'re a genius!')
            else:
                print('You got the correct answer in', attempts, 'attempts! Well done!')

            return True
        elif counter == 2:
            print(f'that\'s not the correct answer. Here\'s a clue: ', clue(answer))
    else:
        print('Please input a number that is 1~10')
        return False

if __name__ =='__main__':
    play_again = True
    while play_again:
        answer = randint(1, 10)
        attempts = 0
        while True:
            try:
                guess = int(input('Please input a number 1~10: '))
                attempts += 1
                if run_guess(guess, answer, attempts):
                    break

            except ValueError:
                print('please enter a number')
                continue

        play_again_input = input('Do you want to give it another try?(yes/no): ')
        if play_again_input.lower() not in ['yes', 'y']:
            print('Come back again! Bye!!!')
            play_again = False

# add score tracker