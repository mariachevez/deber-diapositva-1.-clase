# funciones de cadenas
mensaje = 'hola ' + 'mundo ' + 'Python'
men1=mensaje.split()
men2=' '.join(men1)
print(mensaje[0],mensaje[0:4],men1,men2)
print(mensaje.find("mundo"), mensaje.lower())