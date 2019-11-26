
class Team:
    def __init__(self):
        self.__points=0
    def get_points(self):
        return self.__points
    def score(self):
        self.__points +=1


class Game:
    POINT_NAMES = {
        0: 'love',
        1: 'fifteen',
        2: 'thirty',
        3: 'forty'
    }

    def __init__(self):
        self.teams={
            1: Team(),
            2: Team()
        }

    def points(self, team):
        return self.teams[team].get_points()

    def games(self, team):
        return 0

    def sets(self, team):
        return 0

    def name_points(self,points):
        return self.POINT_NAMES[points]

    def score(self, team):
        self.teams[team].score()
