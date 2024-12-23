import tkinter as tk
from tkinter import messagebox
import random


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "user"
    else:
        return "computer"


def play(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    
    if result == "user":
        user_score += 1
        result_text.set("You win!")
    elif result == "computer":
        computer_score += 1
        result_text.set("You lose!")
    else:
        result_text.set("It's a tie!")

        user_choice_text.set(f"You chose: {user_choice}")
    computer_choice_text.set(f"Computer chose: {computer_choice}")
    score_text.set(f"Score: You {user_score} - {computer_score} Computer")


user_score = 0
computer_score = 0


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="black")


user_choice_text = tk.StringVar()
computer_choice_text = tk.StringVar()
result_text = tk.StringVar()
score_text = tk.StringVar()


user_choice_text.set("You chose: None")
computer_choice_text.set("Computer chose: None")
result_text.set("Result will be shown here.")
score_text.set("Score: You 0 - 0 Computer")


title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("League Spartan", 20), bg="black", fg="white")
title_label.pack(pady=10)


user_label = tk.Label(root, textvariable=user_choice_text, font=("League Spartan", 12), bg="black", fg="white")
user_label.pack()

computer_label = tk.Label(root, textvariable=computer_choice_text, font=("League Spartan", 12), bg="black", fg="white")
computer_label.pack()

result_label = tk.Label(root, textvariable=result_text, font=("League Spartan", 14), bg="black", fg="white")
result_label.pack(pady=10)

score_label = tk.Label(root, textvariable=score_text, font=("League Spartan", 14), bg="black", fg="white")
score_label.pack(pady=5)

button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("League Spartan", 14), bg="blue", fg="white",
                        command=lambda: play('rock'), width=8)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", font=("League Spartan", 14), bg="green", fg="white",
                         command=lambda: play('paper'), width=8)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", font=("League Spartan", 14), bg="red", fg="white",
                            command=lambda: play('scissors'), width=8)
scissors_button.grid(row=0, column=2, padx=5)

exit_button = tk.Button(root, text="Exit", font=("League Spartan", 12), bg="gray", fg="white",
                        command=root.destroy, width=10)
exit_button.pack(pady=10)

root.mainloop()
