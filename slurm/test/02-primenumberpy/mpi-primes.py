from mpi4py import MPI
import concurrent.futures
import math
import time
import os
import resource


def is_prime(n):
    """Verifica se un numero è primo."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(start, end):
    """Trova i numeri primi in un dato intervallo utilizzando il multithreading."""
    primes = []
    for n in range(start, end):
        if is_prime(n):
            primes.append(n)
    return primes


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    max_number = 1000000000

    interval = (max_number // size) + 1
    start = rank * interval + 1
    end = min((rank + 1) * interval, max_number + 1)

    start_time = time.time()  # Avvio del timer

    primes = find_primes(start, end)

    all_primes = comm.gather(primes, root=0)

    if rank == 0:
        end_time = time.time()  # Fine del timer
        all_primes_flat = [prime for sublist in all_primes for prime in sublist]
        print(f"Trovati {len(all_primes_flat)} numeri primi fino a {max_number}.")
        print(f"Tempo di elaborazione: {end_time - start_time:.2f} secondi.")
        print(f"Numero di processi MPI utilizzati: {size}")
        print(f"Versione di MPI: {MPI.get_vendor()}, MPI {MPI.Get_version()}")


if __name__ == "__main__":
    main()
