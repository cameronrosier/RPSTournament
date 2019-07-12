class RPSBot:
    """
    This class represents a Rock Paper Scissors bot

    Rules for your bot:

    ### Rename the class 'RPSBot' to something more unique ###

    (1) The choice function must exist, and must always return an 'R', 'P', or 'S'

    (2) Fill in the __init__ function with a bot name and your name as the author.
        * The other parameters simply exist to aid in your strategy and are expected to exist by the Tournament framework, please keep them there even if you don't use them

    (3) Your bot cannot simply throw a random toss every turn (i.e. come up with an actual strategy whether it be offensive, defensive or a mixture of the two)
        * An example of a bot that throws random:
        
        from random import randint

        def choice(self):
            moves = ['R', 'P', 'S']
            return moves[randint(0, 2)]

    (4) To qualify for the tournament, where you can face others bots, you must send me your bot and it must be able to beat an 'easy' and a 'medium' level RPS AI (the same bot must be able to beat both)
        * Easy -- Throws Rock every turn
        * Medium --- Alternates between the three choices

    (5) You're free to do whatever else you want in this class and I suppose it may be beneficial to have external data storage but let's keep it to just one other file (i.e. 'accumulated_data.csv')

    (6) Feel free to delete this documentation to reduce clutter

    """

    def __init__(self):
        self.name = "CamBot1"
        self.author = "Cameron Rosier"

        self.num_wins = 0
        self.num_rounds_played = 0
    

    def choice(self):
        return 'R'
