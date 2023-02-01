import tkinter as tk
import random

def check_guess(word, guesses, entry, label):
    guess = entry.get()
    if guess == word:
        label.config(text="Correct!", fg="green")
    elif guesses > 1:
        label.config(text="Incorrect, try again. You have {} guesses left".format(guesses - 1), fg="red")
        return False
    else:
        label.config(text="You ran out of guesses! The word was {}".format(word), fg="red")
        disable_entry()
    return True

def disable_entry():
    entry.config(state="disabled")

def enable_entry():
    entry.config(state="normal")
    entry.delete(0, tk.END)

def new_game():
    word_list = ["python", "java", "javascript", "c++", "ruby", "perl"]
    word = random.choice(word_list)
    guesses = 5
    enable_entry()
    label.config(text="Guess the word:")
    for i in range(guesses):
        if check_guess(word, guesses - i, entry, label):
            break

root = tk.Tk()
root.title("Word Guess Game")

label = tk.Label(root, text="Guess the word:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Guess", command=new_game)
button.pack()

root.mainloop()
