def sezar_sifrele(metin, kaydirma):
    sifreli_metin = ""
    for harf in metin:
        if harf.isalpha():  # Sadece harfleri şifrele
            ascii_base = ord('A') if harf.isupper() else ord('a')
            sifreli_harf = chr((ord(harf) - ascii_base + kaydirma) % 26 + ascii_base)
            sifreli_metin += sifreli_harf
        else:
            sifreli_metin += harf  # Harf değilse değiştirme
    return sifreli_metin

def sezar_coz(metin, kaydirma):
    return sezar_sifrele(metin, -kaydirma)  # Şifreleme işlemini tersine çevir

def menu():
    while True:
        print("\n- Sezar Şifreleme Menüsü -")
        print("1. Şifreleme")
        print("2. Şifre Çözme")
        print("3. Çıkış")
        secim = input("Seçiminiz (1/2/3): ")

        if secim == "1":
            metin = input("Şifrelenecek metni girin: ")
            kaydirma = int(input("Kaydırma sayısını girin (örn. 3): "))
            print("Şifrelenmiş metin:", sezar_sifrele(metin, kaydirma))
        elif secim == "2":
            metin = input("Çözülecek metni girin: ")
            kaydirma = int(input("Kaydırma sayısını girin (aynı sayıyı kullanın): "))
            print("Çözülmüş metin:", sezar_coz(metin, kaydirma))
        elif secim == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")

menu()