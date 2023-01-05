def removeDuplicateLetters(s):
    length_of_string = len(s)
    stack = list()
    for char in range(length_of_string):
        if s[char] in stack:
            continue
        else:
            while stack and stack[-1] > s[char] and stack[-1] in s[char + 1:]:
                stack.pop()
            stack.append(s[char])
    return ''.join(stack)

def isPangram(pangram):
    # Write your code here
    result = ''
    for sentence in pangram:
        sentence_without_space = ''.join(sentence.split())
        sentence_with_unique_char = removeDuplicateLetters(sentence_without_space)

        if len(sentence_with_unique_char) == 26:
            result += '1'
        else:
            result += '0'
    return result

string_list = ['pack my box with five dozen liquor jugs', 'this is not a pangram']

print(isPangram(string_list))