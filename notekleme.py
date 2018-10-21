
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

import function_support as fs
global s_id


class YeniNot:
    def __init__(self, tepe=None):
        tepe.geometry("491x450+224+192")
        tepe.title("YeniNot")
        tepe.configure(background="#d9d9d9")

        self.Canvas1 = Canvas(tepe)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

        self.bag_liste = ScrolledListBox(self.Canvas1)
        self.bag_liste.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.35)
        self.bag_liste.bind('<<ListboxSelect>>', self.kayit_id)
        baglantilar = fs.DbAct.bag_arama()
        for baglanti in baglantilar:
            self.bag_liste.insert(END, baglanti)

        self.not_alani = ScrolledText(self.Canvas1)
        self.not_alani.place(relx=0.35, rely=0.0, relheight=0.95, relwidth=0.65)

        self.kayit = Button(self.Canvas1)
        self.kayit.place(relx=0.35, rely=0.95, height=22, width=319)
        self.kayit.configure(text='''Kayıt''', command=self.kayit_func)

    def kayit_func(self):
        yazi = self.not_alani.get("1.0", END)
        fs.DbAct.not_kayit(s_id, yazi)
        global root
        root.destroy()

    @staticmethod
    def kayit_id(evt):
        global s_id
        s_id = fs.DbAct.curselet(evt)
        print(s_id)


class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
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
        '''Hide and show scrollbar as needed.'''
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
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def start():
    global top, root
    # noinspection PyRedeclaration
    root = Tk()
    top = YeniNot(root)
    root.mainloop()


if __name__ == '__main__':
    start()

