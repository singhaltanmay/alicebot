import psutil
import time
import psutil
from datetime import datetime
from datetime import date
import os
import usage_statistics_sql

curdir=os.path.dirname(os.path.abspath(__file__))

def to_mbit(value):
    return ((value/1024)/1024)*8

def write_stat(network_stat,cpu_percent):
    
    if os.stat(curdir+"\\Data\\usage_stat.txt").st_size == 0:
        f=open(curdir+"\\Data\\usage_stat.txt",'a+')
        y=str(date.today())
        network_stat=str(network_stat)
        network_stat=network_stat.strip()
        cpu_percent=str(cpu_percent)
        cpu_percent=cpu_percent.strip()
        now = datetime.now()
        current_time = str(now.strftime("%H:%M"))
        f.write(y+"//"+current_time+"//"+network_stat+"//"+cpu_percent)
        f.close()

    else:
        i=[]
        with open(curdir+"\\Data\\usage_stat.txt") as file:
            for line in file:
                if line.strip()!="":
                    i.append(line.rstrip())
        y=str(date.today())
        if ((i[0]).split("//"))[0]==y:
            f=open(curdir+"\\Data\\usage_stat.txt",'a+')
            network_stat=str(network_stat)
            network_stat=network_stat.strip()
            cpu_percent=str(cpu_percent)
            cpu_percent=cpu_percent.strip()
            now = datetime.now()
            current_time = str(now.strftime("%H:%M"))
            f.write('\n'+y+"//"+current_time+"//"+network_stat+"//"+cpu_percent)
            f.close()
        else:
            while usage_statistics_sql!=True:
                pass
                       
            f=open(curdir+"\\Data\\usage_stat.txt",'w+')
            y=str(date.today())
            network_stat=str(network_stat)
            network_stat=network_stat.strip()
            cpu_percent=str(cpu_percent)
            cpu_percent=cpu_percent.strip()
            now = datetime.now()
            current_time = str(now.strftime("%H:%M"))
            f.write(y+"//"+current_time+"//"+network_stat+"//"+cpu_percent)
            f.close() 

def get_stat(stat_type):
    if stat_type=='Network':
        value1=psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        time.sleep(1)
        value2=psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        return to_mbit(value2-value1)
    elif stat_type=="Cpu_Usage":
        return psutil.cpu_percent()

while True:
    write_stat(get_stat('Cpu_Usage'),get_stat('Network'))
    time.sleep(60)

    

