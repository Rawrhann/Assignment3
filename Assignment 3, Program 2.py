#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output
from tkinter import *
from tkinter import simpledialog
from tkinter import Tk, ttk
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import tkinter.font
from tkinter import font
from tkinter.simpledialog import Dialog

def discount(display_amount_of_money):
    if  display_amount_of_money <= 1000:
        price_under_1000_label = Label(window_main, width="35", height="1", text = price_under_1000, fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        price_under_1000_label_2nd_line = Label(window_main, width="35", height="1", text = price_under_1000_2nd_line, fg="#AED6F1", bg="black", font=("Terminal", 10, "bold"))
        price_under_1000_label.grid(column=2, row=2, pady=1)
        price_under_1000_label_2nd_line.grid(column=2, row=3, pady=1)
        final_price_under_1000_label = Label(window_main, width="35", height="1", text = original_price_of_apple, fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        final_price_under_1000_label.grid(column=2, row=4, pady=1)
        messagebox.showinfo("Discount Offer", "You wont receive any Discount")
        no_deduction_per_apple = original_price_of_apple_number
        final_price_of_apple = (no_deduction_per_apple)
        total_number_of_apple = (display_amount_of_money // final_price_of_apple)
        total_number_of_apple_label = Label(window_main, width = "5", height="1", text = total_number_of_apple, anchor="sw", fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        total_number_of_apple_label.grid(column=3, row=6, pady=1)
        total_number_of_apple_label_word = Label (window_main, width ="40", height="1", text = "You will receive this amount of apples", anchor="se", bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        total_number_of_apple_label_word.grid(column=2, row=6, pady=1)
        money_excess = (display_amount_of_money % final_price_of_apple)
        change_label = Label(window_main, width="5", height="1", text = money_excess, anchor="nw", fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        change_label_word = Label(window_main, width="40", height="1", text = "Your change will be ₱", anchor="ne", fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        change_label.grid(column=3,row=7,pady=1)
        change_label_word.grid(column=2,row=7,pady=1)
        display_final_balance_of_money_label = Label(window_main, width="15", height = "2", text = "Ending Balance", bg="#FFD15F")
        display_final_balance_of_money_label.grid(row=6,column=1,pady=2)
        display_final_amount_of_money_label = Label(window_main, width="15", height = "2", text = money_excess, bg="#FFD15F")
        display_final_amount_of_money_label.grid(row=7,column=1,pady=2)


    elif 1000 < display_amount_of_money <= 10000:
        price_over_1000_but_under_10000_label = Label(window_main, width="45", height="1", text = price_over_1000_but_under_10000, bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        price_over_1000_but_under_10000_label_2nd_line = Label(window_main, width="45", height="1", text = price_over_1000_but_under_10000_2nd_line,bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        price_over_1000_but_under_10000_label.grid(column=2, row=2, pady=1, padx=3)
        price_over_1000_but_under_10000_label_2nd_line.grid(column=2, row=3, pady=1,padx=3)
        number_of_discount_1_25 = simpledialog.askinteger ("Discount Offer", "How much discount would you like?")
        while not number_of_discount_1_25 in range(1,26):
            messagebox.showwarning("Invalid Input", "Please input within the range of 1 to 25")
            number_of_discount_1_25 = simpledialog.askinteger ("Discount Offer", "How much discount would you like?")
        display_number_of_discount = int(number_of_discount_1_25)
        deduction_per_apple = (int(display_number_of_discount * 20 * 0.01))
        price_per_apple_label = Label(window_main, width="5", height="1", text=deduction_per_apple,anchor="w",bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        price_per_apple_label_line_two = Label(window_main, width="50", height="1", text = "The original price of " + original_price_of_apple + " will be deducted by ₱", anchor="e",bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        price_per_apple_label.grid(column=3, row=4, pady=1)
        price_per_apple_label_line_two.grid(column=2, row=4, pady=1)
        final_price_of_apple = (original_price_of_apple_number - deduction_per_apple)
        total_number_of_apple = (display_amount_of_money // final_price_of_apple)
        total_number_of_apple_label = Label(window_main, width = "5", height="1", text = total_number_of_apple, anchor="sw", fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        total_number_of_apple_label.grid(column=3, row=6, pady=1)
        total_number_of_apple_label_word = Label (window_main, width ="50", height="1", text = "You will receive this amount of apples", anchor="se", bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        total_number_of_apple_label_word.grid(column=2, row=6, pady=1)
        money_excess = (display_amount_of_money % final_price_of_apple)
        change_label = Label(window_main, width="5", height="1", text = money_excess, anchor="nw", fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        change_label_word = Label(window_main, width="50", height="1", text = "Your change will be ₱", anchor="ne", fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        change_label.grid(column=3,row=7,pady=1)
        change_label_word.grid(column=2,row=7,pady=1)
        display_final_balance_of_money_label = Label(window_main, width="15", height = "2", text = "Ending Balance", bg="#FFD15F")
        display_final_balance_of_money_label.grid(row=6,column=1,pady=2)
        display_final_amount_of_money_label = Label(window_main, width="15", height = "2", text = money_excess, bg="#FFD15F")
        display_final_amount_of_money_label.grid(row=7,column=1,pady=2)


    else:
        price_over_10000_label = Label(window_main, width="45", height="1", text = price_over_10000, bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        price_over_10000_2nd_line_label = Label(window_main, width="45", height="1", text = price_over_10000_2nd_line,bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        price_over_10000_label.grid(column=2, row=2, pady=1, padx=3)
        price_over_10000_2nd_line_label.grid(column=2, row=3, pady=1, padx=3)
        number_of_discount_1_50 = simpledialog.askinteger ("Discount Offer", "How much discount would you like?")
        while not number_of_discount_1_50 in range(1,51):
            messagebox.showwarning("Invalid Input", "Please input within the range of 1 to 50")
            number_of_discount_1_50 = simpledialog.askinteger ("Discount Offer", "How much discount would you like?")
        display_number_of_discount = int(number_of_discount_1_50)
        deduction_per_apple = (int(display_number_of_discount * 20 * 0.01))
        price_per_apple_label = Label(window_main, width="5", height="1", text=deduction_per_apple,anchor="w",bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        price_per_apple_label_line_two = Label(window_main, width="50", height="1", text = "The original price of " + original_price_of_apple + " will be deducted by ₱", anchor="e",bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        price_per_apple_label.grid(column=3, row=4, pady=1)
        price_per_apple_label_line_two.grid(column=2, row=4, pady=1)
        final_price_of_apple = (original_price_of_apple_number - deduction_per_apple)
        total_number_of_apple = (display_amount_of_money // final_price_of_apple)
        total_number_of_apple_label = Label(window_main, width = "5", height="1", text = total_number_of_apple, anchor="sw", fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        total_number_of_apple_label.grid(column=3, row=6, pady=1)
        total_number_of_apple_label_word = Label (window_main, width ="50", height="1", text = "You will receive this amount of apples", anchor="se", bg="black",fg="#AED6F1",font=("Terminal", 10, "bold"))
        total_number_of_apple_label_word.grid(column=2, row=6, pady=1)
        money_excess = (display_amount_of_money % final_price_of_apple)
        change_label = Label(window_main, width="5", height="1", text = money_excess, anchor="nw", fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        change_label_word = Label(window_main, width="50", height="1", text = "Your change will be ₱", anchor="ne", fg="#AED6F1",bg="black",font=("Terminal", 10, "bold"))
        change_label.grid(column=3,row=7,pady=1)
        change_label_word.grid(column=2,row=7,pady=1)
        display_final_balance_of_money_label = Label(window_main, width="15", height = "2", text = "Ending Balance", bg="#FFD15F")
        display_final_balance_of_money_label.grid(row=6,column=1,pady=2)
        display_final_amount_of_money_label = Label(window_main, width="15", height = "2", text = money_excess, bg="#FFD15F")
        display_final_amount_of_money_label.grid(row=7,column=1,pady=2)
def main():

    try:
        amount_of_money = simpledialog.askinteger("Cash", "How much would you like to spend?")
        display_amount_of_money = int(amount_of_money)
        if display_amount_of_money < 0:
            raise ValueError("Please enter a non-negative amount.")

        display_balance_of_money_label = Label(window_main, width="15", height = "2", text = "STARTING BALANCE", bg="#FFD15F")
        display_balance_of_money_label.grid(row=0,column=1)
        display_amount_of_money_label = Label(window_main, width="15", height = "2", text = display_amount_of_money, bg="#FFD15F")
        display_amount_of_money_label.grid(row=1,column=1)
        result = discount(amount_of_money)
        print(result)

    except ValueError as e:
        print("Error: {e}")

price_under_1000 = "You have to buy the max rate "
price_under_1000_2nd_line = "of an apple which is "
price_over_1000_but_under_10000 = "You will be able to choose how much discount "
price_over_1000_but_under_10000_2nd_line = "You can get from 1% to 25%"
price_over_10000 = "You will be able to choose how much discount "
price_over_10000_2nd_line = "You can get from 1% to 50%"
original_price_of_apple = "₱20"
original_price_of_apple_number = 20

window_main = Tk() 
window_main.title("Startup")
window_main.config(bg = "black")

main_label = Label(window_main, width = "25", height = "1", text= "Come One, Come All!", bg="#7B241C", fg="white", font=("Gigi", 12, "bold"))
main_label_2nd = Label(window_main, width = "25", height = "1", text= "Buy Apples at a 50% Discount!", bg="#7B241C", fg="white", font=("Gigi", 12, "bold"))
main_label.grid(row=2,column=0,padx=5)
main_label_2nd.grid(row=3,column=0,padx=5)

button_start = Button(window_main, width = "15", height = "2", text = "Shop", command = main, bg="green", fg="white")
button_start.grid(row=0,column=0,pady=5,padx=5)

button_end = Button(window_main, width = "15", height = "2", text = "Stop", command = exit, bg="red", fg="white")
button_end.grid(row=1,column=0,pady=5,padx=5)

window_main.geometry("1000x300")
window_main.resizable(False,False)
window_main.mainloop()