import tkinter as tk
import pandas as pd
import random as rd


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data_to_learn = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data_original = pd.read_csv("data/french_words.csv")
    to_learn = data_original.to_dict(orient="records")
else:
    to_learn = data_to_learn.to_dict(orient="records")


def save_words():
    data = pd.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv", index=False)


def pick_words():
    global current_card
    current_card = rd.choice(to_learn)
    return current_card


def unknown_word():
    global flip_timer
    window.after_cancel(flip_timer)
    pick_words()
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card['French'], fill="black")
    canvas.itemconfig(img_on_canvas, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def known_word():
    global flip_timer
    window.after_cancel(flip_timer)

    to_learn.remove(current_card)
    print(f"{current_card['French']} learned. {len(to_learn)} words remaining.")
    save_words()

    pick_words()
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card['French'], fill="black")
    canvas.itemconfig(img_on_canvas, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(img_on_canvas, image=card_back_img)


window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
img_on_canvas = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
unknown_word()
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2 )

cross_img = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_img, highlightthickness=0, command=unknown_word)
unknown_button.grid(row=1, column=0)

check_img = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=check_img, highlightthickness=0,  command=known_word)
known_button.grid(row=1, column=1)


window.mainloop()
