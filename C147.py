# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 18:29:42 2022

@author: shn99
"""

from tkinter import *

root=Tk()
root.title("Length of a word")

root.geometry("400x400")
root.configure(background = 'snow')

test_word = Entry(root)
test_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text = "Name in ASCII : ", bg="light Yellow", fg="black")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        
        btn=Button(root, text="Show name in ASCII", command=asciiConverter, bg='gold', fg='black')
        btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()