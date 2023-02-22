import random

no=['1','2','3','4','5','6','7','8','9','0']
comb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '|', '/', '~', '{', '}', '[', ']', ';', ':', ',', '.', '?', ' ', '\\', "'", '"', '<', '>','’']
value={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52, '`': 53, '!': 54, '@': 55, '#': 56, '$': 57, '%': 58, '^': 61, '&': 60, '*': 62, '(': 63, ')': 64, '-': 65, '_': 66, '+': 67, '=': 68, '|': 69, '/': 70, '~': 71, '{': 72, '}': 73, '[': 74, ']': 75, ';': 76, ':': 77, ',': 78, '.': 79, '?': 80, ' ': 81,"\\":82,"'":83,'"':84,"<":85,">":86,'1':87,'2':88,'3':89,'4':90,'5':91,'6':92,'7':93,'8':94,'9':95,'0':96,'’':97}


def get(string,to_get):
    l=[]
    if to_get=="no1":
        return int(string[0])
    elif to_get=="comb1":
        return string[1]
    elif to_get=="comb2":
        return string[2]
    elif to_get=="comb3":
        return string[3]
    elif to_get=="comb4":
        return string[4]
    elif to_get=="comb5":
        return string[5]
    elif to_get=="comb6":
        return string[6]
    elif to_get=="comb7":
        return string[7]
    elif to_get=="comb8":
        return string[8]
    elif to_get=="no2":
        return int(string[9])
    else:
        return None

def hcf(x, y):
    sys.setrecursionlimit(1500)
    if x > y:
        smaller = y
    else:
        smaller = x
    try:
        for i in range(1, smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i 
        return hcf
    except RecursionError:
        return "Cannot encode the program"

def generate_key():
    global no
    global comb
    global value
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,82)
    d=random.randint(0,82)
    e=random.randint(0,82)
    h=random.randint(0,82)
    i=random.randint(0,82)
    j=random.randint(0,82)
    '''calculating middle two letter'''
    f=random.randint(0,79)
    sum=value[no[a]]+value[no[b]]+value[comb[c]]+value[comb[d]]+value[comb[e]]+value[comb[h]]+value[comb[i]]+value[comb[j]]
    inter_variable_x=int(sum/8)-value[comb[f]]
    if inter_variable_x<0:
        inter_variable_x=int(inter_variable_x)
        inter_variable_x*=(-1)
    else:
        inter_variable_x=int(inter_variable_x)
    g=inter_variable_x
    ''''x=decryption_key'''
    x=str(no[a])+str(comb[c])+str(comb[d])+str(comb[e])+str(comb[f])+str(comb[g])+str(comb[h])+str(comb[i])+str(comb[j])+str(no[b])
    return x
    
    
def valid_key(string):
    global no
    global comb
    global value
    count=1
    for i in string:
        if count==1:
            no1=i
        elif count==2:
            comb1=i
        elif count==3:
            comb2=i
        elif count==4:
            comb3=i
        elif count==5:
            comb4=i
        elif count==6:
            comb5=i
        elif count==7:
            comb6=i
        elif count==8:
            comb7=i
        elif count==9:
            comb8=i
        elif count==10:
            no2=i
        count+=1

    if (no1 in no and no2 in no) and (comb1 in comb and comb2 in comb and comb3 in comb and comb4 in comb and comb5 in comb and comb6 in comb and comb7 in comb and comb8 in comb):
        if ((value[comb4]+value[comb5]))==int((value[no1]+value[no2]+value[comb1]+value[comb2]+value[comb3]+value[comb6]+value[comb7]+value[comb8])/8)+1 or ((value[comb4]))+1==int((value[no1]+value[no2]+value[comb1]+value[comb2]+value[comb3]+value[comb6]+value[comb7]+value[comb8])/8)+value[comb5]:
            return True
        else:
            return False
    else:
        return False

def invalid_index(lis):
    l=[]
    list1=["<","<","<"]
    list2=[">",">",">"]
    list3=["N","U","L","L"]
    for i in range(0,len(lis)):
        try:
            if len(lis)>=i+7:
                if lis[i]=="a":
                    if lis[i+1]=="x":
                        if lis[i+2]=="0":
                            if lis[i+4]=="b":
                                if lis[i+5]=="x":
                                    if lis[i+6]=="0":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)
                if lis[i]=="b":
                    if lis[i+1]=="x":
                        if lis[i+2]=="9":
                            if lis[i+4]=="d":
                                if lis[i+5]=="x":
                                    if lis[i+6]=="9":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)
                if lis[i]=="x":
                    if lis[i+1]=="d":
                        if lis[i+2]=="b":
                            if lis[i+4]=="d":
                                if lis[i+5]=="c":
                                    if lis[i+6]=="e":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)
                if lis[i]=="1":
                    if lis[i+1]=="x":
                        if lis[i+2]=="1":
                            if lis[i+4]=="0":
                                if lis[i+5]=="x":
                                    if lis[i+6]=="a":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)
                if lis[i]=="7":
                    if lis[i+1]=="8":
                        if lis[i+2]=="9":
                            if lis[i+4]=="d":
                                if lis[i+5]=="x":
                                    if lis[i+6]=="1":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)
                if lis[i]=="1":
                    if lis[i+1]=="1":
                        if lis[i+2]=="x":
                            if lis[i+4]=="0":
                                if lis[i+5]=="x":
                                    if lis[i+6]=="7":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)
                if lis[i]=="0":
                    if lis[i+1]=="d":
                        if lis[i+2]=="5":
                            if lis[i+4]=="a":
                                if lis[i+5]=="7":
                                    if lis[i+6]=="7":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)
                if lis[i]=="c":
                    if lis[i+1]=="c":
                        if lis[i+2]=="x":
                            if lis[i+4]=="e":
                                if lis[i+5]=="4":
                                    if lis[i+6]=="5":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)            
                if lis[i]=="x":
                    if lis[i+1]=="1":
                        if lis[i+2]=="0":
                            if lis[i+4]=="2":
                                if lis[i+5]=="1":
                                    if lis[i+6]=="9":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)
                
                if lis[i]=="x":
                    if lis[i+1]=="a":
                        if lis[i+2]=="4":
                            if lis[i+4]=="b":
                                if lis[i+5]=="5":
                                    if lis[i+6]=="c":
                                        l.append(i)
                                        l.append(i+1)
                                        l.append(i+2)
                                        l.append(i+3)
                                        l.append(i+4)
                                        l.append(i+5)
                                        l.append(i+6)


        except Exception as ex:
            print("Error! The Details of the error are following: "+ex)
    return l
                    
def encode(string,no1,comb1,comb2,comb3,comb4,comb5,comb6,comb7,comb8,no2,pb=True):
    global no
    global comb
    global value
    if string.strip()=="":
        return ""
    a=string.split(" ")
    encoded=""
    count_no=0
    for item in a:
        count_no+=1
        if pb==True:
            x=count_no/(len(a)+10)*100
            x=int(x)
            if x<=5:
                x=0
            elif x<=10:
                x=10
            elif x<=15:
                x=10
            elif x<=20:
                x=20
            elif x<=25:
                x=20
            elif x<=30:
                x=30
            elif x<=35:
                x=30
            elif x<=40:
                x=40
            elif x<=45:
                x=40
            elif x<=50:
                x=50
            elif x<=55:
                x=50
            elif x<=60:
                x=60
            elif x<=65:
                x=60
            elif x<=70:
                x=70
            elif x<=75:
                x=70
            elif x<=80:
                x=80
            elif x<=85:
                x=80
            elif x<=90:
                x=90
            elif x<=95:
                x=90
            elif x<=100:
                x=100
            x=x/10
            x=int(x)
            text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no)/(len(a)+10)*100))+"%"+" "
            print(text,end="\r",flush=True)
            f=open(curdir+"\\result\\progress.alice","w+")
            f.write(str(int((count_no)/(len(a)+10)*100)))
            f.close()
        encoded+="<<<NULL"
        abc={}
        if int(no1)+int(no2)==0:
            ijk={}
            ijk=value
        else:
            for inter_variable_1 in range(0,int(no1)+int(no2)):
                x=value[comb1]+value[comb8]
                for i in value:
                    abc[i]=(value[i]+x)
                y=value[comb2]*value[comb7]
                de={}
                for i in abc:
                    de[i]=(abc[i]*y)
                z=hcf((value[comb1]+value[comb8]+value[comb2]+value[comb7]),(value[comb3]*value[comb6]))
                fgh={}
                for i in de:
                    fgh[i]=(de[i]+z)
                ijk={}
                for i in fgh:
                    ijk[i]=hex(fgh[i])
        for i in item:
            encoded+=""+str(ijk[i])+"GFH"
        encoded+="NULL>>>"
    if "ax0" in string or "bx0" in string or "bx9" in string or "dx9" in string or "xdb" in string or "dce" in string or "1x1" in string or "0xa" in string or "789" in string or "dx1" in string or "11x" in string or "0x7" in string or "0d5" in string or "a77" in string or "ccx" in string or "e45" in string or "x10" in string or "219" in string or "xa4" in string or "b5c" in string:
        return "Cannot encode the program"
        
    d=[]
    d=list(encoded)
    encoded=""
    no001=random.randint(1,len(d))
    while (no001-1) in invalid_index(d):
        no1=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no001-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="ax0"+str(no1)+"bx0"
        else:
            encoded+=d[i]
    if pb==True:
        x=(count_no+1)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+1)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+1)/(count_no+10)*100))))
        f.close()

    d=[]
    d=list(encoded)
    encoded=""
    no002=random.randint(1,len(d))
    while (no002-1) in invalid_index(d):
        no002=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no002-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="bx9"+str(no2)+"dx9"
        else:
            encoded+=d[i]
    if pb==True:
        x=(count_no+2)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+2)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+2)/(count_no+10)*100))))
        f.close()

    d=[]
    d=list(encoded)
    encoded=""
    no003=random.randint(1,len(d))
    while (no003-1) in invalid_index(d):
        no003=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no003-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="xdb"+str(comb1)+"dce"
        else:
            encoded+=d[i]

    if pb==True:
        x=(count_no+3)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+3)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+3)/(count_no+10)*100))))
        f.close()

    
    d=[]
    d=list(encoded)
    encoded=""
    no004=random.randint(1,len(d))
    while (no004-1) in invalid_index(d):
        no004=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no004-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="1x1"+str(comb2)+"0xa"
        else:
            encoded+=d[i]

    if pb==True:
        x=(count_no+4)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+4)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+4)/(count_no+10)*100))))
        f.close()

    
    d=[]
    d=list(encoded)
    encoded=""
    no005=random.randint(1,len(d))
    while (no005-1) in invalid_index(d):
        no005=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no005-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="789"+str(comb3)+"dx1"
        else:
            encoded+=d[i]

    if pb==True:
        x=(count_no+5)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+5)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+5)/(count_no+10)*100))))
        f.close()

    
    d=[]
    d=list(encoded)
    encoded=""
    no006=random.randint(1,len(d))
    while (no006-1) in invalid_index(d):
        no006=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no006-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="11x"+str(comb4)+"0x7"
        else:
            encoded+=d[i]

    if pb==True:
        x=(count_no+6)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+6)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+6)/(count_no+10)*100))))
        f.close()

    
    d=[]
    d=list(encoded)
    encoded=""
    no007=random.randint(1,len(d))
    while (no007-1) in invalid_index(d):
        no007=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no007-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="0d5"+str(comb5)+"a77"
        else:
            encoded+=d[i]

    if pb==True:
        x=(count_no+7)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+7)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+7)/(count_no+10)*100))))
        f.close()

    
    d=[]
    d=list(encoded)
    encoded=""
    no008=random.randint(1,len(d))
    while (no008-1) in invalid_index(d):
        no008=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no008-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="ccx"+str(comb6)+"e45"
        else:
            encoded+=d[i]

    if pb==True:
        x=(count_no+8)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+8)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+8)/(count_no+10)*100))))
        f.close()

    
    d=[]
    d=list(encoded)
    encoded=""
    no009=random.randint(1,len(d))
    while (no009-1) in invalid_index(d):
        no009=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no009-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="x10"+str(comb7)+"219"
        else:
            encoded+=d[i]

    if pb==True:
        x=(count_no+9)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+9)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+9)/(count_no+10)*100))))
        f.close()

    
    d=[]
    d=list(encoded)
    encoded=""
    no0010=random.randint(1,len(d))
    while (no0010-1) in invalid_index(d):
        no0010=random.randint(1,len(d))
    for i in range(0,len(d)):
        if i==(no0010-1) and i not in invalid_index(d):
            encoded+=d[i]
            encoded+="xa4"+str(comb8)+"b5c"
        else:
            encoded+=d[i]

    if pb==True:
        x=(count_no+10)/(count_no+10)*100
        x=int(x)
        if x<=5:
            x=0
        elif x<=10:
            x=10
        elif x<=15:
            x=10
        elif x<=20:
            x=20
        elif x<=25:
            x=20
        elif x<=30:
            x=30
        elif x<=35:
            x=30
        elif x<=40:
            x=40
        elif x<=45:
            x=40
        elif x<=50:
            x=50
        elif x<=55:
            x=50
        elif x<=60:
            x=60
        elif x<=65:
            x=60
        elif x<=70:
            x=70
        elif x<=75:
            x=70
        elif x<=80:
            x=80
        elif x<=85:
            x=80
        elif x<=90:
            x=90
        elif x<=95:
            x=90
        elif x<=100:
            x=100
        x=x/10
        x=int(x)
        text=">>>Saving"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int((count_no+10)/(count_no+10)*100))+"%"+" "
        print(text,end="\r",flush=True)
        f=open(curdir+"\\result\\progress.alice","w+")
        f.write(str((int((count_no+10)/(count_no+10)*100))))
        f.close()


    if ("ax0" in encoded) and ("bx0" in encoded) and ("bx9" in encoded) and ("dx9" in encoded) and ("xdb" in encoded) and ("dce" in encoded) and ("1x1" in encoded) and ("0xa" in encoded) and ("789" in encoded) and ("dx1" in encoded) and ("11x" in encoded) and ("0x7" in encoded) and ("0d5" in encoded) and ("a77" in encoded) and ("ccx" in encoded) and ("e45" in encoded) and ("x10" in encoded) and ("219" in encoded) and ("xa4" in encoded) and ("b5c" in encoded):
        return encoded
    else:
        return "Cannot encode the program"
        


    
def decode(string,pb=True):
    if string.strip()=="":
        return ""
    global no
    global comb
    global value
    if ("ax0" in string) and ("bx0" in string) and ("bx9" in string) and ("dx9" in string) and ("xdb" in string) and ("dce" in string) and ("1x1" in string) and ("0xa" in string) and ("789" in string) and ("dx1" in string) and ("11x" in string) and ("0x7" in string) and ("0d5" in string) and ("a77" in string) and ("ccx" in string) and ("e45" in string) and ("x10" in string) and ("219" in string) and ("xa4" in string) and ("b5c" in string):
        '''here now getting the keys'''
        n1=string.split("ax0")
        t=False
        for i in range(1,len(n1)):
            if ((n1[i])[1]+(n1[i])[2]+(n1[i])[3])=="bx0":
                t=True
                no1=str((n1[i])[0])
        if t==False:
            return "The program is wrongly encoded"
        string=string.replace("ax0"+no1+"bx0","")
        n3=string.split("bx9")
        t=False
        for i in range(1,len(n3)):
            if ((n3[i])[1]+(n3[i])[2]+(n3[i])[3])=="dx9":
                t=True
                no2=str((n3[i])[0])
        if t==False:
            return "The program is wrongly encoded"
        string=string.replace("bx9"+no2+"dx9","")
        n5=string.split("xdb")
        t=False
        for i in range(1,len(n5)):
            if ((n5[i])[1]+(n5[i])[2]+(n5[i])[3])=="dce":
                t=True
                comb1=str((n5[i])[0])
        if t==False:
            return "The program is wrongly encoded"

        string=string.replace("xdb"+comb1+"dce","")
        n7=string.split("1x1")
        t=False
        for i in range(1,len(n7)):
            if ((n7[i])[1]+(n7[i])[2]+(n7[i])[3])=="0xa":
                t=True
                comb2=str((n7[i])[0])
        if t==False:
            return "The program is wrongly encoded"
        string=string.replace("1x1"+comb2+"0xa","")
        n9=string.split("789")
        t=False
        for i in range(1,len(n9)):
            if ((n9[i])[1]+(n9[i])[2]+(n9[i])[3])=="dx1":
                t=True
                comb3=str((n9[i])[0])
        if t==False:
            return "The program is wrongly encoded"
        string=string.replace("789"+comb3+"dx1","")
        n11=string.split("11x")
        t=False
        for i in range(1,len(n11)):
            if ((n11[i])[1]+(n11[i])[2]+(n11[i])[3])=="0x7":
                t=True
                comb4=str((n11[i])[0])
        if t==False:
            return "The program is wrongly encoded"
        string=string.replace("11x"+comb4+"0x7","")
        n13=string.split("0d5")
        t=False
        for i in range(1,len(n13)):
            if ((n13[i])[1]+(n13[i])[2]+(n13[i])[3])=="a77":
                t=True
                comb5=str((n13[i])[0])
        if t==False:
            return "The program is wrongly encoded"
        string=string.replace("0d5"+comb5+"a77","")
        n15=string.split("ccx")
        t=False
        for i in range(1,len(n15)):
            if ((n15[i])[1]+(n15[i])[2]+(n15[i])[3])=="e45":
                t=True
                comb6=str((n15[i])[0])
        if t==False:
            return "The program is wrongly encoded"
        string=string.replace("ccx"+comb6+"e45","")
        n17=string.split("x10")
        t=False
        for i in range(1,len(n17)):
            if ((n17[i])[1]+(n17[i])[2]+(n17[i])[3])=="219":
                t=True
                comb7=str((n17[i])[0])
        if t==False:
            return "The program is wrongly encoded"
        string=string.replace("x10"+comb7+"219","")
        n19=string.split("xa4")
        t=False
        for i in range(1,len(n19)):
            if ((n19[i])[1]+(n19[i])[2]+(n19[i])[3])=="b5c":
                t=True
                comb8=str((n19[i])[0])
        if t==False:
            return "The program is wrongly encoded"
        string=string.replace("xa4"+comb8+"b5c","")
        string=string.replace("NULL>>>","")
        list1=string.split("<<<NULL")
                
    else:
        return "The program is wrongly encoded"
    try:
        if valid_key(str(no1)+comb1+comb2+comb3+comb4+comb5+comb6+comb7+comb8+str(no2))==True:
            xyzabc=0
            decoded=""
            count_no=0
            for dist in list1:
                count_no+=1
                if pb==True:
                    x=count_no/len(list1)*100
                    x=int(x)
                    if x<=5:
                        x=0
                    elif x<=10:
                        x=10
                    elif x<=15:
                        x=10
                    elif x<=20:
                        x=20
                    elif x<=25:
                        x=20
                    elif x<=30:
                        x=30
                    elif x<=35:
                        x=30
                    elif x<=40:
                        x=40
                    elif x<=45:
                        x=40
                    elif x<=50:
                        x=50
                    elif x<=55:
                        x=50
                    elif x<=60:
                        x=60
                    elif x<=65:
                        x=60
                    elif x<=70:
                        x=70
                    elif x<=75:
                        x=70
                    elif x<=80:
                        x=80
                    elif x<=85:
                        x=80
                    elif x<=90:
                        x=90
                    elif x<=95:
                        x=90
                    elif x<=100:
                        x=100
                    x=x/10
                    x=int(x)
                    text=">>>Loading"+"|"+(x*"█")+(10-x)*" "+"|"+" "+str(int(count_no/len(list1)*100))+"%"
                    print(text,end="\r",flush=True)
                    f=open(curdir+"\\result\\progress.alice","w+")
                    f.write(str(int(count_no/len(list1)*100)))
                    f.close()
                if xyzabc!=0:
                    decoded+=" "
                xyzabc+=1
                letters=dist.split("GFH")
                for items in letters:
                    if int(no1)+int(no2)==0:
                        ijk={}
                        ijk=value
                    else:
                        abc={}
                        for inter_variable_1 in range(0,int(no1)+int(no2)):
                            x=value[comb1]+value[comb8]
                            for i in value:
                                abc[i]=(value[i]+x)
                            y=value[comb2]*value[comb7]
                            de={}
                            for i in abc:
                                de[i]=(abc[i]*y)
                            z=hcf((value[comb1]+value[comb8]+value[comb2]+value[comb7]),(value[comb3]*value[comb6]))
                            fgh={}
                            for i in de:
                                fgh[i]=(de[i]+z)
                            ijk={}
                            for i in fgh:
                                ijk[i]=hex(fgh[i])
                    
                    for x in ijk:
                        if ijk[x]==items:
                            decoded+=x
            decoded=decoded[1:]
            return decoded
        else:
            return "The program is wrongly encoded"
    except Exception as e:
        return "Error 104! An Unexpected error occured"
