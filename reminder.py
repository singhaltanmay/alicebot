import datetime
import time
import os
import sys
import pandas as pd
from tkinter import *
from tkcalendar import Calendar
import time
from tkinter import messagebox
curdir=os.path.dirname(os.path.abspath(__file__))
def date_conv(date):
    d={'january':'1','february':'2','march':'3','april':'4','may':'5','june':'6','july':'7','august':'8','september':'9','october':'10','november':'11','december':'12'}      
    l=date.split(' ')
    l2=[]
    e=''
    for i in l:
        if i in d:
            l2.append(d[i])
        else:
            l2.append(i)
    for i in l2:
        e=l2[0]+'/'+l2[1]+'/'+l2[2]
    return e
    
    
def leap_year(x):
    if x=="Year Error":
        return "Year Error"
    else:
        if x%4==0 and x%100:
            return True
        elif x%400==0:
            return True
        else:
            return False

    
def date(x):
    a=list(x)
    date=""
    for i in range(0,len(a)):
        if a[i]=="/":
            break
        else:
            date+=str(a[i])
    date=int(date)
    if (month(x)==1 or month(x)==3 or month(x)==5 or month==7 or month(x)==8 or month(x)==10 or month(x)==12) and (date>31 or date<0):
        return "Date Error"
    if (month(x)==4 or month(x)==6 or month(x)==9 or month==11) and (date>30 or date<0):
        return "Date Error"
    if (month(x)==2 and leap_year(year(x))==True and (date>29 or date<1)) or (month(x)==2 and leap_year(year(x))==False and (date>28 or date<1)): 
        return "Date Error"
    else:
        return int(date)


def month(x):
    a=list(x)
    month=""
    for i in range(0,len(a)):
        if a[i]=="/":
            d=0
            for t in range(0,i+1):
                a.remove(a[t-d])
                d+=1   
            break
        else:
           continue

    for i in range(0,len(a)):
        if a[i]=="/":
            break
        else:
            month+=str(a[i])
    month=int(month)
    if month>12 or month<1:
        return "Month Error"
    else:
        return int(month)


def year(x):
    a=list(x)
    year=""
    for i in range(0,len(a)):
        if a[i]=="/":
            d=0
            for t in range(0,i+1):
                a.remove(a[t-d])
                d+=1   
            break
        else:
           continue
    for i in range(0,len(a)):
        if a[i]=="/":
            d=0
            for t in range(0,i+1):
                a.remove(a[t-d])
                d+=1   
            break
        else:
            continue
    for i in range(0,len(a)):
        if a[i]=="/":
            break
        else:
            year+=str(a[i])
    year=int(year)
    if year<0:
        return "Year Error"
    else:
        return int(year)


def days_between(x,y):  
    days=0
    if date(x)=="Date Error" or date(y)=="Date Error" or month(x)=="Month Error" or month(y)=="Month Error" or year(x)=="Year Error" or year(y)=="Year Error":
        
        return "Error 401! Date error"
        
    if year(x)>year(y):
        for i in range(year(y)+1,year(x)):
            if leap_year(i)==True:
                days+=366
            else:
                days+=365
        if leap_year(year(x))==True:
            d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for i in range(1,month(x)):
               days+=(d[i]) 
        else:
            d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for i in range(1,month(x)):
               days+=(d[i])
        days+=date(x)
        if leap_year(year(y))==True:
            d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for i in range(12,month(y),-1):
               days+=(d[i])
            days+=(d[month(x)]-date(x))
        else:
            d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for i in range(12,month(y),-1):
               days+=(d[i])
            days+=(d[month(x)]-date(x))
        return days
        
    elif year(y)>year(x):
        for i in range(year(x)+1,year(y)):
            if leap_year(i)==True:
                days+=366
            else:
                days+=365
        if leap_year(year(y))==True:
            d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for i in range(1,month(y)):
                days+=(d[i]) 
        else:
            d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for i in range(1,month(y)):
               days+=(d[i])
        days+=date(y)
        
        if leap_year(year(x))==True:
            d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for i in range(12,month(x),-1):
               days+=(d[i])
            days+=(d[month(x)]-date(x))
        else:
            d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for i in range(12,month(x),-1):
               days+=(d[i])
            days+=(d[month(x)]-date(x))
        return days

    elif year(x)==year(y):
        if month(y)>month(x):
            if leap_year(year(x))==True:
                d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                for i in range(month(x)+1,month(y)):
                    days+=(d[i])
                days+=date(y)
                days+=(d[month(x)]-date(x))
            else:
                d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                for i in range(month(x)+1,month(y)):
                    days+=(d[i])
                days+=date(y)
                days+=(d[month(x)]-date(x))
            return days
        elif month(x)>month(y):
            if leap_year(year(y))==True:
                d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                for i in range(month(y)+1,month(x)):
                    days+=(d[i])
                days+=date(x)
                days+=(d[month(y)]-date(y))
            else:
                d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                for i in range(month(y)+1,month(x)):
                    days+=(d[i])
                days+=date(x)
                days+=(d[month(y)]-date(y))
            return days
        elif month(x)==month(y):
            if date(x)>date(y):
                days=date(x)-date(y)
            elif date(y)>date(x):
                days=date(y)-date(x)
            else:
                days=0
            return days

            

def tdcalc(t):
    try:
        n=datetime.datetime.today()    
        l=t.split(' ')
        l2=[]
        td=0
        h2=(n.hour)+((n.minute)/60)+((n.second)/3600)    
        if ':' not in l[0]:
            l[0]=int(l[0])
            if l[1]=='pm' or l[1]=='PM' or l[1]=='p.m.' or l[1]=='P.M.':
                l[0]+=12
                td=(l[0]-h2)*3600
            elif l[1]=='am' or l[1]=='AM' or l[1]=='a.m.' or l[1]=='A.M.':
                td=(l[0]-h2)*3600
            else:
                
                return "Error 201! Expected AM/PM Not Found"
                
        elif ':' in l[0]:
            l2=l[0].split(':')
            l2[0]=int(l2[0])
            l2[1]=int(l2[1])
            h=l2[0]+(l2[1]/60)        
            if l[1]=='pm' or l[1]=='PM' or l[1]=='p.m.' or l[1]=='P.M.':
                h+=12            
                td=(h-h2)*3600
            elif l[1]=='am' or l[1]=='AM' or l[1]=='a.m.' or l[1]=='A.M.':
                td=(h-h2)*3600
            else:
                return "Error 201! Expected AM/PM Not Found"            
        else:
            
            return "Error 202! Invalid time format"
            
        td=int(td)
        return td
    except:
        return 'Error 203! Unexpected error occured'


def reminder(q):
    try:
        df=pd.read_csv("Data\\reminder.csv")

    # current date & time
    
        n=datetime.datetime.today()
        nex=datetime.datetime.today()+datetime.timedelta(days=1)
        day_af=datetime.datetime.today()+datetime.timedelta(days=2)
        y=str(n.day)+'/'+str(n.month)+'/'+str(n.year)
        next_day=str(nex.day)+'/'+str(nex.month)+'/'+str(nex.year)
        day_after=str(day_af.day)+'/'+str(day_af.month)+'/'+str(day_af.year)

    # sorting q
    
        if 'remind ' in q:
            q=q.replace('remind ','reminder ')
        else:
            q=q
        if 'set' in q:
            q=q.replace('set','')
        else:
            q=q
        if 'a ' in q:
            q=q.replace('a ','')
        else:
            q=q
        if 'day after tomorrow' in q:
        
            q=q.replace('day after tomorrow','on '+day_after)
        else:
            q=q
        if 'tomorrow' in q:
            q=q.replace('tomorrow','on '+next_day)
        else:
            q=q
        if 'day after' in q:
        
             q=q.replace('day after','on '+day_after)
        else:
            q=q
        if 'next day' in q:
            q=q.replace('next day','on '+next_day)
        else:
            q=q
        if 'am' in q:
            q=q.replace('am',' am')
        else:
            q=q
        if 'pm' in q:
            q=q.replace('pm',' pm')
        else:
            q=q
        if 'a.m.' in q:
            q=q.replace('a.m.',' am')
        else:
            q=q
        if 'p.m.' in q:
            q=q.replace('p.m.',' pm')
        else:
            q=q
    # variable declarations
    
        l=q.split(' ')
        z=None
        time2=[]
        date2=[]
        event=[]
        repeat=[]
        intime=[]
        at_index=None
        t_index=None
        d_index=None
        e_index=None
        ate_index=None
        on_index=None
        de_index=None
        in_index=None
        ind_index=None
        ine_index=None
        days_diff=None
        x=''

    
        for i in l:
            if i in 'of about informing knowing me ok alice the now from' and i not in 'at on to about about for in':
                l.remove(i)
            else:
                l=l

    # getting locations of event,date,time etc.
    
        for i in range(len(l)):
            if l[i]=='at' and t_index==None:
                t_index=i
            elif l[i]=='on' and d_index==None:
                d_index=i
            elif l[i]=='to' and e_index==None:
                e_index=i
            elif l[i]=='about' and e_index==None:
                e_index=i
            elif l[i]=='for' and e_index==None:
                e_index=i
            elif l[i]=='in' and in_index==None:
                in_index=i
            else:
                continue

    # event list
    
        for i in range(e_index+1,len(l)):
            event.append(l[i])

    # time list
    
        if t_index!=None and in_index==None:
            for i in l:
                if i=='':
                    l.remove(i)
                else:
                    continue
            for i in range(t_index+1,t_index+3):
                time2.append(l[i])

    # time diff to final time conversion
    
        elif t_index==None and in_index!=None:
            for i in range(in_index+1,in_index+3):
                intime.append(l[i])
            if 'hours' in intime or 'hrs' in intime or 'hour' in intime or 'hr' in intime:
                if intime[0]!='a':
                    z=(int(intime[0])*3600)
                else:
                    z=1*3600
            elif 'minutes' in intime or 'mins' in intime or 'minute' in intime or 'min' in intime:
                if intime[0]!='a':
                    z=(int(intime[0])*60)
                else:
                    z=(1*60)
            elif 'seconds' in intime or 'secs' in intime or 'second' in intime or 'sec' in intime:
                if intime[0]!='a':
                    z=(int(intime[0])*60)
                else:
                    z=1

    # possible errors in time
    
        elif t_index!=None and in_index!=None:
            print('invalid format')                        # reminder wala interface idhar
        elif t_index==None and in_index==None:
            print('error time daal')


        if d_index!=None:
            for i in range(d_index+1,len(l)):
                date2.append(l[i])
        else:
            x=y

    # sorting date list

        for i in range(len(date2)):
            if date2[i]=='at':
                at_index=i
            elif date2[i]=='for' or date2[i]=='about' or date2[i]=='to':
                de_index=i
            elif date2[i]=='in': 
                ind_index=i
            else:
                continue

    # sorting event list

        for i in range(len(event)):
            if event[i]=='at' and (event[i+2]=='am' or event[i+2]=='a.m.' or event[i+2]=='pm' or event[i+2]=='p.m.' or ((event[i+3]=='am' or event[i+3]=='a.m.' or event[i+3]=='pm' or event[i+3]=='p.m.') and event[i+2]=='')):
                ate_index=i
            elif event[i]=='on':
                on_index=i
            elif event[i]=='in':
                ine_index=i
            else:
                continue
        event2=event
        event=[]
        date3=date2
        date2=[]
    
    # finalising event list
    
        if ate_index!=None and on_index!=None and ine_index!=None and min(ate_index,on_index,ine_index)==ate_index:
            for i in range(0,ate_index):
                event.append(event2[i])
        elif ate_index!=None and on_index!=None and ine_index!=None and min(ate_index,on_index,ine_index)==on_index:
            for i in range(0,on_index):
                event.append(event2[i])
        elif ate_index!=None and on_index!=None and ine_index!=None and min(ate_index,on_index,ine_index)==ine_index:
            for i in range(0,ine_index):
                event.append(event2[i])
        elif ate_index!=None and on_index!=None and ate_index<on_index:
            for i in range(0,ate_index):
                event.append(event2[i])
        elif ate_index!=None and on_index!=None and ate_index>on_index:
        
            for i in range(0,on_index):
                event.append(event2[i])
        elif ate_index!=None and ine_index!=None and ate_index>ine_index:
            for i in range(0,ine_index):
                event.append(event2[i])
        elif ate_index!=None and ine_index!=None and ate_index<ine_index:
            for i in range(0,ate_index):
                event.append(event2[i])
        elif on_index!=None and ine_index!=None and on_index<ine_index:
            for i in range(0,on_index):
                event.append(event2[i])
        elif on_index!=None and ine_index!=None and on_index>ine_index:
            for i in range(0,ine_index):
                event.append(event2[i])        
        elif on_index!=None:
            for i in range(0,on_index):
                event.append(event2[i])
        elif ate_index!=None:
        
            for i in range(0,ate_index):
                event.append(event2[i])
        
        elif ine_index!=None:
            for i in range(0,ine_index):
                event.append(event2[i])
        else:
        
            event=event2

    # finalising date list
    

        if at_index!=None and de_index!=None and ind_index!=None and min(at_index,de_index,ind_index)==at_index:
            for i in range(0,at_index):
                date2.append(date3[i])
        elif at_index!=None and de_index!=None and ind_index!=None and min(at_index,de_index,ind_index)==de_index:
            for i in range(0,de_index):
                date2.append(date3[i])
        elif at_index!=None and de_index!=None and ind_index!=None and min(at_index,de_index,ind_index)==ind_index:
            for i in range(0,ind_index):
                date2.append(date3[i])
        elif at_index!=None and de_index!=None and at_index > de_index:
            for i in range(0,de_index):
                date2.append(date3[i])
        elif at_index!=None and de_index!=None and at_index < de_index:
            for i in range(0,at_index):
                date2.append(date3[i])
        elif at_index!=None and ind_index!=None and at_index < ind_index:
            for i in range(0,at_index):
                date2.append(date3[i])
        elif at_index!=None and ind_index!=None and at_index > ind_index:
            for i in range(0,ind_index):
                date2.append(date3[i])
        elif de_index!=None and ind_index!=None and de_index > ind_index:
            for i in range(0,ind_index):
                date2.append(date3[i])
        elif de_index!=None and ind_index!=None and de_index < ind_index:
            for i in range(0,de_index):
                date2.append(date3[i])       
        elif at_index!=None:
            for i in range(0,at_index):
                date2.append(date3[i])
        elif de_index!=None:
            for i in range(0,de_index):
                date2.append(date3[i])
        elif ind_index!=None:
            for i in range(0,ind_index):
                date2.append(date3[i])
        else:
            date2=date3

    # time diff calculation
        t=''
        
        for i in time2:
            t+=i+' '
        
        if in_index==None:
            z=tdcalc(t)
            z=int(z)
        else:
            z=z

    # date format conversion
    
        if len(date2)!=1 and len(date2)!=0:
            da=date2[0]+' '+date2[1]+' '+date2[2]
            x=date_conv(da)
        elif len(date2)==1:
            x=date2[0]
        else:
            x=y

    # date of alarm date final format
    
        days_diff=(days_between(x,y))
        time_delta=z
        print(time_delta)
        new_time=n+datetime.timedelta(0,int(z))

    # alarm time finalisation
    
        nh=new_time.hour
        nm=new_time.minute
        ns=new_time.second
        alarm_time=''
        if nh>12:
            nh=nh-12
            alarm_time=str(nh)+':'+str(nm)+' pm'
        else:
            alarm_time=str(nh)+':'+str(nm)+' am'

    # event string generation
    
        e=''
        for i in event:
            e+=i+' '
    
    # changing df
    
        df.loc[df.size+1]=[e,alarm_time,x,'False']
        nan_value = float("NaN")
    
        df.replace("", nan_value, inplace=True)

        df.dropna(subset = ["event"], inplace=True)

    # updating csv
        
        df.to_csv("Data\\reminder.csv",index=False)
        return True

    except:
        df=pd.read_csv("Data\\reminder.csv")
        window=Tk()
        window.geometry("600x220")
        window.title('Reminder')
        window.resizable(width=False,height=False)
        root=Canvas(window,width=600,height=220)
        root.pack()
        bg=PhotoImage(file="Themes\\wooden.png")
        icon=PhotoImage(file="Resources\\icon.png")
        window.iconphoto(False,icon)
        root.create_image(600,220,image=bg,anchor='center')
    # Add Calendar
        hr=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
        mi=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']
        sec=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','15','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']
        cal = Calendar(root, selectmode = 'day',
                       year = 2021,date_pattern='y-mm-dd',
                       background='black',disabledbackground="black", bordercolor="#404040",
                       headersbackground="#222222", normalbackground="#404040", foreground='black',
                       normalforeground='white', headersforeground='white')
        cal.config(background = "#fff")

        cal.place(x=10,y=10)

    # Time
        clicked=StringVar()
        clicked2=StringVar()
        clicked3=StringVar()
        clicked.set("0")
        clicked2.set("0")
        clicked3.set("0")
        om=OptionMenu(root, clicked, *hr)
        om.config(bg="#404040",fg='#fff')
        om["highlightthickness"]=0
        om.place(x=300,y=35)
        om2=OptionMenu(root, clicked2, *mi)
        om2.config(bg="#404040",fg='#fff')
        om2["highlightthickness"]=0
        om2.place(x=380,y=35)
        om3=OptionMenu(root, clicked3, *sec)
        om3.config(bg="#404040",fg='#fff')
        om3["highlightthickness"]=0
        om3.place(x=460,y=35)
        
        

        root.create_text(320,90,text='Event : ',fill="#fff",font="Helvetica 11")
        root.create_text(320,20,text='Hr',fill="#fff",font="Helvetica 11")
        root.create_text(400,20,text='Min',fill="#fff",font="Helvetica 11")
        root.create_text(480,20,text='Sec',fill="#fff",font="Helvetica 11")
        my_event=Text(root,height=1,width=30,font="Helvetica 11",bg='#404040',fg='#fff',borderwidth=0,insertbackground='white')
        my_event.place(x=345,y=80)
        my_event.focus()
        
        def grad_date():
            x=cal.get_date()
            l=x.split('-')
            date_of_reminder=''
            
            if len(l)==3:
                date_of_reminder=l[2]+'/'+l[1]+'/'+l[0]
            else:
                messagebox.showinfo("Reminder", "Select date",parent=root)
                return None
           
            if cal.get_date()!='' and len(my_event.get("1.0",END))!=1:
                root.create_text(490,230,fill='#fff',font="Helvetica 11",text = ("Reminder set at \nDate : " + date_of_reminder + "\nTime : " + clicked.get()+':'+clicked2.get()+':'+clicked3.get()+"\nEvent : "+my_event.get("1.0",END)),anchor='se')
            else:
                messagebox.showinfo("Reminder", "Enter Event",parent=root)
            if int(clicked.get())>12:
                h=int(clicked.get())-12
                alarm_time=str(h)+':'+clicked2.get()+' pm'
            else:
                h=clicked.get()
                alarm_time=h+':'+clicked2.get()+' am'
            e=my_event.get("1.0",END)
            if '\n' in e:
                e=e.replace('\n','')
            else:
                e=e
            df.loc[df.size+1]=[e,alarm_time,date_of_reminder,'False']
            nan_value = float("NaN")
    
            df.replace("", nan_value, inplace=True)

            df.dropna(subset = ["event"], inplace=True)
            
            df.to_csv("Data\\reminder.csv",index=False)
            return True
            
            
        Button(root, text = "Set reminder",font="Helvetica 11",
               command = grad_date).place(x=370,y=110)
        
 
        
        root.mainloop()
def reminderWindow():
    df=pd.read_csv("Data\\reminder.csv")
    window=Tk()
    window.geometry("600x220")
    window.title('Reminder')
    window.resizable(width=False,height=False)
    root=Canvas(window,width=600,height=220)
    root.pack()
    bg2=PhotoImage(file="Themes\\wooden.png")
    icon2=PhotoImage(file="Resources\\icon.png")
    window.iconphoto(False,icon2)
    root.create_image(600,220,image=bg2,anchor='center')
    # Add Calendar
    hr=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
    mi=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']
    sec=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','15','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']
    cal = Calendar(root, selectmode = 'day',
                    year = 2021,date_pattern='y-mm-dd',
                    background='black',disabledbackground="black", bordercolor="#404040",
                    headersbackground="#222222", normalbackground="#404040", foreground='black',
                    normalforeground='white', headersforeground='white')
    cal.config(background = "#fff")

    cal.place(x=10,y=10)

    # Time
    clicked=StringVar()
    clicked2=StringVar()
    clicked3=StringVar()
    clicked.set("0")
    clicked2.set("0")
    clicked3.set("0")
    om=OptionMenu(root, clicked, *hr)
    om.config(bg="#404040",fg='#fff')
    om["highlightthickness"]=0
    om.place(x=300,y=35)
    om2=OptionMenu(root, clicked2, *mi)
    om2.config(bg="#404040",fg='#fff')
    om2["highlightthickness"]=0
    om2.place(x=380,y=35)
    om3=OptionMenu(root, clicked3, *sec)
    om3.config(bg="#404040",fg='#fff')
    om3["highlightthickness"]=0
    om3.place(x=460,y=35)
        
        

    root.create_text(320,90,text='Event : ',fill="#fff",font="Helvetica 11")
    root.create_text(320,20,text='Hr',fill="#fff",font="Helvetica 11")
    root.create_text(400,20,text='Min',fill="#fff",font="Helvetica 11")
    root.create_text(480,20,text='Sec',fill="#fff",font="Helvetica 11")
    my_event=Text(root,height=1,width=30,font="Helvetica 11",bg='#404040',fg='#fff',borderwidth=0,insertbackground='white')
    my_event.place(x=345,y=80)
    my_event.focus()
        
    def grad_date():
        x=cal.get_date()
        l=x.split('-')
        date_of_reminder=''
            
        if len(l)==3:
            date_of_reminder=l[2]+'/'+l[1]+'/'+l[0]
        else:
            messagebox.showinfo("Reminder", "Select date",parent=root)
            return None
           
        if cal.get_date()!='' and len(my_event.get("1.0",END))!=1:
            root.create_text(490,230,fill='#fff',font="Helvetica 11",text = ("Reminder set at \nDate : " + date_of_reminder + "\nTime : " + clicked.get()+':'+clicked2.get()+':'+clicked3.get()+"\nEvent 😃 : "+my_event.get("1.0",END)),anchor='se')
        else:
            messagebox.showinfo("Reminder", "Enter Event",parent=root)
        if int(clicked.get())>12:
            h=int(clicked.get())-12
            alarm_time=str(h)+':'+clicked2.get()+' pm'
        else:
            h=clicked.get()
            alarm_time=h+':'+clicked2.get()+' am'
        e=my_event.get("1.0",END)
        if '\n' in e:
            e=e.replace('\n','')
        else:
            e=e
        df.loc[df.size+1]=[e,alarm_time,date_of_reminder,'False']
        nan_value = float("NaN")
    
        df.replace("", nan_value, inplace=True)

        df.dropna(subset = ["event"], inplace=True)
            
        df.to_csv("Data\\reminder.csv",index=False)
        return True
            
            
    Button(root, text = "Set reminder",font="Helvetica 11",
            command = grad_date).place(x=370,y=110)
        
 
        
    root.mainloop()

reminderWindow()

