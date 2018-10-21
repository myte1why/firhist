import sqlite3
import names as n
import datetime
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import re


def set_tk_var():
    global che44
    che44 = StringVar()
    global combobox
    combobox = StringVar()
    global spinbox
    spinbox = StringVar()



db = sqlite3.connect(n.db_name)


class DbAct:
    @staticmethod
    def create():
        db.execute('CREATE TABLE IF NOT EXISTS baglanti (_id INTEGER PRIMARY KEY, ad TEXT, soyad TEXT)')
        db.execute('CREATE TABLE IF NOT EXISTS iletisim(_id INTEGER PRIMARY KEY,b_id INTEGER, cep_tel TEXT, '
                   'is_tel TEXT, ev_tel TEXT, adres TEXT, e_posta TEXT)')
        db.execute('CREATE TABLE IF NOT EXISTS notlar (_id INTEGER PRIMARY KEY, b_id INTEGER, alinan_not TEXT)')
        db.execute('CREATE TABLE IF NOT EXISTS randevu (_id INTEGER PRIMARY KEY, b_id INTEGER, gun TEXT, ay TEXT, '
                   'yil TEXT, saat TEXT, dakika TEXT)')
        '''# test girdileri
        for i in range(100):
            i += 1
            db.execute("INSERT INTO baglanti('ad', 'soyad') VALUES('{}', '{}')".format('deneme'+str(i),'kişisi'+str(i)))

            db.execute("INSERT INTO iletisim('b_id', 'cep_tel', 'ev_tel','ev_tel', 'adres', 'e_posta') VALUES({}, 
            " "'{}','{}', '{}','{}', '{}')".format(i,'5788995' + str(i), '2127778899' + str(i), '2127778899' + str(
            i), 'test adresi' + str(i), 'test'+str(i) + '@g.com')) for j in range(12): db.execute("INSERT INTO 
            randevu ('b_id', 'gun', 'ay', 'yil', 'saat', 'dakika') VALUES({0}, {1}, {1},'2018','10','30')".format(i,
            j)) db.execute("INSERT INTO notlar ('b_id', 'alinan_not') VALUES('{}', '{}')".format(i, str(j) * 100)) '''
        db.commit()

    @staticmethod
    def reader(table: str, items_to_read: list = '*', items_to_compare: list = None, compare_list: list = None):
        """

        :items_to_compare: []
        """
        if compare_list is None:
            compare_list = []
        if items_to_compare is None:
            items_to_compare = []
        query = 'SELECT '
        if items_to_read != '*':
            for i in items_to_read:
                query += i + ','
            query = query[:-1]
        else:
            query += '*'
        query += ' FROM {}'.format(table)
        if items_to_compare:
            query += ' WHERE '
            for i in range(len(items_to_compare)):
                a = items_to_compare[i]
                b = compare_list[i]
                query += a + ' = ' + b + ','
            query = query[:-1]
        ending = db.execute(query)
        return ending.fetchall()

    @staticmethod
    def randevuliste():
        global db
        gun = str(datetime.datetime.now().date().day)
        ay = str(datetime.datetime.now().date().month)
        yil = str(datetime.datetime.now().date().year)
        params = (gun, ay, yil)
        db = sqlite3.connect(n.db_name)
        sql = '''SELECT baglanti.ad, baglanti.soyad, randevu.saat, randevu.dakika FROM randevu INNER JOIN baglanti ON 
        randevu.b_id = baglanti._id WHERE gun = ? AND ay = ? AND yil = ? '''
        randevular = db.execute(sql, params).fetchall()
        return randevular

    @staticmethod
    def bagekle(ad, soyad, cep_tel, ev_tel, is_tel, adres, e_posta, gun, ay, yil,  saat, dakika):
        global db
        params = (ad, soyad)
        db = sqlite3.connect(n.db_name)
        insert_baglanti = '''INSERT INTO baglanti VALUES(NULL,?, ?)'''
        db.execute(insert_baglanti, params)
        db.commit()
        # _id al
        cur = db.execute('SELECT max(_id) FROM baglanti')
        _id = cur.fetchone()[0]

        # iletisim kısmına _id ile iletişim bilgilerini ekle
        params = (_id, cep_tel, ev_tel, is_tel, adres, e_posta)
        insert_iletisim = '''INSERT INTO iletisim VALUES(NULL, ?, ?,?, ?, ?, ?)'''
        db.execute(insert_iletisim, params)
        db.commit()
        # randevu kısmına _ile randevu girişi yap
        params = (_id, gun, ay, yil,  saat, dakika)
        insert_randevu = '''INSERT INTO randevu VALUES(NULL, ?, ?, ?, ?, ?, ?)'''
        db.execute(insert_randevu, params)
        db.commit()

    @staticmethod
    def bag_arama():
        sql = 'select * from baglanti'
        baglantilar = db.execute(sql).fetchall()
        return baglantilar

    @staticmethod
    def bag_arama_birey(evt):

        selected_id = DbAct.curselet(evt)
        baglanti = '''SELECT * FROM baglanti WHERE _id = {} '''.format(selected_id)
        iletisim = '''SELECT cep_tel, is_tel, ev_tel, adres, e_posta  FROM iletisim WHERE b_id = {} '''\
            .format(selected_id)
        randevular = '''SELECT gun, ay, yil, saat, dakika FROM randevu WHERE b_id = {} '''.format(selected_id)
        notlar = '''SELECT alinan_not FROM notlar WHERE b_id = {} '''.format(selected_id)
        baglanti_donus = db.execute(baglanti).fetchone()
        iletisim_donus = db.execute(iletisim).fetchone()
        notlar_donus = db.execute(notlar).fetchall()
        randevu_donus = db.execute(randevular).fetchall()
        dat = ()
        s_id, ad, soyad = baglanti_donus
        tam_ad = ad + ' ' + soyad
        cep_tel, is_tel, ev_tel, adres, e_posta = iletisim_donus
        cep_tel = 'Cep Telefonu : ' + cep_tel
        is_tel = 'İş Telefonu : ' + str(is_tel)
        ev_tel = 'Ev Telefonu : ' + ev_tel
        adres = 'Adres : ' + adres
        e_posta = 'E posta : ' + e_posta
        randevu_name = 'Randevu Geçmişi : '
        dat += tam_ad, cep_tel, is_tel, ev_tel, adres, e_posta, randevu_name
        for i in randevu_donus:
            gun, ay, yil, saat, dakika = i
            yazi = '{}/{}/{} Tarihinde saat {}:{}\'da randevu kaydı vardır.'.format(gun, ay, yil, saat, dakika)
            dat = dat + (yazi,)
        notlar_ayrac = '{} kişisi için alınan notlar :'.format(tam_ad)
        dat += (notlar_ayrac,)
        for i in notlar_donus:
            alinan_not = i[0]
            yazi = '{}'.format(alinan_not)
            dat += (yazi,)
        return dat

    @staticmethod
    def randevu_kayit(_id, gun, ay, yil,  saat, dakika):
        params = (_id, gun, ay, yil,  saat, dakika)
        insert_randevu = '''INSERT INTO randevu VALUES(NULL, ?, ?, ?, ?, ?, ?)'''
        db.execute(insert_randevu, params)
        db.commit()

    @staticmethod
    def curselet(evt):
        widget = evt.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        value = str(value)
        r_id = int(re.search(r'\d+', value).group())
        return r_id

    @staticmethod
    def not_kayit(_id, yazi):
        db.execute("INSERT INTO notlar ('b_id', 'alinan_not') VALUES('{}', '{}')".format(_id, yazi))
        db.commit()
