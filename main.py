from RPSEasy import RPSEasyBot as p1
from RPSRandom import RPSRandom as p3
from RPSMedium import RPSMediumBot as p2
from RPSTournament import RPSTournament

a = p1
b = p2
c = RPSTournament(p2, p3, 10000, True)

print(c.play_tournament())