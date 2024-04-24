import math

class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(50)] for _ in range(50)]
        self.current_player = 'X'
        self.winning_length = 4  # Longitud requerida para ganar

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
    
    def make_move(self, column):
        row = self.get_next_available_row(column)
        if row is not None:
            self.board[row][column] = self.current_player
            return True
        return False

    def get_next_available_row(self, column):
        for row in range(49, -1, -1):
            if self.board[row][column] == ' ':
                return row
        return None

    def check_winner(self):
        # Check horizontal
        for row in self.board:
            for col in range(47):
                if all(cell == self.current_player for cell in row[col:col+self.winning_length]):
                    return True

        # Check vertical
        for col in range(50):
            for row in range(47):
                if all(self.board[row+i][col] == self.current_player for i in range(self.winning_length)):
                    return True

        # Check diagonal \
        for row in range(47):
            for col in range(47):
                if all(self.board[row+i][col+i] == self.current_player for i in range(self.winning_length)):
                    return True

        # Check diagonal /
        for row in range(47):
            for col in range(3, 50):
                if all(self.board[row+i][col-i] == self.current_player for i in range(self.winning_length)):
                    return True

        return False

    def game_over(self):
        return self.check_winner() or all(cell != ' ' for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'


class MinimaxAI:
    def __init__(self, game):
        self.game = game

    def minimax(self, depth, maximizing_player):
        if depth == 0 or self.game.game_over():
            return None, self.evaluate()

        if maximizing_player:
            max_eval = -math.inf
            best_column = None
            for col in range(50):
                if self.game.make_move(col):
                    _, eval = self.minimax(depth - 1, False)
                    self.game.board[self.game.get_next_available_row(col)][col] = ' '
                    if eval > max_eval:
                        max_eval = eval
                        best_column = col
            return best_column, max_eval
        else:
            min_eval = math.inf
            best_column = None
            for col in range(50):
                if self.game.make_move(col):
                    _, eval = self.minimax(depth - 1, True)
                    self.game.board[self.game.get_next_available_row(col)][col] = ' '
                    if eval < min_eval:
                        min_eval = eval
                        best_column = col
            return best_column, min_eval

    def evaluate(self):
        if self.game.check_winner() and self.game.current_player == 'X':
            return 1
        elif self.game.check_winner() and self.game.current_player == 'O':
            return -1
        else:
            return 0

def main():
    game = Game()
    ai = MinimaxAI(game)

    while not game.game_over():
        game.print_board()
        print("Player", game.current_player)

        if game.current_player == 'X':  # Human player
            column = int(input("Enter column (0-49): "))
            while column < 0 or column > 49 or game.board[0][column] != ' ':
                column = int(input("Invalid column. Enter column (0-49): "))
        else:  # AI player
            column, _ = ai.minimax(4, True)

        game.make_move(column)
        game.switch_player()

    game.print_board()
    if game.check_winner():
        print("Player", game.current_player, "wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
