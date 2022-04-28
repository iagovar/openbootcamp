"""
Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
"""

inputString = input("Por favor, introduce una lista de países separados por comas:")
stripedString = inputString.strip()
listedString = stripedString.split(",")
uniqueString = list(set(listedString))
uniqueString.sort()

finalString = ""
for country in uniqueString:
	if country == uniqueString[0]:
		finalString += country
	else:
		finalString += ", " + country


print(finalString)