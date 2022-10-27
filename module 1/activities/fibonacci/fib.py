def fibonacci(nterms, n_0=0, n_1=1):
    current_term = 2
    sequence = [n_0, n_1]
    while current_term < nterms:
        sequence.append(sequence[-1]+sequence[-2])
        current_term += 1
    print(sequence)

fibonacci(20)
 