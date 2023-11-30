
#parketta
matlength = 1291
matwidth = 193

#szoba
roomlength = 4500
roomwidth = 1000

knitwork = 3

xdict = {}

#használható maradék
usable = [0]



#maradék egy sorból
xend = roomlength % matlength
print(xend)

#hány sor fér el egy szobában
yf = roomwidth // matwidth + 1
print(f"Sorok száma {yf} egész db")

y = roomwidth % matwidth
print(f"Sorokból marad a végén {y} mm a {matwidth}-ból")

for i in range(0, yf):
    starts = (matlength // knitwork) * (i % knitwork)
    if starts == 0:
        starts = matlength
    xf = (roomlength - starts) // matlength
    ends = starts + matlength * xf
    xdict.update({i * matwidth : [starts] + [matlength] * xf + [roomlength - ends]})

#ha nem egészre végződik adjon hozzá még egy sort hogy kitöltse a szobát, a maradék meg hulló
#if list(xdict)[-1] < roomwidth:
#    xdict.update({list(xdict)[-1] + matwidth : ylist})




#kiiratás egymás alá a sorokat, és a még felhasználható hulladékokat
for a, b in xdict.items():
    print(a, b)


#print(matlength // knitwork)


