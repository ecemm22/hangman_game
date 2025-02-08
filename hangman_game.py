import tkinter as tk
import random

pencere = tk.Tk() # tk() fonksiyonu ile ana pencere(root window) oluşturdum
pencere.title("Adam Asmaca Oyunu") #pencerenin başlığı

canvas = tk.Canvas(pencere, width=350, height=400) #pencere boyutunu ayarladım
canvas.pack() #canvası arayüze ekler

def cubugu_çiz():
    canvas.create_line(50, 350, 250, 350, width=3)  # zemin
    canvas.create_line(100, 350, 100, 50, width=3)  # direk
    canvas.create_line(100, 50, 200, 50, width=3)  # üst çizgi
    canvas.create_line(200, 50, 200, 100, width=3)  # ip

def kafa_ciz():
    canvas.create_oval(180, 100, 220, 140, width=3)

def govde_ciz():
    canvas.create_line(200, 140, 200, 220, width=3)

def kol_ciz():
    canvas.create_line(200, 160, 170, 190, width=3)  # sol kol
    canvas.create_line(200, 160, 230, 190, width=3)  # sağ kol

def bacak_ciz():
    canvas.create_line(200, 220, 170, 270, width=3)  # sol bacak
    canvas.create_line(200, 220, 230, 270, width=3)  # sağ bacak

cubugu_çiz()

kelimeler =["ecem","oduncu","bilgisayar","mühendis"]
secilen_kelime =random.choice(kelimeler) #rastgele kelime seçer


gizli_kelime= ["_"] * len(secilen_kelime)

yanlış_hak= 6
doğru_harfler= set()
yanlış_harfler= set()

kelime_goster = tk.Label(pencere, text=' '.join(gizli_kelime), font=("Arial", 20)) #label bilgiyi ekranda göstermek için kullanılır
kelime_goster.pack(pady=10) #pack() etiketi ekrana yazdırır,pady bileşenler arasında boşluk bırakır

sonuc_mesaji = tk.Label(pencere, text="", font=("Arial", 14))
sonuc_mesaji.pack(pady=10)

harf_giris = tk.Entry(pencere, font=("Arial", 14)) # entry() kullanıcıdan harf girişi alır
harf_giris.pack(pady=5)

def tahmin_et():
    global yanlış_hak
    harf_tahmini = harf_giris.get().lower()
    harf_giris.delete(0, tk.END)  # Girişi 0dan tk.END'e kadar (sonuna kadar) siler,temizler

    if not harf_tahmini.isalpha() or len(harf_tahmini) != 1:
        sonuc_mesaji.config(text="Lütfen sadece bir harf girin.")
        return

    if harf_tahmini in doğru_harfler or harf_tahmini in yanlış_harfler:
        sonuc_mesaji.config(text="Bu harfi zaten denediniz.")
        return

    if harf_tahmini in secilen_kelime:
        doğru_harfler.add(harf_tahmini)
        for i, harf in enumerate(secilen_kelime):
            if harf == harf_tahmini:
                gizli_kelime[i] = harf_tahmini
        kelime_goster.config(text=" ".join(gizli_kelime))
        sonuc_mesaji.config(text="Tahmin doğru.")
    else:
        yanlış_hak -= 1
        yanlış_harfler.add(harf_tahmini)
        sonuc_mesaji.config(text=f"Tahmin yanlış.Kalan hak: {yanlış_hak}")
        if yanlış_hak == 5:
            kafa_ciz()
        elif yanlış_hak == 4:
            govde_ciz()
        elif yanlış_hak == 3:
            kol_ciz()
        elif yanlış_hak == 2:
            bacak_ciz()


    if "_" not in gizli_kelime:
        sonuc_mesaji.config(text="Tebrikler,kazandınız.")
        harf_giris.config(state=tk.DISABLED)
    elif yanlış_hak == 0:
        sonuc_mesaji.config(text=f"Kaybettiniz.Kelime: {secilen_kelime}")
        harf_giris.config(state=tk.DISABLED)

tahmin_butonu = tk.Button(pencere, text="Tahmin Et", command=tahmin_et, font=("Arial", 14))
tahmin_butonu.pack(pady=20)

pencere.mainloop() 
