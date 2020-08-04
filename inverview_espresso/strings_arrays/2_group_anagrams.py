# TIME: O(n * (m log m)) n = number of strings, m = longest string in array
# SPACE: O(n)
def group_anagrams(arr):
    ht = {}
    for item in arr:
        ss = ''.join(sorted(item))

        if ss in ht:
            ht[ss].append(item)
        else:
            ht[ss] = [item]

    return ht.values()


print(group_anagrams(['ba', 'ab', 'aac', 'caa', 'aca']))