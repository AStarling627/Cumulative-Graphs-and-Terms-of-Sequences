import matplotlib.pyplot as plt
import Sequences as gv  # imports the file which contains all the necessary sequence functions


def comma(ul):  # function is used to insert commas in numbers where appropriate
    ul = list(str(ul))  # as ul is an integer, in order to alter elements we convert it to a list
    if 5 <= len(ul):  # from 1x10^4 commas will be inserted
        pos = -3  # declaring the first place we insert a comma
        i = len(ul)
        while 5 <= i:  # while the length of the integer is great enough to insert commas, we do so
            ul.insert(pos, ',')
            i -= 2  # and in doing so decrease the length, so the code does not run infinitely
            pos -= 4  # as the actual length increases by 1 each loop we must insert a comma 4 from the last digit
        if ul[0] == ',':  # if a comma is inserted at the start (which occurs here when the integer starts with a '100')
            ul.remove(',')  # it is removed under these circumstances
            ul = ''.join(ul)  # converted back to a string
            return ul
        else:
            ul = ''.join(ul)
            return ul
    else:
        ul = ''.join(ul)  # if the numbers length does not meet at least 5, then we alter nothing
        return ul


def plot(x, y, u):  # function plots the cumulative sequence terms against natural numbers
    finalU = comma(u)  # our final upper bound has inserted commas
    plt.plot(x, y)
    plt.xlabel('Natural Numbers')
    if all(isinstance(item, int) for item in gv.seq):  # if the inputted sequence is non-special e.g. 3, 5, 7, 9...
        plt.ylabel('Number of Terms')
        plt.title('Cumulative Terms of Sequence ' + gv.tts + ' from 0 to ' + finalU)  # gv.tts is our imported nth term
    else:
        plt.ylabel('Number of ' + gv.tts + ' Numbers')  # if the sequence is special e.g. the prime numbers
        plt.title('Cumulative ' + gv.tts + ' Numbers from 0 to ' + finalU)
    plt.show()


def terms(s, u):  # function prints out all terms from 0 to the inputted upperbound with extra information
    finalU = comma(u)
    length = comma(len(s))  # this is the number of terms with commas inserted
    print('')  # creates a new line before printing terms
    print(*s, sep=', ')  # as s is a sequence we put a separation between each term of a comma and space
    if all(isinstance(item, int) for item in gv.seq):  # if s is a non-special sequence
        print('\nThere are', length, 'terms from 0 to', finalU, 'for the sequence of nth term', gv.tts)
    else:  # if it is special
        print('\nThere are', length, gv.tts.lower(), 'numbers from 0 to', finalU)


def ref(x, y, s, u):  # function takes in the users preferences and outputs what is desired
    if 'both' in gv.pref:  # if a graph and terms are wanted
        terms(s, u)
        plot(x, y, u)
    elif 'graph' in gv.pref or 'cumulative' in gv.pref:  # just the graph
        plot(x, y, u)
    elif 'terms' in gv.pref or 'numbers' in gv.pref:  # just the terms
        terms(s, u)
    else:  # for when the input is none of the listed
        print('ERROR: are you sure that this was one of the options from question 2?')


if 'prime' in gv.seq or 'primes' in gv.seq:  # calls upon functions necessary for the inputted sequence
    nPrimes, primes = gv.primeSeq()
    ref(gv.natural, nPrimes, primes, gv.uBound)
elif 'triangular' in gv.seq or 'triangulars' in gv.seq:
    nTris, tris = gv.triSeq()
    ref(gv.natural, nTris, tris, gv.uBound)
elif 'fibonacci' in gv.seq or 'fibonaccis' in gv.seq:
    nFibs, fibs = gv.fibSeq()
    ref(gv.natural, nFibs, fibs, gv.uBound)
elif gv.isArithmetic(gv.seq):
    nArs, ars = gv.arithmetic(gv.seq)
    ref(gv.natural, nArs, ars, gv.uBound)
elif gv.isQuadratic(gv.seq):
    nQs, qs = gv.quadratic(gv.seq)
    ref(gv.natural, nQs, qs, gv.uBound)
else:
    exit()
