# pip install googletrans==3.1.0a0

from googletrans import Translator
from gtts import *
from tkinter import *

window = Tk()
window.geometry('900x400')  # Giving the dimensions
window.config(bg='Purple')  # giving background colour
set_bg = PhotoImage(file='images.png')    # Adding a image

label_1 = Label(window,image=set_bg)
label_1.place(x=700, y=200)

e1 = Entry(window, bg='White', fg='Black', font=('Times New Roman',15,'bold'))
e1.place(x=100,y=100)

def convert_language():
    a1 = e1.get()
    t1 = Translator()
    t2 = click_option.get()

    if t2 == "English":
        convert = "en"

    elif t2 == "Hindi":
        convert = "hi"

    elif t2 == "German":
        convert = "de"

    elif t2 == "French":
        convert = "fr"

    elif t2 == "Spanish":
        convert = "es"

    elif t2 == "Russian":
        convert = "ru"

    trans_text = t1.translate(a1, dest = convert)
    trans_text = trans_text.text
    Ob1 = gTTS(text=trans_text, slow=False, lang=convert)
    label_2.config(text=trans_text)

choices = [
    "English",
    "Hindi",
    "Freanch",
    "Spanish",
    "Russian"
]

click_option = StringVar()
click_option.set("Select Language")

list_drop = OptionMenu(window, click_option, *choices)
list_drop.configure(background='green', foreground='white', font=('Times New Roman',15,'bold') )
list_drop.place(x=700,y=20)

label_2 = Label(window, text="\t\t\t\t\t\t",bg='Black',fg='white',font=('Times New Roman',15,'bold'))
label_2.place(x=0, y=120)
label_2 = Label(window, text="Translated Text", bg="black", fg="White",font=('Times New Roman',15,'bold'))
label_2.place(x=180,y=120)

Button_1 = Button(window, text="Translate",bg='red',fg='white',font=('Times New Roman',15,'bold'), command=convert_language)
Button_1.place(x=220,y=200)


window.mainloop()

