#Dvourozměrné pole
pole = [[1, 2, 3], [5, 6, 7], [10, 11, 12]]
#Změnění na druhém řádku a druhém sloupku čísla na 105
pole [1][1] = 105
#Nový řádek
radek1 = [13, 14, 15]
pole.append(radek1)
#Nový sloupec
for i in range(len(pole)):
  pole[i].append(1)
#Výsledek
for i in range(len(pole)):
  print(pole[i])
