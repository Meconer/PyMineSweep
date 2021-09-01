from random import *

# Cell values. Can be either EMPTY or MINE
EMPTY = 0
MINE = -1

class GameBoard:

    def createBoard(self, width, height):
        self.width = width
        self.height = height
        self.gameBoard = []
        for i in range(height):
            cols = []
            for j in range(width):
                cols.append( EMPTY )
            self.gameBoard.append(cols)
        
    def addMines(self, noOfMines):
        for i in range(noOfMines):
            while True:
                row = randint(0,self.width-1)
                col = randint(0,self.height-1)
                if self.gameBoard[row][col] == EMPTY:
                    break
            self.gameBoard[row][col] = MINE

    def printCell( self, cell ):
        cellContent = '_'
        if cell == MINE:
            cellContent = 'X'
        print(cellContent, end='')

    def printBoard(self):
        for row in range(self.height):
            for col in range(self.width):
                self.printCell( self.gameBoard[row][col])
            print()

    def checkCell(self, row, col):
        cellContent = self.gameBoard[row][col]
        neighbourMineCount = 0
        if cellContent == 0:
            for r in range(row-1, row + 2):
                    for c in range(col-1, col+2):
                        if r!=row or c!=col:
                            if r>=0 and r<self.height and c>=0 and c<self.width:
                                if self.gameBoard[r][c] == MINE:
                                    neighbourMineCount += 1
            return neighbourMineCount
        else:
            return cellContent



if __name__ == "__main__":
    board = GameBoard()
    board.createBoard(8,8)
    board.addMines(10)
    board.printBoard()
    print(board.checkCell( 5,5))
