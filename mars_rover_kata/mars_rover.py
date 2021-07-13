class MarsRover:
    def __init__(self, initial_position):
        self._position = initial_position

    def execute(self, command):
        if command == "M":
            if self._position[2] == "N":
                self._position = (self._position[0], self._position[1]+1, self._position[2])
            elif self._position[2] == "E":
                self._position = (self._position[0]+1, self._position[1], self._position[2])
            elif self._position[2] == "W":
                self._position = (self._position[0]-1, self._position[1], self._position[2])
            elif self._position[2] == "S":
                self._position = (self._position[0], self._position[1]-1, self._position[2])

    def final_position(self):
        return self._position
