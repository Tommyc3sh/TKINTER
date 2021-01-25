#tommy cash
#matemaatiline ylesanne

import tkinter as tk


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.geometry("275x70")
root.title('matemaatiline yl')
root.iconbitmap('favicon.ico')
root.resizable(0, 0)

def write_slogans():
    print("Vale vastus")
def write_slogan():
    print("õige vastus!!")
T = tk.Text(height=0, width=28, font=10)
T.pack()
T.insert(tk.END, "kui palju on 74 x 241 ?")

button = tk.Button(frame, 
                   text="69.420",
                   command=write_slogans)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="16.234",
                   command=write_slogans)
slogan.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="17.834",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="11.543",
                   command=write_slogans)
slogan.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="10.239",
                   command=write_slogans)
slogan.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="14.522",
                   command=write_slogans)
slogan.pack(side=tk.LEFT)

 














root.mainloop()
























