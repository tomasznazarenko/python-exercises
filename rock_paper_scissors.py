from random import choice

ROCK = "rock"
SCISSORS = "scissors"
PAPER = "paper"
EXIT_OPTION = "!exit"
SCORE_OPTION = "!rating"
FILE_RATING = "rating.txt"
AI_OPTIONS = [ROCK, SCISSORS, PAPER]
USER_OPTIONS = [ROCK, SCISSORS, PAPER, EXIT_OPTION, SCORE_OPTION]
INVALID_INPUT_MSG = "Invalid input"
POINTS_DRAW = 50
POINTS_WIN = 100
POINTS_LOSING = 0


def get_ai_option():
    return choice(AI_OPTIONS)


def is_user_option_valid(option):
    return option in USER_OPTIONS


def get_user_option():
    while True:
        inp = input()
        if is_user_option_valid(inp):
            return inp
        else:
            print(INVALID_INPUT_MSG)


def determine_winner(option, ai_option, player_name, ratings):
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if option == ai_option:
        ratings[player_name] += POINTS_DRAW
        print(f"There is draw {option}")
    elif wins[option] == ai_option:
        ratings[player_name] += POINTS_WIN
        print(f"Well done. The computer chose {ai_option} and failed")
    else:
        ratings[player_name] += POINTS_LOSING
        print(f"Sorry, but the computer chose {ai_option}")


def play_game(option, ai_option, player_name, ratings):
    determine_winner(option, ai_option, player_name, ratings)


def load_ratings():
    rating_file = open('rating.txt', 'r', encoding='utf-8')
    rating_dic = {}
    for line in rating_file:
        name_score = line.replace('\n', '').split(' ')
        rating_dic[name_score[0]] = int(name_score[1])
    rating_file.close()
    return rating_dic


def get_score(player_name, ratings):
    return 0 if player_name not in ratings else ratings[player_name]


def save_ratings(ratings):
    rating_file = open('rating.txt', 'w', encoding='utf-8')
    for name, points in ratings.items():
        rating_file.write(name + ' ' + str(points) + '\n')
    rating_file.write(name + '\n')
    rating_file.close()


player_name = input("Enter your name: ")
print(f"Hello, {player_name}")
ratings = load_ratings()
score = get_score(player_name, ratings)

while True:
    user_option = get_user_option()
    if user_option == EXIT_OPTION:
        save_ratings(ratings)
        print("Bye!")
        break
    if user_option == SCORE_OPTION:
        print(f'Your rating: {get_score(player_name, ratings)}')
    else:
        play_game(user_option, get_ai_option(), player_name, ratings)
