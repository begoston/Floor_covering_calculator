

#parketta
matlength = 1291
matwidth = 193

#szoba
roomlength = 3000
roomwidth = 2000

#kötések száma
knitwork = 3

#kulcsok a szoba szélességéig felsorolt parketta szélesség indexek, az értékek az adott sorban lévő parketták szélességei
xdict = {}

#használható maradék
usable = []
rest = []
startlist = []

#maradék egy sorból
xend = roomlength % matlength
print(xend)

#hány sor fér el egy szobában
yf = roomwidth // matwidth + 1
print(f"Sorok száma {yf} egész db")

#buildelés
for i in range(0, yf):
    key = i * matwidth #mindig hozzáad egy szélesség indexet
    starts = (matlength // knitwork) * (i % knitwork) #parkettahoszt elosztja a kötésszámmal, majd megszorozza hogy hanyadnál tart
    startlist.append(starts)#feltölti a startlistet
    if starts == 0: #hogy az egész ne 0 legyen
        starts = matlength
    xf = (roomlength - starts) // matlength #azt mutatja meg hogy hány egész parketta van egy sorban
    ends = roomlength - (starts + matlength * xf)#a végén kiszámolja menyi kell a falig
    rest.append(matlength - ends)#kiszámolja menyi marad használható hullónak,é s feltölti a listát
    values = [starts] + [matlength] * xf + [ends] #megcsinálja a szoba hosszúságáhoza a parketták hosszát
    xdict.update({key : values})# feltölti a szélességek indexetek a kulcsokhoz, és az értékekhez a parketteeldenrezést hossz szerint


for key, values in xdict.items():
    print(f"{key} indexü sor --- {values} parketták")


print(f"----Elején felhasználható hulló: {rest}")
print(f"----Kezdések értéke soronként: {startlist}")


startlist.pop(0)#kitörli az első értéket a listából
startlist.append(0)# hozzáfűzi a végéhez a 0-át így elcsúsztattam egyel

print(f"Elején felhasználható hulló: {rest}")
print(f"Kezdések értéke soronként: {startlist}")

# rest startlist összefésülése, majd különbségek kiszámítása, majd rögzítése egy külön listában
for rest, startlist in zip(rest, startlist):
    difference = rest - startlist
    usable.append(difference)


print(f"Hulladékok: {usable}")

