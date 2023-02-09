from random import randint

ekwipunek = ["stary_kilof"]
sakwa_na_mineraly = []
wynik = []

global hartowany_zelazny_kilof
hartowany_zelazny_kilof = 0
global stalowy_kilof
stalowy_kilof = 0
global tytanowe_wiertlo
tytanowe_wiertlo = 0
global stary_kilof
stary_kilof = 1
global zardzewialy_kilof
zardzewialy_kilof = 0

global rubin
rubin = 0
global szmaragd
szmaragd = 0
global opal
opal = 0
global beryl
beryl = 0
global szafir
szafir = 0

global kasa
kasa = 0
startgrynie = 0
startgrytak = 0

global usuwacz
usuwacz = 0
global usuwacz1
usuwacz1 = 0

def tawerna(kasa):
    dzien1 = None
    while dzien1 != "Q":
        dzien1 = input("E - ekwipunek, K - kasa, M = sakwa_na_mineraly, R - start kopania")
        if dzien1 == "E":
            print(ekwipunek)        
        elif dzien1 == "K":
            print(kasa)
        elif dzien1 == "M":
            print(sakwa_na_mineraly)
        elif dzien1 == "R":
            print("Zaczynanie nowego dnia!")
            break 




def petla(szmaragd, rubin, szafir, beryl, opal, budzet):
    dzien1kopanie = randint(0,500)
    print(dzien1kopanie)
    if dzien1kopanie >= 0 and dzien1kopanie <= 5:               #5
        print("##############################")
        print("##### WYDOBYTO MINERAL! ######")
        print("#### ZDOBYWASZ SZMARAGD #####")
        print("##############################")
        szmaragd = szmaragd + 1
        sakwa_na_mineraly.append("szmaragd")
    elif dzien1kopanie >= 6 and dzien1kopanie <= 30:            
        print("################################")                   #24
        print("### GUBISZ CZESC PIENIEDZY! ####")
        print("########  TRACISZ 3000$ ########")
        print("################################")
        budzet = budzet - 3000 
    elif dzien1kopanie >= 31 and dzien1kopanie <= 45:
        print("##############################")                   #14
        print("##### WYDOBYTO MINERAL!  #####")
        print("###### ZDOBYWASZ RUBIN  ######")
        print("##############################")
        rubin = rubin + 1
        sakwa_na_mineraly.append("rubin")
    elif dzien1kopanie >= 46 and dzien1kopanie <= 70:
        print("##################################")
        print("#### GUBISZ CZESC PIENIEDZY! #####")                    #24    
        print("######     TRACISZ 4000$    ######")
        print("##################################")
        budzet = budzet - 4000
    elif dzien1kopanie >= 71 and dzien1kopanie <= 90:
        print("##############################")                    #19
        print("##### WYDOBYTO MINERAL! ######")
        print("###### ZDOBYWASZ SZAFIR  ######")
        print("##############################")
        szafir = szafir + 1
        sakwa_na_mineraly.append("szafir")  
    elif dzien1kopanie >= 91 and dzien1kopanie <= 150:              
        print("###################################")              #59
        print("##### GUBISZ CZESC PIENIEDZY! #####")
        print("######      TRACISZ 1000$   ########")
        print("###################################")
        budzet = budzet - 1000
    elif dzien1kopanie >= 151 and dzien1kopanie <= 159:
        print("##############################")               #8
        print("##### WYDOBYTO MINERAL! ######")
        print("####  ZDOBYWASZ OPAL #######")
        print("##############################")
        opal = opal + 1
        sakwa_na_mineraly.append("opal")
    elif dzien1kopanie >= 160 and dzien1kopanie <= 230:
        print("###################################")                 #70
        print("##### GUBISZ CZESC PIENIEDZY! #####")
        print("######    TRACISZ 500$   ##########")       
        print("###################################")
        budzet = budzet - 500
    elif dzien1kopanie >= 230 and dzien1kopanie <= 249:
        print("##############################")               #19
        print("##### WYDOBYTO MINERAL! ######")
        print("####  ZDOBYWASZ BERYL ########")
        print("##############################")
        beryl = beryl + 1
        sakwa_na_mineraly.append("beryl")
    elif dzien1kopanie >= 250 and dzien1kopanie <=500:
        print("#################################")
        print("#####   NIC NIE WYDOBYWASZ! #####")
        print("#################################")
    wynik.append(szmaragd)
    wynik.append(rubin)
    wynik.append(szafir)
    wynik.append(beryl)
    wynik.append(opal)
    wynik.append(budzet)


def sprzedaz(szmaragd, rubin, szafir, beryl, opal, kasa):
	while True:
		print("Ktore mineraly chcesz sprzedac?")
		print("SZMARAGD (5000$ za brylke) - Sm")
		print("OPAL (4500$ za brylke) - O")
		print("RUBIN (3500$ za brylke) - R")
		print("SZAFIR (2000$ za brylke) - Sz")
		print("BERYL (2000$ za brylke) - Be")
		print("Kliknij C by przejsc dalej")
		mineralinp = input()
		if mineralinp == "Sm" and szmaragd >= 1 or "szmaragd" in sakwa_na_mineraly and mineralinp == "Sm":
			kasa += 5000
			sakwa_na_mineraly.remove("szmaragd")
			szmaragd = szmaragd - 1
			print("Sprzedales szmaragd!")
			print("Saldo:", kasa) 
		elif mineralinp == "R" and rubin >= 1:
			kasa += 3500
			sakwa_na_mineraly.remove("rubin")
			rubin = rubin - 1
			print("Sprzedales rubin!")
			print("Saldo:", kasa) 
		elif mineralinp == "Sz" and szafir >= 1:
			kasa += 2000
			sakwa_na_mineraly.remove("szafir")
			szafir = szafir - 1
			print("Sprzedales szafir!")
			print("Saldo:", kasa)
		elif mineralinp == "O" and opal >= 1:
			sakwa_na_mineraly.remove("opal")
			kasa += 4500
			opal = opal - 1
			print("Sprzedales opal!")
			print("Saldo:", kasa)
		elif mineralinp == "Be" and beryl >= 1:
			sakwa_na_mineraly.remove("beryl")
			kasa += 2000
			beryl = beryl - 1
			print("Sprzedales beryl!")
			print("Saldo:", kasa)
		elif mineralinp == "C":
			break
		else:
			print("Nie mozesz sprzedac mineralu, ktorego nie masz!")
	wynik.append(szmaragd)
	wynik.append(rubin)
	wynik.append(szafir)
	wynik.append(beryl)
	wynik.append(opal)
	wynik.append(kasa)


def sklep(kasa, stary_kilof, stalowy_kilof, hartowany_zelazny_kilof, tytanowe_wiertlo):
	while True:
		print("cennik:")
		print("Stalowy Kilof (Zwieksza szczescie wydobycia mineralow i losowe wydarzenie o 1) - 2000$, klinkij S by kupic")
		print("Hartowany Zelazny Kilof (Zwieksza ilosc losowego wydarzenia o 2) - 3000$, klinkij H by kupic")
		print("Tytanowe Wiertlo (Zwieksza ilosc losowego wydarzenia o 4 i szczescie wydobycia mineralow - 6000$, klinkij T by kupic")
		print("Kliknij C by zakonczyc dzien")
		sklepin = input()
		if sklepin == "S" and kasa >= 2000:
			kasa = kasa - 2000
			ekwipunek.append("stalowy_kilof")
			stary_kilof = stary_kilof - 1
			hartowany_zelazny_kilof = hartowany_zelazny_kilof - 1
			tytanowe_wiertlo = tytanowe_wiertlo - 1
			stalowy_kilof = stalowy_kilof + 1
			print("Zakupiono stalowy kilof!")
		elif sklepin == "H" and kasa >= 3000:
			kasa = kasa - 3000
			ekwipunek.append("hartowany_zelazny_kilof")
			hartowany_zelazny_kilof = hartowany_zelazny_kilof + 1
			stalowy_kilof = stalowy_kilof - 1
			stary_kilof = stary_kilof - 1
			tytanowe_wiertlo = tytanowe_wiertlo - 1
			print("Zakupiono hartowany zelazny kilof!")
		elif sklepin == "T" and kasa >= 6000:
			kasa = kasa - 6000
			ekwipunek.append("tytanowe_wiertlo")
			tytanowe_wiertlo = tytanowe_wiertlo + 1
			stalowy_kilof = stalowy_kilof - 1
			stary_kilof = stary_kilof - 1
			hartowany_zelazny_kilof - 1
			print("Zakupiono tytanowe wiertlo")
		elif sklepin == "C":
			break
		else:
			print("Nie stac cie na ten przedmiot lub wybrales zly przycisk!")
	wynik.append(kasa)
	wynik.append(stary_kilof)
	wynik.append(stalowy_kilof)
	wynik.append(hartowany_zelazny_kilof)
	wynik.append(tytanowe_wiertlo)


def stalowykilofgra(szmaragd, rubin, szafir, beryl, opal, kasa):
	dzien1kopanie = randint(0,320)
	print(dzien1kopanie)
	if dzien1kopanie >= 0 and dzien1kopanie <= 10:               #10
		print("##############################")
		print("##### WYDOBYTO MINERAŁ! ######")
		print("#### ZDOBYWASZ SZMARAGD #####")
		print("##############################")
		szmaragd = szmaragd + 1
		sakwa_na_mineraly.append("szmaragd")  
	elif dzien1kopanie >= 11 and dzien1kopanie <=23 :    #12
		print("################################")
		print("### GUBISZ CZESC PIENIEDZY! ####")
		print("########  TRACISZ 3000$ ########")
		print("################################")
		kasa -= 3000   
	elif dzien1kopanie >= 23 and dzien1kopanie <= 43:
		print("##############################")                   #20
		print("##### WYDOBYTO MINERAŁ!  #####")
		print("###### ZDOBYWASZ RUBIN  ######")
		print("##############################")
		rubin = rubin + 1
		sakwa_na_mineraly.append("rubin")   
	elif dzien1kopanie >= 44 and dzien1kopanie <= 56:
		print("################################")                  #12
		print("### GUBISZ CZESC PIENIEDZY! ####")
		print("########  TRACISZ 4000$ ########")
		print("################################")
		kasa -= 4000  
	elif dzien1kopanie >= 57 and dzien1kopanie <= 97:
		print("##############################")                    #40
		print("##### WYDOBYTO MINERAŁ! ######")
		print("####  ZDOBYWASZ SZAFIR ######")
		print("##############################")
		szafir = szafir + 1
		sakwa_na_mineraly.append("szafir")  
	elif dzien1kopanie >= 98 and dzien1kopanie <= 128:
		print("###################################")                 
		print("##### GUBISZ CZESC PIENIEDZY! #####")                  #30
		print("######      TRACISZ 1000$   ########")
		print("###################################")
		kasa -= 1000    
	elif dzien1kopanie >= 129 and dzien1kopanie <= 150:
		print("##############################")               #21
		print("##### WYDOBYTO MINERAŁ! ######")
		print("####  ZDOBYWASZ OPAL #######")
		print("##############################")
		szafir = szafir + 1
		sakwa_na_mineraly.append("szafir")
	elif dzien1kopanie >= 151 and dzien1kopanie <= 186:
		print("###################################")                 
		print("##### GUBISZ CZESC PIENIEDZY! #####")                  #35
		print("######      TRACISZ 500$   ########")
		print("###################################")
		kasa -= 500
	elif dzien1kopanie >= 187 and dzien1kopanie <= 227:
		print("##############################")                   #40
		print("##### WYDOBYTO MINERAŁ!  #####")
		print("###### ZDOBYWASZ BERYL  ######")
		print("##############################")
		beryl = beryl + 1
		sakwa_na_mineraly.append("beryl")
	elif dzien1kopanie >= 228 and dzien1kopanie <= 320:
		print("#################################")                
		print("#####   NIC NIE WYDOBYWASZ! #####")                
		print("#################################")
	wynik.append(szmaragd)
	wynik.append(rubin)
	wynik.append(szafir)
	wynik.append(beryl)
	wynik.append(opal)
	wynik.append(kasa)

startkasa = randint(0,200)


if startkasa >= 0 and startkasa <= 5:
	kasa += kasa + 9000
	print("Poczatkowe pieniadze: 9000$")
elif startkasa > 5 and startkasa <= 15:
	kasa += kasa + 6000
	print("Poczatkowe pieniadze: 6000$")
elif startkasa > 15 and startkasa <= 30:
	kasa += 4500
	print("Poczatkowe pieniadze 4500$")     
elif startkasa > 30 and startkasa <= 50:
	kasa += 2000
	print("Poczatkowe pieniadze: 2000$")        
elif startkasa > 50 and startkasa <= 80:
	kasa += 1000
	print("Poczatkowe pieniadze: 1000$")
elif startkasa > 80 and startkasa <= 130:
	kasa += 500
	print("Poczatkowe pieniadze: 500$")        
elif startkasa > 130 and startkasa <= 200:
	print("Poczatkowe pieniadze: 0$")
global i
i = 0
while i < 7:
	i = i + 1
	print("dzien - ", i)
	tawerna(kasa)
	petla(szmaragd, rubin, szafir, beryl, opal, kasa)
	szmaragd = wynik[0]
	rubin = wynik[1]
	szafir = wynik[2]
	beryl = wynik[3]
	opal = wynik[4]
	kasa = wynik[5]    
	wynik = []
	petla(szmaragd, rubin, szafir, beryl, opal, kasa)
	szmaragd = wynik[0]
	rubin = wynik[1]
	szafir = wynik[2]
	beryl = wynik[3]
	opal = wynik[4]
	kasa = wynik[5]
	wynik = []
	if i >= 2:
		if stalowy_kilof >= 1:
			wynik = []
			stalowykilofgra(szmaragd, rubin, szafir, beryl, opal, kasa)
			szmaragd = wynik[0]
			rubin = wynik[1]
			szafir = wynik[2]
			beryl = wynik[3]
			opal = wynik[4]
			kasa = wynik[5]
			wynik = []
			stalowykilofgra(szmaragd, rubin, szafir, beryl, opal, kasa)
			szmaragd = wynik[0]
			rubin = wynik[1]
			szafir = wynik[2]
			beryl = wynik[3]
			opal = wynik[4]
			kasa = wynik[5]
		elif hartowany_zelazny_kilof >= 1:
			wynik = []
			petla(szmaragd, rubin, szafir, beryl, opal, kasa)
			szmaragd = wynik[0]
			rubin = wynik[1]
			szafir = wynik[2]
			beryl = wynik[3]
			opal = wynik[4]
			kasa = wynik[5]    
			wynik = []
			petla(szmaragd, rubin, szafir, beryl, opal, kasa)
			szmaragd = wynik[0]
			rubin = wynik[1]
			szafir = wynik[2]
			beryl = wynik[3]
			opal = wynik[4]
			kasa = wynik[5]
			wynik = []
			petla(szmaragd, rubin, szafir, beryl, opal, kasa)
			szmaragd = wynik[0]
			rubin = wynik[1]
			szafir = wynik[2]
			beryl = wynik[3]
			opal = wynik[4]
			kasa = wynik[5]
		elif tytanowe_wiertlo >= 1:
			wynik = []
			petla(szmaragd, rubin, szafir, beryl, opal, kasa)
			szmaragd = wynik[0]
			rubin = wynik[1]
			szafir = wynik[2]
			beryl = wynik[3]
			opal = wynik[4]
			kasa = wynik[5]    
			wynik = []
			petla(szmaragd, rubin, szafir, beryl, opal, kasa)
			szmaragd = wynik[0]
			rubin = wynik[1]
			szafir = wynik[2]
			beryl = wynik[3]
			opal = wynik[4]
			kasa = wynik[5]
			wynik = []
			petla(szmaragd, rubin, szafir, beryl, opal, kasa)
			szmaragd = wynik[0]
			rubin = wynik[1]
			szafir = wynik[2]
			beryl = wynik[3]
			opal = wynik[4]
			kasa = wynik[5]    
			wynik = []
			petla(szmaragd, rubin, szafir, beryl, opal, kasa)
			szmaragd = wynik[0]
			rubin = wynik[1]
			szafir = wynik[2]
			beryl = wynik[3]
			opal = wynik[4]
			kasa = wynik[5]
	sprzedaz(szmaragd, rubin, szafir, beryl, opal, kasa)
	szmaragd = wynik[0]
	rubin = wynik[1]
	szafir = wynik[2]
	beryl = wynik[3]
	opal = wynik[4]
	kasa = wynik[5]
	wynik = []
	sklep(kasa, stary_kilof, stalowy_kilof, hartowany_zelazny_kilof, tytanowe_wiertlo)
	kasa = wynik[0]
	stary_kilof = wynik[1]
	stalowy_kilof = wynik[2]
	hartowany_zelazny_kilof = wynik[3]
	tytanowe_wiertlo = wynik[4]
	print("TWOJE STATYSTYKI PO TYM DNIU:")
	print("TWOJ EKWIPUNEK:", ekwipunek)
	print("TWOJE PIENIADZE:", kasa)
	print("TWOJE MINERALY:", sakwa_na_mineraly)
if kasa >= 25000:
	print("WYGRALES ZDOBYWAJAC OKRESLONA PULE PIENIEDZY, TWOJE PIENIADZE TO:", kasa)
elif kasa < 25000:
	print("NIE WYGRYWASZ, BO NIE OSIAGNALES OKRESLONEJ PULI PIENIEDZY, TWOJE PIENIADZE TO:", kasa)