class Queen:
    def __init__(self, row: int, column: int) -> None:
        if row < 0:
            raise ValueError("row not positive")
        elif row > 7:
            raise ValueError("row not on board")
        elif column < 0:
            raise ValueError("column not positive")
        elif column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.col = column

    def can_attack(self, o: "Queen") -> bool:
        if self.row == o.row and self.col == o.col:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (self.col == o.col or
                self.row == o.row or
                abs(self.col - o.col) == abs(self.row - o.row))
