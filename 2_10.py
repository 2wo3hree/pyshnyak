import math

def shannon_entropy(sentence):
    symbol_counts = {}
    total_symbols = len(sentence)
    
    # Подсчитываем количество каждого символа
    for symbol in sentence:
        if symbol in symbol_counts:
            symbol_counts[symbol] += 1
        else:
            symbol_counts[symbol] = 1
    
    entropy = 0
    for symbol, count in symbol_counts.items():
        probability = count / total_symbols
        information = -math.log2(probability)*probability
        entropy += information

    return entropy * len(sentence)

sentence1 = "Ра, ра, ра, ра, ра, ра, ра."
sentence2 = "Черемуха душистая весною расцвела и ветки золотистые, что кудри завила."
sentence3 = "Соблюдай правила техники безопасности! Не стой под краном!"

print(f"Количество информации в предложении: {shannon_entropy(sentence1):.2f} бит")
print(f"Количество информации в предложении: {shannon_entropy(sentence2):.2f} бит")
print(f"Количество информации в предложении: {shannon_entropy(sentence3):.2f} бит")
