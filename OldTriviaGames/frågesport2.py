import pygame
from dataclasses import dataclass
from pygame.locals import K_BACKSPACE, K_RETURN, KEYDOWN
from typing import List

@dataclass
class TriviaQuestion:
    question: str
    options: List[str]
    answer: str
    font: pygame.font.Font

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

def display_question(screen, font, question):
    # Clear the screen
    screen.fill((255, 255, 255))
    # Render the question text
    text = font.render(question.question, 1, (0, 0, 0))

    # Calculate the position of the text
    x = (screen.get_width() - text.get_width()) // 2
    y = (screen.get_height() - text.get_height()) // 2

    # Draw the text on the screen
    screen.blit(text, (x, y))

    # Render the prompt text
    prompt = question.font.render("Enter your answer: ", 1, (0, 0, 0))
    
    # Calculate the position of the prompt

    x = (screen.get_width() - prompt.get_width()) // 2
    y = y + text.get_height() + 10

    # Draw the prompt on the screen
    screen.blit(prompt, (x, y))

    # Call the display_options() function to display the options
    display_options(screen, font, question, x, y)

    # Update the display
    pygame.display.flip()
    
def display_options(screen, font, question, x, y):
    # Get the list of options
    options = question.options
    # Loop through the options
    for i, option in enumerate(options):
        # Render the option text
        text = question.font.render(option, 1, (0, 0, 0))

        # Calculate the position of the option
        option_x = x + (i * text.get_width()) + 10
        option_y = y + prompt.get_height() + 10
    
        # Draw the option on the screen
        screen.blit(text, (option_x, option_y))

def handle_input(answer):
    # Check for events
    for event in pygame.event.get():
        # Check if the user has closed the window
        if event.type == pygame.QUIT:
            return False
        # Check if the user has pressed a key
        if event.type == KEYDOWN:
            # Get the key code
            key = event.key

            # Check if the key is a letter or number
            if key >= ord('a') and key <= ord('z') or key >= ord('0') and key <= ord('9'):
                # Append the key to the answer
                answer.append(chr(key))
            elif key == K_BACKSPACE:
                # Remove the last character from the answer
                answer = answer[:-1]
            elif key == K_RETURN:
                # Return the answer as a string
                return "".join(answer)

    # Return None if the user has not entered a complete answer
    return None

def check_answer(question, answer):
    # Return True if the answer is correct, False otherwise
    return question.answer == answer

def main():
    # Initialize the game
    screen, font = init_game()
    # Create a list of trivia questions
    questions = [
        TriviaQuestion("What is the capital of France?", ["Paris", "London", "Madrid"], "Paris", font),
        TriviaQuestion("What is the square root of 256?", ["16", "32", "64"], "16", font),
        TriviaQuestion("What is the largest planet in the solar system?", ["Earth", "Jupiter", "Saturn"], "Jupiter", font),
    ]

    # Loop through the questions
    for question in questions:
        # Display the question
        display_question(screen, font, question)

        # Initialize the answer
        answer = []

        # Loop until the user has entered a complete answer
        while True:
            # Handle user input
            result = handle_input(answer)

            # Check if the user has entered a complete answer
            if result is not None:
                # Check the answer and display the result
                if check_answer(question, result):
                    print("Correct!")
                else:
                    print("Incorrect.")

                # Wait for the user to press a key
                input("Press enter to continue...")

                # Break out of the loop
                break

    # Close the window
    pygame.quit()
if __name__ == "__main__":
    main()