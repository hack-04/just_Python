import random


def son_top(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi?")
    taxminlar = 0

    while True:
        taxminlar += 1
        try:
            taxmin = int(input(">>> "))
        except ValueError:
            print("Iltimos, butun son kiriting!")
            taxminlar -= 1
            continue
        if taxmin > tasodifiy_son:
            print(f"Men o'ylagan son bundan kichik")
        elif taxmin < tasodifiy_son:
            print("Men o'ylagan son bundan katta")
        else:
            break
    print(f"Siz {taxminlar} ta taxmin bilan topdingiz")
    return taxminlar


def sontop_pc(x=10):
    input(f"\n1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'ladingiz: to'g'ri (t), "
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-):>> ")
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        elif javob == "t":
            break
        else:
            print("Noto'g'ri belgi yoki harf kiritdingiz! Iltimos, faqat 't', '+' va '-' kiriting.")
            taxminlar -= 1
            continue
    print(f"Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar


def play(x=10):
    yana = True
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = sontop_pc(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} ta taxmin bilan topdim, siz {taxminlar_user} ta taxmin bilan topdingiz. Men yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} ta taxmin bilan topdingiz, men esa {taxminlar_pc} ta taxmin bilan topdim. Siz yutdingiz!")
        else:
            print(f"Ikki tomon ham {taxminlar_user} ta taxmin bilan topdi. Durrang!")

        while True:
            javob = input("Yana o'ynaysizmi? Ha(1)/Yo'q(0): ")
            if javob == "1":
                yana = True
                break
            elif javob == "0":
                yana = False
                break
            else:
                print("Iltimos, 1 yoki 0 ni bosing.")


play()
