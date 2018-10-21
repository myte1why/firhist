import names as n
import kisi as ki
from function_support import DbAct
import bagarama
import yenirandevu as yr
import notekleme as nt

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


class HosGeldiniz:

    @staticmethod
    def kisi():
        ki.start()

    @staticmethod
    def bag_arama():
        bagarama.start()

    @staticmethod
    def yeni_randevu():
        yr.start()

    @staticmethod
    def yeni_not():
        nt.start()

    def __init__(self, page):
        font9 = n.font9
        page.geometry("409x450+571+124")
        page.title("Hoş geldiniz")
        page.configure(background="#d9d9d9")
        self.Label1 = Label(page)
        self.Label1.place(relx=0.05, rely=0.0, height=61, width=377)
        self.Label1.configure(background="#d9d9d9",
                              font=font9,
                              relief=GROOVE,
                              text=n.selam)
        self.Labelframe1 = LabelFrame(page)
        self.Labelframe1.place(relx=0.05, rely=0.14, relheight=0.86, relwidth=0.49)
        self.Labelframe1.configure(background="#d9d9d9",
                                   font=font9,
                                   relief=GROOVE,
                                   text=n.gunluk_program)
        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.05, rely=0.01, height=21, width=31)
        self.Label2.configure(background="#d9d9d9",
                              font=font9,
                              text=n.saat)
        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.25, rely=0.01, height=21, width=147)
        self.Label3.configure(background="#d9d9d9",
                              font=font9,
                              text=n.randevu)
        item_y = 0.06
        for randevu in DbAct.randevuliste():
            self.Label4 = Label(self.Labelframe1)
            self.Label4.place(relx=0.05, rely=item_y, height=21, width=37)
            self.Label4.configure(background="#d9d9d9",
                                  font=font9,
                                  text='{}:{}'.format(randevu[2], randevu[3]))

            self.Label5 = Label(self.Labelframe1)
            self.Label5.place(relx=0.25, rely=item_y, height=21, width=147)
            self.Label5.configure(font=font9,
                                  text=randevu[0] + ' ' + randevu[1])
            item_y += 0.05
        self.Button1 = Button(page)
        self.Button1.place(relx=0.56, rely=0.16, height=24, width=166)
        self.Button1.configure(background="#d9d9d9",
                               font=font9,
                               highlightbackground="#d9d9d9",
                               text=n.bag_ekle,
                               command=self.kisi)
        self.Button2 = Button(page)
        self.Button2.place(relx=0.56, rely=0.22, height=24, width=166)
        self.Button2.configure(background="#d9d9d9",
                               font=font9,
                               highlightbackground="#d9d9d9",
                               text=n.bag_ara,
                               command=self.bag_arama)
        self.Button3 = Button(page)
        self.Button3.place(relx=0.56, rely=0.28, height=24, width=166)
        self.Button3.configure(background="#d9d9d9",
                               font=font9,
                               highlightbackground="#d9d9d9",
                               text=n.yeni+' '+n.randevu,
                               command=self.yeni_randevu)
        self.Not_kayit = Button(page)
        self.Not_kayit.place(relx=0.56, rely=0.34, height=24, width=166)
        self.Not_kayit.configure(background="#d9d9d9",
                                 font=font9,
                                 highlightbackground="#d9d9d9",
                                 text='Not Kayıt',
                                 command=self.yeni_not)


def start():
    global top
    DbAct.create()
    # noinspection PyRedeclaration
    root = Tk()
    top = HosGeldiniz(root)
    root.mainloop()


if __name__ == '__main__':
    start()
