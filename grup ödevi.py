def ana_menu():
    """
    Kullanıcıya ana menüyü sunar.
    """
    print("\nAna Menü:")
    print("1. İnternet Bağlantı Sorunları")
    print("2. Bilgisayar Açılmıyor")
    print("3. Ekran Sorunları")
    print("4. Yazılım ve Uygulama Sorunları")
    print("5. Donanım Sorunları")
    print("6. Çıkış")

def internet_baglanti_sorunlari():
    """
    İnternet bağlantı sorunları için adım adım çözüm.
    """
    print("\nİnternet Bağlantı Sorunları")
    print("Lütfen aşağıdaki adımları dikkatlice takip edin:")
    
    sorular = [
        "1. Modem fişe takılı mı?",
        "2. Modem ışıkları yanıyor mu?",
        "3. Modemin yanındaki tuşa bastınız mı?",
        "4. Bilgisayarınızın Wi-Fi bağlantısını kontrol ettiniz mi?",
        "5. İnternete başka bir cihaz bağlanabiliyor mu?",
        "6. İnternet sağlayıcınızda bir kesinti olabilir mi?"
    ]
    
    for soru in sorular:
        print(soru)
    
    secim = input("\nHangi adımda takıldığınızı yazın (1-6): ")
    
    if secim == "1":
        print("\nModem fişinin düzgün şekilde takıldığından emin olun. Fişin çıkmış olması durumunda tekrar takın.")
        print("Bazı modemler fişin tam takılmaması halinde bağlantı sağlanmayabilir.")
    elif secim == "2":
        print("\nModem ışıkları yanmalı. Modemin üzerindeki ışıkları kontrol edin.")
        print("Eğer ışıklar yanmıyorsa, modeminizin güç kaynağını kontrol edin.")
        print("Işıklar yanıyorsa, bağlantı problemi modemden değil, bilgisayar veya kablolu bağlantıdan kaynaklanabilir.")
    elif secim == "3":
        print("\nModem üzerindeki reset tuşuna basın. Bu, çoğu bağlantı problemini çözebilir.")
        print("Resetleme işlemi birkaç dakika sürebilir, lütfen bekleyin.")
    elif secim == "4":
        print("\nWi-Fi bağlantınızı kontrol edin. Bilgisayarınızın Wi-Fi'ye bağlı olduğundan emin olun.")
        print("Wi-Fi bağlantısı zayıf veya kesilmiş olabilir. Modem ve bilgisayar arasında mesafe varsa, Wi-Fi sinyali zayıflayabilir.")
    elif secim == "5":
        print("\nDiğer cihazlarla interneti test edin. Eğer diğer cihazlar bağlanabiliyorsa, bilgisayarınızda bir problem olabilir.")
        print("Eğer diğer cihazlar da bağlanamıyorsa, modem veya internet servis sağlayıcınızla iletişime geçmek gerekebilir.")
    elif secim == "6":
        print("\nİnternet servis sağlayıcınızın internet sitesi üzerinden kesinti olup olmadığını kontrol edin.")
        print("Bir kesinti durumunda, servis sağlayıcınızın problemi çözmesi birkaç saat sürebilir.")
    else:
        print("Geçersiz seçim. Lütfen doğru bir adım numarası girin.")

    sonuclar = input("\nSorununuz çözülmüş gibi görünüyor mu? (Evet/Hayır): ").strip().lower()
    if sonuclar == "evet":
        print("Sorununuzun çözüldüğüne sevindim! İyi günler dilerim.")
        return True  
    elif sonuclar == "hayır":
        print("Müşteri temsilcimizle iletişime geçmeniz gerekebilir. Yardım almak için lütfen bizimle iletişime geçin.")
    else:
        print("Geçersiz cevap. Lütfen 'Evet' veya 'Hayır' yanıtını verin.")
    return False  

def bilgisayar_acilmiyor():
    """
    Bilgisayar açılmıyor sorununa çözüm önerileri.
    """
    print("\nBilgisayar Açılmıyor")
    print("Lütfen aşağıdaki adımları dikkatlice takip edin:")
    
    sorular = [
        "1. Bilgisayarın güç kablosunu kontrol edin.",
        "2. Bilgisayarınızın güç düğmesine basılı tutun.",
        "3. Farklı bir prizde deneyin.",
        "4. Bilgisayarınızda herhangi bir kısa devre olup olmadığını kontrol edin.",
        "5. RAM veya hard disk bağlantılarını kontrol ettiniz mi?",
        "6. Güç kaynağı (PSU) ile ilgili bir problem olabilir mi?"
    ]
    
    for soru in sorular:
        print(soru)
    
    secim = input("\nHangi adımda takıldığınızı yazın (1-6): ")
    
    if secim == "1":
        print("\nGüç kablosunun düzgün şekilde takıldığından emin olun.")
        print("Bazı bilgisayarlar, güç kablosu tam takılmadığında açılmayabilir.")
    elif secim == "2":
        print("\nBilgisayarınızın güç düğmesine basılı tutarak 10 saniye kadar bekleyin. Bu işlem bilgisayarınızın sıfırlanmasını sağlayabilir.")
    elif secim == "3":
        print("\nBilgisayarınızı farklı bir prizde deneyin. Eğer bilgisayarınız hala açılmıyorsa, güç kaynağınızda sorun olabilir.")
    elif secim == "4":
        print("\nKısa devre veya donanım hatası ihtimaline karşı bilgisayarınızın iç kısmını kontrol edin.")
        print("Eğer bir donanım sorunu olduğunu düşünüyorsanız, teknik servise başvurmanız gerekebilir.")
    elif secim == "5":
        print("\nRAM veya hard disk bağlantılarını kontrol edin. Bu bileşenlerin yerinden çıkmış olması bilgisayarınızın açılmamasına yol açabilir.")
        print("Donanım hatası olup olmadığını anlamak için RAM'i çıkarıp tekrar takmayı deneyin.")
    elif secim == "6":
        print("\nGüç kaynağınızın (PSU) düzgün çalışıp çalışmadığını kontrol edin.")
        print("Güç kaynağında bir arıza varsa, bu bilgisayarın açılmamasına neden olabilir.")
    else:
        print("Geçersiz seçim. Lütfen doğru bir adım numarası girin.")

    sonuclar = input("\nSorununuz çözülmüş gibi görünüyor mu? (Evet/Hayır): ").strip().lower()
    if sonuclar == "evet":
        print("Sorununuzun çözüldüğüne sevindim! İyi günler dilerim.")
        return True  
    elif sonuclar == "hayır":
        print("Müşteri temsilcimizle iletişime geçmeniz gerekebilir. Yardım almak için lütfen bizimle iletişime geçin.")
    else:
        print("Geçersiz cevap. Lütfen 'Evet' veya 'Hayır' yanıtını verin.")
    return False  

def ekran_sorunlari():
    """
    Ekran sorunları için çözüm önerileri.
    """
    print("\nEkran Sorunları")
    print("Lütfen aşağıdaki adımları dikkatlice takip edin:")
    
    sorular = [
        "1. Ekranınızda hiç görüntü var mı?",
        "2. Kablolar düzgün bir şekilde bağlı mı?",
        "3. Ekran parlaklık seviyesini kontrol ettiniz mi?",
        "4. Bilgisayarınız harici bir ekrana bağlı mı?",
        "5. Ekranınızda renk bozulmaları veya ekran titremesi var mı?",
        "6. Ekranda donmalar veya siyah ekran problemi var mı?"
    ]
    
    for soru in sorular:
        print(soru)
    
    secim = input("\nHangi adımda takıldığınızı yazın (1-6): ")
    
    if secim == "1":
        print("\nEkranınızda hiç görüntü yoksa, ekranın düzgün bir şekilde açıldığından emin olun.")
        print("Ekranınızın bağlı olduğundan ve çalıştığından emin olun. Eğer ekranınızda hala görüntü yoksa, başka bir ekranla test edin.")
    elif secim == "2":
        print("\nKabloların düzgün şekilde bağlandığını kontrol edin. HDMI veya VGA kablosu yerinden çıkmış olabilir.")
    elif secim == "3":
        print("\nEkran parlaklık seviyesini kontrol edin. Ekranınızın parlaklığı sıfır olabilir.")
        print("Parlaklık seviyesini ayarlamayı deneyin.")
    elif secim == "4":
        print("\nBilgisayarınız harici bir ekrana bağlıysa, ekranın doğru şekilde seçildiğinden emin olun.")
        print("Ekran kartı ayarlarını kontrol edin ve harici ekranı doğru şekilde yapılandırın.")
    elif secim == "5":
        print("\nRenk bozulmaları veya ekran titremeleri, ekran kartı arızası veya ekranın kendisinden kaynaklanıyor olabilir.")
        print("Ekranınızda titreme veya renk bozulması varsa, ekran kartınızı veya ekranınızı test edin.")
    elif secim == "6":
        print("\nSiyah ekran sorunu yaşıyorsanız, bilgisayarınızın başlatma işlemleri sırasında bir hata olabilir.")
        print("Ekranın açılmaması halinde donanım arızası veya ekranın arızalanmış olması olasılıkları vardır.")
    else:
        print("Geçersiz seçim. Lütfen doğru bir adım numarası girin.")

    sonuclar = input("\nSorununuz çözülmüş gibi görünüyor mu? (Evet/Hayır): ").strip().lower()
    if sonuclar == "evet":
        print("Sorununuzun çözüldüğüne sevindim! İyi günler dilerim.")
        return True  
    elif sonuclar == "hayır":
        print("Müşteri temsilcimizle iletişime geçmeniz gerekebilir. Yardım almak için lütfen bizimle iletişime geçin.")
    else:
        print("Geçersiz cevap. Lütfen 'Evet' veya 'Hayır' yanıtını verin.")
    return False  

def yazilim_ve_uygulama_sorunlari():
    """
    Yazılım ve uygulama sorunları için çözüm önerileri.
    """
    print("\nYazılım ve Uygulama Sorunları")
    print("Lütfen aşağıdaki adımları dikkatlice takip edin:")
    
    sorular = [
        "1. Yazılım güncellemeleri yapılmış mı?",
        "2. Uygulama açılmıyor veya donuyor mu?",
        "3. Bilgisayarınızda yeterli depolama alanı var mı?",
        "4. Yazılım hatası veya çökme sorunu yaşanıyor mu?",
        "5. Antivirüs veya güvenlik yazılımı bilgisayarınızı engelliyor mu?"
    ]
    
    for soru in sorular:
        print(soru)
    
    secim = input("\nHangi adımda takıldığınızı yazın (1-5): ")
    
    if secim == "1":
        print("\nYazılım güncellemelerinin yapılması, programların uyumsuzluk sorunlarını giderebilir.")
        print("Güncellemeleri yüklemek için bilgisayarınızda Windows Update veya ilgili uygulama güncelleyicisini kullanın.")
    elif secim == "2":
        print("\nUygulama açılmıyorsa, uygulamayı yeniden başlatmayı deneyin.")
        print("Uygulama hala açılmıyorsa, uygulamanın güncel sürümünü indirip yeniden yüklemeyi deneyin.")
    elif secim == "3":
        print("\nYeterli depolama alanınız olmadığında yazılımlar düzgün çalışmayabilir.")
        print("Bilgisayarınızda gereksiz dosyaları silerek depolama alanı açmayı deneyin.")
    elif secim == "4":
        print("\nYazılımın çökmesi durumunda, yazılımın güncel sürümünü kontrol edin ve gerekirse yeniden yükleyin.")
        print("Eğer sürekli çökme sorunları devam ediyorsa, yazılım geliştiricilerine hata raporu gönderebilirsiniz.")
    elif secim == "5":
        print("\nAntivirüs yazılımı bazen programları engelleyebilir. Antivirüs yazılımınızı geçici olarak devre dışı bırakıp uygulamayı tekrar başlatmayı deneyin.")
    else:
        print("Geçersiz seçim. Lütfen doğru bir adım numarası girin.")

    sonuclar = input("\nSorununuz çözülmüş gibi görünüyor mu? (Evet/Hayır): ").strip().lower()
    if sonuclar == "evet":
        print("Sorununuzun çözüldüğüne sevindim! İyi günler dilerim.")
        return True  
    elif sonuclar == "hayır":
        print("Müşteri temsilcimizle iletişime geçmeniz gerekebilir. Yardım almak için lütfen bizimle iletişime geçin.")
    else:
        print("Geçersiz cevap. Lütfen 'Evet' veya 'Hayır' yanıtını verin.")
    return False  

def donanim_sorunlari():
    """
    Donanım sorunları için çözüm önerileri.
    """
    print("\nDonanım Sorunları")
    print("Lütfen aşağıdaki adımları dikkatlice takip edin:")
    
    sorular = [
        "1. Bilgisayarınızın ekranında garip bir görüntü var mı?",
        "2. Ses çıkmıyor veya donma problemi yaşıyor musunuz?",
        "3. Bilgisayarınızın fanı çalışıyor mu?",
        "4. Bilgisayarınızda artan ısınma problemi var mı?",
        "5. Hard disk veya SSD arızası belirtisi görüyor musunuz?"
    ]
    
    for soru in sorular:
        print(soru)
    
    secim = input("\nHangi adımda takıldığınızı yazın (1-5): ")
    
    if secim == "1":
        print("\nEkranda garip görüntüler görüyorsanız, ekran kartınızı veya ekran bağlantılarını kontrol edin.")
        print("Ekran kartı arızalıysa, değiştirilmesi gerekebilir.")
    elif secim == "2":
        print("\nSes çıkmıyorsa, ses kartı veya ses kablolarını kontrol edin.")
        print("Ses kartı arızalıysa, donanım değişimi gerekebilir.")
    elif secim == "3":
        print("\nBilgisayarın fanının çalışıp çalışmadığını kontrol edin. Eğer fan çalışmıyorsa, bilgisayar aşırı ısınabilir.")
        print("Fanın düzgün çalışıp çalışmadığını kontrol edin ve gerekirse temizlik yapın.")
    elif secim == "4":
        print("\nBilgisayarınızın aşırı ısındığını düşünüyorsanız, fanı temizlemeyi ve soğutma sistemini kontrol etmeyi deneyin.")
        print("Aşırı ısınma, donanım arızalarına neden olabilir.")
    elif secim == "5":
        print("\nHard disk veya SSD'nizin arızalandığını düşünüyorsanız, veri kaybı riski olabilir.")
        print("Hard disk veya SSD'yi test etmek için yazılımlar kullanın.")
    else:
        print("Geçersiz seçim. Lütfen doğru bir adım numarası girin.")

    sonuclar = input("\nSorununuz çözülmüş gibi görünüyor mu? (Evet/Hayır): ").strip().lower()
    if sonuclar == "evet":
        print("Sorununuzun çözüldüğüne sevindim! İyi günler dilerim.")
        return True 
    elif sonuclar == "hayır":
        print("Müşteri temsilcimizle iletişime geçmeniz gerekebilir. Yardım almak için lütfen bizimle iletişime geçin.")
    else:
        print("Geçersiz cevap. Lütfen 'Evet' veya 'Hayır' yanıtını verin.")
    return False  

def chatbot():
    """
    Kullanıcıya seçenekler sunarak problemleri çözme süreci.
    """
    print("Hoş geldiniz! Lütfen yaşadığınız sorunu seçin.")
    
    while True:
        ana_menu()
        secim = input("\nBir seçenek girin (1-6): ")

        if secim == "1":
            if internet_baglanti_sorunlari():
                break
        elif secim == "2":
            if bilgisayar_acilmiyor():
                break
        elif secim == "3":
            if ekran_sorunlari():
                break
        elif secim == "4":
            if yazilim_ve_uygulama_sorunlari():
                break
        elif secim == "5":
            if donanim_sorunlari():
                break
        elif secim == "6":
            print("Çıkılıyor... İyi günler!")
            break
        else:
            print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")

chatbot()