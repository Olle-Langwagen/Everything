import pygame
from dataclasses import dataclass
from typing import List
import time
# Define the dataclass for a trivia question
@dataclass
class TriviaQuestion:
  question: str
  answers: List[str]
  correct_answer: str

# Define a list of trivia questions
questions = [
  TriviaQuestion(
    question="What is the capital of France?",
    answers=["Paris", "London", "Rome", "Madrid"],
    correct_answer="Paris"
  ),
  TriviaQuestion(
    question="Who is the current President of the United States?",
    answers=["Donald Trump", "Joe Biden", "Barack Obama", "George Washington"],
    correct_answer="Joe Biden"
  ),
  TriviaQuestion(
    question="What is the highest mountain in the world?",
    answers=["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
    correct_answer="Mount Everest"
  ),
]

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Set the font and font size for the trivia game
font = pygame.font.Font(None, 36)

# Initialize the game loop
running = True
current_question_index = 0
score = 0
while running:
  # Get the current question and answers
  question = questions[current_question_index]
  answers = question.answers

  # Clear the screen
  screen.fill((255, 255, 255))

  # Draw the question text on the screen
  question_text = font.render(question.question, True, (0, 0, 0))
  screen.blit(question_text, (100, 100))

  # Draw the answer buttons on the screen
  for i, answer in enumerate(answers):
    button_x = 100
    button_y = 200 + i * 50
    button_rect = pygame.Rect(button_x, button_y, 600, 40)
    pygame.draw.rect(screen, (0, 0, 0), button_rect)
    answer_text = font.render(answer, True, (255, 255, 255))
    screen.blit(answer_text, (button_x + 20, button_y + 10))

  # Update the display
  pygame.display.update()

  # Wait for the player to select an answer
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONUP:
      # Check if the player clicked on one of the answer buttons
      mouse_x, mouse_y = event.pos
      for i, answer in enumerate(answers):
        button_x = 100
        button_y = 200 + i * 50
        button_rect = pygame.Rect(button_x, button_y, 600, 40)
        if button_rect.collidepoint(mouse_x, mouse_y):
          # Check if the selected answer is correct
          if answer == question.correct_answer:
            score += 1
          # Move on to the next question
          current_question_index += 1
          if current_question_index >= len(questions):
            # All questions have been answered, end the game
            running = False
          break

# Display the final score
score_text = font.render(f"Your score: {score}", True, (0, 0, 0))
screen.blit(score_text, (0, 50))
pygame.display.update()
time.sleep(5)
# Wait for the player to close the window
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

# Quit pygame
pygame.quit()
