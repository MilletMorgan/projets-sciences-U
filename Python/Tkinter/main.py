from tkinter import *

def close_window():
    window.destroy()
    exit()

def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "Sorry the is no word like that please try again"
    output.insert(END, definition)

window = Tk()
window.title("My computer Science Glossary")
window.configure(background="#EF12AC")

Label(window, text="Hello World!", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

Label(window, text="\nDefinition : ", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

my_compdictionary = {
    'algorithm': 'blabla', 'bug': 'blablabla'
}

Label(window, text="Click to exit", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)
Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=W)

window.mainloop()
