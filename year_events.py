import wikipedia as wiki
res=wiki.page('Salman Khan') # 1915 ki jagah user ka diya hua year OBVIOUSLY
remove=res.summary
total=res.content
if remove in total:
    total=total.replace(remove,'')
else:
    total=total
birth=None
death=None
nobel=None
ref=None
book=None
events=[]
births=[]
deaths=[]
refrences=[]
nobels=[]
books=[]
l=total.split(' ')
for i in range(len(l)):
    if l[i]=='Births' or l[i]=='births':
        birth=i
    elif l[i]=='Deaths' or l[i]=='deaths':
        death=i
    elif (l[i]=='Nobel' and l[i+1]=='Prizes') or (l[i]=='nobel' and l[i+1]=='prizes'):
        nobel=i
    elif l[i]=='References' or l[i]=='references':
        ref=i
    elif l[i]=='Primary' and l[i+1]=='sources' and l[i+2]=='and' and l[i+3]=='year' and l[i+4]=='books':
        book=i
    else:
        continue
if birth != None:
    for i in range(0,birth-3):
        events.append(l[i])
else:
    'error'
if birth != None and death != None:
    for i in range(birth-3, death-3):
        births.append(l[i])
else:
    'no imp births'
if death != None and nobel != None:
    for i in range(death-3, nobel-3):
        deaths.append(l[i])
else:
    'no imp deaths'
if death != None and ref != None and nobel==None:
    for i in range(death-3, ref-3):
        deaths.append(l[i])
else:
    'no imp deaths'
if nobel != None and ref != None:
    for i in range(nobel-3, ref-3):
        nobels.append(l[i])
else:
    'no nobel prizes'
if ref != None and book!=None:
    for i in range(ref-3, book-3):
        refrences.append(l[i])
else:
    'no ref'
if ref != None and book==None:
    for i in range(ref-3, len(l)):
        refrences.append(l[i])
else:
    'no ref'
if book!=None:
    for i in range(book-1,len(l)):
        books.append(l[i])
    books[0]='\n\n\n==='
else:
    'no source books'
e=''
b=''
d=''
n=''
r=''
s=remove
o=''
if events!=[]:
    for i in events:
        e+=i+' '
else:
    'no events'
if births!=[]:
    for i in births:
        b+=i+' '
else:
    'no imp births'
if deaths!=[]:
    for i in deaths:
        d+=i+' '
else:
    'no deaths'
if nobels!=[]:
    for i in nobels:
        n+=i+' '
else:
    'no nobel'
if refrences!=[]:
    for i in refrences:
        r+=i+' '
else:
    'no ref'
if books!=[]:
    for i in books:
        o+=i+' '
else:
    'no ref books'

print(s+e+o)
# e naam ki string events ki h waise b wali births ki d wali deaths ki n wali nobel prizes ki r wali references ki o wali primary sources aur books ki aur s wali summary ki
# code ko bas conclude karde kaam done h iska phir


















        
