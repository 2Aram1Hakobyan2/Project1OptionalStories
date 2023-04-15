def changer_s1(n,nm,a,pob,SW,v,clr,tov,mot):
    tov = input('Type of Vehicle : ')
    mot = input('Mesure of Time : ')
    i = 0
    while i!=5:
        n[i] = input('Noun : ')
        i+=1
    i = 0
    while i!=3:
        a[i] = input('Adjective : ')
        i+=1
    i = 0
    while i!=2:
        nm[i] = input('Number : ')
        i+=1
    i = 0
    while i!=2:
        pob[i] = input('Part of the Body : ')
        i+=1
    i = 0
    while i!=2:
        v[i] = input('Verb : ')
        i+=1
    clr = input('Color : ')
    SW = input('Silly Word : ')
    print("-")
    s1 = ("It was about " + nm[0] + " " + mot + " ago when I arrived at the hospital in a " + tov + ".The hospital is a/an " + a[0] + " place, there are a lot of " + a[1] + " " + n[0] + " here.There are nurses here who have " + clr + " " + pob[0] + ".If someone wants to come into my room I told them that they have to " + v[0] + " first.I've decorated my room with " + nm[1] + " " + n[1] + ".Today I talked to a doctor and they were wearing a " +  n[2] + " on their " + pob[1] + ".I heard that all doctors " + v[1] + " " + n[3] + " everyday for breakfast.The most " +  a[2] + " thing about being in the hospital is the " + SW + " " + n[4] + ".")
    print(s1)

def changer_s2(n,af,pn,v,SW,adv,clr,animal,mot,nm):
        i = 0
        while i!=3:
            n[i] = input('Noun : ')
            i+=1
        i=0
        while i!=2:
            af[i] = input('Adjective(Feeling) : ')
            i+=1
        i=0
        while i!=3:
            v[i] = input('Verb : ')
            i+=1
        i=0
        pn = input('Proper Noun(Person''s Name) : ')
        adv = input('Adverb : ')
        clr = input('Colour : ')
        animal = input('Animal : ')
        mot = input('Mesure of Time : ')
        nm[i] = input('Number : ')
        SW = input('Silly Word : ')
        print("-")
        s2 = ("This weekend I am going camping with " + pn + ".I packed my lantern,sleeping bag and " + n[0] + ".I am so " + af[0] + " to " + v[0] + " in a tent.I am " + af[1] + " we might see a/an "+ animal + ", I hear they're kind if dangerous.While we are camping,we are going to hike,fish and " + v[1] + ".I have heared that the " + clr + " lake is great for " + v[2] + ".Then we will " + adv + " hike through the forest for " + nm[0] + " " + mot + " .If I see a " + clr + " " + animal + " while hiking,I am going to bring it home as a pet!At night we will tell " + n[1] + " " + SW + " stories and roast " + n[2] + " around the campfire!!")
        print(s2)

def changer_s3(pn,clr,animal,plc,rm,mot,a,mg,n,nplr,nm,v):
    pn = input('Proper Noun(Person''s Name) : ')
    clr = input('Colour : ')
    animal = input('Animal : ')
    plc = input('Place : ')
    rm = input('Room in a House : ')
    mot = input('Mesure of Time : ')
    i=0
    while i!=5:
        a[i] = input('Adjective : ')
        i+=1
    i=0
    while i!=2:
        mg[i] = input('Magical Creature(Plural) : ')
        i+=1
    i=0
    while i!=3:
        n[i] = input("Noun : ")
        i+=1
    i=0
    while i!=2:
        nplr[i] = input('Noun(Plural) : ')
        i+=1
    i=0
    nm[i] = input('Number : ')
    v[i] = input('Verb(ending in ing) : ')
    print("-")
    s3 =("Dear " + pn + ", I am writting to you form a/an " + a[0] + " castle in an enchanted forest.I found myself here one day after going for a ride on a " + clr + " " + animal +" in " + plc + ".There are " + a[1] + " " + mg[0] + " and " + a[2] + "  " + mg[1] + " here!In the " + rm + " there is a pool full of " + n[0] + ".I fall asleep each night on a " + n[1] + " of " + nplr[0] + " and dream of " + a[3] + " " + nplr[1] + ".It feels as though I have lived here for " + nm[0] + " " + mot + ".I hope one day you can visit, although the only way to get here now is " + v[0] + " on a " + a[4] + " " + n[2] + "!!!")
    print(s3)

print("\n---------------------\n")
print("We are going to play a game where you choose 1 of 3 stories with missing words.\nThen it's up to you to insert whatever you fancy! ")
v = ["(Verb)","(Verb)","(Verb(ending in ing))"]
n = ["(Noun)","(Noun)","(Noun)","(Noun)","(Noun)"]
nplr = ["(Noun(Plural))","(Noun(Plural))"]
nm = ["(Number)","(Number)"]
a = ["(Adjective)","(Adjective)","(Adjective)","(Adjective)","(Adjective)"]
af = ["(Adjective(Feeling))","(Adjective(Feeling))"]
pob = ["(Part of the Body)","(Part of the Body)"]
mot = "(Measure of Time)"		
tov = "(Type of Vehicle)"
clr = "(Color)"
SW = "(Silly Word)"
pn = "(Proper Noun(Person's Name))"
animal = "(Animal)"
adv =  "(Adverb(Ending in ly))"
plc = "(Place)"
mg = ["(Magical creature(Plural))","(Magical creature(Plural))"]
rm = "(Room in a House)"
s3 =("Dear " + pn + ", I am writting to you from a/an " + a[0] + " castle in an enchanted forest.I found myself here one day after going for a ride on a " + clr + " " + animal +" in " + plc + ".There are " + a[1] + " " + mg[0] + " and " + a[2] + "  " + mg[1] + " here!In the " + rm + " there is a pool full of " + n[0] + ".I fall asleep each night on a " + n[1] + " of " + nplr[0] + " and dream of " + a[3] + " " + nplr[1] + ".It feels as though I have lived here for " + nm[0] + " " + mot + ".I hope one day you can visit, although the only way to get here now is " + v[2] + " on a " + a[4] + " " + n[2] + "!!!")
s2 = ("This weekend I am going camping with " + pn + ".I packed my lantern,sleeping bag and " + n[0] + ".I am so " + af[0] + " to " + v[0] + " in a tent.I am " + af[1] + " we might see a/an "+ animal + ", I hear they're kind if dangerous.While we are camping,we are going to hike,fish and " + v[1] + ".I have heared that the " + clr + " lake is great for " + v[2] + ".Then we will " + adv + " hike through the forest for" + nm[0] + " " + mot + " .If I see a " + clr + " " + animal + " while hiking,I am going to bring it home as a pet!At night we will tell " + n[1] + " " + SW + " stories and roast " + n[2] + " around the campfire!!")
s1 = ("It was about " + nm[0] + " " + mot + " ago when I arrived at the hospital in a " + tov + ".The hospital is a/an " + a[0] + " place, there are a lot of " + a[1]  + " " + n[0] + " here.There are nurses here who have " + clr + " " + pob[0] + ".If someone wants to come into my room I told them that they have to " + v[0] + " first.I've decorated my room with " + nm[1] + " " + n[1] + ".Today I talked to a doctor and they were wearing a " +  n[2] + " on their " + pob[1] + ".I heard that all doctors " + v[1] + " " + n[3] + " everyday for breakfast.The most " +  a[2] + " thing about being in the hospital is the " + SW + " " + n[4] + ".")
ss = [s1,s2,s3]
print("\nStories\n---------------------\n")
i = 0
while i!=3:
    print("Story Number: ",i+1)
    print("-")
    print(ss[i])
    print("\n---------------------\n")
    if i>3:
        break
    i+=1
print("Time to make a Choice!\n")
c = int(input("Story Number : "))
if c == 1:
    print("\n---------------------\n")
    print("Great Choice!\n-")
    print(ss[c-1])
    print("\nThe Result\n-")
    changer_s1(n,nm,a,pob,SW,v,clr,tov,mot)
    print("\n----\nThe End\n----\n")
elif c == 2:
    print("Nice!!!\n-")
    print(ss[c-1])
    print("\nThe Result\n-")
    changer_s2(n,af,pn,v,SW,adv,clr,animal,mot,nm)
    print("\n----\nThe End\n----\n")
elif c == 3:
    print("I like it too!\n-")
    print(ss[c-1])
    print("\nThe Result\n-")
    changer_s3(pn,clr,animal,plc,rm,mot,a,mg,n,nplr,nm,v)
    print("\n----\nThe End\n----\n")
else:
    print("There are Only 3 stories. \nTry Again!")
    
   #pull request is open
