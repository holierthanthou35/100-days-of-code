from tkinter import *
import pandas as pd
import random
bg_color= "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50)
window['bg']= bg_color

df = pd.read_csv('C:\\Users\\avish\\OneDrive\\Desktop\\data\\data\\french_words.csv')
to_learn = df.to_dict(orient='records')


def next_card():
    global french_word
    french_word = random.choice(to_learn)
    canvas.itemconfig(card_lang, text='French')
    canvas.itemconfig(card_title, text=french_word["French"] )

def cross_clicked():
    canvas.itemconfig(card_lang, text='English')
    canvas.itemconfig(card_title, text=french_word["English"] )
    

canvas = Canvas(width= 800, height= 526)
card_front = PhotoImage(file= "C:\\Users\\avish\\OneDrive\\Desktop\\data\\images\\card_front.png")
canvas.create_image(400, 263, image=card_front)
card_lang = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
card_title = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'italic'))

wrong_button_img = PhotoImage(file="C:\\Users\\avish\\OneDrive\\Desktop\\data\\images\\wrong.png")
wrong_button = Button(image= wrong_button_img, highlightthickness=0, command=cross_clicked)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="C:\\Users\\avish\\OneDrive\\Desktop\\data\\images\\right.png")
right_button = Button(image= right_button_img, highlightthickness=0, command= next_card )
right_button.grid(column=1, row=1)

canvas.config(highlightthickness=0, bg=bg_color)
canvas.grid(column=0, row=0, columnspan=2)


window.mainloop()