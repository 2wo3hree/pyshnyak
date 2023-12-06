import numpy as np

channel_matrix = np.array([
    [0.99, 0.02, 0, 0],
    [0.01, 0.98, 0.01, 0.01],
    [0, 0, 0.98, 0.2],
    [0, 0, 0.01, 0.97]
])

symbol_probabilities = np.array([0.1, 0.3, 0.4, 0.2])

source_entropy = -np.sum(symbol_probabilities * np.log2(symbol_probabilities))

print(f"Энтропия источника сообщений: {source_entropy:.4f} бит")