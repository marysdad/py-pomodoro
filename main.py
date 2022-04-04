from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)

    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text='Timer')
    check_mark.config(text="")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 9 == 0:
        count_down(long_break_sec)
        title_label.config(text='20 Break', fg=RED, bg=YELLOW, font=(FONT_NAME, 50))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='5 Break', fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count/ 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # changes the time in UI
    if count > 0:
       global timer
       timer = window.after(1000, count_down, count - 1)  # decrease time by 1
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(pady=50, padx=100, bg=YELLOW)

# title
title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1,row=0)

# UI components
canvas = Canvas(width=200, height=220, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(100, 120, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# start button
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# restart button
reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# tick
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()