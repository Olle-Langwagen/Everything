import pygame
from dataclasses import dataclass

# Define a dataclass to represent a trivia question
@dataclass
class Question:
    category: str
    difficulty: int
    text: str
    answer: str

# Initialize Pygame and create a window
pygame.init()
window = pygame.display.set_mode((800, 600))

# Define some questions
questions = [
    Question("Geography", 1, "What is the capital of France?", "Paris"),
    Question("Geography", 3, "What is the longest river in the world?", "The Nile"),
    Question("Science", 2, "What is the chemical symbol for hydrogen?", "H"),
    Question("Science", 5, "What is the speed of light in a vacuum?", "299,792,458 m/s"),
]

# Display the categories and let the player choose one
print("Choose a category:")
for i, q in enumerate(questions):
    print(f"{i + 1}. {q.category}")
chosen_category = int(input()) - 1

# Display the questions in the chosen category
for q in questions:
    if q.category == chosen_category:
        # Clear the window
        window.fill((0, 0, 0))
        
        # Render the question text
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(q.text, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (400, 300)
        window.blit(text, text_rect)
        
        # Update the window
        pygame.display.flip()
        
        # Get the player's response
        response = input()
        if response == q.answer:
            print("Correct!")
            player_score += q.difficulty
        else:
            print("Incorrect!")

# Display the player's final score
print(f"Your score: {player_score}")