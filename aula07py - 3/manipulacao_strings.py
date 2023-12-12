def inverter(texto):
   return texto[::-1]


def contar(texto):
   contador = 0
   for i in texto:
      contador += 1
   return contador

def pali(texto):
   if texto == texto[::-1]:
      return "Essa palavra é um Palídromo"
   else:
      return "Essa palavra não é um Palídromo"