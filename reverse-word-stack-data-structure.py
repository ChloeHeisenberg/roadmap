def reverse_word(word):
    stack = []
    for l in word:
        stack.append(l)
    
    reversed_word = ''

    while stack:
        reversed_word += stack.pop()
    return reversed_word

word = 'Ruslana'
result = reverse_word(word)
print(result)