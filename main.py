import random
import Player
import Card


class Game():
    def __init__(self):
        self.starting_cards = 2

        self.current_player_id = 0
        self.game_inverted = False

        self.list_of_player = []
        self.card_stack = []
        self.played_cards = []

        self.add_player()
        self.create_cards()
        random.shuffle(self.card_stack)
        random.shuffle(self.list_of_player)
        self.deal_cards()

        self.center_card = self.card_stack.pop()

    def add_player(self):
        number_of_player = 9
        while number_of_player > 6 or number_of_player < 2:
            number_of_player = int(input("How many player? 2-6 "))

        for number in range(0, number_of_player):
            new_player = Player.Player(input("Whats youre name player {}: ".format(number+1)))
            self.list_of_player.append(new_player)
        print()

    def create_cards(self):
        color_list = ["red", "blue", "green", "yellow"]

        for two_times in range(0, 2):
            for color in color_list:
                for number in range(1, 11):
                    self.card_stack.append(Card.Card(color, number))

    def deal_cards(self):
        for player in self.list_of_player:
            for x in range(self.starting_cards):
                player.cards.append(self.card_stack.pop())

    def update_current_player_id(self):
        if self.game_inverted:
            if self.current_player_id > 0:
                self.current_player_id -= 1
            else:
                self.current_player_id = len(self.list_of_player)-1
        else:
            if self.current_player_id < len(self.list_of_player)-1:
                self.current_player_id += 1
            else:
                self.current_player_id = 0

    def user_interaction(self, player):
        print("Center card: ", self.center_card, "\n")
        print("Player: {}".format(player.name))

        for idx, card in enumerate(player.cards):
            print("{} | ".format(idx), card)

        user_choice = int(input("-1 | take a card\nYour Choice: "))

        print()
        return user_choice

    def play_round(self):
        pass

    def play(self):
        player = self.list_of_player[self.current_player_id]

        while True:
            # derzeit ueber Konsolen Ein und Ausgabe
            user_choice = self.user_interaction(player)

            # Spieler nimmt eine Karte
            if user_choice == -1:
                player.cards.append(self.card_stack.pop())
                self.update_current_player_id()
                break

            # Stimmt die ausgespielte Karte mit der Farbe der letzten gespielten Karte ueberein
            if player.cards[user_choice].color == self.center_card.color:
                self.center_card = player.cards.pop(user_choice)
                self.update_current_player_id()
                break

            # Stimmt die ausgespielte Karte mit der Zahl der letzten gespielten Karte ueberein
            if player.cards[user_choice].number == self.center_card.number:
                self.center_card = player.cards.pop(user_choice)
                self.update_current_player_id()
                break

        # falls der Kartenstapel leer wird, erstelle neue Karten
        # ab 5, da es eine -4 Karte gibt
        if len(uno_game.card_stack) < 5:
            uno_game.create_cards()

        if len(player.cards) == 0:
            print("Congratulatioin {} you are the winner!".format(player.name))
            return False
        else:
            return True


if __name__ == "__main__":
    uno_game = Game()
    play = True

    while play:
        play = uno_game.play()

