try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import function_support
import sys
import datetime


class YeniKisi:

    def __init__(self, topbar=None):
        topbar.geometry("254x402+624+233")
        topbar.title("yeni kişi")
        topbar.configure(background="#d9d9d9")

        self.kisi_bilgileri = LabelFrame(topbar)
        self.kisi_bilgileri.place(relx=0.0, rely=0.0, relheight=0.86, relwidth=0.98)
        self.kisi_bilgileri.configure(relief=FLAT, text='''kişi bilgileri''', background="#d9d9d9")

        self.ad = Label(self.kisi_bilgileri)
        self.ad.place(relx=0.01, rely=0.01, height=21, width=20)
        self.ad.configure(background="#d9d9d9", text='''ad''')

        self.soyad = Label(self.kisi_bilgileri)
        self.soyad.place(relx=0.01, rely=0.06, height=21, width=39)
        self.soyad.configure(background="#d9d9d9", text='''soyad''')

        self.iletisim = Label(self.kisi_bilgileri)
        self.iletisim.place(relx=0.01, rely=0.12)
        self.iletisim.configure(text='''iletişim''', background="#d9d9d9")

        self.cep_label = Label(self.kisi_bilgileri)
        self.cep_label.place(relx=0.01, rely=0.17, height=21, width=73)
        self.cep_label.configure(background="#d9d9d9", text='''cep telefonu''')

        self.ev_label = Label(self.kisi_bilgileri)
        self.ev_label.place(relx=0.01, rely=0.22, height=21, width=65)
        self.ev_label.configure(background="#d9d9d9", text='''ev telefonu''')

        self.is_label = Label(self.kisi_bilgileri)
        self.is_label.place(relx=0.01, rely=0.27, height=21, width=63)
        self.is_label.configure(background="#d9d9d9", text='''İş telefonu''')

        self.e_posta_label = Label(self.kisi_bilgileri)
        self.e_posta_label.place(relx=0.01, rely=0.32, height=21, width=49)
        self.e_posta_label.configure(background="#d9d9d9", text='''E-posta''')

        self.adres_label = Label(self.kisi_bilgileri)
        self.adres_label.place(relx=0.01, rely=0.37, height=21, width=38)
        self.adres_label.configure(background="#d9d9d9", text='''Adres''')

        self.ad_input = Entry(self.kisi_bilgileri)
        self.ad_input.place(relx=0.28, rely=0.01, height=20, relwidth=0.72)

        self.soyad_input = Entry(self.kisi_bilgileri)
        self.soyad_input.place(relx=0.28, rely=0.06, height=20, relwidth=0.72)

        self.cep_input = Entry(self.kisi_bilgileri)
        self.cep_input.place(relx=0.38, rely=0.17, height=20, relwidth=0.6)

        self.ev_input = Entry(self.kisi_bilgileri)
        self.ev_input.place(relx=0.38, rely=0.22, height=20, relwidth=0.6)

        self.is_input = Entry(self.kisi_bilgileri)
        self.is_input.place(relx=0.38, rely=0.27, height=20, relwidth=0.6)

        self.e_posta_input = Entry(self.kisi_bilgileri)
        self.e_posta_input.place(relx=0.38, rely=0.32, height=20, relwidth=0.6)

        self.adres_input = Text(self.kisi_bilgileri)
        self.adres_input.place(relx=0.01, rely=0.45, relheight=0.36, relwidth=0.98)
        self.adres_input.configure(wrap=WORD)

        self.randevu_tarihi_label = LabelFrame(self.kisi_bilgileri)
        self.randevu_tarihi_label.place(relx=0.01, rely=0.81, height=65, relwidth=1)
        self.randevu_tarihi_label.configure(relief=GROOVE, text='''Randevu tarihi''', background="#d9d9d9")

        self.Labelframe4 = LabelFrame(self.randevu_tarihi_label)
        self.Labelframe4.place(relx=0, rely=0, relheight=0.95, relwidth=0.60)
        self.Labelframe4.configure(text='''Gün''', background="#d9d9d9")

        self.gun_input = Spinbox(self.Labelframe4, from_=1, to=31, repeatdelay=1)
        self.gun_input.place(relx=0.0, rely=0.01, height=20, width=30)

        self.ay_input = Spinbox(self.Labelframe4, from_=1, to=12)
        self.ay_input.place(relx=0.24, rely=0.01, height=20, width=60)

        yil = StringVar()
        yil_now = datetime.datetime.now().date().year
        yil.set(yil_now)
        self.yil_input = Spinbox(self.Labelframe4, from_="2000", to="2099", textvariable=yil)
        self.yil_input.place(relx=0.70, rely=0.01, height=20, width=40)

        self.Labelframe5 = LabelFrame(self.randevu_tarihi_label)
        self.Labelframe5.place(relx=0.61, rely=0, relheight=0.95, relwidth=0.38)
        self.Labelframe5.configure(text='''saat''', background="#d9d9d9")

        self.saat_input = Spinbox(self.Labelframe5, from_=1.0, to=100.0)
        self.saat_input.place(relx=0.06, rely=0.01, height=20, width=30)
        self.saat_input.configure(from_="0", to="23", )

        self.dakika_input = Spinbox(self.Labelframe5, from_=1.0, to=100.0)
        self.dakika_input.place(relx=0.56, rely=0.01, height=20, width=30)
        self.dakika_input.configure(from_="0", to="59")

        self.ayrac_saat = Label(self.Labelframe5)
        self.ayrac_saat.place(relx=0.44, rely=0.01, height=21, width=9)
        self.ayrac_saat.configure(background="#d9d9d9", text=''':''')

        self.Button1 = Button(topbar)
        self.Button1.place(relx=0.04, rely=0.87, height=20, width=68)
        self.Button1.configure(background="#d9d9d9", text='''Kaydet''', command=self.kayit)

        self.Button2 = Button(topbar)
        self.Button2.place(relx=0.31, rely=0.87, height=20, width=166)
        self.Button2.configure(background="#d9d9d9", text='''Kaydet ve Yeni Kayıt Sayfası''')

    def kayit(self):
        ad = self.ad_input.get()
        soyad = self.soyad_input.get()
        cep_tel = self.cep_input.get()
        ev_tel = self.ev_input.get()
        is_tel = self.is_input.get()
        adres = self.adres_input.get("1.0", END)
        e_posta = self.e_posta_input.get()
        gun = self.gun_input.get()
        ay = self.ay_input.get()
        yil = self.yil_input.get()
        saat = self.saat_input.get()
        dakika = self.dakika_input.get()
        function_support.DbAct.bagekle(ad, soyad, cep_tel, ev_tel, is_tel, adres, e_posta, gun, ay, yil,  saat, dakika)
        global root
        root.destroy()

def start():
    global top, root
    # noinspection PyRedeclaration
    root = Tk()
    top = YeniKisi(root)
    root.mainloop()


if __name__ == '__main__':
    start()
