from random import randint


def run_guess(guess, answer):

    if 0 < guess < 11:
        if guess == answer:
            print('You got the correct answer in', attempts, 'attempts! You\'re a genius!')
            return True
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
                if run_guess(guess, answer):
                    break

            except ValueError:
                print('please enter a number')
                continue

        play_again_input = input('Do you want to give it another try?(yes/no): ')
        if play_again_input.lower() != 'yes':
            print('Come back again! Bye!!!')
            play_again = False