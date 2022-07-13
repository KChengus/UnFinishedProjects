import random


class Slot:
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.all_possible_bars = [1,2,3,4,5]
        self.probability_table = {
            1 : 40,
            2 : 30, 
            3 : 15,
            4 : 10,
            5 : 5,
        }


    def get_random_bar(self):
        random_number = random.randint(1, 100)
        s = 0
        for bar in self.all_possible_bars:
            s += self.probability_table[bar]
            if random_number <= s:
                return bar
        return self.all_possible_bars[-1]
    
    def generate_board(self, ):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = self.get_random_bar()

    def print_board(self):
        print("This is the board")
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(self.board[i][j], end=" ")
            print()
    
    def run(self):
        self.generate_board()
        self.print_board()


class Casino:
    def __init__(self):
        pass

    

if __name__ == "__main__":
    slot = Slot()
    slot.run()