# Write your code here
import random
import time

PLAYER = 0
COMPUTER = 1

class Domino:
    """A class representing a domino.

    The Domino class has methods for getting the values, checking if it is a double, and checking if it is identical to a given set of values.

    Attributes:
        a: The first value on the domino.
        b: The second value on the domino.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        """
        Convert the object to a string representation.

        :return: A string representation of the object.
        """
        return str([self.a, self.b])

    def swap(self):
        x = self.a
        self.a = self.b
        self.b = x
    def contains_number(self, number: int) -> bool:
        return number in [self.a, self.b]

    def get_list(self) -> list:
        """
        Return a list containing the values of attributes `a` and `b`.

        :return: A list with the attributes `a` and `b`
        :rtype: list
        """
        return [self.a, self.b]

    def is_double(self) -> bool:
        """
        Checks if the values of `a` and `b` are equal.

        :return: True if `a` and `b` are equal, False otherwise.
        :rtype: bool
        """
        return self.a == self.b

    def is_identical(self, a: int, b: int) -> bool:
        """
        Check if the values of 'a' and 'b' are identical to the instance variables 'self.a' and 'self.b'.

        :param a: An integer representing the value to compare with 'self.a'.
        :param b: An integer representing the value to compare with 'self.b'.
        :return: Returns True if both 'a' and 'b' are identical to 'self.a' and 'self.b' respectively, otherwise False.
        """
        if self.a == a and self.b == b:
            return True
        if self.a == b and self.b == a:
            return True
        return False



class DominoStack:
    """

    DominoStack

    A class that represents a stack of domino objects.

    Methods:
        - __init__(self)
            Initializes an empty stack.

        - get_size(self) -> int
            Returns the size of the stack.

        - add_domino(self, domino: object)
            Adds the provided domino object to the stack. If the domino parameter is of type list, the elements of the list will be concatenated to the stack.
            Otherwise, the domino object will be appended as a single element to the stack.

        - remove_domino(self, count: int = 1) -> list
            Removes the specified number of dominos from the stack.
            Returns the removed dominos as a list. If the count exceeds the number of dominos in the stack, returns None.

        - remove_domino_at(self, index: int)
            Removes the domino at the specified index from the stack.

        - __str__(self) -> str
            Returns a string representation of the stack.

        - check_highest_double(self) -> (Domino, int)
            Checks for the highest double domino in the stack.
            Returns a tuple containing the highest double domino found (if any) and its index in the stack.

        - find_domino_index(self, a: int, b: int) -> int
            Finds the index of a domino in the stack based on the given parameters.
            Returns the index of the domino in the stack if found, otherwise -1.

        - get_domino(self, index: int) -> Domino or None
            Retrieves a domino object at the specified index from the stack.
            Returns the domino object if the index is valid, otherwise returns None.

        - print_list(self)
            Prints each domino in the stack with its index.

    """
    def __init__(self):
        self.stack = []

    def do_loop(self, left: int, right: int, weight_list: dict):
        pass

    def get_size(self) -> int:
        """
        Returns the size of the stack.

        :return: The size of the stack.
        :rtype: int
        """
        return len(self.stack)

    def add_domino(self, domino: object, position: int = 1):
        """
        :param domino: The domino object to be added to the stack.
        :return: None

        Adds the provided domino object to the stack. If the domino parameter is of type list, the elements of the list will be concatenated to the stack. Otherwise, the domino object will be
        * appended as a single element to the stack.
        """
        if domino is None:
            return

        if isinstance(domino, list):
            self.stack += domino
        else:
            if position == 1:
                self.stack.append(domino)
            else:
                self.stack.insert(0, domino)

    def remove_domino(self, count: int = 1) -> list:
        """
        Remove Domino

        Removes the specified number of dominos from the stack.

        :param count: (int) The number of dominos to remove from the stack. Default value is 1.
        :return: (list) The removed dominos as a list. If the count exceeds the number of dominos in the stack, returns None.

        """
        if len(self.stack) >= count:
            taken_items = self.stack[:count]
            self.stack = self.stack[count:]
            return taken_items
        else:
            return None

    def remove_domino_at(self, index: int):
        """
        :param index: The index of the domino to remove from the stack.
        :return: None

        Removes the domino at the specified index from the stack.
        """
        if len(self.stack) >= 0:
            if index >= len(self.stack):
                print("The domino is out of range")
            del self.stack[index]

    def __str__(self)-> str:
        """
        Return a string representation of the object.

        :return: String representation of the stack
        """
        return str([i.get_list() for i in self.stack])

    def check_highest_double(self) -> (Domino, int):
        """
        Check for the highest double domino in the stack.

        :return: Tuple containing the highest double domino found (if any) and its index in the stack.
        :rtype: (Domino, int)
        """
        found_domino = None
        index = -1
        for i, d in enumerate(self.stack):
            if d.is_double():
                if found_domino is None or d.a > found_domino.a:
                    found_domino = d
                    index = i
        return found_domino, index

    def find_domino_index(self, a: int, b: int) -> int:
        """
        Find the index of a domino in the stack based on the given parameters.

        :param a: The first number of the domino.
        :param b: The second number of the domino.
        :return: The index of the domino in the stack if found, otherwise -1.
        :rtype: int

        """
        for i in range(self.stack.len()):
            if self.stack[i].is_identical(a, b):
                return i
        return -1

    def get_domino(self, index: int) -> Domino or None:
        """
        :param index: An integer representing the index of the domino to retrieve from the stack.
        :return: Either a Domino object at the specified index or None if the index is out of range.
        """
        if index < len(self.stack):
            return self.stack[index]
        else:
            return None

    def print_list(self):
        """
        Prints the elements in the stack with their corresponding index.

        :param self: The instance of the class.
        :type self: object

        :return: None
        """
        for index, domino in enumerate(self.stack):
            print(f"{index + 1}:{str(domino)}")

    def get_weight_list(self) -> dict:
        weight_list = {i: 0 for i in range(7)}
        for i in self.stack:
            weight_list[i.a] += 1
            weight_list[i.b] += 1

        return weight_list



class DominoPlayer(DominoStack):
    def do_loop(self, left: int, right: int, weight_list: dict):
        print()
        print("Status: It's your turn to make a move. Enter your command.")
        # get a valuable input
        answer = None
        while answer is None:
            try:
                answer = int(input())
                if answer not in range ((-1) * (len(self.stack) + 1), len(self.stack) + 1):
                    raise ValueError(f"Not in range")

                index = abs(answer) - 1
                if answer < 0:
                    if not self.stack[index].contains_number(left):
                        raise Exception("Illegal move. Please try again.")
                if answer > 0:
                    if not self.stack[index].contains_number(right):
                        raise Exception("Illegal move. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
                answer = None
            except Exception as e:
                print(e)
                answer = None

        return answer

class DominoComputer(DominoStack):
    def do_loop(self, left: int, right: int, weight_list: dict) -> int:
        print()
        print("Status: Computer is about to make a move. Press Enter to continue...")
        # get the input any key
        input()

        # get the two weight lists and combine them
        w1 = self.get_weight_list()
        for i in range(7):
            w1[i] += weight_list[i]

        # now check all the dominos if they work, and use the one with the highest ranking
        current_weight = -1
        side = 0
        for index, i in enumerate(self.stack):
            if i.contains_number(left) or i.contains_number(right):
                w = w1[i.a] + w1[i.b]
                if w > current_weight:
                    current_weight = w
                    best_domino = index
                    side = -1 if i.contains_number(left) else 1
        if current_weight == -1:
            value = 0
        else:
            value = best_domino + 1
            value = value * (-1) if side == -1 else value

        return value

class StockPieces(DominoStack):
    """
    Class representing a stock of domino pieces.

    This class inherits from the `DominoStack` class.

    Attributes:
        stack (list): The list representing the stock of domino pieces.

    Methods:
        __init__(): Initializes a new instance of the StockPieces class.
        initialise_stack(): Initializes the stack attribute with a list of domino pieces.
        shuffle(): Randomly shuffles the domino pieces in the stack.
    """
    def __init__(self):
        self.stack = self.initialise_stack()
        self.shuffle()

    def initialise_stack(self):
        """
        Initialise the stack with a list of Domino objects.

        :return: A list of Domino objects representing the initial stack.
        :rtype: list[Domino]
        """
        return [Domino(a, b) for a in range(7) for b in range(a, 7)]

    def shuffle(self):
        """
        Shuffles the elements in the stack randomly.

        :return: None
        """
        random.shuffle(self.stack)

class SnakeStack(DominoStack):
    """
    SnakeStack Class

    A class for representing a stack of dominoes in a snake-like fashion.

    This class is derived from the DominoStack class.

    Methods
    -------
    __init__()
        Initializes an empty SnakeStack object.

    size() -> int
        Returns the current number of dominoes in the stack.

    is_empty() -> bool
        Returns True if the stack is empty, False otherwise.

    push(domino: Domino)
        Pushes a domino onto the top of the stack.

    pop() -> Domino
        Removes and returns the top domino from the stack.

    top() -> Domino
        Returns the top domino from the stack without removing it.
    """
    def __str__(self)-> str:
        """
        Return a string representation of the object.

        :return: String representation of the stack
        """
        ret = ""
        if self.get_size() > 6:
            ret = f"{self.stack[0]} {self.stack[1]} {self.stack[2]}...{self.stack[-3]} {self.stack[-2]} {self.stack[-1]}"
        else:
            for d in self.stack:
                ret += str(d) + " "
        return ret

    def add_domino(self, domino: object, position: int = 1):
        if len(self.stack) > 0:
            if position == 0:
                if domino.b != self.stack[0].a:
                    domino.swap()
            elif position == 1:
                if domino.a != self.stack[-1].b:
                    domino.swap()
        super().add_domino(domino, position)


class Game:
    """
    Class representing a game of Dominoes.

    Attributes:
        stock_pieces (StockPieces): The stock pieces of the game.
        players (list): List of DominoStack objects representing the players of the game.
        snake (SnakeStack): The domino snake of the game.
        current_player (int): Index of the current player in the `players` list.

    Methods:
        __init__(): Initializes a new game.
        set_player(domino, index, next_players): Sets the next player and updates the domino snake.
        initialise_game(): Initializes the game by shuffling dominos and setting the initial player.
        print_status(): Prints the current status of the game.
    """
    def __init__(self):
        random.seed(time.time())
        self.stock_pieces = None
        self.players = []
        self.snake = SnakeStack()
        self.current_player = 0
        ok = False
        while not ok:
            ok = self.initialise_game()

    def set_player(self, domino: Domino, index: int, next_players: int):
        """
        Set the next player and update the game state by adding the played domino to the snake and removing it from the player's hand.

        :param domino: The domino being played.
        :param index: The index of the domino being removed from the current player's hand.
        :param next_players: The index of the next player (should be either 0 or 1).

        :return: None
        """
        self.snake.add_domino(domino)
        self.current_player = next_players
        self.players[(next_players + 1) % 2].remove_domino_at(index)

    def initialise_game(self) -> bool:
        """
        Initialise the game.

        :return: True if the game was successfully initialised, False otherwise.
        """
        self.stock_pieces = StockPieces()
        self.players = [None, None]
        self.players[COMPUTER] = DominoComputer()
        self.players[PLAYER] = DominoPlayer()
        self.players[PLAYER].add_domino(self.stock_pieces.remove_domino(7))
        self.players[COMPUTER].add_domino(self.stock_pieces.remove_domino(7))
        domino_computer,  index_computer = self.players[COMPUTER].check_highest_double()
        domino_player, index_player = self.players[PLAYER].check_highest_double()

        if domino_computer == None and domino_player == None:
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
        """
        Print the status of the game.

        :return: None
        """
        print("=" * 70)
        print(f"Stock size: {self.stock_pieces.get_size()}")
        print(f"Computer pieces: {self.players[COMPUTER].get_size()}")
        print("")
        print(self.snake)
        print()
        print("Your pieces:")
        self.players[PLAYER].print_list()

    def is_win_situation(self):
        if self.players[PLAYER].get_size() == 0:
            print()
            print("Status: The game is over. You won!")
            return True
        elif self.players[COMPUTER].get_size() == 0:
            print()
            print("Status: The game is over. The computer won!")
            return True
        else:
            weight_list = self.snake.get_weight_list()
            if weight_list[self.snake.get_domino(0).a] == 8 and weight_list[self.snake.get_domino(-1) == 8]:
                print()
                print("Status: The game is over. It's a draw!")
                return True
        return False
    def do_game_loop(self):
        while True :
            self.print_status()
            if self.is_win_situation():
                break
            move = self.players[self.current_player].do_loop(self.snake.get_domino(0).a, self.snake.get_domino(-1).b,
                                                             self.snake.get_weight_list())
            if move == 0:
                self.players[self.current_player].add_domino(self.stock_pieces.remove_domino(1))
            elif move > 0:
                domino = self.players[self.current_player].get_domino(move - 1)
                self.players[self.current_player].remove_domino_at(move - 1)
                self.snake.add_domino(domino, 1)
            elif move < 0:
                move = abs(move)
                domino = self.players[self.current_player].get_domino(move - 1)
                self.players[self.current_player].remove_domino_at(move - 1)
                self.snake.add_domino(domino, 0)
            # switch player
            self.current_player = (self.current_player + 1) % 2


game = Game()
game.do_game_loop()

