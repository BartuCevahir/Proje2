def kayıtlarduzelt():    

    dosya = open("rehber.dat")
    okunan = dosya.readlines()
    degisecek = input("Değişecek ad veya okul?          ")
    yenisi    = input("Yerine gelecek yeni ad veya okul?")
    yeniSekli = ""
    for a in okunan:
        temizi = a.strip()
        bilgiler = temizi.split("#")
        if degisecek in bilgiler:  
        degisecekIndex = bilgiler.index(degisecek)    
        bilgiler[degisecekIndex] = yenisi  
    
        yeniSekli += f"{bilgiler[0]}#{bilgiler[1]}\n"


    print(yeniSekli)
    dosya.close()
    dosya = open("rehber.dat","w")
    dosya.write(yeniSekli)
