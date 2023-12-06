import numpy as np

channel_matrix = np.array([
    [0.97, 0.03, 0],
    [0.01, 0.98, 0.01],
    [0, 0.04, 0.96]
])

symbol_probabilities = np.array([0.5, 0.3, 0.2])

receiver_entropy = -np.sum(symbol_probabilities * np.log2(symbol_probabilities))

print(f"Энтропия приемника сообщений: {receiver_entropy:.4f} бит")
