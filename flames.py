import re

# boyName = input("Enter your name : ")
# girlName = input("Enter your partner name : ")



boyName = "amitdh1"
girlName = "nisha"

def regex(boy,girl):
    if re.match('([A-Za-z])\w+',boy) and re.match('([A-Za-z])\w+',girl):
            result = True
    else:
            print("Please Recheck the Names..")
            result = False
    return result

result = regex(boyName,girlName)
print (result);
if result:
    print("done")
else:
    print("something wrong")
        

 

for i in boyName:
    for j in girlName:
        if i == j:
            boyName = boyName.replace(i,"",1)
            girlName = girlName.replace(j,"",1)
            break


num = len(boyName+girlName)
print(num)

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

    print(flames[0])




# print(boyName)
# print(girlName)