#se puede pasar inormación a las funciones mediante el uso de parámetros.
def hi(name, lastname, edad, ci):
    print("Hi,",name, lastname,"edad:", edad,"ci:", ci)
hi("Isaac", "Mena","19", "1727...")
hi("Pam", "Navas","21","1727....")
hi("Carlos","Cortez", "23","1234..")
#También se puede usar funciones con datos solicitados por teclado
a=input("Ingrese su nombre: ")
b= input("Ingrese su apellido: ")
c= input("Ingrese su edad: ")
d= input("Ingrese su número de cédula:")
hi(a,b,c,d)