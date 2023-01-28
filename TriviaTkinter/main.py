import csv
import customtkinter

#Set colorscheme and mode for window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Create the main window
root = customtkinter.CTk()
root.geometry("800x600")
root.title("Trivia Game")

#Create and pack frame
frame = customtkinter.CTkFrame(master=root)
#.Pack = Add widget to window 
#Add frame to window, add padding and make it expandable
frame.pack(pady=20, padx=60, fill="both", expand=True)


# Create the start button
def start_game():
    global category
    category = category_var.get()
    #.pack_forget or .forget = remove widget from window
    category_label.pack_forget()
    category_menu.pack_forget()
    start_button.pack_forget()
    main_menu_label.pack_forget()
    difficulty_label.pack_forget()
    difficulty_menu.pack_forget()
    #Pady and padx are paddings to widgets, in px
    progress_bar.pack(pady=12, padx=10)
    progress_bar.set(0)
    load_questions()
    ask_question()



#Variables for category. Default = Tech
category_label = customtkinter.CTkLabel(master=frame, text="Select a category:")
category_var = customtkinter.StringVar(master=frame)
category_var.set("Tech")
category_menu = customtkinter.CTkOptionMenu(master=frame, values=["Tech", "Music", "History", "Miscellaneous"], variable=category_var)

#Variables for difficulty. Default = easy
difficulty_var = customtkinter.StringVar(root)
difficulty_var.set("Easy")
difficulty_label = customtkinter.CTkLabel(master=frame, text="Select a difficulty level:")
difficulty_menu =  customtkinter.CTkOptionMenu(master=frame, values=["Easy", "Medium", "Hard"], variable=difficulty_var)

#Other variables for labels, buttons and progressbar
quit_button = customtkinter.CTkButton(master=root, text="Quit", command=root.destroy)
start_button = customtkinter.CTkButton(master=frame, text="Start", command=start_game)
progress_bar = customtkinter.CTkProgressBar(master=frame, orientation="horizontal", width=600, height=16)
submit_button = customtkinter.CTkButton(master=frame)
play_again_button = customtkinter.CTkButton(master=frame)
result_label = customtkinter.CTkLabel(master=frame)
score_label = customtkinter.CTkLabel(master=frame)
main_menu_label = customtkinter.CTkLabel(master=frame, text="Welcome to a trivia game!", font=(None, 24))
question_label = customtkinter.CTkLabel(master=frame, text="Question")
answer_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Answer")
pass_button = customtkinter.CTkButton(master=frame)

#Function to pack all main menu widgets
def menu_widgets():
    main_menu_label.pack(pady=12, padx=10)
    category_label.pack(pady=12, padx=10)
    category_menu.pack(pady=12, padx=10)
    difficulty_label.pack(pady=12, padx=10)
    difficulty_menu.pack(pady=12, padx=10)
    start_button.pack(pady=12, padx=10)
    quit_button.pack(pady=12, padx=10)

menu_widgets()

# Load the questions from the appropriate CSV file based on the user's selection
def load_questions():
    #Format in csv file: category,question,answer. !NO SPACES!
    global questions
    questions = []
    if difficulty_var.get() == "Easy":
        with open('TriviaTkinter/easy_questions.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                questions.append(row)
    elif difficulty_var.get() == "Medium":
        with open('TriviaTkinter/medium_questions.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                questions.append(row)
    elif difficulty_var.get() == "Hard":
        with open('TriviaTkinter/hard_questions.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                questions.append(row)

# Create the question-asking function
current_question = 0
score = 0
def ask_question():
    global current_question, score
    # Update the progress bar
    #progress_bar.set(len(questions))
    #progress_bar["value"] = 0
    #progress_bar["maximum"] = len(questions)
    progress_bar.set(current_question/len(questions))
    #Runs if there are still questions that have not been answered
    if current_question < len(questions):
        question = questions[current_question]
        if question[0] == category_var.get():
            question_label.configure(text=question[1])
            question_label.pack(pady=12, padx=10)
            answer_entry.delete(0,customtkinter.END)
            answer_entry.pack(pady=12, padx=10)
            #bind command submit button to checkanswer function
            submit_button.configure(text="Submit", command=lambda: check_answer(answer_entry.get()))
            submit_button.pack(pady=12, padx=10)
            #Bind the return/enter key to submit/check answer function
            root.bind('<Return>', lambda event:check_answer(answer_entry.get()))
            pass_button.configure(text="Pass", command=pass_question)
            pass_button.pack(pady=12, padx=10)
        else:
            current_question += 1
            ask_question()
    #If all questions have been answered       
    else:
        pass
        end_game()

#Function for handling the pass input from the user
def pass_question():
    global current_question
    #Runs if there are still questions
    if current_question < len(questions):
        print("Question passed")
        print(score)
        result_label.configure(text_color="white", text="Passed Question")
        score_label.configure(text="Score: " + str(score))
        result_label.pack()
        score_label.pack()
        current_question += 1
        pass_button.pack_forget()
        question_label.pack_forget()
        answer_entry.pack_forget()
        submit_button.pack_forget()
        ask_question()
    #If all questions have been answered
    else:
        end_game()
# Create the answer-checking function
def check_answer(answer):
    global current_question, score
    #Checks if entry == rightanswer
    if answer.lower() == questions[current_question][2].lower():
        result_label.configure(text_color="green", text="Correct!")
        score += 1
        print("Correct")
        print("Right answer: ", questions[current_question][2])
    #Incorrect, no increment to score
    else:
        result_label.configure(text_color="red", text="Incorrect. The right answer is: " + questions[current_question][2])
        print("Incorrect")
        print("Right answer: ", questions[current_question][2])
    result_label.pack()
    current_question += 1
    score_label.configure(text="Score: " + str(score))
    score_label.pack()
    pass_button.pack_forget()
    question_label.pack_forget()
    answer_entry.pack_forget()
    submit_button.pack_forget()
    ask_question()

#Create the endgame function. Packs final score and play again button
def end_game():
    global result_label, play_again_button, quit_button
    #Unbind enter since submit button is pack_forget. Throws errors otherwise.
    root.unbind('<Return>')
    #Change to endgame menu
    score_label.forget()
    result_label.configure(text_color="white", text="Final score: " + str(score))
    result_label.pack()
    play_again_button.configure(text="Play Again", command=restart_game)
    play_again_button.pack()
    quit_button.pack()
    
#Create the restart game function. Calls if player clicks Play again
def restart_game():
    global current_question, score
    #Forget all widgets in frame
    for widget in frame.winfo_children():
        widget.pack_forget()
    #Call the menu widgets
    menu_widgets()
    #Reset values
    current_question = 0
    score = 0
    progress_bar["value"] = (current_question + 1) / len(questions) * 100
#Run from root
root.mainloop()