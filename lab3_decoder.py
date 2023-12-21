from decimal import Decimal #Числа ВЕЛИЧЕЗНІ після коми, більшує float
import json


def symbol_probability_range(low, high, probability, buffer, len_text): #даємо діапазон, наше число 
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
    for (key_min, value_min), (key_max, value_max) in zip(buffer_min.items(), buffer_max.items()):
        if(value_min < probability and value_max > probability):
            symbol = key_min
            break
    return buffer_min[symbol], buffer_max[symbol], symbol

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1

    for digit in binary:
        if digit == '1':
            decimal += 2 ** power
        power -= 1

    return decimal


binary_code = '1000000100111001011001010010111111110100011010111100101101000001111111'  # "борітеся - поборете!"
len_text = 0
buffer = {}
with open('buffer.json', 'r') as file: # дістаємо буфер-словник, його бажано теж у двійковому коді подівати(не знаю як це правильно зробити, тому json)
    buffer = json.load(file)
print(buffer)
for value in buffer.values():
    len_text+=value
numx = int(binary_code, 2)
numx_decimal = Decimal(numx)
x = Decimal(10) ** len(str(numx))
numx1 = numx_decimal / x
print(numx1)

result = ""
lowx, highx = Decimal('0'), Decimal('1')
for i in range(len_text):
    lowx, highx, symbol = symbol_probability_range(lowx, highx, numx1, buffer, len_text)
    print(lowx, highx, symbol)
    result += symbol
print(result)

'''
for i in range(20):
    lowx, highx = symbol_probability_range(lowx, highx, text[i], buffer, len(text), i)
    print(lowx, highx)
result=""

for l, h in zip(str(lowx), str(highx)):
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

print(decimal_to_binary(int(result_a)))'''