"""
Given:  At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
        Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Solved: Jan. 27, 2021, 1:01 p.m.
"""

def GC_content(seq):
    """
    ((G+C)/length of sequence)*100      returns the percentage of Guanine and Cytosine
    """
    return ((seq.count("C") + seq.count("G")) / len(seq.strip())*100)


def MaxGCseq(filename):
    """
    Opens the fasta file and stores each heading as key in a dictionary and then adds sequence line by line.
    It then calculates the GC content for each heading and picks the key with the highest value.
    """
    with open(filename, "r") as rosaread:
        fastaDict = {}

        for line in rosaread:
            if ">" in line:
                fastaID = line.strip(">").strip("\n")
                fastaDict[fastaID] = " "
            else:
                fastaDict[fastaID] += line.strip("\n")

    for key in fastaDict:
        fastaDict[key] = GC_content(fastaDict[key])


    highPercentageGC = max(fastaDict, key=fastaDict.get)
    print(highPercentageGC)
    print(fastaDict[highPercentageGC])
   

MaxGCseq(r"C:\snooken\ROSALIND\Bioinformatics_stronghold\rosalind_gc.txt")

