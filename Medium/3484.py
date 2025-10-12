class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        # strip leading '=' if present
        if formula.startswith("="):
            formula = formula[1:]

        cells = formula.split("+")
        total = 0
        for c in cells:
            c = c.strip()
            if c[0].isalpha():  # cell reference like A1
                row, col = self.getCell(c)
                total += self.grid[row][col]
            else:  # plain number
                total += int(c)
        return total

    def getCell(self, cell: str) -> tuple[int, int]:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        return row, col
