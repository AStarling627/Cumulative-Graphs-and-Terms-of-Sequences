import numpy as np
import matplotlib.pyplot as plt

p = input('Would you like to see all the terms of your sequence, a cumulative graph or both? ')
seq = input('What is your sequence? (if it is a certain one specify e.g the prime numbers) ')


def primeSeq():
    uBound = int(input('Up to what integer? '))
    primes = []
    nPrimes = [0, 0]
    natural = np.linspace(0, uBound, uBound + 1)
    for num in range(2, uBound + 1):
        if num > 1:
            for i in range(2, int(np.sqrt(num) + 1)):
                if num % i == 0:
                    break
            else:
                if num == 4:
                    nPrimes.append(2)
                    continue
                else:
                    primes.append(num)
        else:
            continue
        nPrimes.append(len(primes))
    if 'both' or 'Both' in p:
        print(*primes, sep=', ')
        plt.plot(natural, nPrimes)
        plt.xlabel('Natural Numbers')
        plt.ylabel('Number of Primes')
        plt.show()
    elif 'graph' or 'Graph' or 'cumulative' or 'Cumulative' in p:
        plt.plot(natural, nPrimes)
        plt.xlabel('Natural Numbers')
        plt.ylabel('Number of Primes')
        plt.show()
    elif 'terms' or 'Terms' or 'numbers' or 'Numbers' in p:
        print(*primes, sep=', ')
    else:
        print('ERROR: are you sure that this is one of the options? ')


def triSeq():
    uBound = int(input('Up to what integer? '))
    tris = []
    nTris = []
    natural = np.linspace(0, uBound, uBound + 1)
    for num in range(0, uBound + 1):
        testNum = 1 + (8 * num)
        sqrtVal = np.sqrt(testNum)
        if int(sqrtVal) ** 2 == testNum:
            tris.append(num)
            nTris.append(len(tris))
        else:
            nTris.append(len(tris))
            continue
    if 'both' or 'Both' in p:
        print(*tris, sep=', ')
        plt.plot(natural, nTris)
        plt.xlabel('Natural Numbers')
        plt.ylabel('Number of Triangulars')
        plt.show()
    elif 'graph' or 'Graph' or 'cumulative' or 'Cumulative' in p:
        plt.plot(natural, nTris)
        plt.xlabel('Natural Numbers')
        plt.ylabel('Number of Triangulars')
        plt.show()
    elif 'terms' or 'Terms' or 'numbers' or 'Numbers' in p:
        print(*tris, sep=', ')
    else:
        print('ERROR: are you sure that this is one of the options?')


if 'prime' in seq or 'Prime' in seq or 'primes' in seq or 'Primes' in seq:
    primeSeq()
elif 'triangular' in seq or 'Triangular' in seq or 'triangulars' in seq or 'Triangulars' in seq:
    triSeq()
else:
    print('ERROR: are you sure that this is a sequence?')
