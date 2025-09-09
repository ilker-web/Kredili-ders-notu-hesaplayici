from datetime import datetime

def zaman():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def dersortalama():
    try:
        vize=int(input("Vize notunuzu giriniz : "))
        final=int(input("Final notunuzu giriniz : "))
        if  100 >= vize >= 0:
            if 100 >= final >= 0:
                nott=(vize*0.4 + final*0.6)
                print(f"Ders ortalamanız : {nott}")
            else:
                print("LÜtfen 0-100 arasında değerler giriniz!")
        else:
            print("LÜtfen 0-100 arasında değerler giriniz!")
    except:
        print("LÜtfen 1-100 arasında değerler giriniz:")


def donemsonuort():

    AA = 4.0
    BA = 3.5
    BB = 3.0
    CB = 2.5
    CC = 2.0
    DC = 1.5
    DD = 1.0
    FF = 0.0

    try:
        toplam_puan = 0
        toplam_kredi = 0

        adet = int(input("Kaç tane dersiniz var: "))

        for i in range(adet):
            kredi = int(input(f"{i + 1}. dersin kredisini girin: "))
            harf = input(f"{i + 1}. dersin harf notunu girin (AA, BA, BB, BC, CC, DC, DD, FF): ").upper()

            if harf == "AA":
                katsayi = AA
            elif harf == "BA":
                katsayi = BA
            elif harf == "BB":
                katsayi = BB
            elif harf == "CB":
                katsayi = CB
            elif harf == "CC":
                katsayi = CC
            elif harf == "DC":
                katsayi = DC
            elif harf == "DD":
                katsayi = DD
            elif harf == "FF":
                katsayi = FF
            else:
                print(f"Geçersiz harf notu: {harf}. Bu ders hesaplamaya dahil edilmeyecek.")
                continue

            ders_puani = katsayi * kredi
            toplam_puan += ders_puani
            toplam_kredi += kredi

            print(f"{i + 1}. ders: {kredi} kredi, {harf} notu = {ders_puani} puan")

        if toplam_kredi > 0:
            ortalama = toplam_puan / toplam_kredi
            print(f"\nToplam kredi: {toplam_kredi}")
            print(f"Toplam puan: {toplam_puan}")
            print(f"Dönem sonu not ortalamanız: {ortalama:.2f}")
        else:
            print("Hiç geçerli ders girilmedi.")

    except ValueError:
        print("Geçersiz giriş! Lütfen sayısal değerler girin.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def yilsonuort():
    try:
        ilkdonem=float(input("1.Dönem sonu ortalamanızı giriniz : "))
        ikincidonem=float(input("2.Dönem sonu ortalamanızı giriniz : "))
        if 4 >= ilkdonem >= 0:
            if 4 >= ikincidonem >= 0:
                yilsonunot = ((ilkdonem + ikincidonem) / 2)
                print(f"Yıl sonu notunuz : {yilsonunot}")
            else:
                print("LÜtfen dönem sonu ortalamanızı 0-4 arasında giriniz:")
        else:
            print("LÜtfen dönem sonu ortalamanızı 0-4 arasında giriniz:")
    except:
        print("LÜtfen dönem sonu ortalamanızı 0-4 arasında giriniz:")


print(f"""
        -- Sunucuya Hoşgeldiniz --
            {zaman()}
        
    1- Ders Ortalaması Hesaplama
    2- Dönem Sonu Ortalama Hesaplama
    3- Yıl Sonu Ortalama Hesaplama
    4- Çıkış
""")

while True:
    secim = input("Yapmak istediğiniz işlemi seçiniz : ")
    if secim == "1": dersortalama()
    elif secim == "2": donemsonuort()
    elif secim == "3": yilsonuort()
    elif secim == "4":
        print("Programdan çıkılıyor...")
        exit()
    else:
        print("Lütfen sadece belirtilen değerleri giriniz!")