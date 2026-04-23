import random
#Karte:
Karte = {
#    "a": 1,
    "A": 11,
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}
Loose=21
# vse barve
barve = ["♠", "♣", "♥", "♦"]
znova=False
i=2
j=2
#Količina
Srebrni = 0
Oranzni = 0
Vijolicni = 0
Crni = 0
Zeleni = 0
Modri = 0
Rdeci = 0
Beli = 0

Srebrni1 = 0
Oranzni1 = 0
Vijolicni1 = 0
Crni1 = 0
Zeleni1 = 0
Modri1 = 0
Rdeci1 = 0
Beli1 = 0


def vleci_karto(deck):
    karta = random.choice(list(deck.keys()))
    vrednost = deck[karta]
    return karta, vrednost
# naredimo poln deck
deck = {}
for barva in barve:
    for karta, vrednost in Karte.items():
        ime = f"{karta}{barva}"
        deck[ime] = vrednost
print("CENE: ")
print("BEL čip: 1 €")
print("RDEČ čip: 5 €")
print("MODER čip: 10 €")
print("ZELEN čip: 25 €")
print("ČRN čip: 100 €")
print("VIJOLIČEN čip: 500 €")
print("ORANŽEN čip: 1000 €")
print("SREBREN čip: 5000 €")
print()
print()
#-------------------------------------------------------------------------------------------------------- 
chips = {
    "SREBRNIH čipov": 5000,
    "ORANŽNIH čipov": 1000,    
    "VIJOLIČNIH čipov": 500,  
    "ČRNIH čipov": 100,
    "ZELENIH čipov": 25,
    "MODRIH čipov": 10,
    "RDEČIH čipov": 5,
    "BELIH čipov": 1,
}
print("=== BLACKJACK ===")
Tvoj_denar=int(input("Koliko denarja imaš? "))
print()
print("Imaš:")
for barva, vrednost in chips.items():
    koliko = Tvoj_denar // vrednost
    Tvoj_denar = Tvoj_denar % vrednost
    print(f"{barva} čipov: {koliko}")
    if barva == "SREBRNIH čipov":
        Srebrni1 += koliko
    elif barva == "ORANŽNIH čipov":
        Oranzni1 += koliko
    elif barva == "VIJOLIČNIH čipov":
        Vijolicni1 += koliko
    elif barva == "ČRNIH čipov":
        Crni1 += koliko
    elif barva == "ZELENIH čipov":
        Zeleni1 += koliko
    elif barva == "MODRIH čipov":
        Modri1 += koliko
    elif barva == "RDEČIH čipov":
        Rdeci1 += koliko
    elif barva == "BELIH čipov":
        Beli1 += koliko
Srebrni = Srebrni1
Oranzni = Oranzni1
Vijolicni = Vijolicni1
Crni = Crni1
Zeleni = Zeleni1
Modri = Modri1
Rdeci = Rdeci1
Beli = Beli1
Vs=0
print()
#-------------------------------------------------------------------------------------------------------- 
while True:
    SrebrniB = 0
    OranzniB = 0
    VijolicniB = 0
    CrniB = 0
    ZeleniB= 0
    ModriB = 0
    RdeciB = 0
    BeliB = 0
    while True:
       print("Koliko in katere čipe staviš?")
       # SREBRNI čipi
       if Srebrni > 0:
           try:
               stava_srebrni = int(input(f"SREBRNIH čipov (max {Srebrni}): "))
           except ValueError:
               print("Vnesi celo število.")
               continue
           if stava_srebrni == 0:
               pass
           elif 0 < stava_srebrni <= Srebrni>0:
               Vs+=1
               Srebrni -= stava_srebrni
               SrebrniB += stava_srebrni
           else:
               print("Nimaš jih toliko.")
               continue

       # ORANŽNI čipi
       if Oranzni > 0:
           stava_oranzni = int(input(f"ORANŽNIH čipov (max {Oranzni}): "))
           if stava_oranzni == 0:
               pass
           elif 0 < stava_oranzni <= Oranzni>0:
               Vs+=1
               Oranzni -= stava_oranzni
               OranzniB += stava_oranzni
           else:
               print("Nimaš jih toliko.")

       # VIJOLIČNI čipi
       if Vijolicni > 0:
           stava_vijolicni = int(input(f"VIJOLIČNIH čipov (max {Vijolicni}): "))
           if stava_vijolicni == 0:
               pass
           elif stava_vijolicni <= Vijolicni>0:
               Vs+=1
               Vijolicni -= stava_vijolicni
               VijolicniB += stava_vijolicni
           else:
               print("Nimaš jih toliko.")

       # ČRNI čipi
       if Crni > 0:
           stava_crni = int(input(f"ČRNIH čipov (max {Crni}): "))
           if stava_crni == 0:
               pass
           elif stava_crni <= Crni>0:
               Vs+=1
               Crni -= stava_crni
               CrniB += stava_crni

           else:
               print("Nimaš jih toliko.")

       # ZELENI čipi
       if Zeleni > 0:
           stava_zeleni = int(input(f"ZELENIH čipov (max {Zeleni}): "))
           if stava_zeleni == 0:
               pass
           elif stava_zeleni <= Zeleni>0:
               Vs+=1
               Zeleni -= stava_zeleni
               ZeleniB += stava_zeleni
           else:
               print("Nimaš jih toliko.")

       # MODRI čipi
       if Modri > 0:
           stava_modri = int(input(f"MODRIH čipov (max {Modri}): "))
           if stava_modri == 0:
               pass
           elif stava_modri <= Modri>0:
               Vs+=1
               Modri -= stava_modri
               ModriB += stava_modri

           else:
               print("Nimaš jih toliko.")

       # RDEČI čipi
       if Rdeci > 0:
           stava_rdeci = int(input(f"RDEČIH čipov (max {Rdeci}): "))
           if stava_rdeci == 0:
               pass
           elif stava_rdeci <= Rdeci>0:
               Vs+=1
               Rdeci -= stava_rdeci
               RdeciB += stava_rdeci
           else:
               print("Nimaš jih toliko.")

       # BELI čipi
       if Beli > 0:
           stava_beli = int(input(f"BELIH čipov (max {Beli}): "))
           if stava_beli == 0:
               break
           elif stava_beli <= Beli>0:
               Vs+=1
               Beli -= stava_beli
               RdeciB += stava_rdeci
               break
           else:
               print("Nimaš jih toliko.")
               break
       if  Vs > 0:
           break
       else:
           print("Staviti moraš vsaj en čip.")
    Igralec=[]
    Hiša=[]
    #--------------------------------------------------------------------------------------------------------      
    # DEALER
    kartaDealer1 = random.choice(list(deck.keys()))
    print("Dealrjeva karta1:", kartaDealer1, "-Vrednost: ", deck[kartaDealer1])
    kartaDealer2 = random.choice(list(deck.keys()))
    print("Dealrjeva karta2", "-", "-Vrednost: ", "-")
    y= deck[kartaDealer1] + deck[kartaDealer2]
    print()
    print()
 #--------------------------------------------------------------------------------------------------------
    # IGRALEC
    nakljucna_karta = random.choice(list(deck.keys()))
    Igralec.append(nakljucna_karta)
    print("Tvoja karta1:", nakljucna_karta, "-Vrednost: ", deck[nakljucna_karta])
    nakljucna_karta2 = random.choice(list(deck.keys()))
    Igralec.append(nakljucna_karta2)
    print("Tvoja karta2:", nakljucna_karta2, "-Vrednost: ", deck[nakljucna_karta2])
    x= deck[nakljucna_karta] + deck[nakljucna_karta2]
    print("Tvoja vsota je:", x)
    print()
    while True:
       hit=input("Želiš hit (da/ne)? ")
       if hit =="da":
        nakljucna_karta3 = random.choice(list(deck.keys()))
        Igralec.append(nakljucna_karta3)
        i+=1
        print(f"Tvoja karta{i}:", nakljucna_karta3, "-Vrednost: ", deck[nakljucna_karta3]) 
        x+= deck[nakljucna_karta3]
        print("Tvoja nova vsota je:", x)
        aces = sum(1 for karta in Igralec if karta.startswith("A"))
        if x>21 and aces > 0:
          x = x - 10
          aces -= 1
          print("As šteje kot 1.")
          print("Tvoja nova vsota: ", x)   
        elif x==21:
          print("Imaš 21!! Počakaj, da vidiš če ima hiša enako.")
       else:
        print("Stand.")
        break
    print()
    print()
 #--------------------------------------------------------------------------------------------------------
  # DEALER
    print("Dealrjeva karta1:", kartaDealer1, "-Vrednost: ", deck[kartaDealer1])
    print("Dealrjeva karta2", kartaDealer2, "-Vrednost: ", deck[kartaDealer2])
    print("Dealrjeva vsota je:", y)
    print()
    while True:
      if y<16:
         kartaDealer3 = random.choice(list(deck.keys()))
         Hiša.append(kartaDealer3)
         j+=1
         print(f"Dealrjeva nova karta{j}:", kartaDealer3, "-Vrednost: ", deck[kartaDealer3]) 
         y+= deck[kartaDealer3]
         acesh = sum(1 for karta in Hiša if karta.startswith("A"))
         if x>21 and acesh > 0:
             x = x - 10
             acesh -= 1
             Hiša.remove(karta.startswith("A"))
             print("As šteje kot 1.")
             print("Tvoja nova vsota: ", x)
         print("Dealrjeva nova vsota je:", y)
         print()
      elif x==y :
          print("Push. Stavljeno dobiš nazaj.")
          print()
          Srebrni +=  SrebrniB 
          Oranzni += OranzniB
          Vijolicni += VijolicniB
          Crni += CrniB
          Zeleni += ZeleniB
          Modri += ModriB
          Rdeci += RdeciB
          Beli += BeliB
          break
      elif x>21 :
         print("Bust. Izgubiš vse čipe. Prevelika vsota.")
         print()
         break
      elif x==21:
          print("Blackjack!! Igralec = 21.")
          if SrebrniB > 0:
             Srebrni += SrebrniB * 1.5
          if OranzniB > 0:
              Oranzni += int(OranzniB * 1.5)
          if VijolicniB > 0:
              Vijolicni += int(VijolicniB * 1.5)
          if CrniB > 0:
              Crni += int(CrniB * 1.5)
          if ZeleniB > 0:
              Zeleni += int(ZeleniB * 1.5)
          if ModriB > 0:
              Modri += int(ModriB * 1.5)
          if RdeciB > 0:
              Rdeci += int(RdeciB * 1.5)
          if BeliB > 0:
              Beli += int(BeliB * 1.5)
          print()
          break
      elif x>21 :
         print("Bust. You loose. Prevelika vsota.")
         print()
         break
      elif y==21:
          print("Bust. Hiša ima 21.")
          print()
          break
      elif y>21 :
         print("Zmagal si!! Hiša je presegala 21. ")
         Srebrni = 2* SrebrniB 
         Oranzni = 2*OranzniB
         Vijolicni = 2*VijolicniB
         Crni = 2*CrniB
         Zeleni = 2*ZeleniB
         Modri = 2*ModriB
         Rdeci = 2*RdeciB
         Beli = 2*BeliB
         print()
         break
      elif x>y and x<21 :
         print("Zmagal si!! Hiša ima majnšo vsoto kot ti. ")
         Srebrni = 2* SrebrniB 
         Oranzni = 2*OranzniB
         Vijolicni = 2*VijolicniB
         Crni = 2*CrniB
         Zeleni = 2*ZeleniB
         Modri = 2*ModriB
         Rdeci = 2*RdeciB
         Beli = 2*BeliB
         print()
         break
      elif x<y :
          print("Bust. You loose. Hiša ima večjo vsoto od tebe.")
          print()
          break
    if Srebrni==0 and Oranzni==0 and Vijolicni==0 and Crni==0 and Zeleni==0 and Modri==0 and Rdeci==0 and Beli==0:
        break
       
 #--------------------------------------------------------------------------------------------------------
    print()
    ihn= input("Ali želiš igraiti še enkrat (da/ne)? ")
    print()
    if ihn == "ne":
      break
if Srebrni>0 or Oranzni>0 or Vijolicni>0 or Crni>0 or Zeleni>0 or Modri>0 or Rdeci>0 or Beli>0:
    iz = Srebrni * 5000 + Oranzni * 1000 + Vijolicni* 500 + Crni*100 + Zeleni*25 + Modri*10 + Rdeci*5 + Beli
    print(f"Vložil si {Tvoj_denar} € in od tega zaslužil {iz} ")
else:
    print("Izgubil si ves denar. Pojdi si poiskat službo.")