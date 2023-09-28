from datetime import datetime, date

now = datetime.now()

zaman = now.strftime("%H:%M:%S")
tarih = date.today()
gün = tarih.strftime("%d/%m/%Y")

toplam = zaman + " " + gün

Kullaniciler = {
    "Ahmed": ["Ahmed", "1234", 100],
    "Zeynep": ["Zeynep", "4321", 0],
    "Alberto": ["Alberto", "4422", 0]
}
Admin = {
    "İbrahim": ["İbrahim", 1122]
}
Gecmis = {
    "Ahmet": {
        "Para_çekme": [],
        "Para_yatırma": [],
        "Para_transfer": []
    },
    "Zeynep": {
        "Para_çekme": [],
        "Para_yatırma": [],
        "Para_transfer": []
    },
    "Alberto": {
        "Para_çekme": [],
        "Para_yatırma": [],
        "Para_transfer": []
    }
}


def Para_transferi(Kullanici_adi):
    print(f"Para transferi menüsüne hoşgeldin {Kullanici_adi}")
    print("Geri dönmek için '000' yazınız.")
    while True:
        Para_trasnfer_kisi = input("Transfer işlemi gerçekleştirmek istediğin kişiyi seç\n>>>")
        Para_transferi_miktar = int(input("Transfer etmek istediğin miktarı gir\n>>>"))
        if Para_trasnfer_kisi not in Kullaniciler and Para_trasnfer_kisi == Kullaniciler[Kullanici_adi][0]:
            print("Transfer etmek isediğiniz kişi bulunamadı!")
        else:
            if Para_transferi_miktar < Kullaniciler[Kullanici_adi][2]:
                Kullaniciler[Kullanici_adi][2] = Kullaniciler[Kullanici_adi][2] - Para_transferi_miktar
                Kullaniciler[Para_trasnfer_kisi][2] = Kullaniciler[Para_trasnfer_kisi][2] + Para_transferi_miktar
                print("Transfer işlemi başarılı.")
                return Kullanici_menu(Kullanici_adi)
            elif Para_transferi_miktar == "000" or Para_trasnfer_kisi == 000:
                return Kullanici_menu(Kullanici_adi)


def Para_yatırma(Kullanici_adi):
    print(f"Para yatırma menüsüne hoşgeldin {Kullanici_adi}")
    print("Geri dönmek için '000' yazınız.")
    while True:
        Para_yatırma_secim = int(input("Lütfen Yatırmak istediğin miktarı gir\n>>>"))
        if Para_yatırma_secim == 000:
            return Kullanici_menu(Kullanici_adi)
        else:
            Kullaniciler[Kullanici_adi][2] = Kullaniciler[Kullanici_adi][2] + Para_yatırma_secim
            print("Para yatırma işlemi başarılı.")
            return Kullanici_menu(Kullanici_adi)


def Para_cekme(Kullanici_adi):
    print(f"Para çekme menüsüne hoşgeldin {Kullanici_adi}")
    print("Geri dönmek için '000' yazınız.")
    while True:
        Para_cekme_secim = int(input("Lütfen çekmek istediğin miktarı gir\n>>>"))
        if Para_cekme_secim < Kullaniciler[Kullanici_adi][2]:
            Kullaniciler[Kullanici_adi][2] = Kullaniciler[Kullanici_adi][2] - Para_cekme_secim
            print("Para çekme işlemi başarılı.")
            return Kullanici_menu(Kullanici_adi)
        elif Para_cekme_secim == 000:
            return Kullanici_menu()
        else:
            print("Çekmek istediğiniz bakiye miktarı hesabınızdaki bakiye miktarından fazla.\nLütfen tekrar deneyiniz.")


def Hesap_bilgileri(Kullanici_adi):
    print(f"-------İSTİNYE BANK-------\n{zaman, gün}\n--------------------------")
    print(f"Kullanıcı adı: {Kullaniciler[Kullanici_adi][0]}")
    print(f"Şifre: {Kullaniciler[Kullanici_adi][1]}")
    print(f"Bakiye: {Kullaniciler[Kullanici_adi][2]}")
    print("---------------------------")
    print("Hesap geçmişi:")
    print("---------------------------")
    return Kullanici_menu(Kullanici_adi)


def Kullanici_menu(Kullanici_adi):
    while True:
        Kullnaici_menu_secim = input(
            f"Kullanıcı menüsüne hoşgeldin {Kullanici_adi}\nLütfen yapmak istediğiniz işlemi seç.\n1-)Para çekme\n2-)Para yatırma\n3-)Para transferi\n4-)Hesap bilgileri\n5-)Çıkış\n>>>")
        if Kullnaici_menu_secim == "1":
            return Para_cekme(Kullanici_adi)
        elif Kullnaici_menu_secim == "2":
            return Para_yatırma(Kullanici_adi)
        elif Kullnaici_menu_secim == "3":
            return Para_transferi(Kullanici_adi)
        elif Kullnaici_menu_secim == "4":
            return Hesap_bilgileri(Kullanici_adi)
        elif Kullnaici_menu_secim == "5":
            print("Geri dönülüyor.")
            return Kullanici_secim()
        else:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")


def Kullanici_giris():
    print("Geri dönmek için 'abort' yazınız.")
    while True:
        Kullanici_adi = input("Kullanıcı adı: ")
        Kullanici_sifre = input("Şifre: ")
        if Kullanici_adi in Kullaniciler and Kullanici_sifre == Kullaniciler[Kullanici_adi][1]:
            print("Kullanıcı girişi başarılı.\nMenüye aktarılıyorsunuz.")
            return Kullanici_menu(Kullanici_adi)
        elif Kullanici_adi == "abort" or Kullanici_sifre == "abort":
            return Kullanici_secim()
        else:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")


def admin_menu(admin_adi):
    while True:
        admin_menu_secim = input(
            f"Admin menüsüne hoşgeldin {admin_adi}\nLütfen yapmak istediğiniz işlemi seç.\n1-)Kullanıcı ekleme\n2-)Kullanıcı silme\n3-)Tüm kullanıcıları görüntüle\n4-)Çıkış\n>>>")
        if admin_menu_secim == "1":
            print("Kullanıcı ekleme bölümüne aktarılıyorsunuz.")
        elif admin_menu_secim == "2":
            print("Kullanıcı silme bölümüne aktarılıyorsunuz.")
        elif admin_menu_secim == "3":
            print("tüm kullanıcıları göürntüleme bölümüne aktarılıyorusunuz.")
        elif admin_menu_secim == "4":
            print("Çıkış yapılıyor.")
            return Kullanici_secim()
        else:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")


def Admin_giris():
    print("Geri dönmek için 'abort' yazınız.")
    while True:
        admin_adi = input("Kullanıcı adı: ")
        admin_sifre = input("Şifre: ")
        if admin_adi == "İbrahim" and admin_sifre == "1122":
            print("Yönetici girişi başarılı.\nMenüye aktarılıyorsunuz.")
            return admin_menu(admin_adi)
        elif admin_adi == "abort" or admin_sifre == "abort":
            return Kullanici_secim()
        else:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")


def Kullanici_secim():
    while True:
        secim = input("1-)Admin giriş\n2-)Kullanıcı giriş\n3-)Çıkış\n>>>")
        if secim == "1":
            return Admin_giris()
        elif secim == "2":
            return Kullanici_giris()
        elif secim == "3":
            return giris()
        else:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")


def giris():
    print(
        f"   _______________\n  /                 \ \n /     İSTANBUL      \ \n | {zaman, gün} |\n \                / \n  \_______________/")
    while True:
        giris = input("1.Giriş\n2.Çıkış\n>>>")
        if giris == "1":
            return Kullanici_secim()
        elif giris == "2":
            break
        else:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")


giris()
