# Import the necessary modules and libraries
import pygame
from dataclasses import dataclass
from typing import List
# Define a dataclass to represent a trivia question
@dataclass
class TriviaQuestion:
    question: str
    options: List[str]
    answer: str

# Define a function to initialize the game
def init_game():
    # Initialize Pygame
    pygame.init()

    # Set the window title and dimensions
    pygame.display.set_caption("Python Trivia")
    screen = pygame.display.set_mode((800, 600))

    # Set the background color
    screen.fill((255, 255, 255))

    # Define a font for the trivia questions
    font = pygame.font.Font(None, 36)

    # Return the screen and font objects
    return screen, font

# Define a function to display a trivia question
def display_question(screen, font, question):
    # Render the question text
    text = font.render(question.question, 1, (0, 0, 0))

    # Calculate the position of the text
    x = (screen.get_width() - text.get_width()) // 2
    y = (screen.get_height() - text.get_height()) // 2

    # Draw the text on the screen
    screen.blit(text, (x, y))

    # Update the display
    pygame.display.flip()
    pygame.display.update()
# Define a function to handle user input
def handle_input():
    # Check for events
    for event in pygame.event.get():
        # Check if the user has closed the window
        if event.type == pygame.QUIT:
            return False

    # Return True to continue the game
    return True

# Define a function to check the answer
def check_answer(question, answer):
    # Return True if the answer is correct, False otherwise
    return question.answer == answer

# Define a main function to run the game
def main():
    # Initialize the game
    screen, font = init_game()

    # Create a list of trivia questions
    questions = [
        TriviaQuestion("What is the capital of France?", ["Paris", "London", "Madrid"], "Paris"),
        TriviaQuestion("What is the square root of 256?", ["16", "32", "64"], "16"),
        TriviaQuestion("What is the largest planet in the solar system?", ["Earth", "Jupiter", "Saturn"], "Jupiter"),
    ]

    # Loop through the questions
    for question in questions:
        # Display the question
        display_question(screen, font, question)
        pygame.display.update()
        pygame.event.pump()
        # Get the user's answer
        answer = input("Enter your answer: ")

        # Check the answer and display the result
        if check_answer(question, answer):
            print("Correct!")
        else:
            print("Incorrect.")

        # Wait for the user to press a key
        input("Press enter to continue...")

    # Close the window
    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()
