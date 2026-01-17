dosya = open("rehber.dat","a")
print("KAYIT EKRANI")
ad = input("Ad giriniz:")
nu = input("Telefon giriniz:")
okul = input("Okulunuzu giriniz:Lise/Üniversite")


dosya.write(f"\n{ad}#{nu}")
