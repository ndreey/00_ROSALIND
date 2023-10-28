"""
Given:  Positive integers n ≤ 100 and m ≤ 20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Solved: Oct. 15, 2022, 1:40 p.m.
"""

# Thought process
"""
# Can i find common formula..                                                       # What about age...
Month                   Pair                                                      Month   baby    1mnth   2mnth    Sum                                                                        
1                       1                                                         1        1        0      0       1
2                       1                                                         2        0        1      0       1            
3                       2     Fn-1+Fn-2     Fn - Fn-1                             3        1        0      1       2          
4                       2                   Fn - Fn-1                             4        1        1      0       2
5                       3                   Fn - Fn-1                             5        1        1      1       3
6                       4     Fn - Fn-2                                           6        2        1      1       4
7                       5                                                         7        2        2      1       5
8                       7                                                         8        3        2      2       7
9                       9                                                         9        4        3      2       9
10                      12                                                        10       5        4      3       12
# Not really                                                                      # Seems to be somehing here.

                                                                                 baby = sum of all mature wabbits
                                                                                 mature wabbit: (n)month = (n-1)month
                                                                                 Tot.wabbits = sum of all wabbits.
                                                                                 
                                                                                 Storing each generations age seems to be the answer!
"""
   
def mortal_sillywabbits(n,m):
    """ Updates number of wabbits of x months old based on the lifespan of wabbit.
        n is number of months, m is the lifespan of a wabbit
    """        
    # Each element is nth month old. 
    # ages[0] = baby, ages[1] = 1 month old, ages[m] = m month old    
    # List of ages, m-1 because we start counting on 0.
    ages = [1] + ([0]*(m-1))     # We always start with one baby wabbit        
    
    # For each month, we need to update the list using past month information.
    for month in range(1,n):       
        # Copy of the ages from past month 
        last_month = ages.copy()
        
        # Updates each mature wabbit from last_month's ages  
        for i in range(1,m):                                     
            ages[i] = last_month[i-1]           
                    
        # baby wabbits = sum of all mature wabbits
        ages[0] = sum(last_month[1:])        
            
    # Total number of wabbits after n months    
    print(sum(ages))


mortal_sillywabbits(32,3)