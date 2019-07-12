class RPSRandom:
    """
    This class represents a Rock Paper Scissors bot
    """

    def __init__(self):
        self.name = "RPS Random Bot"
        self.author = "Cameron Rosier"

        self.num_wins = 0
        self.num_rounds_played = 0
    

    def choice(self):
        from random import randint
        choices = ['R', 'P', 'S']
        
        return choices[randint(0, 2)]
