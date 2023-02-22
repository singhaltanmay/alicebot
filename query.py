import os
import system
import web
import calc
import news
import joke
import dictionary
import browse
import chat


def check(q):
    q=q.strip()
    if 'open' in q:
        return browse.init(q)
    elif 'shutdown' in q:
        n=system.time_sep(q)
        system.shutdown(n)
    elif 'restart' in q:
        n=system.time_sep(q)
        system.restart(n)
    elif 'lock' in q:
        n=system.time_sep(q)
        system.lock(n)
    elif 'log off' in q:
        n=system.time_sep(q)
        system.log_off(n)
    elif 'search' in q:
        web.search(q)
    #maths
    elif 'prime' in q or 'prime number' in q or 'prime no' in q or 'prime no.' in q or 'prime_no.' in q or 'prime_no' in q or 'primeno.' in q or 'primeno' in q or 'prime number' in q or "prime num" in q:
        q=q.replace("prime no.","")
        q=q.replace("prime no","")
        q=q.replace("prime_no.","")
        q=q.replace("prime_no","")
        q=q.replace("primeno.","")
        q=q.replace("primeno","")
        q=q.replace("prime number","")
        q=q.replace("prime num","")
        q=q.replace("number","")
        q=q.replace("whether","")
        q=q.replace("prime","")
        q=q.replace("check","")
        q=q.replace("the","")
        q=q.replace("what","")
        q=q.replace("not","")
        q=q.replace("no","")
        q=q.replace("of","")
        q=q.replace("or","")
        q=q.replace("if","")
        q=q.replace("is","")
        q=q.replace("a","")
        q=q.replace("?","")
        q=q.strip()
        try:
            q=int(q)
        except:
            return "Error 307! Invalid grammar used"
        if q==1:
            return "The number '"+str(q)+"' is not a prime number"
        else:
            abcd=calc.prime_number(q)
        if abcd==True:
            return "The number '"+str(q)+"' is a prime number"
        else:
            return "The number '"+str(q)+"' is a not prime number"

    elif 'composite' in q or 'composite number' in q or 'composite no' in q or 'composite no.' in q or 'composite_no.' in q or 'composite_no' in q or 'compositeno.' in q or 'compositeno' in q or 'composite number' in q or "composite num" in q or "compo number" in q or "comp number" in q or "compo no" in q or "comp no" in q:
        q=q.replace("composite no.","")
        q=q.replace("composite no","")
        q=q.replace("composite_no.","")
        q=q.replace("composite_no","")
        q=q.replace("compositeno.","")
        q=q.replace("compositeno","")
        q=q.replace("composite number","")
        q=q.replace("composite num","")
        q=q.replace("compo","")
        q=q.replace("comp","")
        q=q.replace("number","")
        q=q.replace("whether","")
        q=q.replace("prime","")
        q=q.replace("check","")
        q=q.replace("the","")
        q=q.replace("what","")
        q=q.replace("not","")
        q=q.replace("no","")
        q=q.replace("of","")
        q=q.replace("or","")
        q=q.replace("if","")
        q=q.replace("is","")
        q=q.replace("a","")
        q=q.replace("?","")
        q=q.strip()
        try:
            q=int(q)
        except:
            return "Error 307! Invalid grammar used"
        abcd=calc.prime_number(q)
        if abcd==True:
            return "The number '"+str(q)+"' is not a composite number"
        else:
            return "The number '"+str(q)+"' is a composite number"
    elif 'factor' in q or 'factors' in q or 'fac' in q:
        q=q.replace("factors","")
        q=q.replace("factor","")
        q=q.replace("fac","")
        q=q.replace("the","")
        q=q.replace("what","")
        q=q.replace("of","")
        q=q.replace("are","")
        q=q.replace("is","")
        q=q.replace("a","")
        q=q.replace("?","")
        q=q.replace("no","")
        q=q.replace("number","")
        q=q.strip()
        try:
            q=int(q)
        except:
            return "Error 306! Invalid grammar used"
        x=""
        for i in calc.factors(q):
            x=x+str(i)+","
        x=x[:-1]
        return "The factors of '"+str(q)+"' are '"+x+"'"

    elif ('change' and 'base') in q:
        q=q.replace("?","")
        q=q.replace("becomes","")
        q=q.replace("become","")
        q=q.replace("changed","")
        q=q.replace("converts","")
        q=q.replace("convert","")
        q=q.replace("changes","")
        q=q.replace("change","")
        q=q.replace("base","")
        q=q.replace("will","")
        q=q.replace("value","")
        q=q.replace("what","")
        q=q.replace("when","")
        q=q.replace("of","")
        q=q.replace("the","")
        q=q.replace("number","")
        q=q.replace("into","")
        q=q.replace("is","")
        q=q.replace("no","")
        q=q.replace("a","")
        q=q.strip()
        number=q.split(' ', 1)[0]
        try:
            number=int(number)
        except:
            return "Error 308! Invalid grammar used"
        q=q.replace(str(number),"",1)
        q=q.strip()
        if int(q.find("to"))>(int(q.find("from"))):
            q=q.replace("from","")
            q=q.replace("base","")
            q=q.replace("to","")
            q=q.strip()
            now=q.split(' ', 1)[0]
            try:
                now=int(now)
            except:
                return "Error 308! Invalid grammar used"
            q=q.replace(str(now),"",1)
            q=q.strip()
            q=q.replace("to","")
            q=q.replace("base","")
            q=q.strip()
            to=q.split(' ', 1)[0]
            try:
                to=int(to)
            except:
                return "Error 308! Invalid grammar used"
            try:
                value=calc.basechange(number,to,now,format="Integer")
            except:
                return "Error 308.1! Error Ocurred while calculating base change"
            
            return "The value of the number '"+str(number)+"' becomes '"+str(value)+"' when it's base is changed from '"+str(now)+"' to '"+str(to)+"'"

        else:
            q=q.replace("from","")
            q=q.replace("base","")
            q=q.replace("to","")
            q=q.strip()
            to=q.split(' ', 1)[0]
            try:
                to=int(to)
            except:
                return "Error 308! Invalid grammar used"
            
            q=q.replace(str(to),"",1)
            q=q.strip()
            q=q.replace("to","")
            q=q.replace("base","")
            q=q.strip()
            now=q.split(' ', 1)[0]
            try:
                now=int(now)
            except:
                return "Error 308! Invalid grammar used"
            try:
                value=calc.basechange(number,to,now,format="Integer")
            except:
                return "Error 308.1! Error Ocurred while calculating base change"
            
            return "The value of the number '"+str(number)+"' becomes '"+str(value)+"' when it's base is changed from '"+str(now)+"' to '"+str(to)+"'"
        


        
    elif 'screenshot' in q or 'ss' in q or ('capture' and 'screen') in q:
        system.init(q)
    elif 'multiplies' in q or 'multiplied' in q or 'into' in q or 'add' in q or 'added' in q or 'plus' in q or 'subtract' in q or 'subtracted' in q or 'minus' in q or 'remainder' in q or 'quotient' in q or 'divided' in q or 'divides' in q or 'calculate' in q or 'answer' in q or 'multiply' in q or 'divide' in q or 'calculate' in q or 'value' in q:
        return str(calc.ans(q))
    elif 'news' in q or 'tell me something about' in q or ("new" and "tell") in q and 'jokes' not in q and 'joke' not in q and 'word' not in q and 'meaning' not in q and 'synonym' not in q and 'antonym' not in q and 'similar' not in q and 'opposite' not in q and 'explain' not in q and 'explanation' not in q:
        return news.news(q)
    elif 'joke' in q or 'make me laugh' in q or 'jokes' in q:
        return joke.tell_joke(multiline="random")
        
    elif 'day' in q:
        return calc.day_get(q)
    elif 'translate' in q or 'pronounce' in q or 'pronunciation' in q or 'translation' in q or 'pronunciation,' in q or 'translation,' in q:
        return dictionary.spoken(q)
    elif 'meaning' in q or 'synonym' in q or 'antonym' in q or 'similar' in q or 'opposite' in q or 'explain' in q or 'explanation' in q or 'same' in q and('translate' not in q and 'translation' not in q and 'translation,' not in q and 'pronounce' not in q and 'pronunciation' not in q and 'pronunciation,' not in q):
        return dictionary.dictionary(q)
    else:
        return None

#z=1
#while z<=100:
    #q=input("")
    #print(check(q))
    #z+=1
#print('Session Expired')
