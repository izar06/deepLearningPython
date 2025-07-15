#Variable merupakan tempat untuk menyimpan data

#Menaruh / assignment nilai
a = 10
x = 5
length = 1000

#Pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai length = ", length)

#Penamaan
#tidak boleh ada spasi di penamaan variable
#tidak boleh ada angka di depan nama variable
nilai_y = 15 #Dengan menggunakan underscore
juta10 = 1000000 #ini boleh
nilaiX = 17.9 #ini boleh

#Pemanggilan kedua
print("Nilai a = ", a)
a = 7 
print("Nilai a = ", a)

#assignment indirect
b = a
print("Nilai b = ", b)

### Sesi 2 Tipe Data ###
#tipe data: angka satuan (int)
data_integer = 1
print(data_integer)
print("- bertipe : ", type(data_integer))

#tipe data: angka dengan koma (float)
data_float = 1.5
print(data_float)
print("- bertipe : ", type(data_float))

#tipe data: kumpulan karakter (string)
data_string = "!Paydia6"
print(data_integer)
print("- bertipe : ", type(data_string))

#tipe data: biner true/false (boolean)
data_bool = True
print(data_bool)
print("- bertipe : ", type(data_bool))

## Tipe data khusus
# Bilangan kompleks
data_kompleks = complex(5,10)
print(data_kompleks)
print("- bertipe : ", type(data_kompleks))


# Tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(5.10)
print(data_c_double)
print("- bertipe : ", type(data_c_double))