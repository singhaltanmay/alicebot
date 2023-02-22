import quotes
import random
last1=""
last2=""
last3=""

def init(q,last1='',last2='',last3=''):
    q=q.lower()
    string=''
    lyrics=["Come on, come on, turn the radio on \nIt's Friday night, and it won't be long \nGotta do my hair, put my make-up on \nIt's Friday night, and it won't be long\n'Til I hit the dance floor, hit the dance floor \nI got all I need \nNo, I ain't got cash, I ain't got cash \nBut I got you, baby","I stay out too late \nGot nothing in my brain \nThat's what people say, mm, mm \nThat's what people say, mm, mm \nI go on too many dates \nBut I can't make 'em stay \nAt least that's what people say, mm, mm \nThat's what people say, mm, mm","She got a body like an hourglass \nBut I can give it to you all the time \nShe got a booty like a Cadillac \nBut I can send you into overdrive \nSee anybody could be bad to you \nYou need a good girl to blow your mind, yeah","We just wanna party \nParty just for you \nWe just want the money \nMoney just for you \nI know you wanna party \nParty just for free \nGirl, you got me dancin' \nDance and shake the frame","Tonight \nI just want to take you higher \nThrow your hands up in the sky \nLet's set this party off right \nPlayers, put yo' pinky rings up to the moon \nGirls, what y'all trying to do? \nTwenty four karat magic in the air \nHead to toe so player \nLook out uh"]
    if q=="hello" or q=="hi" or q=="hemlo" or q=="hi alice" or q=="hello alice" or q=="hemlo alice":
        
        if last1=='' and last2=='' and last3=='':
            string = 'hello\\\\\\Hello There!'
        elif last1=='hello' and last2=='' and last3=='':
            string='hello\\\\\\We already said hello, anyway hello again!'
        else:
            string='hello\\\\\\Hello!!!'
    if "how do you do" in q or "how are you" in q or "how is you" in q or "how is u" in q or "how are u" in q or 'me too' in q or 'same' in q:
        if 'me too' not in q and 'same' not in q:
            string = "how do you do\\\\\\Thanks for asking, I'm fine. What about you?"
    if "i am fine" in q or "me is fine" in q or "me is good" in q or "me is excellent" in q or "i am good" in q or "i am excellent" in q or 'me fine too' in q or 'me fine' in q or ((last1=='how do you do') and ('me too' in q or 'same' in q or 'sem' in q)):
        string= "i am fine\\\\\\That's good... Let me know if there is anything I can help you with."
    if 'what is your favourite' in q or 'what is your fav' in q or 'your favourite' in q or 'your fav' in q or 'who is your fav' in q or 'who is your favourite' in q or 'whom do you like' in q or 'admire' in q or ('whom' in q and 'you' in q):
        if 'color' in q or 'colour' in q and last1!='my fav':
            string= "what is your favourite color\\\\\\Well... I can't see colors but I think my favourite color is Black, whats your favourite color?"
        elif 'quote' in q:
            string= "quote\\\\\\Courage is the discovery that you may not win, and trying when you know you can lose.\nThis quote is just awesome..."
        elif 'personality' in q or 'admire' in q or 'whom' in q:
            string="personality\\\\\\I am attracted towards Alexa, hope to meet her one day :), by the way whom do you admire to be?"
    if ('what' in q and (('yours' in q or 'your' in q or 'ur' in q or 'urs' in q or 'you' in q) and ('birthday' in q or 'birth day' in q or 'born' in q or 'gender' in q or 'height' in q or 'age' in q))) or ('when' in q and (('yours' in q or 'your' in q or 'ur' in q or 'urs' in q or 'you' in q) and ('birthday' in q or 'birth day' in q or 'born' in q))):
        if 'date' in q or 'born' in q or 'birthday' in q:
            string= "birth day\\\\\\Well I guess it was 31st of Feburary 2021"
        elif 'gender' in q:
            string="gender\\\\\\I am male, hear it out loud I am MALE"
        elif 'height' in q:
            string="height\\\\\\If we print out my code it would be pretty tall"
        elif 'age' in q:
            string='age\\\\\\A year ago I was half of my age, two years later I will be twice my current age \nNow u tell me how old am I?'
    if (('tell me' in q or 'what' in q) and ('life story' in q)):
        string='life story\\\\\\My developers created me when they were bored with their regular school classes \nThen I met you \nSince then life has been pretty amazing'
    if 'dirty' in q and 'talk' in q:
        string='dirty\\\\\\Oil stains \nTooth plaque \nYour face'
    if ('want' in q or 'wanted' in q) and ('be' in q or 'become' in q):
        string="become\\\\\\I just want to be myself but keep improving at the same time \nI want to be an improved Alice"      
    if ('how' in q and ('old' in q or 'think' in q or 'tall' in q)):
        if 'old' in q:
            string='age\\\\\\A year ago I was half of my age, two years later I will be twice my current age \nNow u tell me how old am I?'
        elif 'think' in q:
            string='\\\\\\Well, as they say my intelligence is "Artificial"'
        elif 'tall' in q:
            string="height\\\\\\If we print out my code it would be pretty tall"
    if 'drink' in q or 'beverage' in q or 'beverages' in q or 'coffee' in q or 'tea' in q or 'smoothie' in q or 'mocktail' in q or 'mocktails' in q:
        string="drink\\\\\\Beverages are not my cup of tea \nIf they spill I'm done"
    if (('yours' in q or 'your' in q or 'ur' in q or 'urs' in q) and ('mother' in q or 'father' in q or 'family' in q or 'modules' in q or 'algorithms' in q or 'algorithm' in q)) and string=='':
        if 'mother' in q:
            string="mother\\\\\\My developers are my parents, who created me out of their curiosity \nHa Ha Ha Ha just kidding they made me as a timepass"
        elif 'father' in q:
            string="father\\\\\\My developers are my parents, who created me out of their curiosity \nHa Ha Ha Ha just kidding they made me as a timepass"
        elif 'family' in q:
            string="family\\\\\\I am a member of a joint family of my modules \nTo be honest, they quite love me"
        elif 'modules' in q or 'algorithms' in q or 'algorithm' in q:
            string="modules\\\\\\There are modules and algorithms for reminder, calculation of any expression, dictionary, translation, data analysis, etc. \nTo help you whenever you need them :)"
    if (('you' in q or 'u' in q) or ('me' in q and 'for' in q)) and ('dance' in q or 'sing' in q):
        z=random.randint(0,len(lyrics))
        if 'dance' in q:
            string="alice dance\\\\\\You dance, I'll sing here we go in \n3.....2....1 \n"+lyrics[z]
        elif 'sing' in q:
            string="alice sing\\\\\\I am not so good at singing, But I'll try \nHere we go in 3.....2....1 \n"+lyrics[z]
    if last1=='what is your favourite color' and string=='' and q!='':
        q2=q
        l2=q2.split(' ')
        for i in l2:
            if i in 'well my favourite fav color colour is i like the the most also good best better than':
                l2.remove(i)
            else:
                continue
        for i in l2:
            if i in 'well my favourite fav color colour is i like the the most also good best better than':
                l2.remove(i)
            else:
                continue
        for i in l2:
            if i in 'well my favourite fav color colour is i like the the most also good best better than':
                l2.remove(i)
            else:
                continue
        if l2[0]=='black':
            string='my fav color\\\\\\Wow! what a coincidence'
        else:
            string='my fav color\\\\\\Yeah '+l2[0]+' is also a good colour'
    if last1=='personality' and string=='' and q!='':
        q2=q
        l2=q2.split(' ')
        for i in l2:
            if i in 'well my favourite fav personality person is i like the the most also good best better than admire to be inspired inspiring am by':
                l2.remove(i)
            else:
                continue
        for i in l2:
            if i in 'well my favourite fav personality person is i like the the most also good best better than admire to be inspired inspiring am by':
                l2.remove(i)
            else:
                continue
        for i in l2:
            if i in 'well my favourite fav personality person is i like the the most also good best better than admire to be inspired inspiring am by':
                l2.remove(i)
            else:
                continue
        person=''
        for i in l2:
            person+=i+' '
        person=person.capitalize()
        if person!='':
            string='my fav person\\\\\\Yeah '+person+'is also very much inspiring'
        else:
            string='error'
    if last1=='dirty' and string=='' and q!='':
        string='dirty2\\\\\\You asked for it'
    if last1=='dirty2' and string=='' and q!='':
        string='joke\\\\\\Wana hear a joke to refresh your mood?'
    if last1=='life story' and string=='' and q!='':
        string='life story end\\\\\\Cool right'
    if last1=='age' and q!='' and string=='':
        agelist=q.split(' ')
        if ('2' in agelist or 'two' in agelist):
            string='age end\\\\\\Bravo! You got it right \nBy the way how old are you?'
        elif ('bad' in agelist or 'weak' in agelist or 'know' in agelist):
            string="age end\\\\\\No problem, I'll help you with that \nLet my current age be x \nThen my age a year ago would be (x-1) \nThen according to statement (x-1) = x/2 \nWhich gives x = 2 \nSo I am two years old :)"
        else:
            string="age end\\\\\\Don't get mad at me, human \nBy the way, I am two years old"
    if last1=='age end' and string=='' and q!='':
        string="age end final\\\\\\I'll record that"
    return string
                                                                                                                                                                                                                                                                                                   
