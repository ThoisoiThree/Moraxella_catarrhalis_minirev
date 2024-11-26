import matplotlib.pyplot as plt

def GC_sequence_percentage(sequence):
    count = sequence.count('G') + sequence.count('C')
    percentage = (count / len(sequence)) * 100
    return percentage
def GC_by_window(sequence, window_size):
    
    lst = []
    for i in range(0, len(sequence)-window_size+1, window_size):
        window = sequence[i:i+window_size]
        percent = GC_sequence_percentage(window)
        lst.append(percent)
    return lst
def read_sequence(file_path):
    with open(file_path, 'r') as file:
        sequence = file.read()
    return sequence
def find_seq(index, window_size, sequence):
    found_seq = sequence[index*window_size:(index+1)*window_size]
    return found_seq 
def write_minmax(min, max, window_size, sequence):
    #min
    with open("/Users/thoisoithree/Desktop/minirev/data/min_seq.txt", "w") as file:
        for item in min:
            seq = find_seq(item[0], window_size, sequence)
            file.write(seq + "\n\n")
    #max
    with open("/Users/thoisoithree/Desktop/minirev/data/max_seq.txt", "w") as file:
        for item in max:
            seq = find_seq(item[0], window_size, sequence)
            file.write(seq + "\n\n")

if __name__ == "__main__":
    window_size = 2000
    sequence = read_sequence('/Users/thoisoithree/Desktop/minirev/data/genomic_processed.fna')
    values = GC_by_window(sequence, window_size)

    indexed_values = list(enumerate(values))
    sorted_indexed_values = sorted(indexed_values, key=lambda x: x[1])
    minvalues = sorted_indexed_values[0:10]
    maxvalues = sorted_indexed_values[-10:]
    write_minmax(minvalues, maxvalues, window_size, sequence)

    print(minvalues, maxvalues)

    plt.plot(values,linewidth=0.5)
    plt.title('GC распределение')
    plt.xlabel('Индекс окна')
    plt.ylabel('GC содержание (%)')
    plt.show()


