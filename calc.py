import math
import os

curdir=os.path.dirname(os.path.abspath(__file__))
def get_index(lis,q):
    for i in range(len(lis)):
        if lis[i]==q:
            return i
        else:
            continue
def list_diff(l1,l2):                                                                                                                                                                   
    if len(l2)<len(l1):
        for i in range(len(l2)):
            if l2[i] in l1:
                l1.remove(l2[i])
            else:
                continue
        return l1
    elif len(l1)<len(l2):
        for i in range(len(l1)):
            if l1[i] in l2:
                l2.remove(l1[i])
            else:
                continue
        return l2
    else:
        for i in range(len(l1)):
            if l1[i] in l2:
                l2.remove(l1[i])
            else:
                continue
        return l2
def prime_number(n):
    upper_limit=int(n**0.5)
    for i in range(2,upper_limit+1):
        if n%i==0:
            return False
    return True

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return int(fact)

def factors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l

def basechange(number,to=2,now=10,format="Integer"):#do not specify any format basechange(number,to,now)
        format=format.lower()
        if now==10:
            string=""
            n=number**(1/to)
            n=n//1
            n=int(n)
            for i in range(n,-1,-1):
                x=number//(to**i)
                string=string+str(x)
                number=number-((to**i)*x)
            if format.lower()=="integer":
                return int(string)
            elif format.lower()=="string":
                return string
        else:
            nlist=[int(x) for x in str(number)]
            m=len(nlist)
            sum=0
            for i in range(0,m):
                sum=sum+(now**i)*nlist[m-i-1]
            string=""
            n=sum**(1/to)
            n=n//1
            n=int(n)
            for i in range(n,-1,-1):
                x=sum//(to**i)
                string=string+str(x)
                sum=sum-((to**i)*x)
            if format.lower()=="integer":
                return int(string)
            elif format.lower()=="string":
                return string

def sin(angle,system="d"):
    if system=="d":
        angle=angle*math.pi/180
    return math.sin(angle)

def cos(angle,system="d"):
    if system=="d":
        angle=angle*math.pi/180
    return math.cos(angle)

def tan(angle,system="d"):
    if system=="d":
        angle=angle*math.pi/180
    return math.tan(angle)

def cosec(angle,system="d"):
    if system=="d":
        angle=angle*math.pi/180
    return 1/(math.sin(angle))

def sec(angle,system="d"):
    if system=="d":
        angle=angle*math.pi/180
    return 1/(math.cos(angle))

def cot(angle,system="d"):
    if system=="d":
        angle=angle*math.pi/180
    return 1/(math.tan(angle))
def mod(exp):
    if '|' in exp:
        z=exp.replace('|','')
        return abs(float(z))
    else:
        return 'Error'

def gif(exp):
    if '[' in exp and ']' in exp:
        z=exp.replace(']','')
        z=z.replace('[','')
        return math.floor(float(z))
    else:
        return 'Error'

def frac(exp):
    if '{' in exp and '}' in exp:
        z=exp.replace('}','')
        z=z.replace('{','')
        return round((float(z)-math.floor(float(z))),3)
    else:
        return 'Error'
def evaluate(exp):
    final=exp
    l=list(exp)
    index_1=None
    index_2=None
    index_3=None
    index_4=None
    gi=[]
    fra=[]
    for i in range(len(l)):
        if l[i]=='[':
            index_1=i
        elif l[i]==']':
            index_2=i
        elif l[i]=='{':
            index_3=i
        elif l[i]=='}':
            index_4=i
    if index_1!=None and index_2!=None:
        for i in range(index_1,index_2+1):
            gi.append(l[i])
        e=''
        for i in gi:
            e+=i
        e=eval(e)
        e=str(e)
        g=gif(e)
        l[index_1]=str(g)
        for i in range(index_1+1,index_2+1):
            l[i]=''
        for i in l:
            if i=='':
                l.remove(i)
            else:
                continue
        final=''
        for i in l:
            final+=i
    else:
        exp=exp
    if index_3!=None and index_4!=None:
        for i in range(index_3,index_4+1):
            fra.append(l[i])
        e=''
        for i in fra:
            e+=i
        e=eval(e)
        e=str(e)
        f=frac(e)
        l[index_3]=str(f)
        for i in range(index_3+1,index_4+1):
            l[i]=''
        for i in l:
            if i=='':
                l.remove(i)
            else:
                continue
        final=''
        for i in l:
            final+=i
    else:
        exp=exp
        
    if int(eval(final))==eval(final):
        return int(eval(final))
    else:
        return eval(final)

def quadratic(a,b,c):
    #l=[number1,number2]
    l=[]
    x1=(-b+((b**2-4*a*c)**0.5))/(2*a)
    x2=(-b-((b**2-4*a*c)**0.5))/(2*a)
    l.append(x1)
    l.append(x2)
    return l

def cubic(a,b,c,d):
    l=[]
    p = (-b)/(3*a)
    q = p**3 + (b*c-3*a*d)/(6*a**2)
    r = c/(3*a)
    x1 = (q + (q**2 + (r-p**2)**3)**(1/2))**(1/3) + (q - (q**2 + (r-p**2)**3)**(1/2))**(1/3) + p
    l.append(x1)
    return l
def date_conv(date):
    d={'january':'1','february':'2','march':'3','april':'4','may':'5','june':'6','july':'7','august':'8','september':'9','october':'10','november':'11','december':'12','jan':'1','feb':'2','mar':'3','apr':'4','jun':'6','jul':'7','aug':'8','sept':'9','oct':'10','nov':'11','dec':'12'}      
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
        return "Error 302! The Entered Date does not exists"
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
            

def day_name(x,format="name"):
    if str(x.lower())=="help" or str(format.lower())=="help":
        a="day_name(date[dd/mm/yyyy],format(Default:Name))"
        b="Name:It returns Sunday, Monday, Tuesday etc"
        c="Number: It returns number 0 for Sunday and 1 for Monday and so on"
        return a+"\n"+b+"\n"+c
        
    a=days_between("01/01/0001",x)
    if a=="Error 302! The Entered Date does not exists":
        return "Error 302! The Entered Date does not exists"
    else:
        z=a%7
        if z==0:
            if format.lower()=="name":
                return "Monday"
            elif format.lower()=="number":
                return 1
        elif z==1:
            if format.lower()=="name":
                return "Tuesday"
            elif format.lower()=="number":
                return 2
            
        elif z==2:
            if format.lower()=="name":
                return "Wednesday"
            elif format.lower()=="number":
                return 3
            
        elif z==3:
            if format.lower()=="name":
                return "Thursday"
            elif format.lower()=="number":
                return 4
            
        elif z==4:
            if format.lower()=="name":
                return "Friday"
            elif format.lower()=="number":
                return 5
            
        elif z==5:
            if format.lower()=="name":
                return "Saturday"
            elif format.lower()=="number":
                return 6
            
        elif z==6:
            if format.lower()=="name":
                return "Sunday"
            elif format.lower()=="number":
                return 0
            

  
def remainder(q):
    try:
        l=q.split(' ')
        l2=[]
        l3=[]
        z=None
        for i in range(len(l)):
            if l[i]=='remainder':
                z=i
            else:
                l=l
        if z==None:
            l=l
        else:
            for i in range(z+2,len(l)):
                l2.append(l[i])
        l3.append(l2[0])
        l3.append(l2[len(l2)-1])
        l3[0]=int(l3[0])
        l3[1]=int(l3[1])
        f=''
        
        a=l3[0]%l3[1]
        a=str(a)
        f='when '+str(l3[0])+' is divided by '+str(l3[1])+' the remainder is '+a
        return f
    except:
        return "Error 303! Unexpected error occured"

def quotient(q):
    try:
        l=q.split(' ')
        l2=[]
        l3=[]
        z=None
        for i in range(len(l)):
            if l[i]=='quotient':
                z=i
            else:
                l=l
        if z==None:
            l=l
        else:
            for i in range(z+2,len(l)):
                l2.append(l[i])
        l3.append(l2[0])
        l3.append(l2[len(l2)-1])
        l3[0]=int(l3[0])
        l3[1]=int(l3[1])
        
        f=''
        a=l3[0]//l3[1]
        a=str(a)
        f='when '+str(l3[0])+' is divided by '+str(l3[1])+' the quotient is '+a
        return f
    except:
        return "Error 303! Unexpected error occured"
def remove(l4):
    for i in range(len(l4)):
        if l4[i]!='factorial' and l4[i]!='sin' and l4[i]!='cos' and l4[i]!='tan' and l4[i]!='sec' and l4[i]!='cosec' and l4[i]!='cot':
            l4=l4
        elif l4[i]=='factorial' in l4:
            
            l4[i]=''
            
            l4[i-1]=str(factorial(int(l4[i-1])))
            
            
        elif l4[i]=='sin':
            l4[i]=''
            
            l4[i+1]=str(sin(float(l4[i+1])))
            
            
            
        elif l4[i]=='cos':
            l4[i]=''
            
            l4[i+1]=str(cos(float(l4[i+1])))
            
        elif l4[i]=='tan':
            l4[i]=''
            
            l4[i+1]=str(tan(float(l4[i+1])))
            
        elif l4[i]=='sec':
            l4[i]=''
            
            l4[i+1]=str(sec(float(l4[i+1])))
            
        elif l4[i]=='cosec':
            l4[i]=''
            
            l4[i+1]=str(cosec(float(l4[i+1])))
            
        elif l4[i]=='cot':
            l4[i]=''
            
            l4[i+1]=str(cot(float(l4[i+1])))
            
        else:
            continue
    for i in l4:
        if i=='':
            l4.remove(i)
        else:
            continue
    return l4
def ans(q):
    if '!' in q:
        q=q.replace('!',' factorial ')
    else:
        q=q
    if 'sin' in q:
        q=q.replace('sin',' sin ')
    else:
        q=q
    if 'cos' in q:
        q=q.replace('cos',' cos ')
    else:
        q=q
    if 'tan' in q:
        q=q.replace('tan',' tan ')
    else:
        q=q
    if 'sec' in q:
        q=q.replace('sec',' sec ')
    else:
        q=q
    if 'cosec' in q:
        q=q.replace('cosec',' cosec ')
    else:
        q=q
    if 'cot' in q:
        q=q.replace('cot',' cot ')
    else:
        q=q
    if '+' in q:
        q=q.replace('+',' + ')
    else:
        q=q
    if '-' in q:
        q=q.replace('-',' - ')
    else:
        q=q
    if '*' in q:
        q=q.replace('*',' * ')
    else:
        q=q
    if '/' in q:
        q=q.replace('/',' / ')
    if '(' in q:
        q=q.replace('(',' ( ')
    if ')' in q:
        q=q.replace(')',' ) ')
    else:
        q=q
    if '^' in q:
        q=q.replace('^',' ** ')
    else:
        q=q
    if 'greatest integer function of' in q:
        q=q.replace('greatest integer function of','gifof')
    else:
        q=q
    if 'greatest integer function' in q:
        q=q.replace('greatest integer function','gifof')
    else:
        q=q
    if 'fractional part of' in q:
        q=q.replace('fractional part of','fracof')
    else:
        q=q
    if 'fractional part' in q:
        q=q.replace('fractional part','fracof')
    else:
        q=q
    l=q.split(' ')
    
    if '' in l:
        l.remove('')
    else:
        l=l
    for i in l:
        if i in 'what is will be the answer calculate when of a an ok alice value':
            l.remove(i)
        else:
            l=l
    for i in l:
        if i in 'what is will be the answer calculate when of a an ok alice value':
            l.remove(i)
        else:
            l=l
    for i in l:
        if i in 'what is will be the answer calculate when of a an ok alice value':
            l.remove(i)
        else:
            l=l
    for i in l:
        if i in 'multiply multiplied' and ('by' in l or 'to' in l or 'into' in l) and ('remainder' not in l and 'quotient' not in l):
            l.remove(i)
            for i in range(len(l)):
                if l[i]=='by' or l[i]=='to' or l[i]=='into':
                    l[i]='*'
                else:
                    l=l
        elif i in 'divide divided' and 'by' in l and ('remainder' not in l and 'quotient' not in l):
            l.remove(i)
            for i in range(len(l)):
                if l[i]=='by':
                    l[i]='/'
                else:
                    l=l
        elif i in 'add added' and ('to' in l or 'and' in l) and ('remainder' not in l and 'quotient' not in l):
            l.remove(i)
            for i in range(len(l)):
                if l[i]=='to' or l[i]=='and':
                    l[i]='+'
                else:
                    l=l
        elif i in 'subtract subtracted' and ('from' in l) and ('remainder' not in l and 'quotient' not in l):
            l.remove(i)
            for i in range(len(l)):
                if l[i]=='from':
                    l[i]='-'
                    l[i-1],l[i+1]=l[i+1],l[i-1]
                else:
                    l=l
        elif i in 'gifof':
            gif_index=get_index(l,'gifof')
            l[gif_index+1]=str('['+str(l[gif_index+1])+']')
            l.remove(i)
        elif i in 'fracof':
            frac_index=get_index(l,'fracof')
            l[frac_index+1]=str('{'+str(l[frac_index+1])+'}')
            l.remove(i)
            
        else:
            continue
    e=''
    
    while 'sin' in l or 'cos' in l or 'tan' in l or 'sec' in l or 'cosec' in l or 'factorial' in l:
        l=remove(l)
        
    
    if 'remainder' not in l and 'quotient' not in l:
        for i in l:
            e+=i
        
        z=evaluate(e)
        return round(z,2)
    
    else:
        e=e
    

    l2=[]
    
    for i in range(len(l)):
        if l[i]=='remainder' or l[i]=='quotient':
            a=i
        elif l[i]=='by':
            b=i
    for i in range(a+1,b-1):
        l2.append(l[i])
    for i in l2:
        if i in 'multiply multiplied' and ('by' in l2 or 'to' in l2 or 'into' in l2) and ('remainder' not in l2 and 'quotient' not in l2):
            l2.remove(i)
            for i in range(len(l2)):
                if l2[i]=='by' or l2[i]=='to' or l2[i]=='into':
                    l2[i]='*'
                else:
                    l2=l2
        elif i in 'divide divided' and 'by' in l2 and ('remainder' not in l2 and 'quotient' not in l2):
            l2.remove(i)
            for i in range(len(l2)):
                if l2[i]=='by':
                    l2[i]='/'
                else:
                    l2=l2
        elif i in 'add added' and ('to' in l2 or 'and' in l2) and ('remainder' not in l2 and 'quotient' not in l2):
            l2.remove(i)
            for i in range(len(l2)):
                if l2[i]=='to' or l2[i]=='and':
                    l2[i]='+'
                else:
                    l2=l2
        elif i in 'subtract subtracted' and ('from' in l2) and ('remainder' not in l2 and 'quotient' not in l2):
            l2.remove(i)
            for i in range(len(l2)):
                if l2[i]=='from':
                    l2[i]='-'
                    l2[i-1],l2[i+1]=l2[i+1],l2[i-1]
                else:
                    l2=l2
        else:
            continue    

    #print(l2)
    while 'sin' in l2 or 'cos' in l2 or 'tan' in l2 or 'sec' in l2 or 'cosec' in l2 or 'factorial' in l2:
        l2=remove(l2)
    #print(l2)
    for i in l2:
        e+=i
    z=evaluate(e)
    if l[a]=='remainder':
        z=z%(float(l[b+1]))
    elif l[a]=='quotient':
        z=z//(float(l[b+1]))
    return round(z,2)
    
def day_get(q0):
    q0=q0.replace('the','')
    q=''
    if 'it will be' in q0:
        q=q0.replace('it will be','')
    elif 'it was' in q0:
        q=q0.replace('it was','')
    elif 'will be' in q0:
        q=q0.replace('will be','')
    elif 'it is' in q0:
        q=q0.replace('it is','')
    else:
        q=q0
    a=None
    a0=''
    l0=q.split(' ')
    for i in range(len(l0)):
        if l0[i]=='day' or l0[i]=='Day':
            a=i
        else:
            a=a
    if a!=None:
        for i in range(a+1,len(l0)):
            a0=a0+l0[i]+' '   
    else:
        return 'Error 601! Expected "day" not found'
    if 'on' in a0:
        a0=a0
    else:
        a0='on '+a0

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

    l2=[]
    z=None
    for i in range(len(l)):
        if l[i]=='day' or l[i]=='Day':
            z=i
        else:
            z=z
    if z!=None:
        for i in range(z+1,len(l)):
            l2.append(l[i])
    else:
        return 'Error 601! Expected "day" not found'
    for i in l2:
        if i in 'on will was it is , be of':
            l2.remove(i)
        else:
            l2=l2
    #print(l2)
    da=''
    e=''
    if len(l2)!=1 and len(l2)==3:
        da=l2[0]+' '+l2[1]+' '+l2[2]
        e=date_conv(da)
    elif len(l2)==1:
        e=l2[0]
    else:
        return 'Error 602! Invalid grammar used'
    n=''
    f=''
    n=day_name(e)
    if 'was' in q0:
        f='It was '+n+' '+a0
    elif 'will' in q0:
        f='It will be '+n+' '+a0
    elif 'is' in q0:
        f='It is '+n+' '+a0
    else:
        f=n+' '+a0
    f1=f.replace("jan","Jan")
    f2=f1.replace("feb","Feb")
    f3=f2.replace("mar","Mar")
    f4=f3.replace("may","May")
    f5=f4.replace("june","June")
    f6=f5.replace("july","July")
    f7=f6.replace("aug","Aug")
    f8=f7.replace("sep","Sep")
    f9=f8.replace("oct","Oct")
    f10=f9.replace("nov","Nov")
    f11=f10.replace("dec","Dec")
    f12=f11.replace("april","April")
    f=f12
    return f

#print(ans('ok alice calculate greatest integer function 5.002'))
