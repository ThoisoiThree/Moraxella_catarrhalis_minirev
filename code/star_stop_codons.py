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
            seq = "".join(lines[1:]).strip()  # Убираем заголовок и объединяем строки
            if seq:
                sequences.append(seq)
    return sequences

seq_in = read_sequence('/Users/thoisoithree/Desktop/minirev/data/CDS_raw.txt')
seq_arr = extract_nucleotides(seq_in)

# Фильтруем лишнее меньше 3 символов
start_list = [seq[0:3] for seq in seq_arr if len(seq) >= 3]
stop_list = [seq[-3:] for seq in seq_arr if len(seq) >= 3]

# Подсчет кодонов
start_counter = Counter(start_list)
stop_counter = Counter(stop_list)

print("\n\n")
#print("-----START------     -----STOP-------")
print("Codon\tCount           Codon\tCount")
for (start_codon, start_count), (stop_codon, stop_count) in zip(sorted(start_counter.items()), sorted(stop_counter.items())):
    print(f"{start_codon:<7} {start_count:<5}           {stop_codon:<7} {stop_count:<5}")
print("\n\n")
