from os import system
from os import system

system('cls')

elsovaltozo = 12
 
 #string konkatenáció
kiir_1 = "A változó értéke: " + str(elsovaltozo)
print(kiir_1)

#fomattált sztring 1.verzió
kiir_1 = "A változó értéke: {}"  .format(elsovaltozo)
print(kiir_1)

#formattált sztring 2.verzió
kiir_1 = f"A változó értéke: " (elsovaltozo)
print(kiir_1)

kiir_1 ="A változás értéke {0}" .format(elsovaltozo)
print(kiir_1)