"""
Given:  A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Solved: Oct. 15, 2022, 7:58 p.m.
"""
from Bio import SeqIO

# So we want seq1 suffix to match seq2 prefix.
head_tail = {}

#  Stores sequence prefix and suffix from each record in a dictionary
for record in SeqIO.parse(r"C:\snooken\ROSALIND\Bioinformatics_stronghold\rosalind.txt", "fasta"):    
    head_tail[record.id] = [record.seq[0:3],record.seq[-3:]]

# List of edges
edges = [] 

# For each key, lets check if prefix matches any other key prefix.
for suffix in head_tail.keys():
    for prefix in head_tail.keys():
                
        # If key = key we skip
        if suffix == prefix:
            pass
        
        # If record(i) suffix matches record(j) prefix, then add match to edges        
        elif head_tail[suffix][1] == head_tail[prefix][0]:
            match = [suffix, prefix]
            edges.append(match)
            
        else:
            pass
        
# Prints out edges
for edge in edges:
    print(*edge)
