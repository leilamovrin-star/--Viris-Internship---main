file_m=input("Input file name:")
tabela=[]
if file_m.endswith(".csv"):
    print("To je csv datoteka")
    with open(file_m, "r", encoding="utf-8") as my:
        for vrstica in my:
            pod= vrstica.strip().split(",")
            tabela.append(pod)

    st=len(tabela[0])
    st_šir=[0]*st
    for vrsti in tabela:
        for i in range(st):
          if len(vrsti[i]) > st_šir[i]:
              st_šir[i]=len(vrsti[i])+2
    
    def č():
        for b in st_šir:
            print("+", "-"*b, end="")
        print("+")
    
    def iz_vr(vrsti):
        for i in range(st):#za vsak stolpec
            print("|" + vrsti[i].center(st_šir[i]), end=" ")
        print("|")
    č()
    iz_vr(tabela[0])
    č()
    for vrsti in tabela[1:]:
      iz_vr(vrsti)
    č()
else:
    print("To ni csv datoteka")


    
