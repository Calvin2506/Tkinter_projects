from tkinter import *
import random
import tkinter.messagebox as tmsg

app = Tk()
count = 0


def generate():
    global comp
    comp = random.randint(1, 101)


def basic():
    app.title("Number Guessing")
    app.geometry("500x500")
    app.minsize(500, 500)
    app.maxsize(500, 500)
    heading = Label(app, text='Number Guessing Game', font="Helvetica 18 bold", bg='black', fg='tomato', padx=170)
    heading.pack()
    try:
        with open('score.txt', 'r') as f:
            hg = f.read()
    except FileNotFoundError:
        hg = "No previous score"
    sc = Label(app, text=f'Previous score: {hg}', font='lucida 8 bold')
    sc.pack(anchor=E, padx=25, pady=5)

    mymenu = Menu(app)
    file_menu = Menu(mymenu, tearoff=0)
    mymenu.add_cascade(label='Start', menu=file_menu)
    file_menu.add_command(label='Restart', command=restart)
    mymenu.add_command(label='About', command=call1)
    mymenu.add_command(label='Quit', command=quit)
    app.config(menu=mymenu)
    generate()


def result():
    global count
    number = userv.get()
    if not number.isdigit():
        tmsg.showerror('Error', "Please enter a valid number")
        return

    n = int(number)
    count += 1

    if count == 10:
        tmsg.showinfo('Game over', 'You lose the Game!')
        generate()
    elif comp == n:
        score = 11 - count
        tmsg.showinfo('Win', f'You guessed the right number!\nYour score: {score}')
        show.config(text='Win!', fg='green')
        with open('score.txt', 'w') as f:
            f.write(str(score))
        generate()
        tmsg.showinfo('Next number', 'Click OK to guess another number')
    elif comp > n:
        show.config(text='Select a greater number', fg='red')
    else:
        show.config(text='Select a smaller number', fg='red')


def restart():
    global count
    count = 0
    tmsg.showinfo('Reset', "Game reset!")
    generate()


def call1():
    str1 = 'This game is developed by CAL'
    tmsg.showinfo('About', str1)


basic()

userv = StringVar()
user = Entry(app, textvariable=userv, justify=CENTER, relief=FLAT, borderwidth=2, font='Helvetica 18 bold')
user.pack(pady=10)

submit = Button(app, text='Submit', command=result, font='Helvetica 18 bold', relief=FLAT)
submit.pack(pady=10)

show = Label(app, text='', font='Helvetica 12 bold')
show.pack(pady=10)

app.mainloop()
