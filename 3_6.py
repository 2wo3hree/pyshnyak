import numpy as np

channel_matrix = np.array([
    [0.9, 0.01, 0, 0],
    [0.05, 0.94, 0.01, 0],
    [0, 0.1, 0.98, 0.01],
    [0, 0, 0.1, 0.9]
])

source_symbols = ['а1', 'а2', 'а3', 'а4']

# а) Вычисление частных условных энтропий для каждого символа
partial_entropies = []
for symbol_index, symbol in enumerate(source_symbols):
    entropy = 0
    for output_symbol_index in range(len(source_symbols)):
        p_b_given_a = channel_matrix[output_symbol_index][symbol_index]
        if p_b_given_a > 0:
            entropy -= p_b_given_a * np.log2(p_b_given_a)
    partial_entropies.append((symbol, entropy))

print("Частные условные энтропии:")
for symbol, entropy in partial_entropies:
    print(f"{symbol}: {entropy:.4f} бит")

# б) Вычисление общей условной энтропии при равновероятных символах источника
equal_probabilities = np.array([1/4, 1/4, 1/4, 1/4])
total_entropy_equal_probabilities = np.sum(equal_probabilities * np.array([entropy for _, entropy in partial_entropies]))
print(f"\nОбщая условная энтропия (равновероятные символы источника): {total_entropy_equal_probabilities:.4f} бит")

# в) Заданные вероятности символов источника на выходе
symbol_probabilities = np.array([0.15, 0.32, 0.25, 0.28])
total_entropy_given_probabilities = -np.sum(symbol_probabilities * np.log2(symbol_probabilities))
print(f"\nОбщая условная энтропия (заданные вероятности): {total_entropy_given_probabilities:.4f} бит")