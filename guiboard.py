from guicell import *
from gameboard import *
import tkinter as tk

class GuiBoard:

    grid = []
    cellState = []
    mainWindow = tk.Tk()

    def getButton(self, row, col):
        return self.grid[row][col]['text']

    def mouseClicked(self, event):
        r = event.widget.grid_info()['row']-1
        c = event.widget.grid_info()['column']
        cell = self.cellState[r][c]
        mouseButtonNo = event.num
        if mouseButtonNo == 1:
            if not cell.revealed:
                self.revealCell( r, c)
        if mouseButtonNo == 3:
            if not cell.revealed:
                self.cellState[r][c].revealed = True
                self.cellState[r][c].content = 'f'
        self.updateGui()
        
    def getHeight(self):
        return len(self.guiBoard)

    def getWidth(self):
        return len( self.guiBoard[0])

    def revealCell(self, row, col):
        if not self.cellState[row][col].revealed:
            self.cellState[row][col].revealed = True
            cellContent = self.gameBoard.checkCell( row, col)
            if cellContent == EMPTY:
                for r in range(row-1, row + 2):
                    for c in range(col-1, col+2):
                        if r!=row or c!=col:
                            if r>=0 and r<self.getHeight() and c>=0 and c<self.getWidth():
                                neighbourCellContent = self.gameBoard.checkCell(r,c)
                                if neighbourCellContent == EMPTY:
                                    self.revealCell( r, c)
                                else:
                                    self.cellState[r][c].content = neighbourCellContent
                                    self.cellState[r][c].revealed = True
            else:
                self.cellState[row][col].content = cellContent

    def createGui(self, mouseClickCallback):
        title = tk.Label(master=self.mainWindow, text='Minesweeper')
        title.pack()

        btnGrid = tk.Frame(master=self.mainWindow)

        for r in range( len(self.guiBoard) ):
            row = []
            stateRow = []

            for c in range( len(self.guiBoard[0]) ):
                button = tk.Button(
                    master=btnGrid,
                    relief=tk.RAISED,
                    borderwidth=2,
                    width=2,
                    height=1,
                    background="lightgray"
                )
                button.bind_all("<Button>", mouseClickCallback)
                button.grid(row = r+1, column=c)
                button.pack_propagate(0)
                row.append( button )
                stateRow.append( GuiCell() )

            self.grid.append(row)
            self.cellState.append( stateRow )

        btnGrid.pack()
        self.mainWindow.mainloop()

    def updateGui(self):
        for r in range(self.getHeight() ):
            for c in range(self.getWidth() ):
                if self.cellState[r][c].revealed:
                    text = self.cellState[r][c].content
                    if text == 0:
                        text = ' '
                    self.grid[r][c]['text'] = text
                    self.grid[r][c].configure(relief=tk.SUNKEN)

    def __init__(self, width, height, noOfMines) -> None:

        self.gameBoard = GameBoard()
        self.gameBoard.createBoard( width, height)
        self.gameBoard.addMines( noOfMines)
        self.gameBoard.printBoard()
        self.guiBoard = [ [GuiCell()] * width ] * height
        self.createGui( self.mouseClicked )


    
