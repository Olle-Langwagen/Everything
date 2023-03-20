import tkinter as tk

class ChessBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pawn_x = 0
        self.pawn_y = 0
        self.title("Pawn Chess")
        self.geometry("800x800")
        self.create_board()
        self.pawns = []
        self.create_pawns()
        self.create_opponent_pawns()
        self.resizable(False,False)

    def create_board(self):
        # Create a 8x8 grid of squares
        for i in range(8):
            self.rowconfigure(i, weight=1)  # Set the weight of each row to 1
            for j in range(8):
                self.columnconfigure(j, weight=1)  # Set the weight of each column to 1
                square = tk.Label(self, bg="white" if (i+j) % 2 == 0 else "black")
                square.grid(row=i, column=j, sticky="nsew") # Make the widgets expand and fill the entire cell
        self.grid_propagate(False) # prevent widgets from resizing the parent frame

    def create_pawns(self):
    # Create pawns on the board
        for i in range(8):
            pawn = tk.Label(self, text="P", font=("Helvetica", 8), bg="green")
            pawn.grid(row=1, column=i)
            pawn.unbind("<ButtonPress-1>")
            pawn.unbind("<ButtonRelease-1>")
            pawn.bind("<ButtonPress-1>", lambda event, pawn=pawn: self.move_pawn_start(event, pawn))
            pawn.bind("<ButtonRelease-1>", lambda event, pawn=pawn: self.move_pawn_end(event, pawn))
            self.pawns.append(pawn)

    def create_opponent_pawns(self):
        # create pawns for the opponent
        for i in range(8):
            pawn = tk.Label(self, text="P", font=("Helvetica", 8), bg="red")
            pawn.grid(row=6, column=i)
            self.pawns.append(pawn)

    def move_pawn(self, pawn, row, col):
        pawn.grid(row=row, column=col, in_=self)

    def move_pawn_start(self, event, pawn):
        pawn.config(relief="sunken")
        self.pawn_x = event.x
        self.pawn_y = event.y
        self.pawn_parent = pawn.grid_info()["column"]

    def move_pawn_end(self, event, pawn):
        current_row = pawn.grid_info()["row"]
        current_col = pawn.grid_info()["column"]
        new_col = current_col
        new_row = current_row + 1
        if new_row > 7:
            new_row = 7
        square = self.grid_slaves(new_row, new_col)[0]
        if square["bg"] != "white" and square["bg"] != "black":
            return
        if event.x > square.winfo_x() and event.x < square.winfo_x() + square.winfo_width() and event.y > square.winfo_y() and event.y < square.winfo_y() + square.winfo_height():
            pawn.unbind("<ButtonPress-1>")
            pawn.unbind("<ButtonRelease-1>")
            self.move_pawn(pawn, new_row, new_col)
            pawn.bind("<ButtonPress-1>", lambda event, pawn=pawn: self.move_pawn_start(event, pawn))
            pawn.bind("<ButtonRelease-1>", lambda event, pawn=pawn: self.move_pawn_end(event, pawn))
if __name__ == "__main__":
    board = ChessBoard()
    board.mainloop()