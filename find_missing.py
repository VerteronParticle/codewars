def find_missing(sequence):    
    return int(
        (sequence[0] + sequence[-1]) * 
        (len(sequence) + 1) / 
        2 - sum(sequence)
    )

if __name__ == '__main__':
    print(find_missing([1, 3, 5, 9, 11]))