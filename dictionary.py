from PyDictionary import PyDictionary
from nltk.corpus import wordnet
import pyttsx3, time 
from deep_translator import MyMemoryTranslator
from gtts import gTTS
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from mutagen.mp3 import MP3
def translate(tex,to,fro=""):
    try:
        if fro=="":
            translated = MyMemoryTranslator(source="auto", target=to).translate(text=tex)
        else:
            translated = MyMemoryTranslator(source=fro, target=to).translate(text=tex)
        return translated
    except:
        return "Error 714! Cannot Translate"

def pronounce(word,lib=1,speed=150):
    try:
        text = word
        tts = gTTS(text)
        tts.save("Sounds\sound.mp3")
        mixer.init()
        audio = MP3("Sounds\sound.mp3")
        mixer.music.load("Sounds\sound.mp3")
        mixer.music.play()
        time.sleep(int(audio.info.length))
        mixer.music.stop()
        return ''
    except:
        try:
            engine = pyttsx3.init()
            engine. setProperty("rate", speed)
            engine.say(word) 
            engine.runAndWait()
            return ''
        except:
            return "Error 715! Unknown Error Occurred"
        
def delete_element_of_a_list(list,element,number=None):
    if number==None:
        #getting default value of number
        number=list.count(element)

    
    newlist=[]
    numrem=1
    for i in list:
        if numrem<=number:
            if i!=element:
                newlist.append(i)
            else:
                numrem+=1
        else:
            newlist.append(i)

    return newlist

def wordnet_use(word):
    try:
        synset = wordnet.synsets(word)
        l = synset[0].examples()
        x=0
        string=""
        for i in l:
            x+=1
            if x==1:
                string+=str(x)+") "+i.capitalize()+". "
            else:
                string+="\n"+str(x)+") "+i.capitalize()+". "
        return ': '+string
    except:
        return "Error 705! No such word in the dictionary"
    
def wordnet_meaning(word):
    try:
        l=PyDictionary.meaning(word)
        string=""
        y=0
        for i in l:
            y+=1
            if y==1:
                string+=i+": "
            else:
                string+="\n"+i+": "
            x=0
            for k in l[i]:
                x+=1
                string+=str(x)+") "+k.capitalize()+". "
        return string
    except:
        try:
            synset = wordnet.synsets(word)
            l=synset[0].definition()
            string=l.capitalize()
            return ": "+string
        except:
            return "Error 702! No such word in the dictionary"

def wordnet_synonym(word):
    try:
        string=": "+word.capitalize()+", "
        synonym = []
        antonym = []
        for synset in wordnet.synsets(word): 
            for i in synset.lemmas(): 
                synonym.append(i.name())
        synonym=delete_element_of_a_list(synonym,word)
        res = []
        for i in synonym:
            if i not in res:
                res.append(i)
        for i in range(0,len(res)):
            string+=(str(synonym[i])).capitalize()+", "
        string=string[:-2]
        return string
  
    except:
        return "Error 703! No such word in the dictionary"

def wordnet_antonym(word):
    try:
        string = ": "
        antonym = [] 
  
        for synset in wordnet.synsets(word):
            for i in synset.lemmas(): 
                if i.antonyms():
                    antonym.append(i.antonyms()[0].name())
        res = []
        for i in antonym:
            if i not in res:
                res.append(i)
        for i in range(0,len(res)):
            string+=(str(antonym[i])).capitalize()+", "
        string=string[:-2]
        return string
  
    except:
        return "Error 704! No such word in the dictionary"
        
def dictionary(q):
    q=q.replace('ok','')
    q=q.replace('alice','')
    if 'pronounce' in q:
        q=q.replace('pronounce','')
    else:
        q=q
    if 'pronunciation' in q:
        q=q.replace('pronunciation','')
    else:
        q=q
    if 'translate' in q:
        q=q.replace('translate','')
    else:
        q=q
    if 'pronunciation,' in q:
        q=q.replace('pronunciation,','')
    else:
        q=q
    if 'translate,' in q:
        q=q.replace('translate,','')
    else:
        q=q
    if 'translation,' in q:
        q=q.replace('translation,','')
    else:
        q=q
    if 'translation' in q:
        q=q.replace('translation','')
    else:
        q=q
    if 'synonyms' in q:
        q=q.replace('synonyms','synonym')
    else:
        q=q
    if 'antonyms' in q:
        q=q.replace('antonyms','antonym')
    else:
        q=q
    if 'synonym,' in q:
        q=q.replace('synonym,','synonym')
    else:
        q=q
    if 'antonym,' in q:
        q=q.replace('antonym,','antonym')
    else:
        q=q
    if 'meaning,' in q:
        q=q.replace('meaning,','meaning')
    else:
        q=q
    q=q.strip()
    l=q.split(' ')
    l2=[]
    for i in l:
        if i in "what is the will be of word a tell me about any one to which give an and what's what also how to it in sentence its suggest dictionary as can you from ,":
            l2=l2
        else:
            if i not in l2:
                l2.append(i)
            else:
                continue
    #print(l2)
        
    f=''
    if len(l2)==2:
        if 'meaning' in l2 or 'explain' in l2 or 'explanation' in  l2:
            for i in l2:
                if i in 'meaning explain explanation':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Meaning of the word "'+l2[0]+'" is '+wordnet_meaning(l2[0])
            else:
                return 'Error 706! Overuse of words or word not found'
        elif 'synonym' in l2 or 'similar' in l2 or 'same' in l2:
            for i in l2:
                if i in 'synonym similar same':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                    f='Synonyms of the word "'+l2[0]+'" is '+wordnet_synonym(l2[0])
            else:
                return 'Error 706! Overuse of words or word not found'
        elif 'antonym' in l2 or 'opposite' in l2:
            for i in l2:
                if i in 'antonym opposite':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Antonyms of the word "'+l2[0]+'" is '+wordnet_antonym(l2[0])
            else:
                return 'Error 706! Overuse of words or word not found'
        elif 'use' in l2 or 'usage' in l2:
            for i in l2:
                if i in 'use usage':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Usage of the word "'+l2[0]+'" is '+wordnet_use(l2[0])
            else:
                return 'Error 706! Overuse of words or word not found'
        else:
            return 'Error 707! Unexpected format used'
    elif len(l2)==3:
        if ('synonym' in l2 or 'similar' in l2 or 'same' in l2) and ('antonym' in l2 or 'opposite' in l2):
            for i in l2:
                if i in 'antonym opposite synonym similar same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite synonym similar same':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Synonyms of the word "'+l2[0]+'" are '+wordnet_synonym(l2[0])+'\nAntonyms of the word "'+l2[0]+'" are '+wordnet_antonym(l2[0])
            else:
                return 'Error 708! Overuse of words or word not found'
        elif ('meaning' in l2 or 'explain' in l2 or 'explanation' in l2) and ('antonym' in l2 or 'opposite' in l2):
            l2.remove(i)
            for i in l2:
                if i in 'antonym opposite meaning explain explanation':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite meaning explain explanation':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Meaning of the word "'+l2[0]+'" is '+wordnet_meaning(l2[0])+'\nAntonyms of the word "'+l2[0]+'" are '+wordnet_antonym(l2[0])
            else:
                return 'Error 708! Overuse of words or word not found'
        elif ('synonym' in l2 or 'similar' in l2 or 'same' in l2) and ('meaning' in l2 or 'explain' in l2 or 'explanation' in l2):
            for i in l2:
                if i in 'synonym similar meaning explain explanation same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'synonym similar meaning explain explanation same':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Meaning of the word "'+l2[0]+'" is '+wordnet_meaning(l2[0])+'\nSynonyms of the word "'+l2[0]+'" are '+wordnet_synonym(l2[0])
            else:
                return 'Error 706! Overuse of words or word not found'
        elif ('synonym' in l2 or 'similar' in l2 or 'same' in l2) and ('use' in l2 or 'usage' in l2):
            for i in l2:
                if i in 'synonym similar use usage same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'synonym similar use usage same':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Synonymns of the word "'+l2[0]+'" are '+wordnet_synonym(l2[0])+'\nUsage of the word "'+l2[0]+'" is '+wordnet_use(l2[0])
            else:
                return 'Error 708! Overuse of words or word not found'
        elif ('antonym' in l2 or 'opposite' in l2) and ('use' in l2 or 'usage' in l2):
            for i in l2:
                if i in 'antonym opposite use usage':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite use usage':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Antonyms of the word "'+l2[0]+'" are '+wordnet_antonym(l2[0])+'\nUsage of the word "'+l2[0]+'" is '+wordnet_use(l2[0])
            else:
                return 'Error 708! Overuse of words or word not found'
        elif ('meaning' in l2 or 'explain' in l2 or 'explanantion' in l2) and ('use' in l2 or 'usage' in l2):
            for i in l2:
                if i in 'meaning explain explanation use usage':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'meaning explain explanation use usage':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Meaning of the word "'+l2[0]+'" is '+wordnet_meaning(l2[0])+'\nUsage of the word "'+l2[0]+'" is '+wordnet_use(l2[0])
            else:
                return 'Error 708! Overuse of words or word not found'
        
        
        else:
            return 'Error 709! Unexpected format used'
    elif len(l2)==4:
        if ('antonym' in l2 or 'opposite' in l2) and ('synonym' in l2 or 'similar' in l2 or 'same' in l2) and ('meaning' in l2 or 'explain' in l2 or 'explanation' in l2):
            for i in l2:
                if i in 'synonym similar meaning explain explanation antonym opposite same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'synonym similar meaning explain explanation antonym opposite same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'synonym similar meaning explain explanation antonym opposite same':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Meaning of the word "'+l2[0]+'" is '+wordnet_meaning(l2[0])+'\nSynonyms of the word "'+l2[0]+'" is '+wordnet_synonym(l2[0])+'\nAntonyms of the word "'+l2[0]+'" are '+wordnet_antonym(l2[0])
            else:
                return 'Error 710! Overuse of words or word not found'
        elif ('use' in l2 or 'usage' in l2) and ('synonym' in l2 or 'similar' in l2 or 'same' in l2) and ('meaning' in l2 or 'explain' in l2 or 'explanation' in l2):
            for i in l2:
                if i in 'synonym similar meaning explain explanation use usage same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'synonym similar meaning explain explanation use usage same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'synonym similar meaning explain explanation use usage same':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Meaning of the word "'+l2[0]+'" is '+wordnet_meaning(l2[0])+'\nSynonyms of the word "'+l2[0]+'" is '+wordnet_synonym(l2[0])+'\nUsage of the word "'+l2[0]+'" is '+wordnet_use(l2[0])
            else:
                return 'Error 707! Overuse of words or word not found'
        elif ('use' in l2 or 'usage' in l2) and ('antonym' in l2 or 'opposite' in l2) and ('meaning' in l2 or 'explain' in l2 or 'explanation' in l2):
            for i in l2:
                if i in 'antonym opposite meaning explain explanation use usage':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite meaning explain explanation use usage':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite meaning explain explanation use usage':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Meaning of the word "'+l2[0]+'" is '+wordnet_meaning(l2[0])+'\nAntonyms of the word "'+l2[0]+'" are '+wordnet_antonym(l2[0])+'\nUsage of the word "'+l2[0]+'" is '+wordnet_use(l2[0])
            else:
                return 'Error 710! Overuse of words or word not found'
        elif ('use' in l2 or 'usage' in l2) and ('antonym' in l2 or 'opposite' in l2) and ('synonym' in l2 or 'similar' in l2 or 'same' in l2):
            for i in l2:
                if i in 'antonym opposite synonym similar use usage same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite synonym similar use usage same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite synonym similar use usage same':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Synonyms  of the word "'+l2[0]+'" are '+wordnet_synonym(l2[0])+'\nAntonyms of the word "'+l2[0]+'" are '+wordnet_antonym(l2[0])+'\nUsage of the word "'+l2[0]+'" is '+wordnet_use(l2[0])
            else:
                return 'Error 710! Overuse of words or word not found'
        else:
            return 'Error 711! Unexpected format used'
    elif len(l2)==5:
        if ('antonym' in l2 or 'opposite' in l2) and ('synonym' in l2 or 'similar' in l2 or 'same' in l2) and ('meaning' in l2 or 'explain' in l2 or 'explanation' in l2) and ('use' in l2 or 'usage' in l2):
            for i in l2:
                if i in 'antonym opposite synonym similar use usage meaning explain explanation same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite synonym similar use usage meaning explain explanation same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite synonym similar use usage meaning explain explanation same':
                    l2.remove(i)
                else:
                    l2=l2
            for i in l2:
                if i in 'antonym opposite synonym similar use usage meaning explain explanation same':
                    l2.remove(i)
                else:
                    l2=l2
            if len(l2)==1:
                f='Synonyms of the word "'+l2[0]+'" are '+wordnet_synonym(l2[0])+'\nAntonyms of the word "'+l2[0]+'" are '+wordnet_antonym(l2[0])+'\nUsage of the word "'+l2[0]+'" is '+wordnet_use(l2[0])+'\nMeaning of the word "'+l2[0]+'" is '+wordnet_meaning(l2[0])
            else:
                return 'Error 712! Overuse of words or word not found'
    else:
        return 'Error 713! Unexpected format used'
    return f

def spoken(q):
    q2=q
    b=None
    q=q.replace('ok','')
    q=q.replace('alice','')
    if 'pronounce' in q:
        q=q.replace('pronounce','pronunciation')
    else:
        q=q
    if 'translation' in q:
        q=q.replace('translation','translate')
    else:
        q=q
    if 'pronunciation,' in q:
        q=q.replace('pronunciation,','pronunciation')
    else:
        q=q
    if 'translate,' in q:
        q=q.replace('translate,','translate')
    else:
        q=q
    if 'translation,' in q:
        q=q.replace('translation,','translate')
    else:
        q=q
    if 'synonyms' in q:
        q=q.replace('synonyms','')
        b=True   
    else:
        q=q
    if 'antonyms' in q:
        q=q.replace('antonyms','')
        b=True
    else:
        q=q
    if 'synonym,' in q:
        q=q.replace('synonym,','')
        b=True
    else:
        q=q
    if 'synonym' in q:
        q=q.replace('synonym','')
        b=True
    else:
        q=q
    if 'antonym,' in q:
        q=q.replace('antonym,','')
        b=True
    else:
        q=q
    if 'meaning' in q:
        q=q.replace('meaning','')
        b=True
    else:
        q=q
    if 'meaning,' in q:
        q=q.replace('meaning,','')
        b=True
    else:
        q=q
    q=q.strip()
    l=q.split(' ')
    l2=[]
    for i in l:
        if i in "what is the will be of word a tell me about any one which give an and what's what also how it in sentence its suggest dictionary as can you language":
            l2=l2
        else:
            if i not in l2:
                l2.append(i)
            else:
                continue
    
    f=None
    t=None
    fro=''
    to=''
    #print(l2)
    if 'translate' in l2:
        for i in range(len(l2)):
            if l2[i]=='from':
                f=i
            elif l2[i]=='to':
                t=i
            else:
                continue
            #print(f,t)
        if f!=None:
            fro=l2[f+1]
        else:
            fro=''
        if t!=None:
            to=l2[t+1]
        else:
            return 'Error 715! Cannot Identify the language to which the word or sentence is to be translated'
        if f!=None:
            l2.remove(fro)
            l2.remove('from')
            q2=q2.replace(fro,'')
        else:
            fro=''
        if t!=None:
            l2.remove(to)
            l2.remove('to')
            q2=q2.replace(to,'')     
    else:
        if 'to' in l2:
            l2.remove('to')
            q2=q2.replace('to','')
        else:
            l2=l2
        if 'from' in l2:
            l2.remove('from')
            q2=q2.replace('from','')
        else:
            l2=l2
    d=''
    if b==True:
        d=dictionary(q2)
    else:
        d=d
    e=''
    if 'translate' in l2 and 'pronunciation' not in l2:
        l2.remove('translate')
        for i in l2:
            e+=i+' '
        if d!='':
            return 'The Translation of '+e+' to '+to+' is '+translate(e, to, fro=fro)+'\n' +d
        else:
            return 'The Translation of '+e+' to '+to+' is '+translate(e, to, fro=fro)
    elif 'pronunciation' in l2 and 'translate' not in l2:
        l2.remove('pronunciation')
        for i in l2:
            e+=i+' '
        if d!='':
            return e+' is '+' prononced as... '+pronounce(e)+'\n'+d
        else:
            return e+' is '+' prononced as... '+pronounce(e)
    elif 'pronunciation' in l2 and 'translate' in l2:
        l2.remove('pronunciation')
        l2.remove('translate')
        for i in l2:
            e+=i+' '
        if d!='':
            return 'The Translation of '+e+' to '+to+' is '+translate(e, to, fro=fro)+'\n'+e+'is pronounced as...'+pronounce(e)+ '\n'+d
        else:
            return 'The Translation of '+e+' to '+to+' is '+translate(e, to, fro=fro)+'\n'+e+'is pronounced as... '+pronounce(e)
    else:
        return 'Error 716! Incorrect Grammar Used'
    
    

#print(spoken('ok alice translate chair from english to hindi and pronounce it and also its synonyms'))    
