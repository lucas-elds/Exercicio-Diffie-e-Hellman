import alice
import bob


def limpaArquivo():
  arquivo = open("canal-inseguro.txt", "w")
  arquivo.write("")
  arquivo.close()


limpaArquivo()

alice.aliceEnvia()
bob.bobEnvia()

print(f"Chave Alice: {alice.aliceCalcula()}")
print(f"Chave Bob: {bob.bobCalcula()}")

if (alice.aliceCalcula() == bob.bobCalcula()):
  print(f"As chaves coincidem!")
else:
  print(f"As chaves não coincidem.")
