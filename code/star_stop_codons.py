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
            if "[pseudo=true]" not in header:
                seq = "".join(lines[1:]).strip()  # Убираем заголовок и объединяем строки
                if seq:
                    sequences.append(seq)
    return sequences


if __name__ == "__main__":

    seq_in = test_sequences = read_sequence('/Users/thoisoithree/Desktop/minirev/data/CDS_raw.txt')

    seq_arr = extract_nucleotides(seq_in)

    # Фильтруем лишнее меньше 3 символов
    start_list = [seq[0:3] for seq in seq_arr if len(seq) >= 3]
    stop_list = [seq[-3:] for seq in seq_arr if len(seq) >= 3]


    # Подсчет кодонов
    start_counter = Counter(start_list)
    stop_counter = Counter(stop_list)
    print(start_counter)
    print(stop_counter)


    max_len = max(len(start_counter), len(stop_counter))

    # Добавляем пустые значения для выравнивания

    print("\n")
    print("Start codons:")
    for codon, value in start_counter.items():
        print(f"{codon}\t{value}")

    print("\n")
    print("Stop codons:")
    for codon, value in stop_counter.items():
        print(f"{codon}\t{value}")

    print("\n")
