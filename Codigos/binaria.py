import time
import numpy

def busca_binaria_recursiva(vetor, chave, base, topo):

  if base > topo:
    return None

  meio = (base + topo) // 2

  if vetor[meio] == chave:
    return meio
  elif vetor[meio] < chave:
    return busca_binaria_recursiva(vetor, chave, meio + 1, topo)
  else:
    return busca_binaria_recursiva(vetor, chave, base, meio - 1)

def busca_binaria(vetor, chave):

  if not vetor:
    return None

  return busca_binaria_recursiva(vetor, chave, 0, len(vetor) - 1)



def main():
    n = 10000
    q = 100

    vetor = numpy.random.randint(0, 2147483647, n)
    vetor_chaves = numpy.random.randint(0, 2147483647, q)

    start_time = time.time()
    vetor.sort()
    for chave in vetor_chaves:
        busca_binaria(vetor, chave)
    execution_time = time.time() - start_time

    print(f"Tempo de execução: {execution_time} segundos")


if __name__ == '__main__':

    main()
