"""
eight ball script: user inputs question and programs responds with an answer
"""

#!/usr/bin/env python

import time
import tkinter as tk
from random import randint

answers = ["It is almost certain",
           "It is decidedly so",
           "Without a doubt",
           "Yes definitely",
           "You may rely on it",
           "As I see it, yes",
           "Most likely",
           "Outlook good",
           "Yes",
           "Signs point to yes",
           "Reply hazy try again",
           "Ask again later",
           "Better not tell you now",
           "Cannot predict now",
           "Concentrate and ask again",
           "Don\'t count on it",
           "My reply is no",
           "My sources say no",
           "Outlook not so good",
           "Very doubtful"]

queries = []

def question():
    query = input("What is your question? ")
    print("thinking...")
    time.sleep(2)
    if query not in queries:
        queries.append(query)
    else:
        print("You already asked that question.")
        restart()
    print(answers[randint(0,19)])
    restart()

def restart():
    reply = input("Thanks for playing. Do you want to ask another question? ")
    if reply in ["YES", "yes", "Yes", "ya", "Ya", "YA", "y", "Y"]:
        question()
    else:
        exit()

"""
def retrieve():
    inputValue = query.get("1.0", "end-1c")
    print(inputValue)
"""

root = tk.Tk()
root.title("Magic 8 Ball Fortune")

button1 = tk.Button(root, text="Ask a Question", command=question)
button1.pack(pady=20, padx=20)

root.mainloop()

#question()