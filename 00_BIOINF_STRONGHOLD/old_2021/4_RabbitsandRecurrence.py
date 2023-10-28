"""
Given:  Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, 
        every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Solved: Feb. 10, 2021, 10:30 p.m.
"""
def sillywabbits(months, bebys):

    wabbit_pairs = 1
    maturepair = 1
    babypair = 0
    oldbabypair = 0

    if months <= 2:
        print(wabbit_pairs)

    else:
        for gen in range(2,months):

            oldbabypair = babypair
            babypair = maturepair * bebys
            maturepair = maturepair + oldbabypair

            wabbit_pairs = maturepair + babypair
    print(wabbit_pairs) 


sillywabbits(5,3)



