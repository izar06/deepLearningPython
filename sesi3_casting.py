# Casting
# Casting merupakan operator untuk merubah tipe data ke tipe lainnya
print("====INTEGER====")
data_integer = 1
data_float = float(data_integer)
data_string = str(data_integer)
data_boolean = bool(data_integer) #akan false jika nilai int bernilai 0
print("data = ", data_float, ",type = ", type(data_integer))
print("data = ", data_string, ",type = ", type(data_string))
print("data = ", data_boolean, ",type = ", type(data_boolean))

#Data Float
print("====FLOAT====")
data_float = 1.0
data_int = int(data_float) #akan dibulatkan kebawah
data_string = str(data_float)
data_boolean = bool(data_float) #akan false jika nilai int bernilai 0
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_string, ",type = ", type(data_string))
print("data = ", data_boolean, ",type = ", type(data_boolean))

#Data String
print("====STRING====")
data_string = "10"
data_int = int(data_string) #string harus berupa angka
data_float = float(data_string) #string harus berupa angka
data_boolean = bool(data_string) #akan false jika nilai int bernilai 0
print("data = ", data_int, ",type = ", type(data_integer))
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_boolean, ",type = ", type(data_boolean))


#Data Boolean
print("====BOOLEAN====")
data_boolean = True
data_int = int(data_boolean) 
data_float = float(data_boolean)
data_string = str(data_boolean) #akan false jika nilai int bernilai 0
print("data = ", data_int, ",type = ", type(data_integer))
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_string, ",type = ", type(data_string))