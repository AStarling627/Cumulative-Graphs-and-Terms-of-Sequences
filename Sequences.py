import numpy as np

seq = input('\nWhat is your sequence? (if it is a special one specify e.g the prime numbers) ').lower()
pref = input('\nWould you like to see all the terms of your sequence, a cumulative graph or both? ').lower()

uBound = int(input('\nUp to what integer? '))
if 'fibonacci' in seq or 'fibonaccis' in seq:  # a repeat of '1' in the fibonacci sequence requires an additional
    # natural number on the x-axis
    natural = np.linspace(0, uBound + 1, uBound + 2)
else:
    natural = np.linspace(0, uBound, uBound + 1)  # for non-repeating term sequences


def isArithmetic(sequence):  # function checks to see if the sequence is arithmetic
    if sequence[1] - sequence[0] == sequence[3] - sequence[2]:  # checks for a 1st common difference
        return True
    else:
        return False


def isQuadratic(sequence):  # function checks to see if the sequence is quadratic
    difference1 = sequence[1] - sequence[0]  # stores three 1st differences
    difference2 = sequence[2] - sequence[1]
    difference3 = sequence[3] - sequence[2]
    if difference2 - difference1 == difference3 - difference2:  # checks for a common 2nd difference
        return True
    else:
        return False


def nthArithmetic(sequence):  # function returns components in the arithmetic sequence to form the nth term
    ds = []  # list of components
    difference = sequence[1] - sequence[0]  # coefficient of 'n'
    ds.append(difference)
    if sequence[0] < difference:  # if the 1st term is less than the coefficient of 'n', the nth term has a negative
        # constant
        bias = difference - sequence[0]  # constant is defined
        ds.append(bias)
        ds.append('-')  # operator is added to list of components
    elif difference < sequence[0]:  # same thing as before but for opposite circumstances
        bias = sequence[0] - difference
        ds.append(bias)
        ds.append('+')
    else:  # if the sequence does not have a constant e.g. nth term: 2n
        bias = 0  # there is no added constant thus it is equal to 0
        ds.append(bias)
        ds.append(0)
    return ds


def nthQuadratic(sequence):  # function returns components in the quadratic sequence needed to form the nth term
    difference1 = sequence[1] - sequence[0]  # stores 2 1st differences
    difference2 = sequence[2] - sequence[1]
    testSequence = []  # the sequence formed by the quadratic term in the final nth term
    compSequence = []  # the sequence that forms the linear expression in the final nth term
    qCoefficient = (difference2 - difference1) // 2  # coefficient of 'n^2'
    for i in range(1, 6):
        testSequence.append(int(qCoefficient * (i ** 2)))  # creates 5 terms of the quadratic terms' sequence
    for i in range(0, 5):
        compSequence.append(sequence[i] - testSequence[i])  # creates  5 terms of the linear sequence formed by the
        # subtraction of the quadratic terms' sequence from the original
    nthArithmetic(compSequence)  # finds the components of the linear nth term part e.g. '2n + 5' in '3n^ 2 + 2n + 5'


def arithmetic(sequence):  # function that stores integers found to be terms in the arithmetic sequence and the number
    # of terms at each integer
    differences = nthArithmetic(seq)  # all the components of the nth term are stored
    difference = differences[0]  # stores each component
    bias = differences[1]
    op = differences[2]
    ars = []  # list of all integers found to terms in the sequence
    nArs = []  # list of the number of terms found at each integer
    if sequence[0] == 0:  # as the range in non-inclusive of 0 we must check to see if it is a term in the sequence
        ars.append(0)
        nArs.append(1)
    else:
        nArs.append(0)
    if op == '-':  # if the coefficient of the constant is negative
        for num in range(1, uBound + 1):
            if (num + bias) % difference == 0:  # solves the equation and checks to see if it is an integer; if so it is
                # part of the sequence
                if num < sequence[0]:  # if the number is not a term of the sequence, but has the same properties we do
                    # not include it
                    nArs.append(len(ars))
                else:
                    ars.append(num)
                    nArs.append(len(ars))
            else:
                nArs.append(len(ars))  # if it is not a term in the sequence
    if op == '+':  # same thing as before, but for when the coefficient of the constant is positive
        for num in range(1, uBound + 1):
            if (num - bias) % difference == 0:
                if num < sequence[0]:
                    nArs.append(len(ars))
                else:
                    ars.append(num)
                    nArs.append(len(ars))
            else:
                nArs.append(len(ars))
    if op == 0:  # same as before, but for when there is no constant
        for num in range(1, uBound + 1):
            if num % difference == 0:
                if num < sequence[0]:
                    nArs.append(len(ars))
                else:
                    ars.append(num)
                    nArs.append(len(ars))
            else:
                nArs.append(len(ars))
    return nArs, ars


def quadratic(sequence):  # function that stores integers found to be terms in the quadratic sequence and the number of
    # terms at each integer
    nthQuadratic(sequence)  # called upon to define compSeq
    differences = nthArithmetic(compSeq)  # stores the components of the nth term
    bias = differences[0]  # stores each component
    c = differences[1]
    op = differences[2]
    difference1 = sequence[1] - sequence[0]
    difference2 = sequence[2] - sequence[1]
    qCoefficient = (difference2 - difference1) // 2  # coefficient of the quadratic term in the final nth term
    qs = []  # list of all integers found to be terms in the sequence
    nQs = []  # list of the number of terms found at each integer
    if sequence[0] == 0:
        qs.append(0)
        nQs.append(1)
    else:
        nQs.append(0)
    if op == '-':
        for num in range(1, uBound + 1):
            if num < sequence[0]:
                nQs.append(len(qs))
            else:
                n1 = (-bias + np.sqrt((bias ** 2) - 4 * (qCoefficient * (-c - num)))) / (2 * qCoefficient)
                n2 = (-bias - np.sqrt((bias ** 2) - 4 * (qCoefficient * (-c - num)))) / (2 * qCoefficient)
                # finds the possible values for n using the quadratic formula
                if n1 % 1 == 0:  # if it is an integer in either instances, it is a term in the sequence
                    qs.append(num)
                    nQs.append(len(qs))
                elif n2 % 1 == 0:
                    qs.append(num)
                    nQs.append(len(qs))
                else:
                    nQs.append(len(qs))  # if n is a non-integer it is not a term in the sequence
    if op == '+':  # same as before but for positive constants
        for num in range(1, uBound + 1):
            if num < sequence[0]:
                nQs.append(len(qs))
            else:
                n1 = (-bias + np.sqrt((bias ** 2) - 4 * (qCoefficient * (c - num)))) / (2 * qCoefficient)
                n2 = (-bias - np.sqrt((bias ** 2) - 4 * (qCoefficient * (c - num)))) / (2 * qCoefficient)
                if n1 % 1 == 0:
                    qs.append(num)
                    nQs.append(len(qs))
                elif n2 % 1 == 0:
                    qs.append(num)
                    nQs.append(len(qs))
                else:
                    nQs.append(len(qs))
    if op == 0:  # same as before but for when there is no constant
        for num in range(1, uBound + 1):
            if num < sequence[0]:
                nQs.append(len(qs))
            else:
                n1 = (-bias + np.sqrt((bias ** 2) - 4 * (qCoefficient * -num))) / (2 * qCoefficient)
                n2 = (-bias - np.sqrt((bias ** 2) - 4 * (qCoefficient * -num))) / (2 * qCoefficient)
                if n1 % 1 == 0:
                    qs.append(num)
                    nQs.append(len(qs))
                elif n2 % 1 == 0:
                    qs.append(num)
                    nQs.append(len(qs))
                else:
                    nQs.append(len(qs))
    return nQs, qs


def primeSeq():  # function that stores integers found to be prime numbers and the number of terms at each integer
    primes = []  # I assume you understand what this is for by now...
    nPrimes = [0, 0]
    for num in range(2, uBound + 1):  # no primes are less than 2 we only need to check from 2
        for i in range(2, int(np.sqrt(num) + 1)):
            if num % i == 0:  # if at any point the integer is divisible by a number not 1 or itself it is not prime
                # thus we break out of the loop
                break
        else:
            if num == 4:  # as this code establishes 4 as a prime number we must manually state otherwise
                nPrimes.append(2)
                continue
            else:
                primes.append(num)  # if it is prime
        nPrimes.append(len(primes))
    return nPrimes, primes


def triSeq():  # function that stores integers found to be triangular numbers and the number of terms at each integer
    tris = []
    nTris = []
    for num in range(0, uBound + 1):
        testNum = 1 + (8 * num)  # must check to see if 1 + 8num is a perfect square, as if it is n will be an integer
        # in the quadratic formula
        sqrtVal = np.sqrt(testNum)
        if int(sqrtVal) ** 2 == testNum:  # if so, it is triangular
            tris.append(num)
            nTris.append(len(tris))
        else:  # if 1 + 8num is not a perfect square n will be a non-integer thus num will not be a term in the sequence
            nTris.append(len(tris))
            continue
    return nTris, tris


def fibSeq():  # function that stores integers found to be fibonacci numbers and the number of terms at each integer
    fibs = [0, 1]  # there is a repeat of 1 in the sequence that will be missed in the for loop
    nFibs = [1, 2]
    pos = 1
    for num in range(1, uBound + 1):
        if fibs[pos] + fibs[pos - 1] == num:  # if num is the sum of the previous 2 terms it is a fibonacci number
            fibs.append(num)
            nFibs.append(len(fibs))
            pos += 1
        else:  # if not, it is not a fibonacci number
            nFibs.append(len(fibs))
            continue
    return nFibs, fibs


if 'prime' in seq or 'primes' in seq:  # this module of code stores the nth term of the sequence in the variable 'tts'
    # used for the axis and titles of the graph and extra information when printing the terms of the sequence; if the
    # sequence is special then tts is just the name of the sequence:
    tts = 'Prime'
elif 'triangular' in seq or 'triangulars' in seq:
    tts = 'Triangular'
elif 'fibonacci' in seq or 'fibonaccis' in seq:
    tts = 'Fibonacci'
elif ',' in seq:
    seq = [eval(j) for j in ''.join([i for i in seq if i != '.']).split(', ')]  # converts input sequence into a list of
    # the terms as integers
    if isArithmetic(seq):
        diffs = nthArithmetic(seq)
        diff = diffs[0]
        b = diffs[1]
        operator = diffs[2]
        if operator == 0:
            tts = str(diff) + 'n'
        else:
            tts = str(diff) + 'n' + operator + str(b)
    elif isQuadratic(seq):
        diff1 = seq[1] - seq[0]
        diff2 = seq[2] - seq[1]
        testSeq = []
        compSeq = []
        a = (diff2 - diff1) // 2
        for i in range(1, 6):
            testSeq.append(int(a * (i ** 2)))
        for i in range(0, 5):
            compSeq.append(seq[i] - testSeq[i])
        diffs = nthArithmetic(compSeq)
        diff = diffs[0]
        b = diffs[1]
        operator = diffs[2]
        if operator == 0:
            if a == 1:
                if diff == 1:
                    tts = 'n^2 + n'
                elif diff == 0:
                    tts = 'n^2'
                else:
                    tts = 'n^2 + ' + str(diff) + 'n'
            else:
                if diff == 1:
                    tts = 'n^2 + n'
                elif diff == 0:
                    tts = 'n^2'
                else:
                    tts = str(a) + 'n^2 +' + str(diff) + 'n'
        else:
            if a == 1:
                if diff == 1:
                    tts = 'n^2 + n'
                elif diff == 0:
                    tts = 'n^2'
                else:
                    tts = 'n^2 + ' + str(diff) + 'n'
            else:
                if diff == 1:
                    tts = 'n^2 + n'
                elif diff == 0:
                    tts = 'n^2'
                else:
                    tts = str(a) + 'n^2 +' + str(diff) + 'n'
else:
    print('\nERROR: are you sure that this is a sequence?')  # if the inputted sequence is not one known by the code, it
    # prints an error message
