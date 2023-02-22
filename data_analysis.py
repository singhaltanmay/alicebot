import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import datetime

from warnings import simplefilter
simplefilter(action='ignore', category=Warning)

class Data_Analysis:
    def __init__(self,data):
        if isinstance(data, pd.DataFrame):
            data1=np.array(data)
            self.data2=data1.tolist()
            self.data=[]
            for i in self.data2:
                self.data.append(i[0])
        elif isinstance(data, np.ndarray):
            self.data=data.tolist()
        elif isinstance(data,list):
            self.data=data
        else:
            raise Exception('The data has to be pandas.DataFrame or numpy.ndarray or list')

    def even(self,num):
        if num//2==num/2:
            return True
        else:
            return False

    def odd(self,num):
        if num//2==num/2:
            return False
        else:
            return True
        
    def max(self):
        return max(self.data)
    
    def min(self):
        return min(self.data)

    def is_stable(self,tolerance=0):
        x=[]
        for i in self.data:
            x.append(i/(min(self.data)))
        t=True
        for i in x:
            if i>=1 and i<=(1+tolerance):
                t=True
            else:
                t=False
                return False
        return t

    def diff(self,n=1):
        diff_count=0
        l1=[]
        l2=[]
        while diff_count<n:
            if diff_count==0:
                for i in range(1,len(self.data)):
                    l1.append(self.data[i]-self.data[i-1])
            else:
                l2=[]
                for i in range(1,len(l1)):
                    l2.append(l1[i]-l1[i-1])
                l1=l2
                l2=[]
            diff_count+=1
        return l1
                
    def average(self,weighted=None,round_digit=None):
        if weighted==None:
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/(len(self.data)))
                    s=0
                s+=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return s/(len(self.data))
                else:
                    return round(s/(len(self.data)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/(len(self.data))+su)
                else:
                    return round((s/(len(self.data))+su),round_digit)
        elif weighted.lower()=="none" or weighted.lower()=="n":
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/(len(self.data)))
                    s=0
                s+=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return s/(len(self.data))
                else:
                    return round(s/(len(self.data)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/(len(self.data))+su)
                else:
                    return round((s/(len(self.data))+su),round_digit)
                
        elif weighted.lower()=="right" or weighted.lower()=="r":
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/((len(self.data)*(len(self.data)+1)/2)))
                    s=0
                s+=self.data[i]*(i+1)
            if len(lis)==0:
                if round_digit==None:
                    return s/((len(self.data)*(len(self.data)+1)/2))
                else:
                    return round(s/((len(self.data)*(len(self.data)+1)/2)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/((len(self.data)*(len(self.data)+1)/2))+su)
                else:
                    return round((s/((len(self.data)*(len(self.data)+1)/2))+su),round_digit)

        elif weighted.lower()=='left' or weighted.lower()=='l':
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/((len(self.data)*(len(self.data)+1)/2)))
                    s=0
                s+=self.data[i]*(len(self.data)-i)
            if len(lis)==0:
                if round_digit==None:
                    return s/((len(self.data)*(len(self.data)+1)/2))
                else:
                    return round(s/((len(self.data)*(len(self.data)+1)/2)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/((len(self.data)*(len(self.data)+1)/2))+su)
                else:
                    return round((s/((len(self.data)*(len(self.data)+1)/2))+su),round_digit)

        elif weighted.lower()=='center' or weighted.lower()=='mid' or weighted.lower()=='middle' or weighted.lower()=='c' or weighted.lower()=='m' :
            if self.even(len(self.data))==False:
                s=0
                lis=[]
                for i in range(0,len(self.data)):
                    if s>10000000000:
                        lis.append(s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))
                        s=0
                    if (i+1)>((len(self.data)+1)/2):
                        s+=self.data[i]*((len(self.data))-(i))
                    else:
                        s+=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return s/(((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))
                    else:
                        return round(s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)),round_digit)
                else:
                    su=0
                    for x in lis:
                        su+=x
                    if round_digit==None:
                        return (s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))+su)
                    else:
                        return round((s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))+su,round_digit)
            else:
                s=0
                lis=[]
                for i in range(0,len(self.data)):
                    if s>10000000000:
                        lis.append(s/(((((len(self.data)/2))*((len(self.data)/2)+1)))))
                        s=0
                    if (i+1)>((len(self.data))/2):
                        s+=self.data[i]*((len(self.data))-(i))
                    else:
                        s+=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return s/(((((len(self.data)/2))*((len(self.data)/2)+1))))
                    else:
                        return round(s/(((((len(self.data)/2))*((len(self.data)/2)+1)))),round_digit)
                else:
                    su=0
                    for x in lis:
                        su+=x
                    if round_digit==None:
                        return (s/(((((len(self.data)/2))*((len(self.data)/2)+1))))+su)
                    else:
                        return round((s/((((len(self.data)/2))*((len(self.data)/2)+1))))+su,round_digit)

    def arithmetic_mean(self,weighted=None,round_digit=None):
        if weighted==None:
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/(len(self.data)))
                    s=0
                s+=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return s/(len(self.data))
                else:
                    return round(s/(len(self.data)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/(len(self.data))+su)
                else:
                    return round((s/(len(self.data))+su),round_digit)
        elif weighted.lower()=="none" or weighted.lower()=="n":
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/(len(self.data)))
                    s=0
                s+=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return s/(len(self.data))
                else:
                    return round(s/(len(self.data)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/(len(self.data))+su)
                else:
                    return round((s/(len(self.data))+su),round_digit)
                
        elif weighted.lower()=="right" or weighted.lower()=="r":
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/((len(self.data)*(len(self.data)+1)/2)))
                    s=0
                s+=self.data[i]*(i+1)
            if len(lis)==0:
                if round_digit==None:
                    return s/((len(self.data)*(len(self.data)+1)/2))
                else:
                    return round(s/((len(self.data)*(len(self.data)+1)/2)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/((len(self.data)*(len(self.data)+1)/2))+su)
                else:
                    return round((s/((len(self.data)*(len(self.data)+1)/2))+su),round_digit)

        elif weighted.lower()=='left' or weighted.lower()=='l':
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/((len(self.data)*(len(self.data)+1)/2)))
                    s=0
                s+=self.data[i]*(len(self.data)-i)
            if len(lis)==0:
                if round_digit==None:
                    return s/((len(self.data)*(len(self.data)+1)/2))
                else:
                    return round(s/((len(self.data)*(len(self.data)+1)/2)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/((len(self.data)*(len(self.data)+1)/2))+su)
                else:
                    return round((s/((len(self.data)*(len(self.data)+1)/2))+su),round_digit)

        elif weighted.lower()=='center' or weighted.lower()=='mid' or weighted.lower()=='middle' or weighted.lower()=='c' or weighted.lower()=='m' :
            if self.even(len(self.data))==False:
                s=0
                lis=[]
                for i in range(0,len(self.data)):
                    if s>10000000000:
                        lis.append(s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))
                        s=0
                    if (i+1)>((len(self.data)+1)/2):
                        s+=self.data[i]*((len(self.data))-(i))
                    else:
                        s+=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return s/(((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))
                    else:
                        return round(s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)),round_digit)
                else:
                    su=0
                    for x in lis:
                        su+=x
                    if round_digit==None:
                        return (s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))+su)
                    else:
                        return round((s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))+su,round_digit)
            else:
                s=0
                lis=[]
                for i in range(0,len(self.data)):
                    if s>10000000000:
                        lis.append(s/(((((len(self.data)/2))*((len(self.data)/2)+1)))))
                        s=0
                    if (i+1)>((len(self.data))/2):
                        s+=self.data[i]*((len(self.data))-(i))
                    else:
                        s+=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return s/(((((len(self.data)/2))*((len(self.data)/2)+1))))
                    else:
                        return round(s/(((((len(self.data)/2))*((len(self.data)/2)+1)))),round_digit)
                else:
                    su=0
                    for x in lis:
                        su+=x
                    if round_digit==None:
                        return (s/(((((len(self.data)/2))*((len(self.data)/2)+1))))+su)
                    else:
                        return round((s/((((len(self.data)/2))*((len(self.data)/2)+1))))+su,round_digit)
            
    def am(self,weighted=None,round_digit=None):
        if weighted==None:
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/(len(self.data)))
                    s=0
                s+=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return s/(len(self.data))
                else:
                    return round(s/(len(self.data)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/(len(self.data))+su)
                else:
                    return round((s/(len(self.data))+su),round_digit)
        elif weighted.lower()=="none" or weighted.lower()=="n":
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/(len(self.data)))
                    s=0
                s+=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return s/(len(self.data))
                else:
                    return round(s/(len(self.data)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/(len(self.data))+su)
                else:
                    return round((s/(len(self.data))+su),round_digit)
                
        elif weighted.lower()=="right" or weighted.lower()=="r":
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/((len(self.data)*(len(self.data)+1)/2)))
                    s=0
                s+=self.data[i]*(i+1)
            if len(lis)==0:
                if round_digit==None:
                    return s/((len(self.data)*(len(self.data)+1)/2))
                else:
                    return round(s/((len(self.data)*(len(self.data)+1)/2)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/((len(self.data)*(len(self.data)+1)/2))+su)
                else:
                    return round((s/((len(self.data)*(len(self.data)+1)/2))+su),round_digit)

        elif weighted.lower()=='left' or weighted.lower()=='l':
            s=0
            lis=[]
            for i in range(0,len(self.data)):
                if s>10000000000:
                    lis.append(s/((len(self.data)*(len(self.data)+1)/2)))
                    s=0
                s+=self.data[i]*(len(self.data)-i)
            if len(lis)==0:
                if round_digit==None:
                    return s/((len(self.data)*(len(self.data)+1)/2))
                else:
                    return round(s/((len(self.data)*(len(self.data)+1)/2)),round_digit)
            else:
                su=0
                for x in lis:
                    su+=x
                if round_digit==None:
                    return (s/((len(self.data)*(len(self.data)+1)/2))+su)
                else:
                    return round((s/((len(self.data)*(len(self.data)+1)/2))+su),round_digit)

        elif weighted.lower()=='center' or weighted.lower()=='mid' or weighted.lower()=='middle' or weighted.lower()=='c' or weighted.lower()=='m' :
            if self.even(len(self.data))==False:
                s=0
                lis=[]
                for i in range(0,len(self.data)):
                    if s>10000000000:
                        lis.append(s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))
                        s=0
                    if (i+1)>((len(self.data)+1)/2):
                        s+=self.data[i]*((len(self.data))-(i))
                    else:
                        s+=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return s/(((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))
                    else:
                        return round(s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)),round_digit)
                else:
                    su=0
                    for x in lis:
                        su+=x
                    if round_digit==None:
                        return (s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))+su)
                    else:
                        return round((s/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))+su,round_digit)
            else:
                s=0
                lis=[]
                for i in range(0,len(self.data)):
                    if s>10000000000:
                        lis.append(s/(((((len(self.data)/2))*((len(self.data)/2)+1)))))
                        s=0
                    if (i+1)>((len(self.data))/2):
                        s+=self.data[i]*((len(self.data))-(i))
                    else:
                        s+=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return s/(((((len(self.data)/2))*((len(self.data)/2)+1))))
                    else:
                        return round(s/(((((len(self.data)/2))*((len(self.data)/2)+1)))),round_digit)
                else:
                    su=0
                    for x in lis:
                        su+=x
                    if round_digit==None:
                        return (s/(((((len(self.data)/2))*((len(self.data)/2)+1))))+su)
                    else:
                        return round((s/((((len(self.data)/2))*((len(self.data)/2)+1))))+su,round_digit)          

    def geometric_mean(self,weighted=None,round_digit=None):
         if weighted==None:
            p=1
            lis=[]
            for i in range(0,len(self.data)):
                if p>10000000000:
                    lis.append(p**(1/(len(self.data))))
                    p=1
                p*=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return p**(1/(len(self.data)))
                else:
                    return round(p**(1/(len(self.data))),round_digit)
            else:
                product=1
                for x in lis:
                    product*=x
                if round_digit==None:
                    return p**(1/(len(self.data)))*product
                else:
                    return round(p**(1/(len(self.data)))*product,round_digit)
                
         elif weighted.lower()=="none" or weighted.lower()=="n":
            p=1
            lis=[]
            for i in range(0,len(self.data)):
                if p>10000000000:
                    lis.append(p**(1/(len(self.data))))
                    p=1
                p*=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return p**(1/(len(self.data)))
                else:
                    return round(p**(1/(len(self.data))),round_digit)
            else:
                product=1
                for x in lis:
                    product*=x
                if round_digit==None:
                    return p**(1/(len(self.data)))*product
                else:
                    return round(p**(1/(len(self.data)))*product,round_digit)
                
         elif weighted.lower()=="right" or weighted.lower()=="r":
            p=1
            lis=[]
            for i in range(0,len(self.data)):
                if p>10000000000:
                    lis.append(p**(1/((len(self.data)*(len(self.data)+1)/2))))
                    p=1
                p*=(self.data[i]*(i+1))
            if len(lis)==0:
                if round_digit==None:
                    return p**(1/((len(self.data)*(len(self.data)+1)/2)))
                else:
                    return round(p**(1/((len(self.data)*(len(self.data)+1)/2))),round_digit)
            else:
                product=1
                for x in lis:
                    product*=x
                if round_digit==None:
                    return p**(1/((len(self.data)*(len(self.data)+1)/2)))*product
                else:
                    return round(p**(1/((len(self.data)*(len(self.data)+1)/2)))*product,round_digit)
                
         elif weighted.lower()=='left' or weighted.lower()=='l':
            p=1
            lis=[]
            for i in range(0,len(self.data)):
                if p>10000000000:
                    lis.append(p**(1/((len(self.data)*(len(self.data)+1)/2))))
                    p=1
                p*=(self.data[i]*(len(self.data)-i))
            if len(lis)==0:
                if round_digit==None:
                    return p**(1/((len(self.data)*(len(self.data)+1)/2)))
                else:
                    return round(p**(1/((len(self.data)*(len(self.data)+1)/2))),round_digit)
            else:
                product=1
                for x in lis:
                    product*=x
                if round_digit==None:
                    return p**(1/((len(self.data)*(len(self.data)+1)/2)))*product
                else:
                    return round(p**(1/((len(self.data)*(len(self.data)+1)/2)))*product,round_digit)

         elif weighted.lower()=='center' or weighted.lower()=='mid' or weighted.lower()=='middle' or weighted.lower()=='c' or weighted.lower()=='m' :
            if self.even(len(self.data))==False:
                p=1
                lis=[]
                for i in range(0,len(self.data)):
                    if p>10000000000:
                        lis.append(p**(1/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))))
                        p=1
                    if (i+1)>((len(self.data)+1)/2):
                        p*=self.data[i]*((len(self.data))-(i))
                    else:
                        p*=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return p**(1/(((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))))
                    else:
                        return round(p**(1/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))),round_digit)
                else:
                    product=1
                    for x in lis:
                        product*=x
                    if round_digit==None:
                        return (p**(1/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))*product)
                    else:
                        return round((p**(1/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))))*product,round_digit)
            else:
                p=1
                lis=[]
                for i in range(0,len(self.data)):
                    if p>10000000000:
                        lis.append(p**(1/(((((len(self.data)/2))*((len(self.data)/2)+1))))))
                        p=1
                    if (i+1)>((len(self.data))/2):
                        p*=self.data[i]*((len(self.data))-(i))
                    else:
                        p*=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return p**(1/(((((len(self.data)/2))*((len(self.data)/2)+1)))))
                    else:
                        return round(p**(1/(((((len(self.data)/2))*((len(self.data)/2)+1))))),round_digit)
                else:
                    product=1
                    for x in lis:
                        product*=x
                    if round_digit==None:
                        return (p**(1/(((((len(self.data)/2))*((len(self.data)/2)+1)))))*product)
                    else:
                        return round((p**(1/((((len(self.data)/2))*((len(self.data)/2)+1)))))*product,round_digit)
                    
    def gm(self,weighted=None,round_digit=None):
         if weighted==None:
            p=1
            lis=[]
            for i in range(0,len(self.data)):
                if p>10000000000:
                    lis.append(p**(1/(len(self.data))))
                    p=1
                p*=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return p**(1/(len(self.data)))
                else:
                    return round(p**(1/(len(self.data))),round_digit)
            else:
                product=1
                for x in lis:
                    product*=x
                if round_digit==None:
                    return p**(1/(len(self.data)))*product
                else:
                    return round(p**(1/(len(self.data)))*product,round_digit)
                
         elif weighted.lower()=="none" or weighted.lower()=="n":
            p=1
            lis=[]
            for i in range(0,len(self.data)):
                if p>10000000000:
                    lis.append(p**(1/(len(self.data))))
                    p=1
                p*=self.data[i]
            if len(lis)==0:
                if round_digit==None:
                    return p**(1/(len(self.data)))
                else:
                    return round(p**(1/(len(self.data))),round_digit)
            else:
                product=1
                for x in lis:
                    product*=x
                if round_digit==None:
                    return p**(1/(len(self.data)))*product
                else:
                    return round(p**(1/(len(self.data)))*product,round_digit)
                
         elif weighted.lower()=="right" or weighted.lower()=="r":
            p=1
            lis=[]
            for i in range(0,len(self.data)):
                if p>10000000000:
                    lis.append(p**(1/((len(self.data)*(len(self.data)+1)/2))))
                    p=1
                p*=(self.data[i]*(i+1))
            if len(lis)==0:
                if round_digit==None:
                    return p**(1/((len(self.data)*(len(self.data)+1)/2)))
                else:
                    return round(p**(1/((len(self.data)*(len(self.data)+1)/2))),round_digit)
            else:
                product=1
                for x in lis:
                    product*=x
                if round_digit==None:
                    return p**(1/((len(self.data)*(len(self.data)+1)/2)))*product
                else:
                    return round(p**(1/((len(self.data)*(len(self.data)+1)/2)))*product,round_digit)
                
         elif weighted.lower()=='left' or weighted.lower()=='l':
            p=1
            lis=[]
            for i in range(0,len(self.data)):
                if p>10000000000:
                    lis.append(p**(1/((len(self.data)*(len(self.data)+1)/2))))
                    p=1
                p*=(self.data[i]*(len(self.data)-i))
            if len(lis)==0:
                if round_digit==None:
                    return p**(1/((len(self.data)*(len(self.data)+1)/2)))
                else:
                    return round(p**(1/((len(self.data)*(len(self.data)+1)/2))),round_digit)
            else:
                product=1
                for x in lis:
                    product*=x
                if round_digit==None:
                    return p**(1/((len(self.data)*(len(self.data)+1)/2)))*product
                else:
                    return round(p**(1/((len(self.data)*(len(self.data)+1)/2)))*product,round_digit)

         elif weighted.lower()=='center' or weighted.lower()=='mid' or weighted.lower()=='middle' or weighted.lower()=='c' or weighted.lower()=='m' :
            if self.even(len(self.data))==False:
                p=1
                lis=[]
                for i in range(0,len(self.data)):
                    if p>10000000000:
                        lis.append(p**(1/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))))
                        p=1
                    if (i+1)>((len(self.data)+1)/2):
                        p*=self.data[i]*((len(self.data))-(i))
                    else:
                        p*=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return p**(1/(((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))))
                    else:
                        return round(p**(1/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))),round_digit)
                else:
                    product=1
                    for x in lis:
                        product*=x
                    if round_digit==None:
                        return (p**(1/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2)))*product)
                    else:
                        return round((p**(1/((((len(self.data)-1)/2))*(((len(self.data)-1)/2)+1)+((len(self.data)+1)/2))))*product,round_digit)
            else:
                p=1
                lis=[]
                for i in range(0,len(self.data)):
                    if p>10000000000:
                        lis.append(p**(1/(((((len(self.data)/2))*((len(self.data)/2)+1))))))
                        p=1
                    if (i+1)>((len(self.data))/2):
                        p*=self.data[i]*((len(self.data))-(i))
                    else:
                        p*=self.data[i]*(i+1)
                if len(lis)==0:
                    if round_digit==None:
                        return p**(1/(((((len(self.data)/2))*((len(self.data)/2)+1)))))
                    else:
                        return round(p**(1/(((((len(self.data)/2))*((len(self.data)/2)+1))))),round_digit)
                else:
                    product=1
                    for x in lis:
                        product*=x
                    if round_digit==None:
                        return (p**(1/(((((len(self.data)/2))*((len(self.data)/2)+1)))))*product)
                    else:
                        return round((p**(1/((((len(self.data)/2))*((len(self.data)/2)+1)))))*product,round_digit)
                    
    def harmonic_mean(self):
        s=0
        for i in self.data:
            s+=(1/i)
        return len(self.data)/s

    def hm(self):
        s=0
        for i in self.data:
            s+=(1/i)
        return len(self.data)/s
    
    def root_mean_square(self):
        s=0
        for i in self.data:
            s+=(i**2)
        return (s/len(self.data))**0.5

    def rms(self):
        s=0
        for i in self.data:
            s+=(i**2)
        return (s/len(self.data))**0.5       
    
    def max_value_index(self):
        m=self.max()
        ind=[]
        for i in self.data:
            if i==m:
                ind.append(i)
        return ind

    def min_value_index(self):
        m=self.min()
        ind=[]
        for i in self.data:
            if i==m:
                ind.append(i)
        return ind
    
    def global_maxima_index(self):
        m=self.max()
        ind=[]
        for i in self.data:
            if i==m:
                ind.append(i)
        return ind

    def global_minima_index(self):
        m=self.min()
        ind=[]
        for i in self.data:
            if i==m:
                ind.append(i)
        return ind
    
    def max_slope(self,magnitude=False):
        '''if magnitude is set to False then it returns the max slope...
           if magnitude is set to True then it returns max slope magnitude wise
           diff1 is the list containing slope of self.data elements
        '''
        if magnitude==False:
            diff1=[]
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            return int(max(diff1))
        else:
            diff1=[]
            for i in range(1,len(self.data)):
                diff1.append(abs(self.data[i]-self.data[i-1]))
            return int(max(diff1))

    def min_slope(self,magnitude=False):
        '''if magnitude is set to False then it returns the min slope...
           if magnitude is set to True then it returns min slope magnitude wise
           diff1 is the list containing slope of self.data elements
        '''
        if magnitude==False:
            diff1=[]
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            return int(min(diff1))
        else:
            diff1=[]
            for i in range(1,len(self.data)):
                diff1.append(abs(self.data[i]-self.data[i-1]))
            return int(min(diff1))

    def frequency_above_average(self):
        avg=self.average()
        count=0
        for i in self.data:
            if i>avg:
                count+=1
        return count/len(self.data)
    
    def frequency_below_average(self):
        avg=self.average()
        count=0
        for i in self.data:
            if i<avg:
                count+=1
        return count/len(self.data)

    def frequency_average(self):
        avg=self.average()
        count=0
        for i in self.data:
            if i==avg:
                count+=1
        return count/len(self.data)
    
    def frequency_maxima(self,weighted=None):
        ''' it returns the probability of a point being on the local maxima
        
        '''
        if weighted==None:
            diff1=[]
            count=0
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(0,len(diff1)):
                if i!=(len(diff1)-1):
                    if diff1[i]>0 and diff1[i+1]<0:
                        count+=1
            return count/len(diff1)
        elif weighted.lower()=="none":
            diff1=[]
            count=0
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(0,len(diff1)):
                if i!=(len(diff1)-1):
                    if diff1[i]>0 and diff1[i+1]<0:
                        count+=1
            return count/len(diff1)
        elif weighted.lower()=="right":
            diff1=[]
            count=0
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(0,len(diff1)):
                if i!=(len(diff1)-1):
                    if diff1[i]>0 and diff1[i+1]<0:
                        count+=1*(i+1)
            return count/((len(diff1))*(len(diff1)+1)/2)
        elif weighted.lower()=='left':
            diff1=[]
            count=0
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(0,len(diff1)):
                if i!=(len(diff1)-1):
                    if diff1[i]>0 and diff1[i+1]<0:
                        count+=1*(len(diff1)-i)
            return count/((len(diff1))*(len(diff1)+1)/2)
        elif weighted.lower()=='center' or weighted.lower()=='mid' or weighted.lower()=='middle':
            if self.even(len(self.data))==True:
                diff1=[]
                count=0
                for i in range(1,len(self.data)):
                    diff1.append(self.data[i]-self.data[i-1])
                for i in range(0,len(diff1)):
                    if i!=(len(diff1)-1):
                        if (i+1)>((len(diff1)+1)/2):
                            if diff1[i]>0 and diff1[i+1]<0:
                                count+=1*((len(diff1))-(i))
                        else:
                            if diff1[i]>0 and diff1[i+1]<0:
                                count+=1*(i+1)
                return (count/((((len(diff1)-1)/2))*(((len(diff1)-1)/2)+1)+((len(diff1)+1)/2)))
            else:
                diff1=[]
                count=0
                for i in range(1,len(self.data)):
                    diff1.append(self.data[i]-self.data[i-1])
                for i in range(0,len(diff1)):
                    if i!=(len(diff1)-1):
                        if (i+1)>((len(diff1))/2):
                            if diff1[i]>0 and diff1[i+1]<0:
                                count+=1*((len(diff1))-(i))
                        else:
                            if diff1[i]>0 and diff1[i+1]<0:
                                count+=1*(i+1)
                return (count/(((len(diff1)/2))*((len(diff1)/2)+1)))

    def frequency_minima(self,weighted=None):
        if weighted==None:
            diff1=[]
            count=0
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(0,len(diff1)):
                if i!=(len(diff1)-1):
                    if diff1[i]<0 and diff1[i+1]>0:
                        count+=1
            return count/len(diff1)
        elif weighted.lower()=="none":
            diff1=[]
            count=0
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(0,len(diff1)):
                if i!=(len(diff1)-1):
                    if diff1[i]<0 and diff1[i+1]>0:
                        count+=1
            return count/len(diff1)
        elif weighted.lower()=="right":
            diff1=[]
            count=0
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(0,len(diff1)):
                if i!=(len(diff1)-1):
                    if diff1[i]<0 and diff1[i+1]>0:
                        count+=1*(i+1)
            return count/((len(diff1))*(len(diff1)+1)/2)
        elif weighted.lower()=='left':
            diff1=[]
            count=0
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(0,len(diff1)):
                if i!=(len(diff1)-1):
                    if diff1[i]<0 and diff1[i+1]>0:
                        count+=1*(len(diff1)-i)
            return count/((len(diff1))*(len(diff1)+1)/2)
        elif weighted.lower()=='center' or weighted.lower()=='mid' or weighted.lower()=='middle':
            if self.even(len(self.data))==True:
                diff1=[]
                count=0
                for i in range(1,len(self.data)):
                    diff1.append(self.data[i]-self.data[i-1])
                for i in range(0,len(diff1)):
                    if i!=(len(diff1)-1):
                        if (i+1)>((len(diff1)+1)/2):
                            if diff1[i]<0 and diff1[i+1]>0:
                                count+=1*((len(diff1))-(i))
                        else:
                            if diff1[i]<0 and diff1[i+1]>0:
                                count+=1*(i+1)
                return (count/((((len(diff1)-1)/2))*(((len(diff1)-1)/2)+1)+((len(diff1)+1)/2)))
            else:
                diff1=[]
                count=0
                for i in range(1,len(self.data)):
                    diff1.append(self.data[i]-self.data[i-1])
                for i in range(0,len(diff1)):
                    if i!=(len(diff1)-1):
                        if (i+1)>((len(diff1))/2):
                            if diff1[i]<0 and diff1[i+1]>0:
                                count+=1*((len(diff1))-(i))
                        else:
                            if diff1[i]<0 and diff1[i+1]>0:
                                count+=1*(i+1)
                return (count/(((len(diff1)/2))*((len(diff1)/2)+1)))

    def index_of_local_maxima(self):
        diff1=[]
        ind=[]
        for i in range(1,len(self.data)):
            diff1.append(self.data[i]-self.data[i-1])
        for i in range(0,len(diff1)):
            if i!=(len(diff1)-1):
                if diff1[i]>0 and diff1[i+1]<0:
                    ind.append(i+1)
        return ind
    
    def index_of_local_minima(self):
        diff1=[]
        ind=[]
        for i in range(1,len(self.data)):
            diff1.append(self.data[i]-self.data[i-1])
        for i in range(0,len(diff1)):
            if i!=(len(diff1)-1):
                if diff1[i]<0 and diff1[i+1]>0:
                    ind.append(i+1)
        return ind

    def index_of_elements_in_interval(self,start,stop):
        ind=[]
        for i in range(0,len(self.data)):
            if self.data[i]>=start and self.data[i]<stop:
                ind.append(i)
        return ind
        
    def frequency_of_interval(self,start,stop):
        count=0
        for i in self.data:
            if i>=start and i<stop:
                count+=1
        return count/len(self.data)

    def mode_of_interval(self,step):
        minimum=self.min()
        maximum=self.max()
        l={}
        x=[]
        num=1
        t=True
        while t==True:
            lower=minimum+(num-1)*step
            upper=minimum+(num)*step
            if upper>=maximum:
                t=False
            l[self.frequency_of_interval(lower,upper)]=lower
            x.append(self.frequency_of_interval(lower,upper))
            num+=1
        lis={}
        maximum=max(x)
        for i in l:
            if i==maximum:
                lis[l[i]]=(l[i]+step)
        return lis

    def point_of_inflection(self,approx=False,round_digit=2):
        if approx==False:
            diff1=[]
            diff2=[]
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(1,len(diff1)):
                diff2.append(diff1[i]-diff1[i-1])
            ind=[]
            for i in range(0,len(diff2)):
                if diff2[i]==0:
                    ind.append(i)
            return ind
        elif approx==True:
            diff1=[]
            diff2=[]
            for i in range(1,len(self.data)):
                diff1.append(self.data[i]-self.data[i-1])
            for i in range(1,len(diff1)):
                diff2.append(diff1[i]-diff1[i-1])
            ind1=[]
            ind=[]
            for i in range(0,len(diff2)):
                ind1.append((diff2[i])/(max(diff2)))
            for i in range(0,len(ind1)):
                if round(ind1[i],round_digit)==0:
                    ind.append(i)
            return ind
            
    def plot(self,xlab='',ylab='',title='Data Analysis'):
        y=self.data
        x=[]
        for i in range(0,len(self.data)):
            x.append(i)
        plt.plot(x, y, label = "yesh")
        plt.legend()
        plt.show()

x=(np.arange(-1.0, 1.0, 0.001)).tolist()
l=[]
for i in x:
    l.append(i**3)
x=Data_Analysis(l)
print(x.point_of_inflection(True))
y=x.point_of_inflection(True)
for i in y:
    print(l[i])
print("--------------------")
df_bitcoin = pd.read_csv("Data\\bch.csv")
ok=df_bitcoin['PriceUSD']
c1234=pd.DataFrame(ok)
c123=ok.head(10)
c123=pd.DataFrame(c123)
check1=ok.head(6)
check2=pd.DataFrame(check1)
check=check2.tail(1)
c1=np.array(check)
c=c1.tolist()
xyz=Data_Analysis(c1234)
print(xyz.data)    
print(xyz.diff(10000))
print(xyz.diff(2))
print(xyz.diff(3))
print(xyz.diff(4))
print('.,')
print(xyz.am())
print(xyz.am('left'))
print(xyz.am('right'))
print(xyz.am('center'))
print(xyz.gm())
print(xyz.gm('left'))
print(xyz.gm('right'))
print(xyz.gm('center'))
print('.,')
hmm=ok.head(5)
x = np.array(hmm)
omkay = x.tolist()
l=[]
for i in omkay:
    l.append(int(i))
diff1=[]
diff2=[]
diff3=[]
diff4=[]
for i in range(1,len(l)):
    diff1.append(l[i]-l[i-1])
for i in range(1,len(diff1)):
    diff2.append(diff1[i]-diff1[i-1])
for i in range(1,len(diff2)):
    diff3.append(diff2[i]-diff2[i-1])
for i in range(1,len(diff3)):
    diff4.append(diff3[i]-diff3[i-1])
x=l[len(l)-1]+diff1[len(diff1)-1]+diff2[len(diff2)-1]+diff3[len(diff3)-1]
if diff4[0]>0:
    if x<0:
        x=x*-1
elif diff4[0]<0:
    if x>0:
        x=x*-1
if diff4[0]>x:
    y=x*(diff4[0]//x)
else:
    y=x*(diff4[0]//x)
diff4.append(y)
e3=diff3[len(diff3)-1]+y
diff3.append(e3)
e2=diff2[len(diff2)-1]+e3
diff2.append(e2)
e1=diff1[len(diff1)-1]+e2
diff1.append(e1)
e0=l[len(l)-1]+e1
l.append(e0)
print("Expected value "+str(e0))
print("Original value "+str(c[0]))
    














def date_conv(q):
    if q==None:
        return None
    q=q.strip()
    q=q.replace("of","")
    
    try:
        x=''
        x2=''
        x3=''
        x4=''
        if 'rd' in q:
            x=q.replace('rd','',1)
        elif 'st' in q:
            x=q.replace('st','',1)
        elif 'nd' in q:
            x=q.replace('nd','',1)
        elif 'th' in q:
            x=q.replace('th','',1)
        else:
            x=q
        if ',' in x:
            x2=x.replace(',','')
        else:
            x2=x
    
        if 'rd' in x2:
            x3=x2.replace('rd','',1)
        elif 'st' in x2:
            x3=x2.replace('st','',1)
        elif 'nd' in x2:
            x3=x2.replace('nd','',1)
        elif 'th' in x2:
            x3=x2.replace('th','',1)
        else:
            x3=x2
        if 'augu' in x3:
            x4=x3.replace('augu','aug')
        else:
            x4=x3

        l=x4.split(' ')
        for i in l:
            if i=='':
                l.remove(i)
            else:
                l=l
        d={'january':'01','february':'02','march':'03','april':'04','may':'05','june':'06','july':'07','august':'08','september':'09','october':'10','november':'11','december':'12','jan':'01','feb':'02','mar':'03','apr':'04','jun':'06','jul':'07','aug':'08','sept':'09','oct':'10','nov':'11','dec':'12','augu':'08'}      
        l2=[]
        e=''
        for i in l:
            if i in d:
                l2.append(d[i])
            else:
                l2.append(i)
        for i in l2:
            if len(l2[1])==1:
                l2[1]="0"+str(l2[1])
            if len(l2[0])==1:
                l2[0]="0"+str(l2[0])
            e=str(l2[2])+'-'+str(l2[1])+'-'+str(l2[0])
        return e.strip()
    except:
        q=q.replace(' ','')
        try:
            o = datetime.datetime.strptime(q, '%d/%m/%Y')
            x=q.split("/")
            if len(x[0])==1:
                x[0]="0"+str(x[0])
            if len(x[1])==1:
                x[1]="0"+str(x[1])    
            e=str(x[2])+'-'+str(x[1])+'-'+str(x[0])
            return e.strip()
        except:
            try:
                o=datetime.datetime.strptime(q, '%Y/%m/%d')
                x=q.split("/")
                if len(x[0])==1:
                    x[0]="0"+str(x[0])
                if len(x[1])==1:
                    x[1]="0"+str(x[1])    
                e=str(x[0])+'-'+str(x[1])+'-'+str(x[2])
                return e.strip()
            except:
                try:
                    o=datetime.datetime.strptime(q, '%d-%m-%y')
                    x=q.split("-")
                    if len(x[0])==1:
                        x[0]="0"+str(x[0])
                    if len(x[1])==1:
                        x[1]="0"+str(x[1])    
                    e=str(x[2])+'-'+str(x[1])+'-'+str(x[0])
                    return e.strip()
                except:
                    try:
                        o=datetime.datetime.strptime(q, '%Y-%m-%d')
                        x=q.split("-")
                        if len(x[0])==1:
                            x[0]="0"+str(x[0])
                        if len(x[1])==1:
                            x[1]="0"+str(x[1])    
                        e=str(x[0])+'-'+str(x[1])+'-'+str(x[2])
                        return e.strip()
                    except:
                        return q.strip()

def new_cases(country_name,date1=None,date2=None,operation='mean'):
    date1=date_conv(date1)
    date2=date_conv(date2)
    if operation=='mean':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["New_cases"].mean(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["New_cases"].mean(),2)
                else:
                    return round(select_row2["New_cases"].mean(),2)
                
    elif operation=='median':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["New_cases"].median(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["New_cases"].mecian(),2)
                else:
                    return round(select_row2["New_cases"].median(),2)
                
    elif operation=='mode':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["New_cases"].mode(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["New_cases"].mode(),2)
                else:
                    return round(select_row2["New_cases"].mode(),2)
                
                
def cumulative_cases(country_name,date1=None,date2=None,operation='mean'):
    date1=date_conv(date1)
    date2=date_conv(date2)
    if operation=='mean':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["Cumulative_cases"].mean(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["Cumulative_cases"].mean(),2)
                else:
                    return round(select_row2["Cumulative_cases"].mean(),2)
                
    elif operation=='median':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["Cumulative_cases"].median(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["Cumulative_cases"].mecian(),2)
                else:
                    return round(select_row2["Cumulative_cases"].median(),2)
                
    elif operation=='mode':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["Cumulative_cases"].mode(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["Cumulative_cases"].mode(),2)
                else:
                    return round(select_row2["Cumulative_cases"].mode(),2)
                
def new_deaths(country_name,date1=None,date2=None,operation='mean'):
    date1=date_conv(date1)
    date2=date_conv(date2)
    if operation=='mean':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["New_deaths"].mean(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["New_deaths"].mean(),2)
                else:
                    return round(select_row2["New_deaths"].mean(),2)
                
    elif operation=='median':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["New_deaths"].median(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["New_deaths"].mecian(),2)
                else:
                    return round(select_row2["New_deaths"].median(),2)
                
    elif operation=='mode':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["New_deaths"].mode(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["New_deaths"].mode(),2)
                else:
                    return round(select_row2["New_deaths"].mode(),2)
                

def cumulative_deaths(country_name,date1=None,date2=None,operation='mean'):
    date1=date_conv(date1)
    date2=date_conv(date2)
    if operation=='mean':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["Cumulative_deaths"].mean(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["Cumulative_deaths"].mean(),2)
                else:
                    return round(select_row2["Cumulative_deaths"].mean(),2)
                
    elif operation=='median':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["Cumulative_deaths"].median(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["Cumulative_deaths"].mecian(),2)
                else:
                    return round(select_row2["Cumulative_deaths"].median(),2)
                
    elif operation=='mode':
        s=""
        country_name=country_name.strip()
        r=country_name.split(" ")
        for i in range(0,len(r)):
            if i==0:
                s+=r[i].capitalize()
            else:
                s+=" "+r[i].capitalize()
        s=s.strip()
        country_name=s
        if date1==None and date2==None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                return round(select_row1["Cumulative_deaths"].mode(),2)
        elif date1!=None and date2!=None:
            select_row1=df_cov.loc[df_cov['Country']== country_name]
            if select_row1.empty:
                return "Error 904! No such country found"
            else:
                select_row1['date']=pd.to_datetime(select_row1['Date_reported'])
                mask=(select_row1['Date_reported'] >= date1) & (select_row1['Date_reported'] <= date2)
                select_row2=select_row1.loc[mask]
                if select_row2.empty:
                    mask=(select_row1['Date_reported'] >= date2) & (select_row1['Date_reported'] <= date1)
                    select_row2=select_row1.loc[mask]
                    if select_row2.empty:
                       return "Error 905! No such date in database"
                    else:
                        return round(select_row2["Cumulative_deaths"].mode(),2)
                else:
                    return round(select_row2["Cumulative_deaths"].mode(),2)
                

def country_record(country_name,date,new_cases=True,cumulative_cases=True,new_deaths=True,cumulative_deaths=True):
    date=date_conv(date)
    s=""
    country_name=country_name.strip()
    r=country_name.split(" ")
    for i in range(0,len(r)):
        if i==0:
            s+=r[i].capitalize()
        else:
            s+=" "+r[i].capitalize()
    s=s.strip()
    country_name=s
    select_row1=df_cov.loc[df_cov['Country']== country_name]
    string=""
    if select_row1.empty:
        return "Error 901! No such country found"
    else:
        select_row2=select_row1.loc[select_row1['Date_reported'] == date]
        if select_row2.empty:
            return "Error 902! No such date in database"
        else:
            string+="Country: "+country_name.capitalize()
            string+="\nDate: "+date
            if new_cases==True:
                var=select_row2['New_cases'].to_string()
                var1=var.split("    ")
                string+="\nNew Cases: "+var1[1]
            if cumulative_cases==True:
                var=select_row2['Cumulative_cases'].to_string()
                var1=var.split("    ")
                string+="\nCumulative Cases: "+var1[1]
            if new_deaths==True:
                var=select_row2['New_deaths'].to_string()
                var1=var.split("    ")
                string+="\nNew Deaths: "+var1[1]
            if cumulative_deaths==True:
                var=select_row2['Cumulative_deaths'].to_string()
                var1=var.split("    ")
                string+="\nCumulative Deaths: "+var1[1]

            return string

def plot(country_name):
    s=""
    country_name=country_name.strip()
    r=country_name.split(" ")
    for i in range(0,len(r)):
        if i==0:
            s+=r[0].capitalize()
        else:
            s+=" "+r[i].capitalize()
    s=s.strip()
    country_name=s
    select_row=df_cov.loc[df_cov['Country']== country_name]
    x=[]
    y=[]
    if select_row.empty:
        return "Error 903! No such country found"
    else:
        d = select_row['Date_reported']
        a = [datetime.datetime.strptime(abc, '%Y-%m-%d') for abc in d]
        x1 = matplotlib.dates.date2num(a)
        y1 = select_row['New_cases']
        y2 = select_row['New_deaths']
        y3 = select_row['Cumulative_cases']
        y4 = select_row['Cumulative_deaths']
        fig, ax = plt.subplots(2,2, figsize=(12,5))
        fig.set_facecolor("white")
        ax[0,0].plot(x1,y1, label="New Cases", color='purple')
        ax[0,0].set(title='New Cases')
        ax[0,0].xaxis.set_major_locator(mdates.WeekdayLocator(interval=13))
        ax[0,0].xaxis.set_major_formatter(DateFormatter("%d/%m/%y"))

        ax[0,1].plot(x1, y2, label = "New Deaths", color='red')
        ax[0,1].set(title="New Deaths")
        ax[0,1].xaxis.set_major_locator(mdates.WeekdayLocator(interval=13))
        ax[0,1].xaxis.set_major_formatter(DateFormatter("%d/%m/%y"))
        
        ax[1,0].plot(x1,y3, label="Cumulative Cases", color='black')
        ax[1,0].set(title="Cumulative Cases")
        ax[1,0].xaxis.set_major_locator(mdates.WeekdayLocator(interval=13))
        ax[1,0].xaxis.set_major_formatter(DateFormatter("%d/%m/%y"))
        
        ax[1,1].plot(x1, y4, label = "Cumulative Deaths", color='blue')
        ax[1,1].set(title="Cumulative Deaths")
        ax[1,1].xaxis.set_major_locator(mdates.WeekdayLocator(interval=13))
        ax[1,1].xaxis.set_major_formatter(DateFormatter("%d/%m/%y"))
        
        fig.suptitle(country_name+"'s Corona Report", fontsize=26,color='orange')
        fig.legend(ax,labels=['New Cases', 'New Deaths','Cumulative Cases', 'Cumulative Deaths'],borderaxespad=0.3)
        fig.subplots_adjust(top=0.85,left=0.85)
        fig.tight_layout(pad=0.5)
        fig.show()
        
df_cov = pd.read_csv("Data\Covid 19.csv")
df_rain = pd.read_csv("Data\Rainfall 1901-2015.csv")
#print(new_cases('Sri Lanka',None,None,'mean'))       
#print(country_record('Sri Lanka','5 may 2021'))
#plot('india')

















