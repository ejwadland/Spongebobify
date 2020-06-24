from itertools import cycle
from tkinter import *


win = Tk()
win.title("Spongebobifer")
win.resizable(0,0)


def Spongbobifier():
   output.delete("1.0", END)
   func = cycle([str.upper(), str.lower])
   result = ''.join(next(func)(c) for c in entry.get("1.0", END) if c != '  ')
   output.insert(END, result)





l1 = Label(win, text="Enter text: ")
entry = Text(win, width=50, height = 3, wrap=WORD)
button = Button(win, text="Spongebobify", width=20)
l2 = Label(win, text="Your text M'Lady:")
output = Text(win, width=50, height=3, wrap=WORD)

l1.grid(row=1, column=1, padx=5, sticky=W)
entry.grid(row=2, column=1, columnspan=2, padx=5, pady=(0,10))
button.grid(row=3, column=1, columnspan=2, pady=5)
l2.grid(row=4, column=1, padx=5, sticky=W)
output.grid(row=5, column=1, columnspan=2, padx=5, pady=(0,10))

button.configure(command=Spongbobifier)



win.mainloop()



