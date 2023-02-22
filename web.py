import os
import webbrowser

curdir=os.path.dirname(os.path.abspath(__file__))

def search(q):
    l2=q.split(' ')
    if 'for' in l2:
        l2.remove('for')
    else:
        l2=l2
    if 'me' in l2:
        l2.remove('me')
    else:
        l2=l2    
    if 'that' in l2:
        l2.remove('that')
    else:
        l2=l2
    if 'about' in l2:
        l2.remove('about')
    else:
        l2=l2
    if 'of' in l2:
        l2.remove('of')
    else:
        l2=l2
    if 'on' in l2:
        l2.remove('on')
    else:
        l2=l2
    if 'google' in l2:
        l2.remove('google')
    else:
        l2=l2
    if 'yahoo' in l2:
        l2.remove('yahoo')
    else:
        l2=l2    
    if 'bing' in l2:
        l2.remove('bing')
    else:
        l2=l2
    if 'wikipedia' in l2:
        l2.remove('wikipedia')
    else:
        l2=l2
    if 'duckduckgo' in l2:
        l2.remove('duckduckgo')
    else:
        l2=l2
    l=[]
    c=0
    e=''
    for i in range(len(l2)):
        if l2[i]=='search':
            c=i
        else:
            l2=l2
    for i in range(c+1,len(l2)):
        l.append(l2[i])
    for i in l:
        e+=i+'+'
    if 'google' in q:
        z="https://www.google.com/search?q="+e+"&rlz=1C1CHBF_enIN913IN913&oq=test&aqs=chrome.1.69i59l3j0i67l4j69i60.2647j0j7&sourceid=chrome&ie=UTF-8"
    elif 'wikipedia' in q:
        z="https://en.wikipedia.org/w/index.php?search="+e+"&title=Special%3ASearch&go=Go&ns0=1"
    elif 'bing' in  q:
        z="https://www.bing.com/search?q="+e+"&form=QBLH&sp=-1&pq=test+test&sc=8-9&qs=n&sk=&cvid=6C32A09223124F0A929B34609DE78B8F"
    elif 'yahoo' in q:
        z="https://in.search.yahoo.com/search;_ylt=AwrPiBRnNVRg3GwAGQm6HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZAN3QmVLRGdGbFFmdWpOeEFlWmxsVzlBBG5fcnNsdAMwBG5fc3VnZwMwBG9yaWdpbgNpbi5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMxMARxdWVyeQN0ZXN0JTIwdGVzdDIEdF9zdG1wAzE2MTYxMzE0MzU-?p="+e+"&fr=sfp&iscqry=&fr2=sb-top-search"
    elif 'duckduckgo' in q:
        z="https://duckduckgo.com/?q="+e+"&t=hy&va=g&ia=web"
    else:
        z="https://www.google.com/search?q="+e+"&rlz=1C1CHBF_enIN913IN913&oq=test&aqs=chrome.1.69i59l3j0i67l4j69i60.2647j0j7&sourceid=chrome&ie=UTF-8"
    try:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(z)
        return "Searching Google for '"+str(z)+"'"
    except:
        return "Error 606! Can't get Google Chrome's location"

