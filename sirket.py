def şirket():
    print("""
efendi yazılım
          
1. bilgiler
          
2. isciler         
cıkam icin q
""")
    
sirket_isim = "efendi yazılım"
sirket_müdürü = "efe efendioğlu"
sirket_konumu = "sakarya/karasu"

while True:
    şirket()
    secim = input("yapacağınız islemin numarasını giriniz:")
    if secim == "q":
        print("iyi günler")
        break
    elif secim == "1":
        print("ismi: {}\nmüdürü: {}\nkonum: {}".format(sirket_isim,sirket_müdürü,sirket_konumu))
    elif secim == "2":
        def calısanlar():
            print("""
calısanlar
                  
1. ahmet
""")
        calısanlar()
        calısan_secim = input("calısan seciniz:")
        if calısan_secim == "1":
            def ahmetin_paneli():
                print("""
***********************************
          ahmet dedeoğlu

1. bilgiler

2. maaş değistirme

3.dil ekle

Çıkmak için 'q' tuşlayın
***********************************
""")

                isim = "ahmet dedeoğlu"
                bildiği_diller = ["python", "java"]
                maaş = 50

                while True:
                    ahmetin_paneli()
                    panel_cevap = input("Lütfen seçiminizin numarasını giriniz (çıkmak için 'q'): ")

                    if panel_cevap == "q":
                        print("Programdan çıkılıyor...")
                        break
                    elif panel_cevap == "1":
                        print("İsim: {}\nMaaş: {}\nBildiği diller: {}".format(isim, maaş, ', '.join(bildiği_diller)))
                    elif panel_cevap == "2":
                        maaş_değistirme = int(input("Yeni maaşı yazın: "))
                        maaş = maaş_değistirme
                    elif panel_cevap == "3":
                        yeni_dil = input("Yeni dil giriniz: ")
                        bildiği_diller.append(yeni_dil)
                    else:
                        print("Lütfen doğru bir seçenek giriniz.")
