# Cell values. Either EMPTY, MINE, FLAG or a number representing adjacent mines.
EMPTY = 0
MINE = -1
FLAG = -2
UNCLICKED = -3


class GuiCell:

    def __init__(self) -> None:
        self.content = EMPTY
        self.revealed = False

