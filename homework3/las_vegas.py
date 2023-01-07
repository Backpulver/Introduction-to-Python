import random

class Card:
    def __init__(self, suit, face):
        self._suit = suit
        self._face = face

    def get_suit(self):
        return self._suit

    def get_face(self):
        return self._face


class Deck:
    def __init__(self, face_filter=[]):
        self._face_filter = face_filter
        self.deck_cards = []
        self.__suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.__faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        if len(self._face_filter) != 0:
            self.__faces = self._face_filter

        for suit in self.__suits:
            for face in self.__faces:
                self.deck_cards.append(Card(suit, face))

    def cut(self):
        cut_pivot = random.randint(1, len(self.deck_cards) - 1)
        self.deck_cards = self.deck_cards[cut_pivot:] + self.deck_cards[:cut_pivot]

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def get_cards(self):
        return self.deck_cards


class Player:
    def __init__(self):
        self.player_cards = []

    def get_cards(self):
        return self.player_cards


class Game(Deck):
    def __init__(self, number_of_players, dealing_direction, dealing_instructions):
        self.number_of_players = number_of_players
        self.dealing_direction = dealing_direction.lower()
        self.dealing_instructions = dealing_instructions
        self.deck = Deck()
        self.players = []
        for _player in range(number_of_players):
            self.players.append(Player())

    def get_players(self):
        return self.players

    def prepare_deck(self):
        for player in self.players:
            while len(player.player_cards) != 0:
                self.deck.deck_cards.append(player.player_cards.pop())

        self.deck.shuffle()
        self.deck.cut()

    def deal(self, player):
        pivot = self.players.index(player)
        self.players = self.players[pivot:] + self.players[:pivot]

        if self.dealing_direction == "rtl":
            first_elem = self.players.pop(0)
            self.players.reverse()
            self.players.insert(0, first_elem)

        for number_of_cards in self.dealing_instructions:
            for player in self.players:
                for elem in range(number_of_cards):
                    player.player_cards.append(self.deck.deck_cards.pop(0))

    def get_deck(self):
        return self.deck


class Belot(Game):
    def __init__(self):
        super().__init__(4, "ltr", (2, 3, 3))
        self.deck = Deck(["7", "8", "9", "10", "J", "Q", "K", "A"])


class Poker(Game):
    def __init__(self):
        super().__init__(9, "rtl", (1, 1, 1, 1, 1))

# deck = Deck()
# list1 = deck.get_cards()
# for elem in list1:
#     print(elem.get_face())
# deck.cut()
# list1 = deck.get_cards()
# for elem in list1:
#     print(elem.get_face())

# game = Game(4, "ltr", (2, 3, 3))
# players = game.get_players()
# list_players = game.get_players()
# game.deal(list_players[3])

# for i in players[3].player_cards:
#     print(i.get_face())

# poker = Poker()
# deck1 = poker.deal
# players1 = poker.get_players()
# poker.deal(players1[0])

# cards = players1[5].get_cards()
# for elem in cards:
#     print(elem.get_face())


# belot = Belot()
# deck2 = belot.deck.deck_cards

# players = belot.get_players()
# belot.deal(players[3])

# for elem in deck2:
#     # print(elem)
#     print(elem.get_face())

# cards = players[0].get_cards()
# for elem in cards:
#     print(elem.get_face())