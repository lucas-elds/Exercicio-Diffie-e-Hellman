import random

n = 47
g = 3

x = random.randint(1, 99)
a = (g**x) % n

sa = None


def aliceEnvia():
  arquivo = open("canal-inseguro.txt", "a")
  arquivo.write(f"{a}\n")
  arquivo.close()


def aliceCalcula():
  arquivo = open("canal-inseguro.txt", "r")
  conteudo = arquivo.read()
  arquivo.close()

  b = int(conteudo.split("\n")[1])
  sa = (b**x) % n
  return (sa)
