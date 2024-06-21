from tkinter import *
from textblob import TextBlob

def clearAll():
    word1_field.delete(0, END)
    word2_field.delete(0, END)

def correction():
    input_word = word1_field.get()
    blob_obj = TextBlob(input_word)
    corrected_word = str(blob_obj.correct())
    word2_field.delete(0, END)
    word2_field.insert(0, corrected_word)

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.geometry("450x200")
    root.title("Correction tool")

    headlabel = Label(root, text='I can correct wrong word', fg='black', bg='green')
    label1 = Label(root, text="Input word", fg='black', bg='dark green')
    label2 = Label(root, text="Corrected word", fg='black', bg='dark green')

    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0)
    label2.grid(row=3, column=0, padx=10)

    word1_field = Entry(root)
    word2_field = Entry(root)
    word1_field.grid(row=1, column=1, padx=10, pady=10)
    word2_field.grid(row=3, column=1, padx=10, pady=10)

    button1 = Button(root, text="Correct", bg="red", fg="black", command=correction)
    button1.grid(row=2, column=1)

    button2 = Button(root, text="Clear", bg='red', fg='black', command=clearAll)
    button2.grid(row=4, column=1)

    root.mainloop()
