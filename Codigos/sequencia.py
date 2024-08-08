import numpy
import time


def sequencia(vetor, chave):

    for i, value in enumerate(vetor):
        if value == chave:
            return i
    return None


def main():

    n = 10000
    q = 100

    vetor = numpy.random.randint(0, 2147483647, n)
    vetor_chaves = numpy.random.randint(0, 2147483647, q)
    start_time = time.time()

    for chave in vetor_chaves:
        sequencia(vetor, chave)
    execution_time = time.time() - start_time

    print(f"Tempo de execução: {execution_time} segundos")


if __name__ == '__main__':

    main()
