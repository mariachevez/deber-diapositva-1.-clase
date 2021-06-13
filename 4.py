# Comprehension – [var for var in datos condicion]
[car for car in['a','e','i','o','u'] if car not in('a','i','o')]
edad,_peso = 50, 70.5
nombres = 'Daniel Vera'
dirDomiciliaria= "Chile y Guayaquil"
Tipo_sexo = 'M'
civil = True
usuario = ('dchiki','1234','chiki@gmail.com')
materias = ['Programacion Web','PHP','POO']
docente = {'nombre':'Daniel','edad':50}
print("""Mi nombre es {}, tengo {}      años""".format(nombres,edad))
print(usuario,materias,docente)
import math
num1, num2, num, men = 12.572,  15.4,  4,  '1234'
print(math.ceil(num1), '\t',math.floor(num1))
print(round(num1,1),'\t',type(num),'\t',type(men))