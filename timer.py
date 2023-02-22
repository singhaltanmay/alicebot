import time
from tkinter import *
from tkinter import messagebox
import threading
def disable_event():
    pass

root = Tk()
  

root.geometry("300x250")
root.config(bg='#003153')  

root.title("Timer")
root.protocol("WM_DELETE_WINDOW", disable_event)

hour=StringVar()
minute=StringVar()
second=StringVar()
hourtag=StringVar()
minutetag=StringVar()
secondtag=StringVar()
 

hour.set("00")
minute.set("00")
second.set("3")
hourtag.set("Hr")
minutetag.set("Min")
secondtag.set("Sec")


hourEntry= Label(root, width=3, font=("Arial",18,""),
                 textvariable=hour)

hourEntry.place(x=70,y=80)
ht=Label(root, width=3, font=("Arial",15,""),
                 textvariable=hourtag,bg='#003153',fg='#fff')
ht.place(x=80,y=40)
  
minuteEntry= Label(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=120,y=80)

mt=Label(root, width=3, font=("Arial",15,""),
                   textvariable=minutetag,bg='#003153',fg='#fff')
mt.place(x=130,y=40)
  
secondEntry= Label(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=170,y=80)
st=Label(root, width=3, font=("Arial",15,""),
                   textvariable=secondtag,bg='#003153',fg='#fff')
st.place(x=180,y=40)
  
  
def submit():
    try:
        
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        mins,secs = divmod(temp,60)
        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        if (temp == 0):
            messagebox.showinfo("Timer", "Time's up ",parent=root)
            root.destroy()
        temp -= 1
btn = Button(root, text='Begin',font=("Arial",15,""), bd='5',
             command= submit, bg='#FFFF00',fg='#FF0000')
btn.place(x = 110,y = 150)
root.mainloop()
