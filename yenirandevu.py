import function_support as fs
import kisi as ki
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


class YeniRandevu:

    @staticmethod
    def kisi():
        ki.start()

    @staticmethod
    def kayit(evt):
        global selected_id
        selected_id = fs.DbAct.curselet( evt )
        return selected_id

    def kayit_end(self):
        global selected_id
        gun = self.gun.get()
        ay = self.ay.get()
        yil = self.yil.get()
        saat = self.saat.get()
        dakika = self.dakika.get()
        fs.DbAct.randevu_kayit(selected_id, gun, ay, yil,  saat, dakika)

    def __init__(self, yenirandevutop=None):
        yenirandevutop.geometry("305x529+310+32")
        yenirandevutop.title("Yeni Randevu")

        self.randevuAnaFrame = LabelFrame(yenirandevutop)
        self.randevuAnaFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.randevuAnaFrame.configure(relief=GROOVE, text='''Randevu Kayıt''')
        self.baglantilistlabel = Label(self.randevuAnaFrame)
        self.baglantilistlabel.place(relx=0, rely=0)
        self.baglantilistlabel.configure(text='''Bağlantılar listesi''')

        self.baglantiliste = ScrolledListBox(self.randevuAnaFrame)
        self.baglantiliste.place(relx=0, rely=0, relheight=0.8, relwidth=1)
        self.baglantiliste.bind('<<ListboxSelect>>', YeniRandevu.kayit)
        baglantilar = fs.DbAct.bag_arama()
        for baglanti in baglantilar:
            self.baglantiliste.insert(END, baglanti)

        self.yenibaglanti = Button(self.randevuAnaFrame)
        self.yenibaglanti.place(relx=0, rely=0.8, relheight=0.05, relwidth=1)
        self.yenibaglanti.configure(text='''Yeni bağlantı''', command=self.kisi)

        self.tarih = LabelFrame(self.randevuAnaFrame)
        self.tarih.place(relx=0, rely=0.85, relheight=0.09, relwidth=0.65)
        self.tarih.configure(relief=GROOVE, text='''Tarih''')

        self.gun = Spinbox(self.tarih, from_=1.0, to=30.0)
        self.gun.place(relx=0, rely=0, relheight=0.94, relwidth=0.24)

        self.ay = Spinbox(self.tarih, from_=1.0, to=100.0)
        self.ay.place(relx=0.25, rely=0, relheight=0.94, relwidth=0.5)

        self.yil = Spinbox(self.tarih, from_=1.0, to=100.0)
        self.yil.place(relx=0.75, rely=0, relheight=0.94, relwidth=0.24)

        self.saatlabel = LabelFrame(self.randevuAnaFrame)
        self.saatlabel.place(relx=0.66, rely=0.85, relheight=0.09, relwidth=0.34)
        self.saatlabel.configure(relief=GROOVE, text='''saat''')

        self.saat = Spinbox(self.saatlabel, from_=0.0, to=23.0)
        self.saat.place(relx=0, rely=0, relheight=0.94, relwidth=0.45)

        self.saatayrac = Label(self.saatlabel)
        self.saatayrac.place(relx=0.45, rely=0, relheight=0.94, relwidth=0.10)
        self.saatayrac.configure(text=''':''')

        self.dakika = Spinbox(self.saatlabel, from_=0.0, to=59.0)
        self.dakika.place(relx=0.55, rely=0, relheight=0.94, relwidth=0.45)

        self.randevukayit = Button(self.randevuAnaFrame)
        self.randevukayit.place(relx=0, rely=0.94, relwidth=1, relheight=0.06)
        self.randevukayit.configure(text='''randevu kaydet''', command=self.kayit_end)




# noinspection PyBroadException
class AutoScroll(object):

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                      | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                      + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped


class ScrolledListBox(AutoScroll, Listbox):
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def start():
    global top
    # noinspection PyRedeclaration
    root = Tk()
    top = YeniRandevu(root)
    root.mainloop()


if __name__ == '__main__':
    start()
