from operator import truediv
import re
import sys

boyName = input("Enter your name : ")
girlName = input("Enter your partner name : ")

# boyName = "nisha"
# girlName = "admit"


def innerRegex(boy,girl):
    x=[]
    name = boy + girl
    for i in name:
        if re.findall("[a-zA-Z]",i):
            x.append(1)
        else:
            x.append(0)
    x.sort(reverse = False)
    if x[0] == 0:
        print("Avoid Using Symbols or Numbers")
        sys.exit()
    else:
        return True


def outerRegex(boy,girl):
    if boy == girl:
        print("Please Give Two Different Name")
        sys.exit()
    elif innerRegex(boy,girl):
        return True
    else:
        sys.exit()

if outerRegex(boyName,girlName):
    for i in boyName:
        for j in girlName:
            if i == j:
                boyName = boyName.replace(i,"",1)
                girlName = girlName.replace(j,"",1)
                break
    
num =  len(boyName+girlName)

if num > 0:
    flames = ["Friends","Lover","Affectionate","Marriage","Enemy","Sibling"]
    while len(flames) > 1:
        formula = num%len(flames)
        removeIndex = formula - 1
        if removeIndex >= 0:
            left = flames[:removeIndex]
            right = flames[removeIndex+1:]
            flames = right+left
        else:
            flames = flames[:len(flames)-1]

    print("RelationShip Between You and your loved one is: {}".format(flames[0]))
