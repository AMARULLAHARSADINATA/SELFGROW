# Latihan konversi satuan temperatur

print("=====PROGRAM KONVERSI TEMPERATUR====")
print("=====>>>>Celcius")

celcius = float(input("Masukan suhu dalam celcius : "))

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah :", reamur,"Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah :", fahrenheit,"Fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah :", kelvin,"Kelvin")


print("=====>>>>Reamur")

reamur = float(input("masukan suhu dalam reamur : "))

# celcius
celcius = (5/4) * reamur
print("suhu dalam kelvin adalah :", kelvin,"Kelvin")

#fahrenheit
fahrenheit = ((9/5) * reamur) + 32
print("suhu dalam fahrenheit adalah :", fahrenheit,"Fahrenheit")

# kelvin
kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin adalah :", kelvin,"Kelvin")


print("=====>>>>Fahrenheit")

fahrenheit = float(input("masukan suhu dalam fahrenheit :"))

# celcius
celcius = (5/9) * (fahrenheit - 32)
print("suhu dalam celcius adalah :", celcius,"Celcius")

#reamur
reamur = (4/9) * (fahrenheit - 32)
print("suhu dalam reamur adalah :", reamur,"Reamur")

# kelvin
kelvin = (celcius + 273)
print("suhu dalam kelvin adalah :", kelvin,"Kelvin")


print("=====>>>>Kelvin")

kelvin = float(input("masukan suhu dalam kelfvin : "))

# celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah :", celcius,"Celcius")

#reamur
reamur = (4/5) * (kelvin - 273)
print("suhu dalam reamur adalah :", reamur,"Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah :", fahrenheit,"Fahrenheit")
