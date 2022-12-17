import numpy as np
import matplotlib.pyplot as plt

pref = input('Would you like to see all the terms of your sequence, a cumulative graph or both? ')
seq = input('What is your sequence? (if it is a certain one specify e.g the prime numbers) ')


def comma(ul):
    ul = list(str(ul))
    if 5 <= len(ul):
        pos = -3
        i = len(ul)
        while 5 <= i:
            ul.insert(pos, ',')
            i -= 2
            pos -= 4
        ul = ''.join(ul)
        return ul
    else:
        ul = ''.join(ul)
        return ul


def plot(x, y, u):
    comma(u)
    plt.plot(x, y)
    plt.xlabel('Natural Numbers')
    plt.ylabel('Number of ' + tts + ' Numbers')
    plt.title('Cumulative ' + tts + ' Numbers from 0 to ' + comma(u))
    plt.show()


def terms(s, u):
    l = len(s)
    comma(u)
    comma(l)
    print(*s, sep=', ')
    print('There are', comma(l), tts.lower(), 'numbers from 0 to', comma(u))


def ref(x, y, s, u):
    if 'both' in pref or 'Both' in pref:
        terms(s, u)
        plot(x, y, u)
    elif 'graph' in pref or 'Graph' in pref or 'cumulative' in pref or 'Cumulative' in pref:
        plot(x, y, u)
    elif 'terms' in pref or 'Terms' in pref or 'numbers' in pref or 'Numbers' in pref:
        terms(s, u)
    else:
        print('ERROR: are you sure that this is one of the options? ')


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
    ref(natural, nPrimes, primes, uBound)


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
    ref(natural, nTris, tris, uBound)


if 'prime' in seq or 'Prime' in seq or 'primes' in seq or 'Primes' in seq:
    tts = 'Prime'
    primeSeq()
elif 'triangular' in seq or 'Triangular' in seq or 'triangulars' in seq or 'Triangulars' in seq:
    tts = 'Triangular'
    triSeq()
else:
    print('ERROR: are you sure that this is a sequence?')
