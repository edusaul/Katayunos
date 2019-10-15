class ScubaDiver:
    def __init__(self):
        self.oxigen = 150
        self.depth = 0

    def is_alive(self):
        oxigen = 3
        if self.oxigen > 0:
            return True
        else:
            return False

    def get_oxigen(self):
        return self.oxigen


class ScubaDaughter(ScubaDiver):
    def __init__(self):
        super().__init__()
        self.cosa_nueva = "esta es la nueva cosa"

    def get_cosa_nueva(self):
        return self.cosa_nueva

