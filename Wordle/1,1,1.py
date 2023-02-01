import tkinter as tk
from random import choice

def create_wordle(words):
    wordle = []
    for word in words:
        word_len = len(word)
        font_size = word_len * 10
        color = choice(["red", "blue", "green", "purple", "orange"])
        wordle.append((word, font_size, color))
    return wordle

def display_wordle(wordle):
    root = tk.Tk()
    root.title("Wordle")
    for word, font_size, color in wordle:
        label = tk.Label(root, text=word, font=("Helvetica", font_size), fg=color)
        label.pack()
    root.mainloop()

def play_wordle(words):
    word = choice(words)
    root = tk.Tk()
    root.title("Wordle Game")
    instructions = tk.Label(root, text="Guess the word:")
    instructions.pack()
    entry1 = tk.Entry(root, width=1)
    entry1.pack(side="left")
    entry1.focus_set()
    entry2 = tk.Entry(root, width=1)
    entry2.pack(side="left")
    entry3 = tk.Entry(root, width=1)
    entry3.pack(side="left")
    entry4 = tk.Entry(root, width=1)
    entry4.pack(side="left")
    entry5 = tk.Entry(root, width=1)
    entry5.pack(side="left")
    result = tk.Label(root)
    result.pack()
    
    def focus_next_entry(event, next_entry, prev_entry):
        if event.keysym == "BackSpace" and len(event.widget.get()) == 0:
            prev_entry.focus_set()
        elif len(event.widget.get()) == 0:
            next_entry.focus_set()
        
    def check_word():
        guess = entry1.get() + entry2.get() + entry3.get() + entry4.get() + entry5.get()
        if guess == word:
            result.config(text="Correct!")
            submit.config(state="disabled")
            entry1.config(state="disabled")
            entry2.config(state="disabled")
            entry3.config(state="disabled")
            entry4.config(state="disabled")
            entry5.config(state="disabled")
        else:
            result.config(text="Incorrect. Try again.")
    
    entry1.bind("<Key>", lambda event: focus_next_entry(event, entry2, None))
    entry2.bind("<Key>", lambda event: focus_next_entry(event, entry3, entry1))
    entry3.bind("<Key>", lambda event: focus_next_entry(event, entry4, entry2))
    entry4.bind("<Key>", lambda event: focus_next_entry(event, entry5, entry3))
    entry5.bind("<Key>", lambda event: focus_next_entry(event, None, entry4))
    submit = tk.Button(root, text="Submit", command=check_word)
    submit.pack()
    root.mainloop()

words = ["Hello", "World", "Python", "Tkinter", "Wordle"]
play_wordle(words)
