estado = 0
validado = True

with open('linguagem.txt') as f:
  numero = f.readline()
  lines = f.readlines()


def s0(lista):
  if not lista: return True
  x = lista.pop(0)
  if x == 'a':
    return s1(lista)
  elif x == 'b':
    return s0(lista)

  return True
 

def s1(lista):
  if not lista: return False
  x = lista.pop(0)
  if x == 'b':
    return s2(lista)

  return False
  

def s2(lista):
  if not lista: return False
  x = lista.pop(0)
  if x == 'b':
    return s0(lista)


def valido(palavra):
  return s0(list(palavra))

      
def main(lines):
  for x, z in enumerate(lines):
    
    if (valido(lines[x])):
      print(f"{z.strip()}: pertence")
    else:
      print(f'{z.strip()}: não pertence')

main(lines)
  
