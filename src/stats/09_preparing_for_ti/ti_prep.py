


'''
You are sitting on a dock watching boats go by. On average, two out of every 13 boats that goes by has shipping containers on it. What is the probability that, in one particular set of observations, 10 out of 20 boats have shipping containers on them?
'''
from math import factorial, e

def combs(n,k):
    return factorial(n) / (factorial(n-k)* factorial(k))

def binomial_pmf(n,k,p):
    return combs(n,k)  *  p**k  * (1-p)**(n-k)

n = 20
k = 10
p = 2/13

# print(binomial_pmf(n,k,p))


'''
2 black cars go pass the stop sign every 15 minutes.

What is the proba that more than 10 black cars pass the stop sign in one hour?
'''
lmbda = 8


def poisson_pmf(lmbda, k):
    return e**(-lmbda) * lmbda**k / factorial(k)

def poisson_cdf(lmbda, k_high):
    accum = 0.0

    for k in range(0, k_high+1):
        accum += poisson_pmf(lmbda, k)
    return accum

# print(1 - poisson_cdf(lmbda, 10))

'''
A is the result of rolling a 4-sided die 5 times, and processing it through this function:

single_roll = [1,2,3,4]

ex set of rolls = [1,3,1,2,4]
a = 1 * 4/1 + 3 * 4/2 + 1 * 4/3 + 2 * 4/4 + 5 * 4/5
'''
from random import choice

def get_four_sided_roll():
    return choice([1,2,3,4])

def roll_math(lst):
    accum = 0.0

    for idx, val in enumerate(lst, 1):
        accum += val * (4/idx)
    
    return accum

def get_roll_5():
    roll1 = []
    for _ in range(5):
        roll1.append(get_four_sided_roll())
    return roll1

# print(roll_math(roll1))


def analyze_outcomes(n=5, num_samples=10000):
    d = dict()

    for _ in range(num_samples):
        roll_result = get_roll_5()
        res = round(roll_math(roll_result))

        if res not in d:
            d[res] = 0
        d[res] += 1

    return d


d = analyze_outcomes(n=5, num_samples=10000)
for outcome, cnt in sorted(d.items()):
    print(f'{outcome}: {cnt}')
