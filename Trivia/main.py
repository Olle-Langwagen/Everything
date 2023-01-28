import tkinter as tk
import csv

# main window
main_window = tk.Tk()
main_window.title("Trivia Game")

score = 0
question_num = 0
current_category = ""
questions = []

# main menu function
def main_menu():
    global main_window
    main_window.geometry("800x600")

    # Create start button
    start_button = tk.Button(main_window, text="Start", command=choose_category)
    start_button.pack()

    # Create quit button
    quit_button = tk.Button(main_window, text="Quit", command=main_window.destroy)
    quit_button.pack()



# Function to choose category
def choose_category():
    global main_window
    main_window.geometry("800x600")
    # clear widgets from the main window
    for widget in main_window.winfo_children():
        widget.destroy()
    # Create category buttons
    category_1_button = tk.Button(main_window, text="Games", command=lambda: play_game("Games"))
    category_1_button.pack()
    category_2_button = tk.Button(main_window, text="History", command=lambda: play_game("History"))
    category_2_button.pack()
    category_3_button = tk.Button(main_window, text="Geography", command=lambda: play_game("Geography"))
    category_3_button.pack()
    category_4_button = tk.Button(main_window, text="Science", command=lambda: play_game("Science"))
    category_4_button.pack()

# Function to play the game
def play_game(category):
    global questions, current_category, question_num, score
    current_category = category
    question_num = 0
    score = 0
    questions = []
    # Open CSV file with questions and answers
    with open("Trivia\questions.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == category:
                questions.append(row)
        if questions:
            ask_question()
        else:
            print("No question found for this category.")

# Function to ask question
def ask_question():
    global main_window, questions, question_num, score, current_category
    if question_num >= len(questions):
        end_game()
    else:
        main_window.geometry("800x600")
        # clear widgets from the main window
        for widget in main_window.winfo_children():
            widget.destroy()
        question = questions[question_num]
        question_label = tk.Label(main_window, text=question[1])
        question_label.pack()
        player_answer = tk.Entry(main_window)
        player_answer.pack()
        result_label = tk.Label(main_window)
        result_label.pack()
        submit_button = tk.Button(main_window, text="Submit", command=lambda: check_answer(question[2], player_answer.get(), result_label))
        submit_button.pack()

def check_answer(correct_answer, player_answer, result_label):
  global question_num, score

  if player_answer.lower() == correct_answer.lower():
    result_label.config(text="Correct!")
    score += 1
  else:
    result_label.config(text="Incorrect.")
  question_num += 1
  ask_question()

def end_game():
  global main_window, score, current_category
  main_window.geometry("800x600")
  # clear widgets from the main window
  for widget in main_window.winfo_children():
    widget.destroy()
    end_label = tk.Label(main_window, text="Your Score for "+current_category+" category is :"+str(score))
    end_label.pack()
    restart_button = tk.Button(main_window, text="Play Again", command=main_menu)
    restart_button.pack()
    quit_button = tk.Button(main_window, text="Quit", command=main_window.destroy)
    quit_button.pack()
main_menu()
main_window.mainloop()