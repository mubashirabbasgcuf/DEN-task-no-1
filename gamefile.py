import argparse
import random

class RedBlueNimGame:
    def __init__(self, num_red, num_blue, version, first_player, depth):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.first_player = first_player
        self.depth = depth
        self.current_player = first_player
        self.game_over = False
        self.score = 0

    def play_game(self):
        while not self.game_over:
            if self.current_player == 'human':
                self.human_move()
            else:
                self.computer_move()
            self.calculate_score()
            self.switch_player()
        print(f"Game over! Final score: {self.score}")

    def human_move(self):
        while True:
            move = input("Enter your move (1-2 red or 1-2 blue): ")
            if move in ['1 red', '2 red', '1 blue', '2 blue']:
                self.update_game_state(move)
                break
            else:
                print("Invalid move. Try again!")

    def computer_move(self):
        if self.version == 'standard':
            move_ordering = ['2 red', '2 blue', '1 red', '1 blue']
        else:
            move_ordering = ['1 blue', '1 red', '2 blue', '2 red']
        best_move = self.minimax(self.depth, float('-inf'), float('inf'))
        self.update_game_state(best_move)

    def minimax(self, depth, alpha, beta):
        if self.game_over:
            return self.calculate_score()
        if depth == 0:
            return self.heuristic_evaluation()
        if self.current_player == 'computer':
            best_value = float('-inf')
            for move in self.get_possible_moves():
                self.update_game_state(move)
                self.switch_player()
                value = self.minimax(depth - 1, alpha, beta)
                self.undo_move(move)
                self.switch_player()
                best_value = max(best_value, value)
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_value
        else:
            best_value = float('inf')
            for move in self.get_possible_moves():
                self.update_game_state(move)
                self.switch_player()
                value = self.minimax(depth - 1, alpha, beta)
                self.undo_move(move)
                self.switch_player()
                best_value = min(best_value, value)
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value

    def get_possible_moves(self):
        if self.game_over:
            return []
        moves = []
        if self.num_red >= 2:
            moves.append('2 red')
        if self.num_red >= 1:
            moves.append('1 red')
        if self.num_blue >= 2:
            moves.append('2 blue')
        if self.num_blue >= 1:
            moves.append('1 blue')
        return moves

    def update_game_state(self, move):
        if move == '1 red':
            self.num_red -= 1
        elif move == '2 red':
            self.num_red -= 2
        elif move == '1 blue':
            self.num_blue -= 1
        elif move == '2 blue':
            self.num_blue -= 2
        if self.num_red == 0 or self.num_blue == 0:
            self.game_over = True

    def undo_move(self, move):
        if move == '1 red':
            self.num_red += 1
        elif move == '2 red':
            self.num_red += 2
        elif move == '1 blue':
            self.num_blue += 1
        elif move == '2 blue':
            self.num_blue += 2

    def switch_player(self):
        if self.current_player == 'human':
            self.current_player = 'computer'
        else:
            self.current_player = 'human'

    def calculate_score(self):
        if self.version == 'standard':
            if self.num_red == 0:
                self.score = self.num_blue * 3
            else:
                self.score = self.num_red * 2
        else:
            if self.num_blue == 0:
                self.score = self.num_red * 2
            else:
                self.score = self.num_blue * 3

    def heuristic_evaluation(self):
        if self.version == 'standard':
            return self.num_red * 2 + self.num_blue * 3
        else:
            return self.num_blue * 3 + self.num_red * 2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--num-red', type=int, default=10)
    parser.add_argument('--num-blue', type=int, default=10)
    parser.add_argument('--version', type=str, default='standard')
    parser.add_argument('--first-player', type=str, default='human')
    parser.add_argument('--depth', type=int, default=5)

    args = parser.parse_args()

    game = RedBlueNimGame(args.num_red, args.num_blue, args.version, args.first_player, args.depth)
    game.play_game()