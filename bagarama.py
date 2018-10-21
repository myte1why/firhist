import function_support as fs
from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class BagArama:
    def __init__(self, topbagarama=None):

        topbagarama.geometry("650x426+296+211")
        topbagarama.title("Bağlantı Arama")

        baglantilar = fs.DbAct.bag_arama()
        self.bagliste = ScrolledListBox(topbagarama)
        self.bagliste.place(relx=0, rely=0, relheight=0.83, relwidth=0.4)
        self.bagliste.bind('<<ListboxSelect>>', self.kisi_select)
        for baglanti in baglantilar:
            self.bagliste.insert(END, baglanti)

        self.ayrinti = ScrolledListBox(topbagarama)
        self.ayrinti.place(relx=0.45, rely=0, relheight=0.86, relwidth=0.51)

    @staticmethod
    def kisi_select(evt):
        test = fs.DbAct.bag_arama_birey(evt)
        top.ayrinti.delete(0, 'end')
        for i in test:
            top.ayrinti.insert(END, i)


class AutoScroll(object):
    # Configure the scrollbars for a widget.

    def __init__(self, masteritem):
        #  Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            # noinspection PyBroadException
            vsb = ttk.Scrollbar(masteritem, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(masteritem, orient='horizontal', command=self.xview)

        try:
            # noinspection PyBroadException
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0,  row=0,  sticky='nsew')
        try:
            vsb.grid(column=1,  row=0,  sticky='ns')
        except:
            pass
        hsb.grid(column=0,  row=1,  sticky='ew')

        masteritem.grid_columnconfigure(0, weight=1)
        masteritem.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of masteritem  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                      | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                      + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config',  'configure'):
                setattr(self, meth, getattr(masteritem, meth))

    @staticmethod
    def _autoscroll(sbar):
        # Hide and show scrollbar as needed.
        def wrapped(first,  last):
            first,  last = float(first),  float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first,  last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    # Creates a ttk Frame with a given master,  and use this new frame to place the scrollbars and the widget.
    def wrapped(cls,  master,  **kw):
        """

        :param cls:
        :type master: object
        """
        container = ttk.Frame(master)
        return func(cls,  container,  **kw)
    return wrapped


class ScrolledListBox(AutoScroll,  Listbox):
    # standard Tkinter Text widget with scrollbars that will automatically show/hide as needed.
    @_create_container
    def __init__(self, masteritem, **kw):
        Listbox.__init__(self, masteritem, **kw)
        AutoScroll.__init__(self, masteritem)


def start():
    global top
    root = Tk()
    fs.set_tk_var()
    top = BagArama(root)
    root.mainloop()


if __name__ == '__main__':
    start()
