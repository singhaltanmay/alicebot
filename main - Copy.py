import socket
import threading
import tkinter
from tkinter import *
from tkinter import font
import tkinter as tk
import query
import time
import speech_rec
from queue import Empty, Full
from PIL import Image, ImageTk
class GUI:
    
    
    def __init__(self):
        #global root
        #root = Tk()
        #top = Toplevel(root)
        #top.overrideredirect(1)
        #root.title("check_for_icon")
        #self.photo_icon=PhotoImage(file="Resources\icon.png")
        #root.iconphoto(False,self.photo_icon)
        #root.attributes("-alpha",0.0)

        #def onRootIconify(event): top.Window.withdraw()
        #root.bind("<Unmap>", onRootIconify)
        #def onRootDeiconify(event): top.deiconify()
        #root.bind("<Map>", onRootDeiconify)
        self.Window = Tk()
        #self.Window = tkinter.Frame(master=top)
        self.Window.withdraw()
        self.login = Toplevel()
        self.photo1=PhotoImage(file="Resources\icon.png")
        self.login.iconphoto(False,self.photo1)
        
        self.login.title("Login")
        self.login.resizable(width = False,
                             height = False)
        self.login.configure(width = 400,
                             height = 200)
        self.labelName = Label(self.login,
                               text = "Name: ",
                               font = "Helvetica 12")
         
        self.labelName.place(relheight = 0.2,
                             relx = 0.1,
                             rely = 0.2)
        self.labelName.place(relheight = 0.2,
                             relx = 0.2,
                             rely = 0.15)
        self.entryName = Entry(self.login,
                             font = "Helvetica 14")
         
        self.entryName.place(relwidth = 0.4,
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.2)
         
        self.entryName.focus()
        
        self.go = Button(self.login,
                         text = "HUMAN VERIFICATION",
                         font = "Helvetica 14 bold",
                         command = lambda: self.goAhead(self.entryName.get()))
        
         
        self.go.place(relx = 0.2,
                      rely = 0.4)
        
        def enter(event):
            if self.entryName.get()!='':
                self.goAhead(self.entryName.get())
            else:
                pass
            
        x_window_loc, y_window_loc, = 0, 0
        to_drag=False
        
        def mouse_motion(event):
            global x_window_loc,y_window_loc,to_drag
            
            offset_x, offset_y = event.x - x_window_loc, event.y - y_window_loc 
            new_x = self.Window.winfo_x() + offset_x
            new_y = self.Window.winfo_y() + offset_y
            new_geometry = f"+{new_x}+{new_y}"
            self.Window.geometry(new_geometry)
            
        def mouse_press(event):
            global x_window_loc, y_window_loc,to_drag
            x_window_loc,y_window_loc = event.x, event.y
    
        self.login.bind('<Return>',enter)

        #self.Window.bind("<B1-Motion>", mouse_motion)
        #self.Window.bind("<Button-1>", mouse_press)
        
        self.Window.mainloop()
    


    
    def goAhead(self, name):
        
        self.login.destroy()
        self.layout(name)

    def layout(self,name):
        self.name=name
        
        self.Window.deiconify()
        self.messages=StringVar()
        self.messages.set('')
        self.Window.title("ALICE")
        
        self.Window.iconphoto(False,self.photo1)
        self.Window.resizable(width = False,
                              height = False)
        
        self.Window.configure(width = 900,
                              height = 650,
                              bg = "#0E1621")
        self.textCons = Text(self.Window,
                             width = 20,
                             height = 2,
                             bg = "#0E1621",
                             fg = "#EAECEE",
                             font = "Helvetica 14",
                             padx = 5,
                             pady = 5,
                             bd=0)
        self.textCons.place(relheight = 0.82,
                            relwidth = 1,
                            rely = 0.02)
        self.bgCanvas=Canvas(self.Window,bg= "#0E1621",width=900,height=650)
        self.bgCanvas.place(x=0,y=0)
        print(type(self.bgCanvas))
        
         
        self.labelBottom = Label(self.Window,
                                 bg = "#17202B",
                                 height = 80)
         
        self.labelBottom.place(relwidth = 1,
                               rely = 0.9)
        
         
        self.entryMsg = Entry(self.labelBottom,
                              bg = "#17202B",
                              fg = "#EAECEE",
                              font = "Helvetica 13",
                              
                              borderwidth=0,
                              
                              state = NORMAL)
        self.entryMsg.place(relwidth = 0.72,
                            relheight = 0.035,
                            rely = 0.008,
                            relx = 0.12)
        self.entryMsg.configure(bg="#17202B", insertbackground='white')
        
        self.entrylabel = Label(self.labelBottom,
                              text='Write a message....',
                              bg = "#17202B",
                              fg = "#66717C",
                                anchor = 'w',
                              font = "Helvetica 13",
                              borderwidth=0,
                              relief="flat",
                              state = DISABLED,
                              cursor="xterm")
        
        self.entrylabel.place(relwidth = 0.72,
                            relheight = 0.035,
                            rely = 0.008,
                            relx = 0.1233)
        self.entrylabel3=Label(self.labelBottom,
                              text='Listening....',
                              bg = "#17202B",
                              fg = "#66717C",
                                anchor = 'w',
                              font = "Helvetica 13",
                              borderwidth=0,
                              relief="flat",
                              state = DISABLED,
                              cursor="xterm")
        self.entrylabel3.place(relwidth = 0.72,
                            relheight = 0.035,
                            rely = 0.008,
                            relx = 0.1233)
        self.entrylabel3.place_forget()
        
        
        
        self.photo=PhotoImage(file="Resources\\send_btn.png")
        self.photo2=PhotoImage(file="Resources\\at_btn.png")
        self.photo3=PhotoImage(file="Resources\\m_btn.png")
        self.photo4=PhotoImage(file="Resources\\m_focus.png")

        self.theme1=PhotoImage(file="Themes\\cubes.png")
        image=self.bgCanvas.create_image(220,200,image=self.theme1,anchor='center')

        vbar=Scrollbar(self.Window,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        
        vbar.config(command=self.bgCanvas.yview)
        
        self.buttonMsg = Button(self.labelBottom,
                                text="⮞",
                                font = "Helvetica 35 bold",
                                width = 15,
                                bg = "#17202B",
                                image=self.photo,
                                borderwidth=0,
                                command = lambda : self.sendButton(self.entryMsg.get()))
         
        self.buttonMsg.place(relx = 0.935,
                             rely = 0.008,
                             relheight = 0.035,
                             relwidth = 0.055)
        def enter(event):
            if self.entryMsg.get()!='':
                self.sendButton(self.entryMsg.get())
            else:
                pass
        self.Window.bind('<Return>',enter)
        
        self.buttonMsg2 = Button(self.labelBottom,
                                text="⮞",
                                font = "Helvetica 35 bold",
                                width = 15,
                                bg = "#17202B",
                                image=self.photo3,
                                borderwidth=0,
                                command = lambda : self.micButton()
                               )
         
        self.buttonMsg2.place(relx = 0.065,
                             rely = 0.008,
                             relheight = 0.035,
                             relwidth = 0.05)
        self.buttonMsg3 = Button(self.labelBottom,
                                text="⮞",
                                font = "Helvetica 35 bold",
                                width = 15,
                                bg = "#17202B",
                                image=self.photo2,
                                borderwidth=0
                               )
         
        self.buttonMsg3.place(relx = 0.015,
                             rely = 0.008,
                             relheight = 0.033,
                             relwidth = 0.041)
         
        self.textCons.config(cursor = "arrow")

         
        self.textCons.config(state = DISABLED)
        self.entryMsg.focus()
        t1=threading.Thread(target = self.check)
        t2=threading.Thread(target=self.focus)
        threads=[]
        
        threads.append(t1)
        threads.append(t2)
        for i in threads:
            if bool(self.Window.winfo_ismapped)==True:
                i.start()
                
            else:
                self._stop_event.set()
                
        def click(*args):
            #global root
            self.buttonMsg2['image']=self.photo4
            self.buttonMsg2.focus()
            self.buttonMsg.focus()
            self.buttonMsg3.focus()
            self.entryMsg.focus()
            
            self.entrylabel3.place(relwidth = 0.72,
                            relheight = 0.035,
                            rely = 0.008,
                            relx = 0.1233)
            
            self.buttonMsg2.focus()
            self.buttonMsg.focus()
            self.buttonMsg3.focus()
            self.entryMsg.focus()
            
            
        self.buttonMsg2.bind("<Button-1>",click)
        
    def micButton(self):
        
        inp=speech_rec.init('onetime')
        self.msg=inp
        t=threading.Thread(target=self.sendMessage)
        t.start()
        self.entrylabel3.place_forget()
        self.buttonMsg2['image']=self.photo3
    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        self.msg=msg
        self.entryMsg.delete(0, END)
        snd= threading.Thread(target = self.sendMessage)
        t1=threading.Thread(target = self.check)
        #t2=threading.Thread(target=self.focus)
        threads=[]
        threads.append(snd)
        threads.append(t1)
        #threads.append(t2)
        
        for i in threads:
            if bool(self.Window.winfo_ismapped)==True:
                i.start()
                
            else:
                self._stop_event.set()
        
    def check(self):
        #global root
        while True:
            
            if len(self.entryMsg.get())!=0:
                self.entrylabel.place_forget()
                self.entrylabel3.place_forget()
            else:
                self.entrylabel.place(relwidth = 0.72,
                            relheight = 0.035,
                            rely = 0.008,
                            relx = 0.1233)
            self.buttonMsg.focus()
            self.buttonMsg2.focus()
            self.buttonMsg3.focus()
            self.entryMsg.focus()
        
            time.sleep(0.02)
            #if root.state()!='normal':
            if self.Window.state()!='normal':
                quit()
            else:
                continue
            
    def focus(self):
        while True:
            self.buttonMsg.focus()
            self.buttonMsg2.focus()
            self.buttonMsg3.focus()
            self.entryMsg.focus()
            time.sleep(5)
            if bool(self.Window.winfo_ismapped)==True:
                break
            else:
                continue
            
        
        
    def sendMessage(self):
        
        self.textCons.config(state=DISABLED)
        self.Window.focus()
        
        self.entryMsg.focus()
        name=self.name.capitalize()
        canvasVar=StringVar()
        canvasVar.set('')
        while True:
            
            mes=(f"{self.msg}")
            message = (f"{name+' '}: {self.msg}")
            
            self.textCons.config(state = NORMAL)
            self.textCons.insert(END,
                                    message+"\n\n")
            canvasVar.set(canvasVar.get()+"\n\n"+self.textCons.get("1.0",END))
            self.textCons.config(state = DISABLED)
            
            self.textCons.see(END)
            
            self.resp=query.check(mes)
            
            l=[]
            if '////' in self.resp:
                l=self.resp.split('////')
                alice=(f"{'Alice '}: {l[0]}")
                self.textCons.config(state = NORMAL)
                self.textCons.insert(END,
                                    alice+"\n\n")
                canvasVar.set(canvasVar.get()+"\n\n"+self.textCons.get("1.0",END))
                print(self.textCons.get("1.0",END))
                self.bgCanvas.create_text(90,100,fill='#fff',font='Helvetica 14',text=canvasVar.get())
                self.bgCanvas.update
                time.sleep(2)
                alice=(f"{'         '}  {l[1]}")
                self.textCons.config(state = NORMAL)
                
                self.textCons.insert(END,
                                    alice+"\n\n")
                canvasVar.set(canvasVar.get()+"\n\n"+self.textCons.get("1.0",END))
                print(self.textCons.get("1.0",END))
                self.bgCanvas.create_text(90,10,fill='#fff',font='Helvetica 14',text=canvasVar.get())
                self.bgCanvas.update
                
            else:
                alice=(f"{'Alice '}: {self.resp}")
                self.textCons.config(state = NORMAL)
                self.textCons.insert(END,
                                    alice+"\n\n")
                canvasVar.set(canvasVar.get()+"\n\n"+self.textCons.get("1.0",END))
                print(self.textCons.get("1.0",END))
                self.bgCanvas.create_text(90,10,fill='#fff',font='Helvetica 14',text=canvasVar.get())
                self.bgCanvas.update
               
            self.textCons.config(state = DISABLED)
            self.textCons.see(END)
            time.sleep(1)
            break
        
    
        
g=GUI()

