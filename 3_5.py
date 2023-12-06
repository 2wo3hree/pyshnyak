import math

conditional_probabilities = [
    [0.98, 0.01, 0.01],
    [0.15, 0.75, 0.1],
    [0.3, 0.2, 0.5]
]


P_X = [1/3, 1/3, 1/3]

H_Y_given_X_a = 0
for x in range(3):
    for y in range(3):
        term = conditional_probabilities[x][y] * math.log2(conditional_probabilities[x][y] / P_X[x])
        H_Y_given_X_a -= term

P_X_b = [0.7, 0.2, 0.1]

H_Y_given_X_b = 0
for x in range(3):
    for y in range(3):
        term = conditional_probabilities[x][y] * math.log2(conditional_probabilities[x][y] / P_X_b[x])
        H_Y_given_X_b -= term

print(f"Полная условная энтропия H(Y|X) для случая (а): {H_Y_given_X_a:.4f} бит")
print(f"Полная условная энтропия H(Y|X) для случая (б): {H_Y_given_X_b:.4f} бит")