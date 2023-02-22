import pandas as pd
import datetime
from tkinter import *
from tkinter import messagebox
import time as timelib
import reminder
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
        if a[i]=="/" or a[i]=='-':
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
        if a[i]=="/" or a[i]=='-':
            d=0
            for t in range(0,i+1):
                a.remove(a[t-d])
                d+=1   
            break
        else:
           continue

    for i in range(0,len(a)):
        if a[i]=="/" or a[i]=='-':
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
        if a[i]=="/" or a[i]=='-':
            d=0
            for t in range(0,i+1):
                a.remove(a[t-d])
                d+=1   
            break
        else:
           continue
    for i in range(0,len(a)):
        if a[i]=="/" or a[i]=='-':
            d=0
            for t in range(0,i+1):
                a.remove(a[t-d])
                d+=1   
            break
        else:
            continue
    for i in range(0,len(a)):
        if a[i]=="/" or a[i]=='-':
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
                days=date(x)-date(y)
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
def reminderShow():
    window=Tk()
    window.geometry("300x200")
    window.title('Reminder')
    window.resizable(width=False,height=False)
    icon3=PhotoImage(file="Resources\\icon.png")
    window.iconphoto(False,icon3)
    root=Canvas(window,width=600,height=220,bg='#0E1621')
    root.pack()
    b1=Button(root,text='Ok',width=21,command = lambda : window.destroy())
    b1.place(x=140,y=172)
    b2=b1=Button(root,text='Set another reminder',width=21, command = lambda : reminder.reminderWindow())
    b1.place(x=0,y=172)
    window.mainloop()

def init():
    df=pd.read_csv("Data\\reminder.csv")
    df=df.dropna()
    events=df['event']
    times=df['time']
    dates=df['date']
    statuses=df['status']
    event=[]
    time=[]
    date=[]
    status=[]
    days_left=[]
    time_left=[]
    time_diff=[]
    current_day=str(datetime.datetime.today().day)+'/'+str(datetime.datetime.today().month)+'/'+str(datetime.datetime.today().year)
    for i in range(events.size):
        event.append(events[i])
    for i in range(times.size):
        time.append(times[i])
    for i in range(dates.size):
        date.append(dates[i])
    for i in range(statuses.size):
        status.append(statuses[i])
    for i in date:
        days_left.append(days_between(i,current_day))
    for i in time:
        time_left.append(tdcalc(i))
    for i in range(len(days_left)):
        time_diff.append((days_left[i]*24*3600)+(time_left[i]))
    for i in range(len(time_diff)):
        if time_diff[i] > 0 and time_diff[i] < 20 and status[i]==False:
            e=event[i]
            status[i]=True
            df.loc[df.event==e,'status']=True
            timelib.sleep(time_diff[i])
            reminderShow()
        else:
            df=df
    
    df.to_csv("Data\\reminder.csv",index=False)
    
while True:
    init()

