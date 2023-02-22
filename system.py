import os
import ctypes
import time
from datetime import datetime
import glob
import subprocess

curdir=os.path.dirname(os.path.abspath(__file__))

def tdcalc(t):
    try:
        n=datetime.now()    
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
        return "Error 203! Unexpected error occured"
        
def time_sep(q):
    try:
        t=0
        l2=q.split(' ')
        l=[]
        l3=[]
        z=None
        b=0
        for i in range(len(l2)):
            if l2[i]=='off':
                z=i
            else:
                l2=l2
        if z==None:
            l2=l2
        else:
            l2.remove(l2[z])
            l2[z-1]='log-off'
        for i in range(len(l2)):
            if l2[i]=='shutdown' or l2[i]=='restart' or l2[i]=='lock' or l2[i]=='log-off':
                b=i
        for i in range(b,len(l2)):
            l.append(l2[i])
        if l[0]=='shutdown' or l[0]=='restart' or l[0]=='lock' or l[0]=='log-off':
            l[0]==''        
            if 'in' in l:
                for i in range(len(l)):
                    if l[i]=='in':
                        c=i
                for i in range(c+1,len(l)):
                    l3.append(l[i])         
                if l3[0]=='a' or l3[0]=='an':
                    l3[0]=1
                    if l3[1]=='min' or l3[1]=='minute':
                        l3[1]=60
                    elif l3[1]=='sec' or l3[1]=='second':
                        l3[1]=1
                    elif l3[1]=='hour':
                        l3[1]=3600                    
                else:
                    l3[0]=int(l3[0])
                    if l3[1]=='min' or l3[1]=='minute' or l3[1]=='minutes' or l3[1]=='mins':
                        l3[1]=60
                    elif l3[1]=='sec' or l3[1]=='second' or l3[1]=='seconds' or l3[1]=='secs':
                        l3[1]=1
                    elif l3[1]=='hour' or l3[1]=='hours':
                        l3[1]=3600   
                t=l3[0]*l3[1]
                return t
            elif 'at' in l:
                c=1
                for i in range(len(l)):
                    if l[i]=='at':
                        c=i
                for i in range(c+1,len(l)):
                    l3.append(l[i])
                e=l3[0]+' '+l3[1]
                td=tdcalc(e)
                return td             
            else:
                t=0
                return t
        else:
            return "Error 203! Unexpected error occured" 
            
    except:
        return "Error 203! Unexpected error occured" 

def shutdown(t):
    os.system("shutdown /s /t "+str(t))
def restart(t):
    os.system("shutdown /r /t "+str(t))
def lock(t):
    time.sleep(t)
    ctypes.windll.user32.LockWorkStation()
def log_off(t):
    time.sleep(t)
    os.system("shutdown -l")
    
def screenshot(Fullscreen=True,copy=True,PNGsave=True):
    try:
        return None
        
    except:     
        return "Error 206! Unexpected error occured"

def init(string):
    if 'shutdown' in string:
        n=system.time_sep(string)
        system.shutdown(n)
    elif 'restart' in string:
        n=system.time_sep(string)
        system.restart(n)
    elif 'lock' in string:
        n=system.time_sep(string)
        system.lock(n)
    elif 'log off' in string:
        n=system.time_sep(string)
        system.log_off(n)
    elif 'screenshot' in string or 'ss' in string or ('capture' in string and 'screen' in string) or ('capture' in string and 'window' in string):
        screenshot()
        
