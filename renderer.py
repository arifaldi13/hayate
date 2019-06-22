import os
import random

def createArray(n):
    array = []
    for i in range(n):
        array.append(i)
    return(array)

def renderText(text,cmd,n):
    value = 0
    if cmd in text:
        if text.find(cmd) == 0:
            spaceNum = 0
            for i in text:
                if i.isspace():
                    spaceNum +=1
                else:
                    canExec = False
            if spaceNum == n:
                spacePos = createArray(n)
                arrayPos = -1
                checkPos = 0
                for i in text:
                    if i.isspace():
                        arrayPos += 1
                        spacePos[arrayPos] = checkPos
                    checkPos += 1
                canExec = True
                value   = createArray(n)
                for i in range(n):
                    if i+1 == n:
                        value[i] = text[(spacePos[i]+1):]
                    else:
                        value[i] = text[(spacePos[i]+1):(spacePos[i+1])]
            else:
                canExec = False
        else:
            canExec = False
    else:
        canExec = False
    return(canExec,value)

def renderList(cmd,exce):
    file = os.open(f"list/{cmd}.txt",os.O_RDONLY)
    isi = os.read(file,1000000).splitlines()
    n = 0
    for i in isi:
        isi[n] = str(i,'utf-8',errors='ignore')
        n += 1
    os.close(file)
    asa = createArray(len(isi))
    n = 0
    p = 0
    for i in range(len(isi)):
        m = 0
        asa[i] = isi[n]
        if isi[n].find('<grup>') == 0:                
            m = 0
            for j in range(n+1,len(isi)):
                if isi[j].find('<grup>') == 0:
                    asa[i] = f"""{asa[i]}
{isi[j]}"""
                    m += 1
                else:
                    break
        p += m
        n = n+m+1
        if n >= len(isi):
            break
    del asa[len(asa)-p:len(asa)]
    for i in asa:
        if i == "":
            asa.remove("")
    n = 0
    for i in asa:
        if i.find('<grup>') == 0:
            asa[n] = i.replace('<grup>','')
        n += 1
    a = []
    for i in range(len(asa)):
        if asa[i].find("[EXCEPTION]") == 0:
            a.append(i)
    a.append(len(asa)-1)
    if exce != "none": 
        x = []
        n = 0
        for i in a:
            x.append(asa[i].replace("[EXCEPTION] text=",""))
        x.pop(len(x)-1)
        for i in range(len(x)):
            if exce == x[i]:
                if a[i+1] == len(asa)-1:
                    num = random.randint(a[i]+1,a[i+1])
                    return(asa[num])
                num = random.randint(a[i]+1,a[i+1]-1)
                return(asa[num])
    for i in range(len(a)-1):
        asa.pop(a[i])
    if len(a) != 1:
        num  = random.randint(0,a[0]-1)
    else:
        num  = random.randint(0,a[0])
    return(asa[num])

def renderPhrase2(text,cmd,secText):
    obj = ""
    canExec = False
    if text.find(cmd) == 0:
        if text[len(cmd)].isspace():
            if text.endswith(secText):
                obj = text.replace(cmd+" ","")
                obj = obj.replace(secText,"")
                canExec = True
    return(canExec,obj)

def renderPhrase3(text,firText,secText,thrText):
    canExec = False
    obj = []
    if text.find(firText) == 0:
        if text[len(firText)].isspace():
            if text[text.find(secText)-1].isspace():
                if text[text.find(secText)+len(secText)].isspace():
                    if text.endswith(thrText):
                        dum1 = text.replace(firText+" ","")
                        dum2 = dum1.replace(thrText,"")
                        obj = dum2.split(" "+secText+" ")
                        canExec = True
                        return(canExec,obj)

def renderZero(num):
    text = str(num)
    if text.endswith(".0"):
        text = text.replace(".0","")
    return(text)