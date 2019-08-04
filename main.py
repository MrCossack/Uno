import random


class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []


class Card():
    def __init__(self, color, number):
        self.color = color
        self.number = number


def add_player():
    player_list = []
    number_of_player = 9
    while number_of_player > 6 or number_of_player < 2:
        number_of_player = int(input("How many player? 2-6 "))

    for number in range(0, number_of_player):
        new_player = Player(input("Whats youre name player {}: ".format(number+1)))
        player_list.append(new_player)

    return player_list


def create_cards():
    color_list = ["red", "blue", "green", "yellow"]
    card_list = []
    id = 0

    for two_times in range(0, 2):
        for color in color_list:
            for number in range(1, 11):
                card_list.append(Card(color, number))
                id += 1

    return card_list


def play(player):
    count = 0
    for card in player.cards:
        print("{}:  Color = {} - Number = {}".format(count, card.color, card.number))
        count += 1

    while True:
        user_input = int(input("Choose a card: "))

        if user_input > 0 and user_input < len(player.cards):
            break

    return player.cards.pop(user_input)


def game():
    player_list = add_player()
    card_list = create_cards()
    random.shuffle(card_list)

    for player in player_list:
        for x in range(5):
            player.cards.append(card_list.pop())


    table_card = card_list.pop()
    print("\nCurrent card\nColor: {}\nNumber: {}\n".format(table_card.color, table_card.number))
    while True:
        for player in player_list:
            table_card = play(player)

            print("Current card\nColor: {}\nNumber: {}".format(table_card.color, table_card.number))

            if(len(player.cards) == 0):
                print("{} wins".format(player.name))
                break



game()