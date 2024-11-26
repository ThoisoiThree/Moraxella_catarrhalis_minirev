def count_nucleotides(seq_body_arr):
    codons = dict()
    for seq in seq_body_arr:
        for i in range(0, len(seq)-2, 3):
            codon = seq[i:i+3]
            if codon in codons:
                codons[codon] += 1
            else:
                codons[codon] = 1
    return codons
x = ["ATGGTAAGTTGAGATAGT"]

x = count_nucleotides(x)
print(x)