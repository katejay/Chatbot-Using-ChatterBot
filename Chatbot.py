import tkinter as tk
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from Conversation import conv

window = Tk()

window.title("KGCE BE-IT 2020")
window.configure(background='black')
window.geometry('1280x680')

lbl = tk.Label(window, text="CHATBOT", width=60, fg="black", bg="white", height=2, font=('times', 24, ' bold'))
lbl.place(x=100, y=20)

frame = Frame(window)
frame.place(x=100, y=120, width=625, height=400)

vscrollbar = Scrollbar(frame, orient=VERTICAL)
hscrollbar = Scrollbar(frame, orient=HORIZONTAL)
msg = Listbox(frame, width=100, height=20)
vscrollbar.pack(side=RIGHT, fill=Y)
hscrollbar.pack(side=BOTTOM, fill=X)
msg.pack(side=LEFT, fill=BOTH)
vscrollbar.config(command = msg.yview )
hscrollbar.config(command = msg.xview )

chatbot = ChatBot("Chatbot")
trainer = ListTrainer(chatbot)
trainer.train(conv)

def send_message():
    question = txt.get()
    msg.insert(END, "You : " + question)
    try:
        answer = chatbot.get_response(question)
        msg.insert(END, "Kgce Bot : " + str (answer))
        msg.insert(END, "")
    except:
        msg.insert(END, "Kgce Bot : I am sorry, I don't have an answer for this. Please try again with different question.")
        msg.insert(END, "")
    txt.delete(0, 'end')

def clear():
    txt.delete(0, 'end')

txt = tk.Entry(window, width=62, bg="white", fg="black", font=('times', 15, ' bold '))
txt.place(x=100, y=525)

btn = tk.Button(window, text="Send Message", fg="black", bg="white", width=20, height=1, activebackground = "Green", font=('times', 15, ' bold '), command=send_message)
btn.place(x=150, y=560)

btn1 = tk.Button(window, text="Clear Message", fg="black", bg="white", width=20, height=1, activebackground = "Red", font=('times', 15, ' bold '), command=clear)
btn1.place(x=450, y=560)


lbl11 = tk.Label(window, text="Frequent Ask Question",  fg="red", bg="black", font=('times', 30, ' bold')) 
lbl11.place(x=800, y=120)

def btn11():
    msg.insert(END, "You : what is the timing of college ?")
    msg.insert(END, "Kgce Bot : From Morning 8 am to 5 pm, and it varies according to your batch in which you are enrolled.")
    msg.insert(END, "")

btn11 = tk.Button(window, text="What is the timing of college ?", fg="black", bg="white", width=30, height=1, activebackground = "yellow", font=('times', 18, ' bold '), command=btn11)
btn11.place(x=800, y=200)

def btn12():
    msg.insert(END, "You : what is the working time of office ?")
    msg.insert(END, "Kgce Bot : From Morning 10 am to 5 pm.")
    msg.insert(END, "")

btn12 = tk.Button(window, text="What is the working time of office ?", fg="black", bg="white", width=30, height=1, activebackground = "yellow", font=('times', 18, ' bold '), command=btn12)
btn12.place(x=800, y=270)

def btn13():
    msg.insert(END, "You : is KGCE NAAC accredited ?")
    msg.insert(END, "Kgce Bot : Yes, college has been awarded with B+ grade.")
    msg.insert(END, "")

btn13 = tk.Button(window, text="Is KGCE NAAC accredited ?", fg="black", bg="white", width=30, height=1, activebackground = "yellow", font=('times', 18, ' bold '), command=btn13)
btn13.place(x=800, y=340)

def btn14():
    msg.insert(END, "You : what are the placement opportunity in kgce ?")
    msg.insert(END, "Kgce Bot : https://kgce.edu.in/placement-summary/ This is the kgce placement record.")
    msg.insert(END, "")

btn14 = tk.Button(window, text="What are the placement opportunity ?", fg="black", bg="white", width=30, height=1, activebackground = "yellow", font=('times', 18, ' bold '), command=btn14)
btn14.place(x=800, y=410)

def btn15():
    msg.insert(END, "You : what is the fee structure ?")
    msg.insert(END, "Kgce Bot : Fee structure will be available to you in our office.")
    msg.insert(END, "")

btn15 = tk.Button(window, text="What is the fee structure ?", fg="black", bg="white", width=30, height=1, activebackground = "yellow", font=('times', 18, ' bold '), command=btn15)
btn15.place(x=800, y=480)

def btn16():
    msg.insert(END, "You : who is your creator ?")
    msg.insert(END, "Kgce Bot : Jay Kate create me using Python's NLTK library.")
    msg.insert(END, "")

btn16 = tk.Button(window, text="Who is your creator ?", fg="black", bg="white", width=30, height=1, activebackground = "yellow", font=('times', 18, ' bold '), command=btn16)
btn16.place(x=800, y=550)

lbl21 = tk.Label(window, text="CHATBOT MINI-PROJECT BY KGCE BE-IT BATCH 2020, GROUP NO : 10", width=80, fg="white", bg="black", font=('times', 15, ' bold')) 
lbl21.place(x=200, y=620)

window.mainloop()