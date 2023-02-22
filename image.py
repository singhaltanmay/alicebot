import cv2
import os
import face_recognition

def identify_face(img,percentage=False,match_distance=0.6):
    # match percentage default is 0.6
    d={}
    with open('Data\image.csv', encoding='utf-8') as f:
        lines = f.readlines()
        xyz=0
        for abc in lines:
            xy=abc.split(",",2)
            if xyz!=0:
                l=xy[1].replace("[","")
                l=l.replace("]","")
                l=l.strip()
                k=l.split(" ")
                list1=[]
                for j in k:
                    if j!="":
                        j=float(j)
                        list1.append(j)
                t=xy[2]
                t=t.strip()
                t1=t[:-1]
                t2=t1[1:]
                d[xy[0]+":"+t2]=list1
            xyz+=1        
    image1 = face_recognition.load_image_file(img)
    encoding1 = face_recognition.face_encodings(image1)[0]
    
    for i in d:
        encoding2=d[i]
        face_distances = face_recognition.face_distance([encoding2], encoding1)
        face_match_percentage = (1-face_distances)*100
        if face_distances<=match_distance:
            if percentage==True:
                m=i.split(":")
                return "The image matches with '"+m[0]+"' with a match of "+str(round(float(face_match_percentage),1))+"%."+"\n"+m[1]+"."
            else:
                m=i.split(":")
                return "The image matches with '"+m[0]+"'."+"\n"+m[1]+"."
        else:
            return "No matching image found!"

    
def tbd(img):
    name=input("name ? ")
    bio=input("bio ? ")
    string=""
    string+=name.strip()+","+"["
    image1 = face_recognition.load_image_file(img)
    encoding1 = face_recognition.face_encodings(image1)[0]
    x=list(encoding1)
    for i in x:
        string+=str(i)+" "
    string=string.strip()
    string+="],"+'"'+bio.strip()+'"'
    print(string)
    with open('readme.txt', 'w') as f:
        f.write(string)
        f.close()
        print("done")
#tbd("C:\\Users\\Admin\\Desktop\\abc.png")       
print(identify_face("C:\\Users\\Admin\\Desktop\\download.jpg",True))
