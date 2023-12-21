from decimal import Decimal #Числа ВЕЛИЧЕЗНІ після коми, більшує float
import json


def symbol_probability_range(low, high, letter, buffer, len_text): #літеру з тексту проганяєм і шукаємо діапазон
    n_buffer = {}
    for key, value in buffer.items():
        n_buffer[key] = (high - low) * Decimal(value) / Decimal(len_text)
    buffer_min = {}
    buffer_max = {}
    a = Decimal(low)
    for key, value in n_buffer.items():
        buffer_min[key] = a
        a += value
    a = Decimal(low)
    for key, value in n_buffer.items():
        a += value
        buffer_max[key] = a
    return buffer_min[letter], buffer_max[letter]

def decimal_to_binary(decimal): #найпростіший алгоритм десяткового у двійкове
    if decimal == 0:
        return '0'
    
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    
    return binary


text = "борітеся - поборете!"  # "борітеся - поборете!"
buffer = {}
for i in text[::-1]: #ПРОБЛЕМА-КОСТИЛЬ: кінцеве число виходить 0.0.....(тому [::-1]), тобто число в кінці починається з 0 , а це int не сприймає, і перевести у двійкову правильно не виходить
    if i not in buffer:
        buffer[i] = 1
    else:
        buffer[i] += 1
print(buffer)
with open('buffer.json', 'w') as file:
    json.dump(buffer, file)
lowx, highx = Decimal('0'), Decimal('1')
for i in range(len(text)):
    lowx, highx = symbol_probability_range(lowx, highx, text[i], buffer, len(text))
    print(lowx, highx)
result=""

for l, h in zip(str(lowx), str(highx)): #цей цикл зменшує довжину вихідного числа, шукаючи найменше у діапазоні min i max
    if l == h:
        result += l
    else:
        result += str(int(l)+1)
        break
print(result)
result_a=""
for i in result[::-1]:
    if(i!="."):
        result_a+=i
    else:
        result_a=result_a[::-1]
        break

print(decimal_to_binary(int(result_a)))
