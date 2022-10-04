#code by Nyanab

#8-ball said: i'm just a computer science, don't trust me

from random import randint
from tkinter import *
from turtle import onclick
root=Tk()

sentences = [
  "Certainly",
  "It's certain!",
  "Of course",
  "Yes",
  "Yes, definitly",
  "Why not?",
  "Absolutely",
  "Sure",
  "I think so",
  "No doubt",
  "Ask again",
  "Try Again",
  "Maybe",
  "Maybe Not",
  "I have doubt on it",
  "Impossible",
  "Of Course Not",
  "No",
  "I don't think so",
  "Certainly not"
]

def asking():
    send="You: "+question.get()
    if question.get()!="":
      win.insert('end',"\n"+send)
      win.insert('end',f"\n🎱 {sentences[randint(0,len(sentences)-1)]}")
      question.delete(0, END)

root.title("8-ball🎱")
win = Text(root,bg="#D7C49E",fg='#343148')
Font_text = ("Comic Sans MS", 14, "bold")
Font_btn = ("Comic Sans MS", 12, "bold")
Font_entry = ("Comic Sans MS", 10, "bold")
win.configure(font = Font_text)
win.grid(row=0, column=0, columnspan=2)
question = Entry(root, width=80)
question.configure(font = Font_entry)
Ask = Button(root, bg='#343148', fg='#D7C49E', activebackground='#D7C49E', activeforeground='#343148', text="Ask", width=10, command=asking)
Ask.configure(font = Font_btn)
Ask.grid(row=1,column=1)
question.grid(row=1, column=0)
win.insert('end',"Welcome to 8-ball🎱\nAsk anything without bound\n")
root.mainloop()