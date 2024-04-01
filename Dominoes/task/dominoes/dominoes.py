# Write your code here
import random
import time

PLAYER = 0
COMPUTER = 1

class Domino:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return str([self.a, self.b])

    def get_list(self):
        return [self.a, self.b]

    def is_double(self):
        return self.a == self.b

    def is_identical(self, a, b):
        if self.a == a and self.b == b:
            return True
        if self.a == b and self.b == a:
            return True
        return False



class DominoStack:
    def __init__(self):
        self.stack = []

    def add_domino(self, domino):
        if isinstance(domino, list):
            self.stack += domino
        else:
            self.stack.append(domino)

    def remove_domino(self, count = 1):
        if len(self.stack) >= count:
            taken_items = self.stack[:count]
            self.stack = self.stack[count:]
            return taken_items
        else:
            return None

    def remove_domino_at(self, index):
        if len(self.stack) >= 0:
            del self.stack[index]

    def get_size(self):
        return len(self.stack)

    def __str__(self):
        return str([i.get_list() for i in self.stack])

    def check_highest_double(self):
        found_domino = None
        index = -1
        for i, d in enumerate(self.stack):
            if d.is_double():
                if found_domino is None or d.a > found_domino.a:
                    found_domino = d
                    index = i
        return found_domino, index

    def find_domino_index(self, a, b):
        for i in range(self.stack.len()):
            if self.stack[i].is_identical(a, b):
                return i
        return -1

    def del_domino(self, index):
        if index < len(self.stack):
            self.stack.remove(index)

    def get_domino(self, index):
        if index < len(self.stack):
            return self.stack[index]
        else:
            return None

class StockPieces(DominoStack):

    def __init__(self):
        self.stack = self.initialise_stack()
        self.shuffle()

    def initialise_stack(self):
        return [Domino(a, b) for a in range(7) for b in range(a, 7)]

    def shuffle(self):
        random.shuffle(self.stack)

class SnakeStack(DominoStack):
    pass
class Game:

    def __init__(self):
        random.seed(time.time())
        self.stock_pieces = None
        self.players = []
        self.snake = SnakeStack()
        self.current_player = 0
        ok = False
        while not ok:
            ok = self.initialise_game()
        self.print_status()

    def set_player(self, domino, index, next_players):
        self.snake.add_domino(domino)
        self.current_player = next_players
        self.players[(next_players + 1) % 2].remove_domino_at(index)

    def initialise_game(self):
        self.stock_pieces = StockPieces()
        self.players.append(DominoStack())
        self.players.append(DominoStack())
        self.players[PLAYER].add_domino(self.stock_pieces.remove_domino(7))
        self.players[COMPUTER].add_domino(self.stock_pieces.remove_domino(7))
        domino_computer,  index_computer = self.players[COMPUTER].check_highest_double()
        domino_player, index_player = self.players[PLAYER].check_highest_double()

        if domino_computer == None and domino_player == None:
            print("have to reshuffle")
            print(f"Player: {self.players[PLAYER]}")
            print(f"Computer: {self.players[COMPUTER]}")
            print("----------------------------------")
            return False
        if domino_computer == None:
            self.set_player(domino_player, index_player, COMPUTER)
        elif domino_player == None:
            self.set_player(domino_computer, index_computer, PLAYER)
        elif domino_player.a > domino_computer.a:
            self.set_player(domino_player, index_player, COMPUTER)
        else:
            self.set_player(domino_computer, index_computer, PLAYER)
        return True

    def print_status(self):
        print(f"Stock pieces: {self.stock_pieces}")
        print(f"Computer pieces: {self.players[COMPUTER]}")
        print(f"Player pieces: {self.players[PLAYER]}")
        print(f"Domino snake: {self.snake}")
        print("Status: {}".format("player" if self.current_player == PLAYER else "computer"))


game = Game()

