import numpy as np

channel_matrix = np.array([
    [0.9, 0.1, 0, 0],
    [0.05, 0.84, 0.01, 0],
    [0.03, 0.06, 0.98, 0.1],
    [0.02, 0, 0.01, 0.9]
])

symbol_probabilities = np.array([1/4, 1/4, 1/4, 1/4])

total_entropy = 0
for a_index in range(len(symbol_probabilities)):
    for b_index in range(len(symbol_probabilities)):
        p_b_given_a = channel_matrix[b_index][a_index]
        if p_b_given_a > 0:
            total_entropy -= symbol_probabilities[a_index] * p_b_given_a * np.log2(p_b_given_a)

print(f"Общая условная энтропия: {total_entropy:.4f} бит")