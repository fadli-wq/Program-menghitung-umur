import datetime as dt
tanggal=int(input('tanggal:'))
bulan=int(input('bulan:'))
tahun=int(input('tahun:'))
tanggal_lahir=dt.date(tahun,bulan,tanggal)
print(f'\ntanggal lahir anda adalah: {tanggal_lahir}')
print(f'hari nya adalah: {tanggal_lahir:%A}')

hari_ini=dt.date.today()
print('hari ini tanggal:',hari_ini)
umur_hari=hari_ini-tanggal_lahir
umur_tahun=umur_hari.days//365
umur_bulan_sisa=(umur_hari.days%365)//30
print('Umur anda adalah: ',umur_tahun,'tahun',umur_bulan_sisa,'bulan')