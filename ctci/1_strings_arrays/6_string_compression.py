# problem: Implement a method to perform basic string compression using the counts of repreated characters.

# Example
#   INPUT: aabcccccaaa
#   OUTPUT: a2b1c5a3

def string_compression(item):
    '''
    TIME: O(n)
    SPACE: O(n)
    '''
    answer = ''
    i = 0
    while i in range(len(item)):
        j = i + 1
        count = 1
        while j in range(len(item)) and item[i] == item[j]: 
            count += 1
            j += 1
        answer = answer + f'{item[i]}{count}'
        i = j 
    return answer

print(string_compression('aabcccccaaazzzzzzffddgshhshshshsfdsfsfs'))
