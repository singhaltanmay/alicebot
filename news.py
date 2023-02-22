from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk
def news(q):
    n=nltk.download('punkt')
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config=Config()
    config.browser_user_agent=user_agent
    l=q.split(' ')
    for i in l:
        if i=='language':
            l.remove(i)
        elif i=='something':
            l.remove(i)
        elif i=='something':
            l.remove(i)
        elif i=='tell':
            l.remove(i)
        elif i=='me':
            l.remove(i)
        else:
            continue
    z=None
    a=None
    b=None
    for i in range(len(l)):
        if l[i]=='news':
            z=i
        elif l[i]=='in':
            a=i
        elif l[i]=='about':
            b=i
        else:
            continue
    search=''
    if b!=None:
        search=l[b+1]
    else:
        search=''

    langu=''
    if a!=None:
        langu=l[a+1]
        if langu=='Hindi' or langu=='hindi':
            langu='hi'
        elif langu=='English' or langu=='english':
            langu='en'
        else:
            return 'Error 501! Unsupported Language'
    elif a==None:
        langu='en'
    else:
        return 'Error 504! Unexpected error occured'
    gn=GoogleNews(langu,'d')
    if search != '':
        gn.search(search)
    elif search=='':
        gn.search('india')
    else:
        return 'Error 503! Incorrect grammar used'
    for i in range(1,3):
        gn.getpage(i)
        r=gn.result()
        df=pd.DataFrame(r)
    l2=[]
    for i in df.index:
        d={}
        a=Article(df['link'][i])
        a.download()
        a.parse()
        a.nlp()
        d['date']=df['date'][i]
        d['title']=a.title
        d['summary']=a.summary
        l2.append(d)
    l4=[]
    for i in range(len(l2)):
        l4.append(l2[i]['title'])
    string=''
    for i in range(0,len(l4)):
        string+=str(i+1)+") "+l4[i]+"\n"
    return string
