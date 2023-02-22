import matplotlib.pyplot as plt
import datetime
import os
from matplotlib.ticker import MaxNLocator
import numpy as np
from scipy.interpolate import make_interp_spline
import pandas as pd

i=[]
curdir=os.path.dirname(os.path.abspath(__file__))

with open(curdir+"\\Data\\usage_stat.txt") as file:
    for line in file:
        if line.strip()!="":
            i.append(line.rstrip())

detail_network_with_time={}
for item in i:
    detail_network_with_time[item.split("//")[1]]=item.split("//")[3]

detail_network_dict={}    
for m in range(0,24):
    for n in range(0,60):
        hour=str(m)
        minute=str(n)
        if m<10:
            hour="0"+str(m)
        if n<10:
            minute="0"+str(n)
        time=hour+":"+minute
        if time in detail_network_with_time:
            detail_network_dict[time+":00"]=round(float(detail_network_with_time[time]),4)
        else:
            detail_network_dict[time+":00"]=0
        
detail_cpu_with_time={}
for item in i:
    detail_cpu_with_time[item.split("//")[1]]=item.split("//")[2]

detail_cpu_dict={}    
for m in range(0,24):
    for n in range(0,60):
        hour=str(m)
        minute=str(n)
        if m<10:
            hour="0"+str(m)
        if n<10:
            minute="0"+str(n)
        time=hour+":"+minute
        if time in detail_cpu_with_time:
            detail_cpu_dict[time+":00"]=round(float(detail_cpu_with_time[time]),4)
        else:
            detail_cpu_dict[time+":00"]=0
def plot_usage(category='both'):
    if category=='cpu':
        x,y=zip(*sorted(zip(detail_cpu_dict.keys(),detail_cpu_dict.values())))
        fig,ax=plt.subplots(1,1)
        fig.set_facecolor("white")
        l=list(detail_cpu_dict.keys())
        l2=[]
        for i in l:
            if ':' in i:
                i=i.replace(':','')
                l2.append(float(i))
            else:
                continue

        x=np.array(l2)
        y=np.array(list(detail_cpu_dict.values()))
        ser=pd.Series(y,index=x)
        ser.plot.kde()
        #ax.set_xticks(l)
        #ax.set_yticks(y)
        ax.xaxis.set_major_locator(MaxNLocator(12, min_n_ticks=12))
        ax.set_title('CPU Usage(%)')
        ax.grid(True)
        fig.suptitle("Usage Statistics", fontsize=26,color='orange')
        
        for tick in ax.get_xticklabels():
            tick.set_rotation(30)
        fig.show()
        
    elif category=='network':
        fig,ax=plt.subplots(1,1)
        fig.set_facecolor("white")
        ax.plot(detail_network_dict.keys(),detail_network_dict.values())
        ax.xaxis.set_major_locator(MaxNLocator(12, min_n_ticks=12))
        ax.set_title('Network Usage(in mbit)')
        ax.grid(True)
        fig.suptitle("Usage Statistics", fontsize=26,color='orange')
        
        for tick in ax.get_xticklabels():
            tick.set_rotation(30)
        fig.show()
        
    elif category=='both':
        fig,ax=plt.subplots(2)
        fig.set_facecolor("white")
        ax[1].plot(detail_network_dict.keys(),detail_network_dict.values(),color='green')
        ax[1].xaxis.set_major_locator(MaxNLocator(12, min_n_ticks=12))
        ax[1].set(title='Network Usage(in mbit)')
        ax[1].grid(True)
        ax[0].plot(detail_cpu_dict.keys(),detail_cpu_dict.values(),color='blue')
        ax[0].xaxis.set_major_locator(MaxNLocator(12, min_n_ticks=12))
        ax[0].set(title='CPU Usage(%)')
        ax[0].grid(True)
        fig.suptitle("Usage Statistics", fontsize=26,color='orange')
        
        for tick in ax[1].get_xticklabels():
            tick.set_rotation(30)
        for tick in ax[0].get_xticklabels():
            tick.set_rotation(30)

        fig.legend(ax,labels=['Network Usage(in mbit)','CPU Usage(%)'],borderaxespad=0.9)
        fig.subplots_adjust(top=0.85,left=0.85)
        fig.tight_layout(pad=0.5)
        fig.show()

        
plot_usage(category='cpu')
