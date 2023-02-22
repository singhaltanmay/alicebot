import subprocess
import os
import webbrowser
import random
import sys

curdir=os.path.dirname(os.path.abspath(__file__))


def web_open(short_link):
    short_link=short_link.lower()
    try:
        try:
            f=open(curdir+"\\Data\\browse.txt")
            ijkl=f.readlines()
            f.close()
        except:
            return "Error 102! The browse.txt file is corrupted"
        
        x=[]
        for i in ijkl:
            if i.strip()!="":
                x.append(i.strip())
        l=x
        xyz=True
        if xyz==True:
            firstline=l[0]
            secondline=l[1]
            firstline=firstline.strip()
            secondline=secondline.strip()
            f2=''
            d={}
            for i in l:
                f2+=i
            l2=f2.split('\\\\')
            for i in l2:
                if i=='':
                    l2.remove(i)
                else:
                    continue

            for i in range(len(l2)-1):
                if i%2==0:
                    d[l2[i]]=l2[i+1]
                else:
                    d=d
            if short_link in d:
                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(d[short_link])
                return "Done"
            else:
                return ""
        else:
            return "Cancel"
    except:
        return "Error 106! An unknown error occured"



def del_web(name):
    name=name.lower()
    try:
        try:
            f=open(curdir+"\\Data\\browse.txt")
            l=f.readlines()
            f.close()
        except:
            return "Error 102! The browse.txt file is corrupted"

        secondline=l[1]
        firstline=l[0]
        firstline=firstline.strip()
        secondline=secondline.strip()
        xyz=True
        if xyz==True:
            l2=firstline.split('\\\\')
            for i in l2:
                if i=='':
                    l2.remove(i)
                else:
                    continue
            abc=[]
            index1=None
            for i in range(len(l2)):
                if l2[i]==name and i%2==0:
                    index1=i
            if index1!=None:
                for i in range(len(l2)):
                    if i==index1 or i==(index1+1):
                        pass
                    else:
                        if i==(len(l2)-1):
                            abc+=l2[i]
                        else:
                            abc+=l2[i]+"\\\\\\\\"
                firstline=abc
            else:
                for i in range(len(l2)):
                    if i==(len(l2)-1):
                        abc+=l2[i]
                    else:
                        abc+=l2[i]+"\\\\\\\\"
                firstline=abc
            string=""
            for i in firstline:
                string+=i
            try:
                f=open(curdir+"\\Data\\browse.txt","w+")
                f.write(string+"\n"+secondline)
                f.close()
                return "Changes made to browse.txt successfully!"
            except:
                return "Error 103! Cannot save changes to browse.txt"
    except:
        return "Error 106! An unknown error occured"
            
def edit_web(new,link,old=""):
    new=new.lower()
    link=link.lower()
    old=old.lower()
    try:
        try:
            f=open(curdir+"\\Data\\browse.txt")
            l=f.readlines()
            f.close()
        except:
            return "Error 102! The browse.txt file is corrupted"
        secondline=l[1]
        firstline=l[0]
        firstline=firstline.strip()
        secondline=secondline.strip()
        xyz=True
        if xyz==True:            
            f2=''
            d={}
            for i in firstline:
                f2+=i
            l2=f2.split("\\\\")
            for i in l2:
                if i=='':
                    l2.remove(i)
                else:
                    continue
            
            f.close()
            for i in range(len(l2)-1):
                if i%2==0:
                    d[l2[i]]=l2[i+1]
                else:
                    d=d
            d2={}
            fl=''
            for i in d:
                fl+=i+'\\\\\\\\'+d[i]+'\\\\\\\\'
            l2=[]
            for i in d:
                l2.append(i)
            if old in l2 and new!='':
                d2[new]=d[old]
            elif old not in l2 and new=='':
                d2[old]=link
            elif old=='' and new!='':
                d2[new]=link
            else:
                return "Error No 105! Cannot save changes to browse.txt"
            e=''
    
            for i in d2:
                e+=i+"\\\\\\\\"+d2[i]+"\\\\\\\\"
            f=fl+e
            firstline=f
            try:
                f=open(curdir+"\\Data\\browse.txt","w+")
                f.write(firstline+"\n"+secondline)
                f.close()
                return "Changes made to browse.txt successfully!"
            except:
                return "Error No 103! Cannot save changes to browse.txt"
    except:
        return "Error No 106! An unknown error occured"    

def open_pro(pro):
    pro=pro.lower()
    try:
        try:
            f=open(curdir+"\\Data\\browse.txt")
            ijkl=f.readlines()
            f.close()
        except:
            return "Error No 102! The browse.txt file is corrupted"
        x=[]
        for i in ijkl:
            if i.strip()!="":
               x.append(i.strip())
        l=x
        xyz=True
        if xyz==True:
            firstline=l[0]
            secondline=l[1]
            firstline=firstline.strip()
            secondline=secondline.strip()
            f2=''
            d={}
            for i in secondline:
                f2+=i
            l2=f2.split('\\\\')
            for i in l2:
                if i=='':
                    l2.remove(i)
                else:
                    continue
            f.close()
            for i in range(len(l2)-1):
                if i%2==0:
                    d[l2[i]]=l2[i+1]
                else:
                    d=d
            if pro in d:
                subprocess.Popen(d[pro])
                return "Done"
            else:
                return ""
        else:
            return "Cancel"
    except:
        return "Error No 106! An unknown error occured"

    
def edit_pro(new,loc,old=""):
    new=new.lower()
    loc=loc.lower()
    old=old.lower()
    try:
        try:
            f=open(curdir+"\\Data\\browse.txt")
            l=f.readlines()
            f.close()
        except:
            return "Error 102! The browse.txt file is corrupted"
        secondline=l[1]
        firstline=l[0]
        firstline=firstline.strip()
        secondline=secondline.strip()
        xyz=True
        if xyz==True:
            f2=''
            d={}
            for i in secondline:
                f2+=i
            l2=f2.split("\\\\")
            for i in l2:
                if i=='':
                    l2.remove(i)
                else:
                    continue
            f.close()
            for i in range(len(l2)-1):
                if i%2==0:
                    d[l2[i]]=l2[i+1]
                else:
                    d=d
            d2={}
            sl=''
            for i in d:
                sl+=i+"\\\\\\\\"+d[i]+"\\\\\\\\"
            l2=[]
            for i in d:
                l2.append(i)
            if old in l2 and new!='':
                d2[new]=d[old]
            elif old not in l2 and new=='':
                d2[old]=loc
            elif old=='' and new!='':
                d2[new]=loc
            else:
                return "Error No 105! Cannot save changes to browse.txt"
            
            e=''
            for i in d2:
                e+=i+"\\\\\\\\"+d2[i]+"\\\\\\\\"
            f=sl+e
            secondline=f
            try:
                f=open(curdir+"\\Data\\browse.txt","w+")
                f.write(firstline+"\n"+secondline)
                f.close()
                return "Changes made to browse.txt successfully!"
            except:
                return "Error No 103! Cannot save changes to browse.txt"
    except:
        return "Error No 106! An unknown error occured"
    
def del_pro(name):
    name=name.lower()
    try:
        try:
            f=open(curdir+"\\Data\\browse.txt")
            l=f.readlines()
            f.close()
        except:
            return "Error 102! The browse.txt file is corrupted"
        secondline=l[1]
        firstline=l[0]
        firstline=firstline.strip()
        secondline=secondline.strip()
        xyz=True
        if xyz==True:
            l2=secondline.split('\\\\')
            for i in l2:
                if i=='':
                    l2.remove(i)
                else:
                    continue
            abc=[]
            index1=None
            for i in range(len(l2)):
                if l2[i]==name and i%2==0:
                    index1=i
            if index1!=None:
                for i in range(len(l2)):
                    if i==index1 or i==(index1+1):
                        pass
                    else:
                        if i==(len(l2)-1):
                            abc+=l2[i]
                        else:
                            abc+=l2[i]+"\\\\\\\\"
                secondline=abc
            else:
                for i in range(len(l2)):
                    if i==(len(l2)-1):
                        abc+=l2[i]
                    else:
                        abc+=l2[i]+"\\\\\\\\"
                secondline=abc
            string=""
            for i in secondline:
                string+=i
            
            try:
                f=open(curdir+"\\Data\\browse.txt","w+")
                f.write(firstline+"\n"+string)
                f.close()
                return "Changes made to browse.txt successfully!"
            except:
                return "Error No 103! Cannot save changes to browse.txt"
    except:
        return "Error No 106! An unknown error occured"
    

def init(string):
    string=string.replace("ok","")
    string=string.replace("alice","")
    string=string.replace("open","")
    string=string.strip()
    if "program" in string or "programs" in string or "app" in string or "application" in string or "applications" in string:
        a=open_pro(string)
        if a!="Done" and a!="Cancel" and "Error" not in a:
            string1=string
            string1=string1.replace("program","")
            string1=string1.replace("programs","")
            string1=string1.replace("app","")
            string1=string1.replace("application","")
            string1=string1.replace("applications","")
            string1=string1.replace("  "," ")
            string1=string1.strip()
            b=open_pro(string1)
            if b!="Done" and b!="Cancel" and "Error" not in b:
                string2=string
                string2=string2.replace("the","")
                string2=string2.replace("  "," ")
                string2=string2.strip()
                c=open_pro(string2)
                if c!="Done" and c!="Cancel" and "Error" not in c:
                    string3=string
                    string3=string3.replace("program","")
                    string3=string3.replace("programs","")
                    string3=string3.replace("app","")
                    string3=string3.replace("application","")
                    string3=string3.replace("applications","")
                    string3=string3.strip()
                    string3=string3.replace("the","")
                    string3=string3.replace("  "," ")
                    string3=string3.strip()
                    d=open_pro(string3)
                    if d!="Done" and d!="Cancel" and "Error" not in d:
                        return "Error No 101! No such application exists"

                    elif d!="Cancel" and "Error" not in d:
                        return "Opening "+string3+" ......"
                elif c!="Cancel" and "Error" not in c:
                    return "Opening "+string2+" ......"
            elif b!="Cancel" and "Error" not in b:
                return "Opening "+string1+" ......"
        elif a!="Cancel" and "Error" not in a:
            return "Opening "+string+" ......"

            
    elif "link" in string or "links" in string or "webpage" in string or "webpages" in string or "web" in string or "site" in string or "chrome" in string or "url" in string:
        a=web_open(string)
        if a!="Done" and a!="Cancel" and "Error" not in a:
            string1=string
            string1=string1.replace("link","")
            string1=string1.replace("links","")
            string1=string1.replace("webpage","")
            string1=string1.replace("webpages","")
            string1=string1.replace("web","")
            string1=string1.replace("site","")
            string1=string1.replace("chrome","")
            string1=string1.replace("url","")
            string1=string1.replace("  "," ")
            string1=string1.strip()
            b=web_open(string1)
            if b!="Done" and b!="Cancel" and "Error" not in b:
                string2=string
                string2=string2.replace("the","")
                string2=string1.replace("  "," ")
                string2=string2.strip()
                c=web_open(string2)
                if c!="Done" and c!="Cancel" and "Error" not in c:
                    string3=string
                    string3=string3.replace("link","")
                    string3=string3.replace("links","")
                    string3=string3.replace("webpage","")
                    string3=string3.replace("webpages","")
                    string3=string3.replace("web","")
                    string3=string3.replace("site","")
                    string3=string3.replace("chrome","")
                    string3=string3.replace("url","")
                    string3=string3.strip()
                    string3=string3.replace("the","")
                    string3=string3.replace("  "," ")
                    string3=string3.strip()
                    d=web_open(string3)
                    if d!="Done" and d!="Cancel" and "Error" not in d:
                        return "Error No 101! No such site exists"
                    elif d!="Cancel" and "Error" not in d:
                        return "Opening "+string3+" ......"
                elif c!="Cancel" and "Error" not in c:
                    return "Opening "+string2+" ......"
            elif b!="Cancel" and "Error" not in b:
                return "Opening "+string1+" ......"
        elif a!="Cancel" and "Error" not in a:
            return "Opening "+string+" ......"
    else:
        string=string.replace("ok","")
        string=string.replace("alice","")
        string=string.replace("open","")
        string=string.strip()
        a=open_pro(string)
        if a!="Done" and a!="Cancel" and "Error" not in a:
            b=web_open(string)
            if b!="Done" and b!="Cancel" and "Error" not in b:
                return "Error No 101! No such application or link exists"
            elif b!="Cancel" and "Error" not in b:
                return "Opening "+string+" ......"
        elif a!="Cancel" and "Error" not in a:
            return "Opening "+string+" ......"
