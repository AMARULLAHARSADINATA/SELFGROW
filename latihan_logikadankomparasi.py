print('SOAL NOMOR 1\n----------0++++++++++5------------8+++++++++11\n')

inputuser = float(input('masukan angka diantara 0><5 or 8><11 :'))

lebihdarinol = (inputuser > 0)
print('Lebih dari 0 :', lebihdarinol)

kurangdarilima = (inputuser < 5)
print('Kurang dari 5 :', kurangdarilima)

cek = lebihdarinol and kurangdarilima
print('angka yang dimasukan :', cek)

lebihdari8 = (inputuser > 8)
print('Lebih dari 8 :', lebihdari8)

kurangdari11 = (inputuser < 5)
print('Kurang dari 11 :', kurangdari11)

correct = lebihdari8 and kurangdari11
print('angka yang dimasukan :', correct)

hasil = cek or correct
print('hasil seluruh angka yang dimasukan :', hasil )

print('\nSOAL NOMOR 2\n+++++++++++0----------5++++++++++++8-------------11\n')

inputuser = float(input('masukan angka diantara <0 or 5><8 or 11> :'))

kurangdari0 = (inputuser < 0)
print('angka yang dimasukan :', kurangdari0)

lebihdari5 = (inputuser > 5)
print('Lebih dari 5 :', lebihdari5)

kurangdari8 = (inputuser < 8)
print('Kurang dari 8 :', kurangdari8)

cek = lebihdari5 and kurangdari8
print('angka yang dimasukan :', cek)

lebihdari11 = (inputuser > 11)
print('angka yang dimasukan :', lebihdari11)

hasil = kurangdari0 or cek or lebihdari11
print('hasil seluruh angka yang dimasukan :', hasil )
