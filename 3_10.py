import numpy as np

channel_matrix = np.array([
    [0.3, 0, 0],
    [0.2, 0.3, 0.1],
    [0, 0.1, 0]
])

def conditional_entropy_B_given_A(matrix):
    H_B_given_A = 0
    for a_index in range(matrix.shape[0]):
        p_a = sum(matrix[a_index, :])
        for b_index in range(matrix.shape[1]):
            p_b_given_a = matrix[a_index, b_index] / p_a if p_a > 0 else 0
            if p_b_given_a > 0:
                H_B_given_A -= p_a * p_b_given_a * np.log2(p_b_given_a)
    return H_B_given_A

def conditional_entropy_A_given_B(matrix):
    H_A_given_B = 0
    for b_index in range(matrix.shape[1]):
        p_b = sum(matrix[:, b_index])
        for a_index in range(matrix.shape[0]):
            p_a_given_b = matrix[a_index, b_index] / p_b if p_b > 0 else 0
            if p_a_given_b > 0:
                H_A_given_B -= p_b * p_a_given_b * np.log2(p_a_given_b)
    return H_A_given_B

H_B_given_A = conditional_entropy_B_given_A(channel_matrix)
H_A_given_B = conditional_entropy_A_given_B(channel_matrix)

print(f"Полная условная энтропия H(В/А): {H_B_given_A:.4f} бит")
print(f"Полная условная энтропия H(А/В): {H_A_given_B:.4f} бит")