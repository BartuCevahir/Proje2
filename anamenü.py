def anamenü():
    print("╔══════════════════════════════════╗")
    print("║      KÜTÜPHANE                   ║")
    print("╠══════════════════════════════════╣")
    print("║   1-Öğrenci Ekle                 ║")
    print("║   2-Kayıtları Listele            ║")
    print("║   3-Kayıtları Düzelt             ║")
    print("║   4-Öğrenci Sil                  ║")
    print("║   5-Çıkış                        ║")
    print("║                                  ║")
    print("║         Seçiminiz nedir?         ║")
    print("╚══════════════════════════════════╝")

    seçim=input()

    if seçim == "1":
        import modüller.ogrenciekle
        modüller.ogrenciekle.ogrencieklemenü()
    if seçim == "2":
        import modüller.kayıtlistele
        modüller.kayıtlistele.kayıtlistele()
    if seçim == "3":
        import modüller.kayıtlarıdüzelt
        modüller.kayıtlarıdüzelt.kayıtlarduzelt()
    if seçim == "4":
        import modüller.ogrencisil
        modüller.ogrencisil.ogrencisil()
    anamenü()

anamenü()