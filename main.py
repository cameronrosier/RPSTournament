from RPSEasy import RPSEasyBot as p1
from RPSMedium import RPSMediumBot as p2
from RPSTournament import RPSTournament

a = p1
b = p2
c = RPSTournament(p1, p2, 100, True)

print(c.play_tournament())