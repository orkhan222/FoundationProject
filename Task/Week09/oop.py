# meshularin idare olunmasi
# sirketlerin idare olunmasi
# satislarin idare olunmasi

# mesulun eksikizi

# (ad,novu,ceksi,qiymeti)

class Meyve():
    def __init__(self,_ad,_nov,_ceki,_qiymet,filename):
        self.ad=_ad
        self.nov=_nov
        self.ceki=_ceki
        self.qiymet=_qiymet
        self.bazayaElaveEt(filename)
    def deyerHesabla(self):
        return self.ceki*self.qiymet
    def melumatlariGoster(self):
        return f'Meyveinin adi: {self.ad}\r\nMeyvenin Novu : {self.nov}\r\nMeyvenin Miqdari : {self.ceki}\r\nMeyvenin qiyemti: {self.qiymet}\r\n------------------------------------\r\n'
    def bazayaElaveEt(self,filename):
        file=open('data.text','a')
        file.write(self.melumatlariGoster())





# meyveler=[
#     Meyve('QizlEhmed','Alma',12,3),
#     Meyve('Palmit','Alma',32,5),
#     Meyve('Nar Armud','Armud',22,4),
#     Meyve('Nar Armud','Armud',45,5)
#     ]

# eh bahli meyvenin miqdari
# anbarimdaki umini mailin qiymetini


# def enBahaliMeyveniTap():
#     qiymetler=[]
#     for meyve in meyveler:
#         qiymetler.append(meyve.qiymet)
#     for meyve in meyveler:
#         if meyve.qiymet==max(qiymetler):
#             print(meyve.melumatlariGoster())



def totalMeblegiHesabla():
    totalMebleg=0
    for meyve in meyveler:
        totalMebleg+=meyve.deyerHesabla()
    return totalMebleg

def meyveDaxilEt(filename):
    ad=input('Meyveini adini daxil et: ')
    nov=input('Meyveini novunu daxil et: ')
    ceki=input('Meyveini cekisini daxil et: ')
    qiymet=input('Meyveini qiymetini daxil et: ')
    meyve=Meyve(ad,nov,ceki,qiymet,filename)

meyveDaxilEt('date.text')


