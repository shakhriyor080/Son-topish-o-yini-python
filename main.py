""" 
1.11.2023

"SONNI topish" O'yini

Muallif SHahriyor Qosimov

web sahifa: https:
"""

import random 
 
def sontop(x=10):
    tasodifiy_son  = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim . Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o;ylagan son bundan kattaroq. Yana harakat qiling: ")
        elif taxmin>tasodifiy_son:
            print("xato men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            break
    return taxminlar
    print(f"Tabriklayman. {taxminlar} bilan topdingiz Topdingiz")
    

def sontop_pc(x=10):
    input(f"1dan {x} gacha son o'ylang va istalgan tugma bosing. Men topaman ")
    quyi = 1
    yuqori = x 
    taxminlar = 0
    while True:
        taxminlar +=1
        if quyi != yuqori:
          taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javop = input(f"siz {taxmin} sonini o'yladingizmi , to'gri (tugri),"
                   f"men o'ylagan son bundan kattaroq (+), yoki kichikroq(-)".lower())
        if javop== "-":
            yuqori = taxmin - 1
        elif javop == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"men {taxminlar}urunish bilan Topdim 😂")


def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user>taxminlar_pc:
              print("men yutdim")
        elif taxminlar_user<taxminlar_pc:
                print("siz yutdingiz")
        else:
            print("Durrang!")
        yana = int(input("yana oynaysizmi? Ha(1)/Yo'q(0)"))


play()
