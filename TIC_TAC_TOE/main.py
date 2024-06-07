import math

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def empty_squares(self):
        return ' ' in [cell for row in self.board for cell in row]

    def num_empty_squares(self):
        return len(self.available_moves())

    def make_move(self, square, letter):
        if self.board[square[0]][square[1]] == ' ':
            self.board[square[0]][square[1]] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row
        row_ind = square[0]
        row = self.board[row_ind]
        if all([s == letter for s in row]):
            return True
        # Check the column
        col_ind = square[1]
        column = [self.board[r][col_ind] for r in range(3)]
        if all([s == letter for s in column]):
            return True
        # Check the diagonals
        if square[0] == square[1]:
            diagonal1 = [self.board[i][i] for i in range(3)]
            if all([s == letter for s in diagonal1]):
                return True
        if square[0] + square[1] == 2:
            diagonal2 = [self.board[i][2 - i] for i in range(3)]
            if all([s == letter for s in diagonal2]):
                return True
        return False

def minimax(state, depth, alpha, beta, maximizing_player):
    max_player = 'X'  # AI is 'X'
    other_player = 'O'  # Human is 'O'

    if state.current_winner == other_player:
        return {'position': None, 'score': 1 * (depth + 1) if other_player == max_player else -1 * (depth + 1)}
    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    if maximizing_player:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for possible_move in state.available_moves():
        state.make_move(possible_move, max_player if maximizing_player else other_player)
        sim_score = minimax(state, depth + 1, alpha, beta, not maximizing_player)

        state.board[possible_move[0]][possible_move[1]] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move

        if maximizing_player:
            if sim_score['score'] > best['score']:
                best = sim_score
            alpha = max(alpha, sim_score['score'])
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
            beta = min(beta, sim_score['score'])

        if beta <= alpha:
            break

    return best

def draw_board(board):
    print("\n  0 | 1 | 2 ")
    print(" -----------")
    for i, row in enumerate(board):
        print(i, "|", " | ".join(row), "|")

def play_game():
    t = TicTacToe()
    print("\nWelcome to Tic Tac Toe!")
    draw_board(t.board)

    letter = 'X'
    while t.empty_squares():
        if letter == 'O':
            while True:
                row = int(input('Enter the row (0, 1, 2): '))
                col = int(input('Enter the column (0, 1, 2): '))
                if (row, col) in t.available_moves():
                    break
                else:
                    print("Invalid move. Try again.")
            t.make_move((row, col), letter)
        else:
            print("\nAI's turn (X):")
            move = minimax(t, 0, -math.inf, math.inf, True)['position']
            t.make_move(move, letter)

        draw_board(t.board)
        if t.current_winner:
            print("\n" + letter + ' wins!')
            return
        letter = 'O' if letter == 'X' else 'X'

    print("\nIt's a tie!")

play_game()
