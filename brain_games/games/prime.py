#!/usr/bin/env python
import random


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
primes_limit = 101  # in range 0, 100


# Sieve of Eratosthenes to generate prime numbers sequence
def erathosthenes_sieve(primes_limit):

    # prime list initialization
    prime_list = []

    # boolean array for primes_limit range
    boolean_array = [True] * primes_limit

    for i in range(2, primes_limit):
        if boolean_array[i]:
            for j in range(i ** 2, primes_limit, i):
                boolean_array[j] = False
    for i in range(2, primes_limit):
        if boolean_array[i]:
            prime_list.append(i)
    return prime_list


prime_list = erathosthenes_sieve(primes_limit)


def game():
    random_number = random.randrange(2, 100)
    question = random_number
    correct_answer = 'yes' if random_number in prime_list else 'no'
    return [question, correct_answer]
