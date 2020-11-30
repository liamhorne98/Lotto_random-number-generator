##Liam Horne Class 1
from tkinter import *
from tkinter import messagebox
from datetime import *

age_win=Tk()
age_win.title("Age_window")
age_win.geometry("500x500")
age_win.config(bg='orange')
date=datetime.now()

#Date
datelb=Label(age_win)
datelb.place(x=350,y=20)
datelb.config(text="date" + date.strftime('%d/%m/%y %H:%M'))
#photo
photo = PhotoImage(file="lotto2.png")
plabel = Label(age_win, image=photo)
plabel.pack(side=BOTTOM)
#Label
age_lbl= Label(age_win, text="enter age:\n")
age_lbl.pack(side=TOP)
age_entry= Entry(age_win)
age_entry.pack(side=TOP)
#checkbox
var = IntVar()
c = Checkbutton(age_win,text="Agree to the terms and conditions",variable=var)
c.pack(side=TOP)
#function age
def qualifying_age():
    amount = int(age_entry.get())
    try:
        if amount < 18:
            raise ValueError(messagebox.showinfo('Message',"Only people over the age of eighteen can play"))
    except ValueError as e:
        print(e)
        age_entry.delete(0, END)

    else:
        messagebox.showinfo('Message', "You qualify to play the lotto")
        age_entry.delete(0, END)
        file=open('lotto.txt',"w")
        file.write("age:"+ str(amount))
        age_win.withdraw()
        import lotto_page

#checkbutton
checkbutton = Button(age_win, text="Check qualification", command=qualifying_age)
checkbutton.config(bg="Linen")
checkbutton.pack(side=TOP)

age_win.mainloop()