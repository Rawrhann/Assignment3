#Create a program that will ask how many apples and oranges you want to buy.
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
#Display the output
from tkinter import *
from tkinter import simpledialog
from tkinter import Tk, ttk
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import tkinter.font
from tkinter import font
from tkinter.simpledialog import Dialog

def popup():

    number_of_apple = simpledialog.askinteger ("Apple", "How many Apples would you like to buy?")
    display_number_of_apple = str(number_of_apple)
    amount_to_pay_for_apple = (str(number_of_apple * 20))   
    print(amount_to_pay_for_apple)
    
    number_of_orange = simpledialog.askinteger ("Orange", "How many Oranges would you like to buy?")
    display_number_of_oranges = str(number_of_orange)
    amount_to_pay_for_orange = (str(number_of_orange * 25))
    print(amount_to_pay_for_apple)

    window_results = tk.Toplevel(window_main)
    window_results.title ("Results")
    window_results.configure(bg="yellow")
    window_results.minsize(width=300, height=300)
    
    frame_apple = tkinter.Frame(window_results)
    frame_apple.grid(row=0, column=0, pady=10)
    frame_orange = tkinter.Frame(window_results)
    frame_orange.grid(row=1, column=0, pady=10)
    frame_buttons = tkinter.Frame(window_results)
    frame_buttons.grid(row=2, column=0, pady=10)

    gulimche_font = ("GulimChe", 18, "bold")
    amount_to_pay_for_apple_label = Label(frame_apple, text=("You have to pay ₱" + amount_to_pay_for_apple + " for " + display_number_of_apple + " Apples"),
        width = "50", height = "2", fg="red", bg="black")
    amount_to_pay_for_apple_label.configure(font = gulimche_font)
    amount_to_pay_for_apple_label.grid(row=0, column=0,)
    amount_to_pay_for_apple_label.pack()
    

    amount_to_pay_for_orange_label = Label(frame_orange, text=("You have to pay ₱" + amount_to_pay_for_orange + " for " + display_number_of_oranges + " Oranges"),
        width = "50", height = "2", fg="orange", bg= "black")
    amount_to_pay_for_orange_label.configure(font = gulimche_font)
    amount_to_pay_for_orange_label.grid(row=1, column=0)
    amount_to_pay_for_orange_label.pack()

    def purchase_confirmation():
        messagebox.showinfo("Purchase Complete", "Thank you for shopping at Orples!")
        window_main.destroy()
        
    def purchase_cancel():
        messagebox.showwarning("Cancelling Purchase", "Sorry for the inconvenience!")
        window_results.destroy()
    
    button_confirm = Button(frame_buttons, width = "15", height = "2", text = "Confirm Purchase", command = purchase_confirmation, bg="green", fg="white")
    button_confirm.pack()
    button_cancel = Button(frame_buttons, width = "15", height = "2", text = "Cancel Purchase", command = purchase_cancel, bg="red", fg="white")
    button_cancel.pack()
    
    window_results.mainloop()

window_main = Tk() 
window_main.title("Startup")
window_main.config(bg = "#6FD6FF")
david_font = ("David", 18, "bold")
gigi_font = ("Gigi", 25, "bold")
stencil_font = ("Stencil", 18)

title_store_label = Label(window_main, text = "Welcome to Orples", width = "36", height = "1", bg="#6FD6FF", )
description_label_line_one = Label(window_main, text = "Where we sell Oranges and Apples", bg = "#6FD6FF")
description_label_line_two = Label(window_main, text = " at a fix rate of 25 Pesos and 20 Pesos respectively", bg = "#6FD6FF")
title_store_label.configure(font = gigi_font)
description_label_line_one.configure(font = gigi_font)
description_label_line_two.configure(font = gigi_font)

button_start = Button(window_main, width = "15", height = "2", text = "Start Shopping", command = popup, bg="green", fg="white")
button_start.pack()
button_end = Button(window_main, width = "10", height = "2", text = "Leave", command = exit, bg="red", fg="white")

button_start.grid(row = 0, column = 0, padx=5, pady=5) 
button_end.grid(row = 4, column = 2, padx=5, pady=5 )
title_store_label.grid(row = 1, column = 1)
description_label_line_one.grid(row = 2, column = 1)
description_label_line_two.grid(row = 3, column = 1)

window_main.geometry("940x258")
window_main.resizable(False,False)
window_main.mainloop()