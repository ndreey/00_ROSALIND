"""
Given:  A DNA string s of length at most 1000 bp.

Return: The reverse complement of s.

Solved: Jan. 26, 2021, 8:50 p.m.
"""


def revComplement(seq):
    """
    Prints out the reverse complement of seq by first complementing seq then reversing.
    """
    s = seq.upper()
    compli_dna = []
    reverse_complimentDNA = {"A": "T", "C": "G", "G": "C", "T": "A"}

    for nuc in s:
        compli_dna.append(reverse_complimentDNA[nuc])
    compli_dna.reverse()
    
    print(*compli_dna, sep="")

DNAstring = "TCCATCGTTCCCTTAAGGGGACTCGCCGTTCCCTGAAA"    
revComplement(DNAstring)


