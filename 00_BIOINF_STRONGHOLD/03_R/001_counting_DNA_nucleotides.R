library(tidyverse)

# Given: A DNA string s of length at most 1000nt
# Return: Four integers (separated by spaces) counting the respective numbers
# of times that the symbols "A", "C", "G", and "T" occur in s.

# Open the file
dna_file <- file("00_DATA/rosalind_dna.txt", "r")

# Read the file
dna_str <- readLines(dna_file)

# Close the file
close(dna_file)

# Is a vector with one element
dna_str

# Empty numeric vector to append the counts to
nuc_cnts <- numeric()

# Count each nucleotide using for loop and piping to append to the vector
for (nuc in c("A", "C", "G", "T")) {
  
  count_nuc <- dna_str %>% 
    str_count(nuc)
  
  nuc_cnts <- c(nuc_cnts, count_nuc)
}

print(nuc_cnts)