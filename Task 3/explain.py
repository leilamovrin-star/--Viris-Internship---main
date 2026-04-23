import random  # imports the random module so the program can pick random cards

# Karte:
Karte = {  # dictionary that stores card ranks and their blackjack values
#    "a": 1,  # commented out alternative Ace value
    "A": 11,  # Ace counts as 11 (later can become 1)
    "K": 10,  # King
    "Q": 10,  # Queen
    "J": 10,  # Jack
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

Loose=21  # maximum value before busting (over 21 means losing)

# vse barve (all card suits)
barve = ["♠", "♣", "♥", "♦"]

znova=False  # variable that could be used for restarting game (not really used)
i=2  # counter for player cards
j=2  # counter for dealer cards

# Količina (number of chips the player has)
Srebrni = 0
Oranzni = 0
Vijolicni = 0
Crni = 0
Zeleni = 0
Modri = 0
Rdeci = 0
Beli = 0

# initial chip counts
Srebrni1 = 0
Oranzni1 = 0
Vijolicni1 = 0
Crni1 = 0
Zeleni1 = 0
Modri1 = 0
Rdeci1 = 0
Beli1 = 0


def vleci_karto(deck):  # function that draws a random card from the deck
    karta = random.choice(list(deck.keys()))  # randomly pick card name
    vrednost = deck[karta]  # get the value of that card
    return karta, vrednost  # return both card name and value

# naredimo poln deck (create full deck of cards)
deck = {}
for barva in barve:  # for each suit
    for karta, vrednost in Karte.items():  # for each card rank
        ime = f"{karta}{barva}"  # combine rank and suit (example: A♠)
        deck[ime] = vrednost  # store card with its value

# print chip prices
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
chips = {  # chip values dictionary
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

Tvoj_denar=int(input("Koliko denarja imaš? "))  # ask user how much money they have
print()

print("Imaš:")
for barva, vrednost in chips.items():  # convert money into chip amounts
    koliko = Tvoj_denar // vrednost  # integer division (how many chips)
    Tvoj_denar = Tvoj_denar % vrednost  # remaining money
    print(f"{barva} čipov: {koliko}")

    # store chip counts
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

# copy initial chip values
Srebrni = Srebrni1
Oranzni = Oranzni1
Vijolicni = Vijolicni1
Crni = Crni1
Zeleni = Zeleni1
Modri = Modri1
Rdeci = Rdeci1
Beli = Beli1

Vs=0  # counts if at least one chip is bet
print()

#-------------------------------------------------------------------------------------------------------- 
while True:  # main game loop

    # chips placed in the bet
    SrebrniB = 0
    OranzniB = 0
    VijolicniB = 0
    CrniB = 0
    ZeleniB= 0
    ModriB = 0
    RdeciB = 0
    BeliB = 0

    while True:  # betting loop
       print("Koliko in katere čipe staviš?")

       # betting silver chips
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

       # same logic repeats for every chip color
       # subtract chips from player and add to bet

       # (other chip sections omitted explanation because they are identical)

       if  Vs > 0:  # check if at least one chip was bet
           break
       else:
           print("Staviti moraš vsaj en čip.")

    Igralec=[]  # list for player's cards
    Hiša=[]  # list for dealer cards

#--------------------------------------------------------------------------------------------------------      
# DEALER
    kartaDealer1 = random.choice(list(deck.keys()))  # dealer first card
    print("Dealrjeva karta1:", kartaDealer1, "-Vrednost: ", deck[kartaDealer1])

    kartaDealer2 = random.choice(list(deck.keys()))  # dealer hidden card
    print("Dealrjeva karta2", "-", "-Vrednost: ", "-")

    y= deck[kartaDealer1] + deck[kartaDealer2]  # dealer total
    print()
    print()

#--------------------------------------------------------------------------------------------------------
# PLAYER
    nakljucna_karta = random.choice(list(deck.keys()))  # player first card
    Igralec.append(nakljucna_karta)
    print("Tvoja karta1:", nakljucna_karta, "-Vrednost: ", deck[nakljucna_karta])

    nakljucna_karta2 = random.choice(list(deck.keys()))  # player second card
    Igralec.append(nakljucna_karta2)
    print("Tvoja karta2:", nakljucna_karta2, "-Vrednost: ", deck[nakljucna_karta2])

    x= deck[nakljucna_karta] + deck[nakljucna_karta2]  # player's total
    print("Tvoja vsota je:", x)
    print()

    while True:
       hit=input("Želiš hit (da/ne)? ")  # ask if player wants another card

       if hit =="da":
        nakljucna_karta3 = random.choice(list(deck.keys()))
        Igralec.append(nakljucna_karta3)
        i+=1
        print(f"Tvoja karta{i}:", nakljucna_karta3, "-Vrednost: ", deck[nakljucna_karta3]) 

        x+= deck[nakljucna_karta3]  # update player total
        print("Tvoja nova vsota je:", x)

        # check if player has Ace
        aces = sum(1 for karta in Igralec if karta.startswith("A"))

        if x>21 and aces > 0:  # convert Ace from 11 to 1
          x = x - 10
          aces -= 1
          print("As šteje kot 1.")
          print("Tvoja nova vsota: ", x)

        elif x==21:
          print("Imaš 21!! Počakaj, da vidiš če ima hiša enako.")
       else:
        print("Stand.")  # player stops taking cards
        break

#--------------------------------------------------------------------------------------------------------
# DEALER TURN
    print("Dealrjeva karta1:", kartaDealer1, "-Vrednost: ", deck[kartaDealer1])
    print("Dealrjeva karta2", kartaDealer2, "-Vrednost: ", deck[kartaDealer2])
    print("Dealrjeva vsota je:", y)
    print()

    while True:
      if y<16:  # dealer must hit if below 16
         kartaDealer3 = random.choice(list(deck.keys()))
         Hiša.append(kartaDealer3)
         j+=1

         print(f"Dealrjeva nova karta{j}:", kartaDealer3, "-Vrednost: ", deck[kartaDealer3]) 

         y+= deck[kartaDealer3]
         print("Dealrjeva nova vsota je:", y)
         print()

      # game outcome checks
      elif x==y :
          print("Push. Stavljeno dobiš nazaj.")  # tie
          break

      elif x>21 :
         print("Bust. Izgubiš vse čipe.")  # player bust
         break

      elif x==21:
          print("Blackjack!! Igralec = 21.")  # blackjack payout
          break

      elif y==21:
          print("Bust. Hiša ima 21.")  # dealer blackjack
          break

      elif y>21 :
         print("Zmagal si!! Hiša je presegala 21.")  # dealer bust
         break

      elif x>y and x<21 :
         print("Zmagal si!! Hiša ima manjšo vsoto kot ti.")  # player wins
         break

      elif x<y :
          print("Bust. You loose. Hiša ima večjo vsoto.")  # dealer wins
          break

    # check if player lost all chips
    if Srebrni==0 and Oranzni==0 and Vijolicni==0 and Crni==0 and Zeleni==0 and Modri==0 and Rdeci==0 and Beli==0:
        break
       
#--------------------------------------------------------------------------------------------------------
    print()
    ihn= input("Ali želiš igraiti še enkrat (da/ne)? ")  # play again?
    print()

    if ihn == "ne":
      break

# final money calculation
if Srebrni>0 or Oranzni>0 or Vijolicni>0 or Crni>0 or Zeleni>0 or Modri>0 or Rdeci>0 or Beli>0:
    iz = Srebrni * 5000 + Oranzni * 1000 + Vijolicni* 500 + Crni*100 + Zeleni*25 + Modri*10 + Rdeci*5 + Beli
    print(f"Vložil si {Tvoj_denar} € in od tega zaslužil {iz} ")
else:
    print("Izgubil si ves denar. Pojdi si poiskat službo.")  # player lost everything