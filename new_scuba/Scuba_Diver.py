class ScubaDiver():
    FULL_OXYGEN = 150
    SEA_LEVEL = 0
    ONE_METER = 1

    def __init__(self):
        self.oxygen = self.FULL_OXYGEN
        self.depth = self.SEA_LEVEL
        self.is_alive = True

    def hold_depth(self):
        pass

    def dive(self):
        self.depth -= self.ONE_METER

    def ascend(self):
        if (self.is_under_sea_level()):
            self.depth += self.ONE_METER

    def is_under_sea_level(self):
        return self.depth < self.SEA_LEVEL

    def score(self):
        return 0