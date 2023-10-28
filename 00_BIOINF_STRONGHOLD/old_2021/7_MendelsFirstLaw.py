"""
Given:  Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
        k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). 
        Assume that any two organisms can mate.

Solved: Feb. 5, 2021, 11:11 p.m.
"""

k1 = 20
m1 = 24
n1 = 24

population = k1 + m1 + n1

# Because K is dominant homozygous, all its offspring will have dominant allele.
# What is the chance that dominant homozygous is picked first
k = k1 / population

# What is the chance that heterozygous is picked first.
m = m1 / population 

# What is the chance that heterozygous is picked second after Aa
# and have dominant offspring.
mm = m * (m1 - 1.0)/(population - 1.0)* 0.75 

# What is the chance that dominant is picked second after Aa
# and have dominant offspring
mk = m * k1 / (population - 1.0)

# What is the chance recessive is picked second after Aa
# and have dominant offspring
mn = m * n1 / (population - 1.0) * 0.5

# What is the chance that recessive is picked first.
n = n1 / population

# What is the chance recessive is picked second after aa
# and offspring is dominant
nn = 0

# What is the chance heterozyous is picked second after aa
# and offspring is dominant
nm = n * m1 / (population - 1.0) * 0.5

# What is the chance dominant homozygot is picked second after aa
# and offspring is dominant
nk = n * k1 / (population - 1.0)


probability = k + mm + mk + mn + nn + nm + nk
print(round(probability,5))
