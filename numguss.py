
import tkinter as tk
import random
from tkinter import messagebox

# Generate a random number
secret_number = random.randint(1, 100)
attempts = 0


def check_guess():
    global attempts

    try:
        guess = int(guess_entry.get())

        if guess < 1 or guess > 100:
            result_label.config(
                text="Enter a number between 1 and 100!",
                fg="orange"
            )
            return

        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")

        if guess < secret_number:
            result_label.config(
                text="Too low! Try a higher number.",
                fg="blue"
            )
        elif guess > secret_number:
            result_label.config(
                text="Too high! Try a lower number.",
                fg="red"
            )
        else:
            result_label.config(
                text=f"Correct! You won in {attempts} attempts!",
                fg="green"
            )
            messagebox.showinfo(
                "Congratulations!",
                f"You guessed the number {secret_number}!"
            )
            guess_button.config(state="disabled")

    except ValueError:
        result_label.config(
            text="Please enter a valid number!",
            fg="red"
        )

    guess_entry.delete(0, tk.END)


def restart_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    attempts_label.config(text="Attempts: 0")
    result_label.config(
        text="Enter your guess below!",
        fg="black"
    )
    guess_entry.delete(0, tk.END)
    guess_button.config(state="normal")


# Create main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x400")
root.resizable(False, False)
root.configure(bg="#EAF2F8")

# Heading
title_label = tk.Label(
    root,
    text="Number Guessing Game",
    font=("Arial", 20, "bold"),
    bg="#EAF2F8",
    fg="#154360"
)
title_label.pack(pady=20)

# Instructions
instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 12),
    bg="#EAF2F8"
)
instruction_label.pack(pady=5)

# Input field
guess_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    width=15
)
guess_entry.pack(pady=15)
guess_entry.focus()

# Guess button
guess_button = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 12, "bold"),
    bg="#2874A6",
    fg="white",
    command=check_guess
)
guess_button.pack(pady=5)

# Result message
result_label = tk.Label(
    root,
    text="Enter your guess below!",
    font=("Arial", 11, "bold"),
    bg="#EAF2F8"
)
result_label.pack(pady=15)

# Attempts counter
attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 12),
    bg="#EAF2F8"
)
attempts_label.pack(pady=5)

# Restart button
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 11),
    bg="#239B56",
    fg="white",
    command=restart_game
)
restart_button.pack(pady=10)

# Press Enter to check the guess
guess_entry.bind("<Return>", lambda event: check_guess())

# Run application
root.mainloop()
