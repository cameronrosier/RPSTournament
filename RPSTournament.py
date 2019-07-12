class RPSTournament:

    def __init__(self, p1, p2, num_rounds, extra_stats=False):
        self.p1 = p1()
        self.p2 = p2()
        self.extra_stats = extra_stats
        self.p1_moves = [0, 0, 0]
        self.p2_moves = [0, 0, 0]
        self.num_rounds = num_rounds

    def get_winner(self, c1, c2):
        if c1 == 'R':
            self.p1_moves[0] += 1
            if c2 == 'R':
                self.p2_moves[0] += 1
                return -1
            elif c2 == 'P':
                self.p2_moves[1] += 1
                return 0
            elif c2 == 'S':
                self.p2_moves[2] += 1
                return 1
        elif c1 == 'P':
            self.p1_moves[1] += 1
            if c2 == 'R':
                self.p2_moves[0] += 1
                return 1
            elif c2 == 'P':
                self.p2_moves[1] += 1
                return -1
            elif c2 == 'S':
                self.p2_moves[2] += 1
                return 0
        elif c1 == 'S':
            self.p1_moves[2] += 1
            if c2 == 'R':
                self.p2_moves[0] += 1
                return 0
            elif c2 == 'P':
                self.p2_moves[1] += 1
                return 1
            elif c2 == 'S':
                self.p2_moves[2] += 1
                return -1

    def play_round(self, p1, p2):
        p1_choice = p1.choice()
        p2_choice = p2.choice()

        win_code = self.get_winner(p1_choice, p2_choice)
        if win_code == 1:
            self.p1.num_wins += 1
            print(self.p1.name + ' wins with: ' + p1_choice)
        elif win_code == 0:
            self.p2.num_wins += 1
            print(self.p2.name + ' wins with: ' + p2_choice)

        self.p1.num_rounds_played += 1
        self.p2.num_rounds_played += 1

    
    def play_tournament(self):
        for i in range(self.num_rounds):
            self.play_round(self.p1, self.p2)
        
        print('\n\n+=====+=====+=====+=====+=====+=====+')
        print('+ - G A M E   S T A T I S T I C S - +')
        print('+=====+=====+=====+=====+=====+=====+')
        print('Total Rounds Played: %s' % str(self.num_rounds))
        print("%s's wins: %s. Win Ratio: %s%%" % (self.p1.name, str(self.p1.num_wins), str(self.p1.num_wins / self.num_rounds * 100)))
        print("%s's wins: %s. Win Ratio: %s%%" % (self.p2.name, str(self.p2.num_wins), str(self.p2.num_wins / self.num_rounds * 100)))
        if self.p1.num_wins == self.p2.num_wins:
            print("\nIt was a tie!  Congratulations to both %s and %s!" % (self.p1.name, self.p2.name))
        else:
            print("\nOur winner is...")
            print("%s!" % str(max(self.p1.num_wins, self.p2.num_wins)))
        
        if self.extra_stats:
            print("\n+~+~+~+~+~+~+~+~+~+~+~+~+~+~+")
            print("Player: %s #" % self.p1.name)
            print("---------------------------")
            print("Number of Rocks Thrown: %s" % str(self.p1_moves[0]))
            print("Number of Paper Thrown: %s" % str(self.p1_moves[1]))
            print("Number of Scissors Thrown: %s" % str(self.p1_moves[2]))

            print("\nPlayer: %s #" % self.p2.name)
            print("---------------------------")
            print("Number of Rocks Thrown: %s" % str(self.p2_moves[0]))
            print("Number of Paper Thrown: %s" % str(self.p2_moves[1]))
            print("Number of Scissors Thrown: %s" % str(self.p2_moves[2]))
        else:
            print("Note: Run with RPSTournament parameter 'extra_stats' set to True for a larger game breakdown")
