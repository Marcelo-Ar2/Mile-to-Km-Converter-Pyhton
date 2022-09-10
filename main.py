from tkinter import *

window = Tk()
window.title("Mile to km Calculator")
window.minsize(width=300, height=200)
window.config(pady=30)

blank_text = Label()
blank_text.grid(column=0, row=0)

text1 = Label(text="is equal to", font=('Arial', 12, 'normal'))
text1.grid(column=0, row=1)
text1.config(pady=15, padx=20)

text2 = Label(text=0, font=('Arial', 12, 'normal'))
text2.grid(column=1, row=1)

text3 = Label(text='Miles', font=('Arial', 12, 'normal'))
text3.grid(column=2, row=0)
text3.config(pady=15, padx=20)

text4 = Label(text='Km', font=('Arial', 12, 'normal'))
text4.grid(column=2, row=1)


def convert():
    miles = float(num_input.get())
    result = round(miles * 1.60934, 2)
    text2.config(text=result)


button = Button(text='Calculate', command=convert)
button.grid(column=1, row=2)

num_input = Entry(width=15)
num_input.grid(column=1, row=0)

window.mainloop()
