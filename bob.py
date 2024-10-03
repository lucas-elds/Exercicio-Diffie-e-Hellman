import random

n = 47
g = 3

y = random.randint(1, 99)
b = (g**y) % n


def bobEnvia():
  arquivo = open("canal-inseguro.txt", "a")
  arquivo.write(f"{b}\n")
  arquivo.close()


def bobCalcula():
  arquivo = open("canal-inseguro.txt", "r")
  conteudo = arquivo.read()
  arquivo.close()

  a = int(conteudo.split("\n")[0])
  sb = (a**y) % n
  return (sb)
