def ogrencisil():   

    dosya = open("rehber.dat")
    okunan = dosya.readlines()
    silinecek = input("Silinecek ad veya okul?")


    yeniSekli = ""
    for a in okunan:
        temizi = a.strip()
        bilgiler = temizi.split("#")
        if silinecek not in bilgiler:        
            yeniSekli += f"{bilgiler[0]}#{bilgiler[1]}\n"


    print(yeniSekli)
    dosya.close()
    dosya = open("rehber.dat","w")
    dosya.write(yeniSekli)
