import tkinter as tk
import pandas as pd
import random as rd


BACKGROUND_COLOR = "#B1DDC6"
prev_fr = ""
data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict()
# print(data_dict)
learned_words_list = []
total_word_pairs = len(data_dict['French'])
print(total_word_pairs)
fr_ = ""
en_ = ""


def pick_words():
    word_index = rd.randint(0, 100)
    fr_word = data_dict['French'][word_index]
    en_word = data_dict['English'][word_index]
    if len(learned_words_list) >= total_word_pairs:
        print("All word pairs learned.")
        return "All word pairs learned", ""
    elif fr_word in learned_words_list:
        return pick_words()
    else:
        return fr_word, en_word


def unknown_word():
    global prev_fr, flip_timer
    window.after_cancel(flip_timer)
    global fr_, en_
    fr_, en_ = pick_words()
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=fr_, fill="black")
    canvas.itemconfig(img_on_canvas, image=card_front_img)
    prev_fr = fr_
    flip_timer = window.after(3000, func=flip_card)


def known_word():
    global prev_fr, flip_timer
    window.after_cancel(flip_timer)
    global fr_, en_
    fr_, en_ = pick_words()
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=fr_, fill="black")
    canvas.itemconfig(img_on_canvas, image=card_front_img)
    learned_words_list.append(prev_fr)
    print(f"{prev_fr} learned. {len(learned_words_list)} words learned.")
    prev_fr = fr_
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=en_, fill="white")
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
