from tkinter import *
from tkinter.ttk import *
# If using Linux - must install tkinter #
from time import strftime

root=Tk()
root.title('Time Clock')

def time():# Define the clock Specs - 12 Hour, Minute, And AM or PM #
    string=strftime('%I:%M %p')
    label.config(text=string)
    label.after(1000, time)
 # Digital Font and Color of the Time #
label=Label(root, font=('ds-digital', 80), background='black', foreground='red')
label.pack(anchor='center')
time()

mainloop()
