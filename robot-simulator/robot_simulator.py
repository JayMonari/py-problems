# Globals for the directions

EAST = 0.0
NORTH = 1.0
WEST = 2.0
SOUTH = 3.0


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = x_pos, y_pos

    def _turn(self, dir: float) -> None:
        self.direction = (self.direction + dir) % 4.0

    def _advance(self) -> None:
        if self.direction == NORTH:
            self.coordinates = self.coordinates[0], self.coordinates[1] + 1
        elif self.direction == SOUTH:
            self.coordinates = self.coordinates[0], self.coordinates[1] - 1
        elif self.direction == EAST:
            self.coordinates = self.coordinates[0] + 1, self.coordinates[1]
        elif self.direction == WEST:
            self.coordinates = self.coordinates[0] - 1, self.coordinates[1]

    def move(self, instructions: str) -> None:
        for ins in instructions:
            if ins == "L":
                self._turn(1.0)
            elif ins == "R":
                self._turn(-1.0)
            elif ins == "A":
                self._advance()
