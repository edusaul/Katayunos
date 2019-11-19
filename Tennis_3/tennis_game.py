
class Game:
    SCORES = {0: "love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    def __init__(self):
        self.__present_score_team_1 = 0
        self.__present_score_team_2 = 0

    def points(self,team):
        if team==1:
            return self.SCORES[self.__present_score_team_1]
        else:
            return self.SCORES[self.__present_score_team_2]

    def score(self,team):
        if team==1:
            self.__present_score_team_1 += 1
        else:
            self.__present_score_team_2 += 1


