"""
author: john haney
language: python 3
description: eight ball script - user inputs question and program responds with an answer from available answers in the list
modules: tkinter, time, random
"""

#!/usr/bin/env python

import time
from tkinter import *
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
           "Don't count on it",
           "My reply is no",
           "My sources say no",
           "Outlook not so good",
           "Very doubtful"]

queries = []
repeat = "You already asked that question."
think = "thinking..."
sorry = "Sorry, I didn't understand you. Exiting..."
yes = ["YES", "yes", "Yes", "ya", "Ya", "YA", "y", "Y"]
no = ["NO", "no", "No", "nah", "Nope", "n", "N"]

"""
def question():
    query = input("What is your question? ")
    print(think)
    time.sleep(2)
    if query not in queries:
        queries.append(query)
    else:
        print(repeat)
        restart()
    print(answers[randint(0,19)])
    restart()
"""

def question():
    query = e1.get()
    print(think)
    time.sleep(2)
    if query not in queries:
        queries.append(query)
    else:
        print(repeat)
        restart()
    print(answers[randint(0,19)])
    restart()

def restart():
    reply = input("Thanks for playing. Do you want to ask another question? ")
    if reply in yes:
        question()
    elif reply in no:
        exit()
    else:
        print(sorry)
        exit()

root = Tk()
root.title("Magic 8 Ball")

logo = PhotoImage(file="img/8ball.png")
w1 = Label(root, image=logo).pack(side="top")
w2 = Label(root,
           justify=CENTER,
           pady=10,
           padx=20,
           font="Verdana 12 bold",
           text="Hello! Welcome to the Magic 8 Ball.").pack(side="top")

w3 = Label(root,
           justify=LEFT,
           font="Verdana 10",
           text="Enter your question here: ").pack(side="top")

e1 = Entry(root,
           width=50).pack(side="top")

b1 = Button(root,
            width=10,
            text="Submit",
            command=question).pack(side="top")

w4 = Label(root,
           justify=LEFT,
           pady=20,
           font="Verdana 10",
           text="Answer:").pack(side="top")

root.mainloop()