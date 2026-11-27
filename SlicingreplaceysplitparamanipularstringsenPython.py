#indice     0123456789... los espacios tambien cuentan
practica = "Esto es un texto"

print(practica[0]) 
print(practica[0:4])
print(practica[:7]) # aqui es desde el pricio hasta el indice 7 sin incluirlo
print(practica[5:]) # aqui es desde el indice 5 hasta el final incluyendo el 5

curso = "este curso de de java"
print(curso)
print(curso.replace("java", "python")) # reemplaza java por python
print(curso)

textodiv = curso.split(" ") # separa el texto en palabras y lo guarda en una lista
print(textodiv)

#normalizacion

texto2 = "EstE TEXTO eS un TeXto "
print("texto" in texto2 )
print("texto" in texto2.lower()) # normaliza el texto a minusculas y luego busca la palabra