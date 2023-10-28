"""
Input:  FASTA file with sequence.
Output: Consensus and profile matrix
Solved: Oct. 9, 2022, 3:04 p.m.

Each sequence is a row and each nuc is a column.
Then calculate the consensus sequence.

            A T C C A G C T
            G G G C A A C T
            A T G G A T C T
            A A G C A A C C
            T T G G A A C T
            A T G C C A T T
            A T G G C A C T

        A   5 1 0 0 5 5 0 0
        C   0 0 1 4 2 0 6 1
        G   1 1 6 3 0 1 0 0
        T   1 5 0 0 0 1 1 6

Consensus	A T G C A A C T

"""
import numpy as np
from Bio import SeqIO

#Seq_list is a list containing lists.
seq_list = []
 
#Each sequence becomes a list where the elements is each nucleotide.
for record in SeqIO.parse("C:\snooken\ROSALIND\Bioinformatics_stronghold\Consensus_Profile.txt", "fasta"):    
    tmp_ls = [] 
    for nucs in record.seq:    #For each nucleotide in record (sequence)         
        tmp_ls.append(nucs)    #Appends each nucleotide to tmp.list
    seq_list.append(tmp_ls)    #Then stores the record list in seq_list.

#Creates an array where each row is the record           
A = np.array(seq_list)

#Here we will store the counts for each nuc in position i of record.
nucdic = {"A":[],"C":[],"G":[],"T":[]}

#Variable to store the consensus sequence.
consensus = ""

#For each nucleotide in sequence.
for i in range(0,len(seq_list[0])):
    nuc = ["A","C","G","T"]                       #List of A,C,G,T to index from
    #Calculates amount of times each nucleotide is at position i    
    nucdic["A"].append(list(A[:,i]).count("A"))   # A[:,i] is the ith column in the array)
    nucdic["C"].append(list(A[:,i]).count("C"))
    nucdic["G"].append(list(A[:,i]).count("G"))
    nucdic["T"].append(list(A[:,i]).count("T"))
    #Temp list that stores the counts for each nucleotide at position i
    temp = [nucdic["A"][i],nucdic["C"][i],nucdic["G"][i],nucdic["T"][i]]    
    
    #If temp[n] is the max, then we write the corresponding nucleotide to consensus.
    for n, element in enumerate(temp):        
        if element == max(temp):            
            consensus = consensus + nuc[n]
            break         #Break the loop to avoid other nucs that == max. We only need 1
        else:
            pass
    
print(consensus)
#Prints profile matrix    
for key,item in nucdic.items():
    print(key + ":", end =" ")    
    print(*item)   

