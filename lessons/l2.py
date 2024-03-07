def yazdir(x):
    print("Sonuç =", x)

def toplama(a, b):
    yazdir(a + b)

def cikarma(a, b):
    yazdir(a - b)

def carpma(a, b):
    yazdir(a * b)

def bolme(a, b):
    if b == 0:
        print("Bir sayı sıfıra bölünemez!")
    else:
        yazdir(a / b)

while True:
    print("""Bir işlem seçiniz.
    Toplama (1)
    Çıkarma (2)
    Çarpma (3)
    Bölme (4)
    Çıkış yapmak için herhangi bir tuşa basınız.
""")
    
    islem = int(input())
    if islem in [1, 2, 3, 4]:
        s1 = int(input("Sayı 1: "))
        s2 = int(input("Sayı 2: "))

        if islem == 1:
            toplama(s1, s2)
        elif islem == 2:
            cikarma(s1, s2)
        elif islem == 3:
            carpma(s1, s2)
        elif islem == 4:
            bolme(s1, s2)
    else:
        print("Geçersiz işlem numarası! Lütfen tekrar deneyin.")
        break
    
    
