from collections import Counter

def read_sequence(file_path):
    with open(file_path, 'r') as file:
        sequence = file.read()
    return sequence.split('>')

def extract_nucleotides(seq_arr):
    sequences = []
    for record in seq_arr:
        lines = record.split('\n')
        if len(lines) > 1:
            header = lines[0]
            if "[pseudo=true]" not in header:  # Игнорируем псевдогены
                seq = "".join(lines[1:]).strip()  
                if seq:
                    sequences.append(seq)
    return sequences

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


if __name__ == "__main__":
    
    seq_in = read_sequence('/Users/thoisoithree/Desktop/minirev/data/CDS_raw.txt')
    seq_arr = extract_nucleotides(seq_in)

    stop_codons = ["TAA", "TAG", "TGA"]

    # Тело без старт и стопа
    seqbody = [seq[3:-3] for seq in seq_arr]

    # Подсчет кодонов
    codon_dict = count_nucleotides(seqbody)
    print(codon_dict)
    print("\n")
    for codon in stop_codons:
        print(f"{codon}: {codon_dict[codon]}")
    print("\n")


