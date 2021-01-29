import string
key=53*5 #Zahl 1: key ----- Zahl 2: secret_factor
jump_pause=3
jump_height=-2
#--------------------------------
multiplicator,times=1,1
alphabet=string.ascii_letters
atk=alphabet*(key**2)
jump=1
NA=""
while len(alphabet) != 0 and len(atk)!=0:
    for i in range(26):
        try:
            NA=NA+atk[(key*multiplicator)-jump]
            #print(atk[(key*multiplicator)-jump], times, alphabet[times-1])
            atk=atk.replace(atk[(key*multiplicator)-jump], "")
            times+=1
            multiplicator+=1
            if multiplicator % jump_pause == 0:
                jump-=jump_height
            else:
                jump=1
        except:
            multiplicator=1
            continue
current_letter = 0
newtext=""
text=input("Welchen Text möchtest du verschlüsseln? ")
for j in range(len(text)):
    if text[current_letter] not in (string.punctuation+" "):
        result=NA.find(text[current_letter])
        current_letter+=1
        newtext=newtext+alphabet[result]
    else:
        result=NA.find(text[current_letter])
        current_letter+=1
        newtext=newtext+text[current_letter-1]
print(text, ":", newtext)
