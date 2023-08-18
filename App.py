from random import randint, choice
import click


class Player:

    def __init__(self):
        self.name = None
        self.points = 0

    def name_get(self):
        self.name = input(f'Set your username: ')

    def name_print(self):
        print(f'Username set to: ', self.name)

    def congratulate(self):
        print(f'Great job, {self.name}!')
        self.points += 1

    # create name_display function


def clue(correct_answer):
    options = [correct_answer - 1, correct_answer + 1]
    return choice(options)


# @click.command()
# @click.option("--guess", prompt="Dare to guess?", help="Write a guess: ") # click interrupted code functionality
def run_guess(guess, correct_answer, attempt):
    counter = attempt
    if 0 < guess < 11:
        if guess == correct_answer:
            if attempt > 3:
                print('You got the correct answer in', attempt, 'attempts! Well done!')
                player.congratulate()
            elif attempt <= 2:
                print('You got the correct answer in', attempt, 'attempts! You\'re a genius!')
                player.congratulate()
            else:
                print('You got the correct answer in', attempt, 'attempts! Well done!')
                player.congratulate()

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
                if run_guess(guess, answer, attempts):  # error to fix
                    break

                attempts += 1
            except ValueError:
                print('please enter a number')
                continue

        play_again_input = input('Do you want to give it another try?(yes/no): ')
        if play_again_input.lower() not in ['yes', 'y']:
            print('Come back again! Bye!!!')
            play_again = False

    # add score tracker
