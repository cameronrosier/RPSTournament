class RPSMediumBot:
    """
    This class represents a Rock Paper Scissors bot

    """

    def __init__(self):
        self.name = "RPS Medium Bot"
        self.author = "Cameron Rosier"

        self.num_wins = 0
        self.num_rounds_played = 0
        self.current_num = 1

    def choice(self):
        if self.current_num == 1:
            self.current_num += 1
            return 'R'
        elif self.current_num == 2:
            self.current_num += 1
            return 'P'
        elif self.current_num == 3:
            self.current_num = 1
            return 'S'
