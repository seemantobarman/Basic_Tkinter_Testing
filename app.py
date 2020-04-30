import tkinter as tk
from tkinter import Label,Button
import time

localtime = time.asctime(time.localtime(time. time()))

class App:
    def __init__(self,top_window):
        self.top_window = top_window
        top_window.title("Restraurant Management") #title of the window
        top_window.geometry("1028x500") #width and height of the window
        top_window.configure(background="#091833")

        font10 = "{Courier New} 10 normal" #font name and size bold
        font11 = "{Times New Roman} 18 bold"
        font12 = "Al-Aramco 11 bold"
        font13 = "{Courier New} 10 bold"
        font14 = "{Segoe UI} 15 bold"
        font15 = "Arial 13 bold"
        font16 = "{Segoe UI} 13 bold"

        self.Label_1 = tk.Label(master=top_window, text="RESTRAURANT MANAGEMENT SYSTEM", background="#091833", font=font11, foreground="#f2a343")
        self.Label_1.place(relx=0.268, rely=0.02, height=51, width=507)

        localtime1 = tk.Label(master=top_window, text=localtime, background="#091833", font=font16, fg="steel blue")
        localtime1.place(relx=0.420, rely=0.12,)

        #_____Label Food_____

        self.Label_2 = tk.Label(master=top_window, text="Order Number : ", foreground="#B40404", font=font12, background="#091833")
        self.Label_2.place(relx=0.054, rely=0.25)

        self.Label_3 = tk.Label(master=top_window, text="Fried Potatos : ", foreground="#B40404", font=font12, background="#091833")
        self.Label_3.place(relx=0.061, rely=0.32)

        self.Label_4 = tk.Label(master=top_window, text="Chicken Burger : ", foreground="#B40404", font=font12, background="#091833")
        self.Label_4.place(relx=0.045, rely=0.4)

        self.Label_5 = tk.Label(master=top_window, text="Big King : ", foreground="#B40404", font=font12, background="#091833")
        self.Label_5.place(relx=0.094, rely=0.48)

        self.Label_6 = tk.Label(master=top_window, text="Chicken Royal : ", foreground="#B40404", font=font12, background="#091833")
        self.Label_6.place(relx=0.055, rely=0.56)

        self.Label_7 = tk.Label(master=top_window, text="Salad : ", foreground="#B40404", font=font12, background="#091833")
        self.Label_7.place(relx=0.115, rely=0.64)

        self.Label_2 = tk.Label(master=top_window, text="Drinks : ", foreground="#B40404", font=font12, background="#091833")
        self.Label_2.place(relx=0.108, rely=0.71)

        #_____Food Entry_____
        self.Entry_1 = tk.Entry(master=top_window, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.Entry_1.place(relx=0.18, rely=0.253)

        self.Entry_2 = tk.Entry(master=top_window, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.Entry_2.place(relx=0.18, rely=0.325)

        self.Entry_3 = tk.Entry(master=top_window, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.Entry_3.place(relx=0.18, rely=0.405)

        self.Entry_4 = tk.Entry(master=top_window, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.Entry_4.place(relx=0.18, rely=0.485)

        self.Entry_5 = tk.Entry(master=top_window, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.Entry_5.place(relx=0.18, rely=0.565)

        self.Entry_6 = tk.Entry(master=top_window, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.Entry_6.place(relx=0.18, rely=0.64)

        self.Entry_7 = tk.Entry(master=top_window, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.Entry_7.place(relx=0.18, rely=0.711)



root = tk.Tk()
my_gui = App(root)
root.mainloop()
