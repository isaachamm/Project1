import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.

    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)

    if (y % 2) == 0:
        return (z**2) % N
    else:
        return x * (z**2) % N


def fprobability(k):
    # You will need to implement this function and change the return value.

    fprob = 1.0
    fprob -= (1 / 2**k)

    return fprob


def mprobability(k):
    # You will need to implement this function and change the return value.   
    mprob = 1.0
    mprob -= (1 / 4**k)

    return mprob


def fermat(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    prime = True
    for i in range(k):
        a = random.randint(1, N - 1)
        if (mod_exp(a, N - 1, N)) != 1:
            prime = False
            break

    if prime:
        return 'prime'
    else:
        return 'composite'


def miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    prime = True
    for i in range(k):
        exponent = N - 1
        a = random.randint(1, exponent)

        if (exponent % 2) != 0:
            prime = False

        while True:
            mod_result = (mod_exp(a, exponent, N))
            if mod_result == 1:
                if(exponent % 2) == 0:
                    break
                exponent /= 2
            elif mod_result == -1:
                break
            else:
                prime = False
                break

        if not prime:
            break

    if prime:
        return 'prime'
    else:
        return 'composite'

    # TODO USE 6601 to break it
