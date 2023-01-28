import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This class represents a single square on the chess board
class Square:
    def __init__(self, x, y, color):
        # Set the position and color of the square
        self.x = x
        self.y = y
        self.color = color

        # Set the piece on the square to None
        self.piece = None

    def draw(self, surface):
        # Draw the square
        pygame.draw.rect(surface, self.color, [self.x, self.y, 50, 50])

        # If there is a piece on the square, draw it
        if self.piece is not None:
            self.piece.draw(surface)

# This class represents a chess piece
class Piece:
    def __init__(self, x, y, color, type):
        # Set the position and color of the piece
        self.x = x
        self.y = y
        self.color = color
        self.type = type

    def draw(self, surface):
        # Draw the piece using a circle for now, to represent a pawn
        pygame.draw.circle(surface, self.color, [self.x + 25, self.y + 25], 25)

# This class represents the chess board
class Board:
    def __init__(self):
        # Set up the board with all the squares
        self.squares = []
        for y in range(0, 400, 50):
            for x in range(0, 400, 50):
                if (x + y) % 100 == 0:
                    self.squares.append(Square(x, y, WHITE))
                else:
                    self.squares.append(Square(x, y, BLACK))

        # Set up the pieces on the board
        self.squares[0].piece = Piece(0, 0, BLACK, "pawn")
        self.squares[7].piece = Piece(50, 0, BLACK, "pawn")
        self.squares[56].piece = Piece(0, 50, WHITE, "pawn")
        self.squares[63].piece = Piece(50, 50, WHITE, "pawn")

        # Set the current player to WHITE
        self.current_player = WHITE

    def draw(self, surface):
        # Draw all the squares on the board
        for square in self.squares:
            square.draw(surface)

    def get_square(self, x, y):
        # Get the square at the given coordinates
        for square in self.squares:
            if square.x == x and square.y == y:
                return square
        return None

    def move_piece(self, from_x, from_y, to_x, to_y):
        # Move the piece from the source square to the destination square
        from_square = self.get_square(from_x, from_y)
        to_square = self.get_square(to_x, to_y)
        to_square.piece = from_square.piece
        from_square.piece = None

        # Handle pawn promotion
        if to_square.piece.type == "pawn" and (to_y == 0 or to_y == 350):
            to_square.piece.type = "queen"

        # Switch the current player
        if self.current_player == WHITE:
            self.current_player = BLACK
        else:
            self.current_player = WHITE

# Set up the pygame window
pygame.init()
window_size = [400, 400]
screen = pygame.display.set_mode(window_size)

# Set up the chess board
board = Board()

# Run the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the clicked square
            x, y = event.pos
            x = x // 50 * 50
            y = y // 50 * 50
            square = board.get_square(x, y)

            # If the player clicked on a piece, set it as the selected piece
            if square.piece is not None and square.piece.color == board.current_player:
                selected_piece = square.piece
            # If the player clicked on an empty square and a piece is selected, try to move the selected piece there
            elif square.piece is None and selected_piece is not None:
                # Check if the move is legal
                if is_legal_move(selected_piece, x, y, board):
                    board.move_piece(selected_piece.x, selected_piece.y, x, y)
                    selected_piece = None

    # Clear the screen
    screen.fill(GREEN)

    # Draw the board
    board.draw(screen)

    # Display the current player's turn
    if board.current_player == WHITE:
        text = "White's turn"
    else:
        text = "Black's turn"
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (10, 10))

    # Update the display
    pygame.display.flip()

# Close the window
pygame.quit()

