from random import randint, choice


class Player:

    def __init__(self):
        self.name = None
        # self.points = points

    def name_get(self):
        self.name = input(f'Set your username: ')

    def name_print(self):
        print(f'Username set to: ', self.name)

    # create name_display function


def clue(answer):
    options = [answer - 1, answer + 1]
    return choice(options)



def run_guess(user_guess, correct_answer, attempt):
    counter = attempt
    if 0 < user_guess < 11:
        if user_guess == correct_answer:
            if attempt > 3:
                print('You got the correct answer in', attempt, 'attempts! Well done!')
            elif attempt <= 2:
                print('You got the correct answer in', attempt, 'attempts! You\'re a genius!')
            else:
                print('You got the correct answer in', attempt, 'attempts! Well done!')

            return True
        elif counter == 2:
            print(f'that\'s not the correct answer. Here\'s a clue: ', clue(correct_answer))
    else:
        print('Please input a number that is 1~10')
        return False


if __name__ == '__main__':

    player = Player()
    player.name_get()
    player.name_print()

    play_again = True
    while play_again:
        answer = randint(1, 10)
        attempts = 0
        while True:
            try:
                guess = int(input('Please input a number 1~10: '))
                attempts += 1
                if run_guess(guess, answer, attempts): #error to fix
                    break

            except ValueError:
                print('please enter a number')
                continue

        play_again_input = input('Do you want to give it another try?(yes/no): ')
        if play_again_input.lower() not in ['yes', 'y']:
            print('Come back again! Bye!!!')
            play_again = False

    # add score tracker
